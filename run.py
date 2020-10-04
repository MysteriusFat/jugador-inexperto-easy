import stem
import stem.connection

import sys 
import requests
import time 
import os 
import socket
import socks 

from stem import Signal
from stem.control import Controller

URL_VOTES = 'https://votes.flowics.com/paul/public/votes/o/12416/5f492f838d6fc400476c40b5'
URL_GETS = 'https://paul.flowics.com/paul/public/polls/12416/5f492f838d6fc400476c40b5?profile=interactive' 
session = requests.Session()

# Headers se usan para todas las requests 
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0',
    'Accept': '*/*',
    'Accept-Language': 'es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://viz.flowics.com/public/208b11a4a060fb0faee34f51e28ac1b4/5f342daf7e547780c73fecd7/live?fluid=true',
    'content-type': 'application/vnd.flowics.bulk.v1.avro+json',
    'Origin': 'https://viz.flowics.com',
}

def renew_connection():
	with Controller.from_port(port = 9050) as controller:
		controller.authenticate(password = 'Jugodepinavall3')
		controller.signal(Signal.NEWNYM)
		controller.close()


def GetVotes(): 
	r = session.get(URL_GETS, headers=headers)
	res = []	
	# print(r.status_code)
	for player in r.json()['polls'][0]['items']:
		res.append({'name':player['name'], 'id': player['id'], 'votes':player['results']['count']})
	return res 

def Vote(filename):
	with open(filename) as file:
		payload = file.read()
		r = session.post(URL_VOTES, data=payload, headers=headers)
		return r.status_code 


def ShowVotes():
	print("+---------------------------+--------------------------------------+------------+")
	print(  "| {:25} | {:30}       | {:10} |".format('name', 'id', 'votes')) 
	print("+---------------------------+--------------------------------------+------------+")
	for player in GetVotes():
		print("| {:25} | {:30} | {:10} |".format(player['name'], player['id'], player['votes']))
	print("+---------------------------+--------------------------------------+------------+")
	
if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("[!] Select file and time rate")		
		exit()

	payload = sys.argv[1]
	time_rate = int(sys.argv[2])
	n_votes = 0

	print("\n[*] Payload: {}".format(sys.argv[1]))
	print("[*] Time rate: {}\n".format(sys.argv[2]))
		
	ShowVotes()
 	
	while True:
		time.sleep(time_rate)
		status = Vote(payload)
		if status == 204 or status == 200:
			n_votes += 1
			print("[+] status {} \t votes: {}".format(status, n_votes))
		else:
			print("[!] status {} \t votes: {}".format(status, n_votes))
			print("[*] Clean cookies ")
			session.cookies.clear()
			time.sleep(4)

