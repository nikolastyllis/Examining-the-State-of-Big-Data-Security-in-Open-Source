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
  cves = []
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

def check(cve):
  conn = sqlite3.connect('data.db')
  c=conn.cursor()
  c.execute('''SELECT CVE FROM VULNERS WHERE CVE=?;''',(cve,))
  el = c.fetchall()
  if len(el) > 0:
    return True
  else:
    return False

cves = get_all_cves()

i = 0
for cve in enumerate(cves):
  i=i+1
  cve_name = cve[1][0]
  print(cve_name, "... ", i, "/", len(cves))
  if check(cve_name):
    print("Skipping!")
    continue
  sleep(6)
  request = requests.get(f'https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_name}')
  json_object = json.loads(request.content)
  
  cwe = json_object['vulnerabilities'][0]['cve']['weaknesses'][0]['description'][0]['value']
  desc = json_object['vulnerabilities'][0]['cve']['descriptions'][0]['value']
  try:
    cvss = json_object['vulnerabilities'][0]['cve']['metrics']['cvssMetricV31'][0]['cvssData']['baseScore']
  except:
    try:
      cvss = json_object['vulnerabilities'][0]['cve']['metrics']['cvssMetricV30'][0]['cvssData']['baseScore']
    except:
      cvss = json_object['vulnerabilities'][0]['cve']['metrics']['cvssMetricV2'][0]['cvssData']['baseScore']
  print("="*100)
  print(cve_name)
  print("DESCRIPTION: ", desc)
  print("SCORE: ", cvss)
  print("CWE-ID: ", cwe)
  print("="*100)

  insert(cve_name, desc, cvss, cwe)


