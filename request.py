import requests
import time
import threading

from config import headers, URL_VOTE, URL_GETPLAYERS

n_votes = 0

def GetPlayers():
	r = requests.get(URL_GETS, headers=headers)
	res = []
	for player in r.json()['polls'][0]['items']:
		res.append({'name':player['name'], 'id': player['id'], 'votes':player['results']['count']})
	return res

def Vote(session, payload, proxies={}):
	r = session.post(URL_VOTE, data=payload, headers=headers, proxies=proxies)
	return r.status_code

def MakeVotes(filename, stop, proxies):
	session = requests.Session()
	global n_votes
	with open(filename) as file:
		payload = file.read()
		while n_votes < stop:
			status = Vote(session, payload, proxies)
			if status == 200 or status == 204:
				n_votes += 1
			else:		
				session.cookies.clear()
			print('[' + time.ctime() + '] ' + '[+] status: {} \t votes: {} \t '.format(status, n_votes), end='\r', flush=True) 
			time.sleep(1)
