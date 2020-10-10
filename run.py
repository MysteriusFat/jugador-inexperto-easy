import threading 
import argparse

from request import MakeVotes, GetPlayers

if __name__ == '__main__':	
	parser = argparse.ArgumentParser()
	parser.add_argument('--stop' , help='limit votes', type=int, default=1000)
	parser.add_argument('--proxy', help='proxy server example https://localhost:8080', default="://")
	
	required = parser.add_argument_group('required arguments')
	required.add_argument('-p', '--payload', required=True)
	required.add_argument('-t', '--threads', required=True, type=int)

	argv = parser.parse_args()
	
	payload = argv.payload
	threads = argv.threads
	stop = argv.stop
	proxy = { argv.proxy.split('://')[0] : argv.proxy.split('://')[1]}
	
	print('[*] payload: {}'.format(payload))
	print('[*] threads: {}'.format(threads))
	print('[*] votes limit: {}'.format(stop))	
	
	input('\n[>] Press start')
	for i in range(threads):
		thread = threading.Thread(target=MakeVotes, args=(payload, stop, proxy))
		thread.start()
