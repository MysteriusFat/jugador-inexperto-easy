import sys
import requests
import time
import os
import argparse
import threading

URL_VOTES = 'https://votes.flowics.com/paul/public/votes/o/12416/5f492f838d6fc400476c40b5'
URL_GETS = 'https://paul.flowics.com/paul/public/polls/12416/5f492f838d6fc400476c40b5?profile=interactive'

n_votes = 0

# Headers se usan para todas las requests
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0',
    'Accept': '*/*',
    'Accept-Language': 'es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://viz.flowics.com/public/208b11a4a060fb0faee34f51e28ac1b4/5f342daf7e547780c73fecd7/live?fluid=true',
    'content-type': 'application/vnd.flowics.bulk.v1.avro+json',
    'Origin': 'https://viz.flowics.com',
}

def GetVotes():
	session = requests.Session()
	r = session.get(URL_GETS, headers=headers)
	res = []
	# print(r.status_code)
	for player in r.json()['polls'][0]['items']:
		res.append({'name':player['name'], 'id': player['id'], 'votes':player['results']['count']})
	return res

def Vote(session, filename):
	with open(filename) as file:
		payload = file.read()
		r = session.post(URL_VOTES, data=payload, headers=headers)
		return r.status_code


def ShowVotes():
	table += "+---------------------------+--------------------------------------+------------+"
	table += "| {:25} | {:30}       | {:10} |".format('name', 'id', 'votes')
	table += "+---------------------------+--------------------------------------+------------+"
	for player in GetVotes():
		table += "| {:25} | {:30} | {:10} |".format(player['name'], player['id'], player['votes'])
	table += "+---------------------------+--------------------------------------+------------+"
	print(table)

def MakeVotes(payload, stop):
	session = requests.Session()
	global n_votes 	
	while n_votes < stop:
		status = Vote(session, payload)
		if status == 200 or status == 204:
			n_votes += 1
			print('[+] status: {} \t votes: {}'.format(status, n_votes))
		else:
			print('[!] status: {} \t votes: {}'.format(status, n_votes))
			print('[!] Cleaning cookies')		
			session.cookies.clear()
			time.sleep(1)

if __name__ == '__main__':	
	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--stop', help='limit votes', type=int, default=1000000000)
	
	required = parser.add_argument_group('required arguments')
	required.add_argument('-p', '--payload', required=True)
	required.add_argument('-t', '--threads', required=True, type=int)

	argv = parser.parse_args()
	
	payload = argv.payload
	threads = argv.threads
	stop = argv.stop

	print('[*] payload: {}'.format(payload))
	print('[*] threads: {}'.format(threads))
	if stop is not None:
		print('[*] votes limit: {}'.format(stop))	
	
	try:
		ShowVotes()
	except:
		print("[!] No hay partidos activos")
		exit()

	input('\n[>] Press start')	
	for i in range(threads):
		thread = threading.Thread(target=MakeVotes, args=(payload, stop))
		thread.start()
