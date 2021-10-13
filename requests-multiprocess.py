import requests
from multiprocessing.pool import Pool

#use request for session later

url = "http://httpbin.org/uuid"

def fetch(session,url):
    with session.get(url) as result:
        print(result.json()['uuid'])

def main():
    with Pool() as pool:
        with requests.Session() as session:
            pool.starmap(fetch,[(session,url) for n in range(100)])

main()
