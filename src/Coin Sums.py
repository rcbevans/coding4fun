#1 5
#2 2 1 1
#1 2 3 1
#5 1
from math import floor

if __name__ == '__main__':
	total_sum = 200
	num_ways = 0
	for twopounds in range(0, int(floor(total_sum/200) + 1)):
		for pounds in range(0, int(floor((total_sum - twopounds*200)/100) + 1)):
			for fiftypence in range(0, int(floor((total_sum - twopounds*200 - pounds * 100 )/50) + 1)):
				for twentypence in range(0, int(floor((total_sum - twopounds*200 - pounds*100 - fiftypence*50)/20) + 1)):
					for tenpence in range(0, int(floor((total_sum - twopounds*200 - pounds*100 - fiftypence*50 - twentypence*20)/10) + 1)):
						for fivepence in range(0, int(floor((total_sum - twopounds*200 - pounds*100 - fiftypence*50 - twentypence*20 - tenpence*10)/5) + 1)):
							for twopence in range(0, int(floor((total_sum - twopounds*200 - pounds*100 - fiftypence*50 - twentypence*20 - tenpence*10 - fivepence*5)/2) + 1)):
								for pence in range(0, int(floor((total_sum - twopounds*200 - pounds*100 - fiftypence*50 - twentypence*20 - tenpence*10 - fivepence*5 - twopence*2)/1) + 1)):
									if pence + 2*twopence + 5*fivepence + 10*tenpence + 20*twentypence + 50*fiftypence + 100*pounds + 200*twopounds == total_sum:
										num_ways += 1
	print num_ways