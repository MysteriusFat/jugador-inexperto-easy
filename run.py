import threading 
import argparse

from request import MakeVotes, GetPlayers, MakeTables

if __name__ == '__main__':	
	parser = argparse.ArgumentParser()
	parser.add_argument('--stop' , help='limit votes', type=int, default=1000)
	parser.add_argument('--proxy', help='proxy server example https://localhost:8080', default="://")
	
	required = parser.add_argument_group('required arguments')
	required.add_argument('-t', '--threads', required=True, type=int)

	argv = parser.parse_args()
	
	threads = argv.threads
	stop = argv.stop
	proxy = { argv.proxy.split('://')[0] : argv.proxy.split('://')[1]}
	
	print('[*] threads: {}'.format(threads))
	print('[*] votes limit: {}'.format(stop))	
		
	players = MakeTables()
	n = input('\n[>] Select player (Number): ')
	
	with open('payload.txt') as file:
		no_payload = file.read().split('{}')		

		payload = no_payload[0]
		payload += players[int(n)][2]
		payload += no_payload[1]
		
	
		for i in range(threads):
			thread = threading.Thread(target=MakeVotes, args=(payload, stop, proxy))
			thread.start()
