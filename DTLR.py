import requests 
from bs4 import BeautifulSoup
from threading import Thread

def scrape(start,stop,file_name):

	info_list = []

	print 'Scraping started'
	
	while start <= stop:

		end_pt = requests.get('http://dtlr.com/lbiquickview?id=%s' % str(start))
		
		soup = BeautifulSoup(end_pt.content, 'html.parser')

		link = soup.find('a',{'id':'view_product'})['href']
		name = soup.find('div',{'itemprop':'name'}).text

		info = str(start) + ' : ' + str(name) + ' : '+str(link)

		info_list.append(info)

		start += 1

	txt = open(file_name, 'w')
	
	for info in info_list:
		txt.write(info+'\n')

	txt.close()

	print 'Scraping compleat'

