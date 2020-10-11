import requests
import time
import threading

from tabulate import tabulate
from config import headers, URL_VOTE, URL_GETPLAYERS
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
n_votes = 0

def GetPlayers():
	r = requests.get(URL_GETPLAYERS, headers=headers)	
	if len(r.json()['polls']) <= 0:
		return [['No existen','partidos','activos'],]
	
	res = []
	for i, player in enumerate(r.json()['polls'][0]['items']):
		res.append([i, player['name'], player['id'], player['results']['count']])
	return res

def Vote(session, payload, proxies={}):
	r = session.post(URL_VOTE, data=payload, headers=headers, proxies=proxies)
	return r.status_code

def MakeVotes(payload, stop, proxies):
	session = requests.Session()
	global n_votes
	while n_votes < stop:
		status = Vote(session, payload, proxies)
		if status == 200 or status == 204:
			n_votes += 1
		else:		
			session.cookies.clear()
		print('[' + time.ctime() + '] ' + '[+] status: {} \t votes: {} \t '.format(status, n_votes), end='\r', flush=True) 
		time.sleep(1)

def MakeTables():
	players = GetPlayers()
	print('\n' + tabulate(players, headers=['N°', 'Name', 'ID', 'Votes'], tablefmt='orgtbl'))
	return players
