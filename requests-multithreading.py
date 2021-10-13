import requests
from concurrent.futures import ThreadPoolExecutor

#use request for session later

url = "http://httpbin.org/uuid"

def fetch(session,url):
    with session.get(url) as result:
        print(result.json()['uuid'])

def main():
    with ThreadPoolExecutor(max_workers=60) as executor:
        with requests.Session() as session:
            executor.map(fetch,[session]*100,[url]*100)
            executor.shutdown(wait=True)

main()
