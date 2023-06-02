import requests
import json
import requests
import base64
from github import Github
import threading
from threading import Thread
import sqlite3
from time import sleep
import re

conn = sqlite3.connect('data.db')

conn.execute('''CREATE TABLE IF NOT EXISTS VULNERS
     ( CVE TEXT NOT NULL,
     DESCR TEXT  NOT NULL,
     CVSS TEXT  NOT NULL,
     CWE TEXT  NOT NULL);''')

conn.commit()
conn.close()

tools = ['HADOOP', 'FLINK', 'SPARK', 'KAFKA', 'HIVE', 'STORM', 'MySQL', 'CASSANDRA', 'ELASTICSEARCH', 'MONGODB', 'MARIADB', 'REDIS']

def get_all_cves():
  conn = sqlite3.connect('data.db')
  c=conn.cursor()
  for tool in tools:
    c.execute("SELECT CVE FROM "+tool+"_VULNS;")
    cves = cves + c.fetchall()
  return cves

def insert(cve, desc, cvss, cwe):
  conn = sqlite3.connect('data.db')
  conn.execute('''INSERT INTO VULNERS (CVE, DESCR, CVSS, CWE) VALUES (?,?,?,?);''', (cve, desc, cvss, cwe));
  conn.commit()
  conn.close()


cves = get_all_repos()

for cve in enumerate(cves):
  sleep(6)
  request = requests.get(f'https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve}')
  json_object = json.loads(request.content)
  print("="*100)
  print(json_object)
  print("="*100)


