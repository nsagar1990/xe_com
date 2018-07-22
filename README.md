# xe_com scraper and visualization

Scraper to scrape and create line plot of INR vs USD rates. Runs every 10 minutes once and fetches the prices.

## Requirements
	- lxml ( pip install lxml )
	- Seaborn ( pip install seaborn )
	- python-Tkinter ( apt-get install python-tk )
	- Pandas ( pip install pandas )
	

## How to run
	- Scraper
		python xe_com.py -t crawl

	- Visualization
		python xe_com.py -t viz

## Crontab

	*/10 * * * * cd <PATH>; python xe_com.py -t crawl >> /tmp/backup2.log 2>&1
