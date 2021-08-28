# for free proxies visit https://free-proxy-list.net/

#if there is any connectionRefuse error trychanging the IP-Address


import requests
import csv
import concurrent.futures

proxylist=[]

with open('proxylist.csv','r') as f:
  reader = csv.reader(f)
  for row in reader:
    proxylist.append(row[0])

def extract(proxy):
  try:
    r = requests.get('https://httpbin.org/ip',proxies={'http':proxy,'https':proxy}) #you can also set timeout=ns 
    print(r.status_code,r.json(),' - Working !')
  except:
    pass
  return proxy

extract("Enter your IP...")

with concurrent.futures.ThreadPoolExecutor() as exector:
  exector.map(extract,proxylist)
