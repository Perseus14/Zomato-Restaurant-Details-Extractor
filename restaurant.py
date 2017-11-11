from pyzomato import Pyzomato
import os, sys

ZOMATO_API = '1805ac2da536bd40cdfc7e003dbaa421'

#Initialise Zomato API
res_api = Pyzomato(ZOMATO_API)

def search(restaurant_name):	
	res_results = res_api.search(q=restaurant_name)
	res_results = res_results['restaurants']
	if(not os.path.isfile('res_details.csv')):
		os.system('touch res_details.csv')
		with open('res_details.csv','w') as fin:
			fin.write('Restaurant Name' + ","+  'Location' + ","+ 'Price for 2'+ ","+  'Rating' + "\n") 

	with open('res_details.csv','a') as fin:
		for i in xrange(min(2,len(res_results))):
			res_details = res_results[i]['restaurant']
			if(res_details['location']['city']!='Bangalore'):
				break
			else:
				print res_details['name'],'\n',res_details['location']['address'], '\nPrice for 2: ', res_details['average_cost_for_two'], ' Rs\nRating: ', res_details['user_rating']['aggregate_rating'] 
				print "\n"
				try:
					fin.write(res_details['name'] + ","+ " ".join(res_details['cuisines'].split(',')) + "," + " ".join(res_details['location']['locality'].split(',')) + "," + str(res_details['average_cost_for_two']) + ","+ str(res_details['user_rating']['aggregate_rating'] + "\n")) 
				except:
					continue
'''
while(True):
	restaurant_name = raw_input('Enter Restaurant Name (q to exit): ')
	if(restaurant_name == 'q'):
		break
	print '\n'
	search(restaurant_name)
'''
if(len(sys.argv)==1):
	restaurant_name = raw_input('Enter Restaurant Name (q to exit): ')
	if(restaurant_name == 'q'):
		sys.exit()	
	print '\n'
	search(restaurant_name)	
if(len(sys.argv)==2):
	with open(sys.argv[1],"r") as fin:
		lines = fin.readlines()
		for line in lines:
			search(line[:-1])
else:
	print "Usage python restaurant.py or python restaurant.py <filelistof restaurant>"
