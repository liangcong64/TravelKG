from scrapy import cmdline

# cmdline.execute('scrapy crawl chizhouurl -o data/chizhou/zhaopinurl.csv'.split())
# cmdline.execute('scrapy crawl chizhouItem -o data/chizhou/zhaopinItem.csv'.split())
# cmdline.execute('scrapy crawl 51jobUrl -o data/chizhou/51jobUrl4.csv'.split())
cmdline.execute('scrapy crawl 51jobItem -o data/chizhou/51jobItem.csv'.split())
# cmdline.execute('scrapy crawl chizhoujobUrl -o data/chizhou/chizhoujobUrl.csv'.split())
# cmdline.execute('scrapy crawl chizhoujobItem -o data/chizhou/NewchizhoujobItem.csv'.split())
# cmdline.execute('scrapy crawl baipinItem -o data1/chizhou/baipinItem.csv'.split())