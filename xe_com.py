
import os
import sys
import argparse
import requests
import logging
import pandas as pd
import seaborn as sns
from lxml import html
import matplotlib.pyplot as plt
from datetime import datetime

URL = "https://xe.com/currencyconverter/convert/?Amount=1&From=USD&To=INR"
FILENAME = "%s.csv" %datetime.today().strftime("%Y%m%d")

def viz():
	df = pd.read_csv(FILENAME)
	ax = sns.pointplot(x = "time", y = "rate", data = df)
	plt.show()

def crawl():
	resp = requests.get(URL)

	if resp.status_code == 200:
		hdoc = html.fromstring(resp.text)
	else:
		sys.exit(1)
		print("Got non 200 status :: %s" %status_code)		

	rate = "".join(hdoc.xpath('//span[@class="uccResultAmount"]//text()'))
	data = ','.join([datetime.now().strftime("%H:%M"), rate])
	
	if os.path.exists(FILENAME):
		with open(FILENAME, "a+") as fp:
			fp.write("%s\n" %data)
	else:
		with open(FILENAME, "a+") as fp:
			fp.write('time,rate\n')
			fp.write("%s\n" %data)

def main(options):

	if options.type == "crawl":
		crawl()
	elif options.type == "viz":
		viz()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('-t', action='store', dest='type',
	                    help='Action to perform')
	options = parser.parse_args()
	main(options)
