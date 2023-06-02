import requests
import base64
from github import Github
import threading
from threading import Thread
import sqlite3
from time import sleep
import re

conn = sqlite3.connect('data.db')

conn.execute('''CREATE TABLE IF NOT EXISTS HADOOP
		 ( REPO_NAME TEXT NOT NULL,
		 HADOOP_VERSION TEXT 	NOT NULL,
		 LAST_PUSH TEXT 	NOT NULL,
		 GIT_URL TEXT NOT NULL);''')

conn.execute('''CREATE TABLE IF NOT EXISTS SEARCHED
		 ( REPO_NAME TEXT NOT NULL);''')

conn.commit()
conn.close()

def insert_into_db(repo_name, hadoop_version, last_push, git_url):
	conn = sqlite3.connect('data.db')
	conn.execute('''INSERT INTO HADOOP (REPO_NAME,HADOOP_VERSION,LAST_PUSH,GIT_URL) VALUES (?, ?, ?, ?)''', (repo_name, hadoop_version, last_push, git_url));
	conn.commit()
	conn.close()

def insert_into_searched(repo_name):
	conn = sqlite3.connect('data.db')
	conn.execute('''INSERT INTO SEARCHED (REPO_NAME) VALUES (?)''', (repo_name,));
	conn.commit()
	conn.close()

def check_if_exists(repo_name):
	conn = sqlite3.connect('data.db')
	c=conn.cursor()
	c.execute('''SELECT * FROM HADOOP WHERE REPO_NAME=?;''', (repo_name,))
	exists = c.fetchall()
	if len(exists)==0:
		return False
	else:
		return True

def check_if_searched(repo_name):
	conn = sqlite3.connect('data.db')
	c=conn.cursor()
	c.execute('''SELECT * FROM SEARCHED WHERE REPO_NAME=?;''', (repo_name,))
	exists = c.fetchall()
	if len(exists)==0:
		return False
	else:
		return True

g = Github("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")

#Gets required data from a repository using hadoop
def get_hadoop_version_maven(file):
	hadoop_version = ""
	try:
		string = file.decoded_content.decode('utf-8')
		pattern = r"<[^>//]*hadoop[^>//]*version[^>//]*>"
		hadoop_version = re.split(pattern, string)[1].split("</",1)[0].strip()
		return hadoop_version
	except:
		pass
	
	try:
		string = file.decoded_content.decode('utf-8')
		pattern = r"<dependency>\s*<groupId>.*hadoop.*</groupId>\s*<artifactId>.*hadoop.*\s*</artifactId>\s*<version>"
		hadoop_version = re.split(pattern, string)[1].split("</",1)[0].strip()
		return hadoop_version
	except:
		return ""

def get_hadoop_version_gradle_or_ant(file):
	hadoop_version = ""
	try:
		string = file.decoded_content.decode('utf-8')
		pattern = r"hadoop.*version\s*="
		hadoop_version = re.split(pattern, string,1,re.IGNORECASE)[1].split("\n",1)[0].strip()
		return hadoop_version
	except:
		pass
	try:
		string = file.decoded_content.decode('utf-8')
		pattern = r"version.*hadoop\s*="
		hadoop_version = re.split(pattern, string,1,re.IGNORECASE)[1].split("\n",1)[0].strip()
		return hadoop_version
	except:
		return ""

results = g.search_repositories("hadoop language:java license:mit  license:apache-2.0  license:gpl")
for i, repo in enumerate(results):
	repoName = repo.full_name
	
	if check_if_exists(repoName) == True:
		continue

	if check_if_searched(repoName) == True:
		continue

	insert_into_searched(repoName)

	#sleep(1)

	hadoop_version = ""

	try:
		file = repo.get_contents("pom.xml")
		hadoop_version = get_hadoop_version_maven(file)
	except:
		try:
			file = repo.get_contents("gradle.properties")
			hadoop_version = get_hadoop_version_gradle_or_ant(file)
		except:
			try:
				file = repo.get_contents("build.gradle")
				hadoop_version = get_hadoop_version_gradle_or_ant(file)
			except:
				try:
					file = repo.get_contents("ivy/libraries.properties")
					hadoop_version = get_hadoop_version_gradle_or_ant(file)
				except:
					continue

	if hadoop_version == "":
		continue

	# Define the regex pattern to match the version number
	pattern = r'\d+\.\d+\.\d+'

	# Use the re.search() function to find the version number in the input string
	match = re.search(pattern, hadoop_version)

	# Check if a match was found
	if match:
	    # Extract the version number from the match object
	    version_number = match.group()
	else:
	    continue

	insert_into_db(repoName, version_number, repo.pushed_at, repo.git_url)
	print("="*100)
	print(repoName)
	print("HADOOP_VERSION:", version_number)
	print("="*100)

