#!/usr/bin/env python
# encoding:utf8

import requests
from bs4 import BeautifulSoup
import sys

# config-start
keyword = sys.argv[1]
resultFileName = "webshells.txt"
# config-end

url = "http://www.baidu.com/s?wd=" + keyword
print "Getting : " + url + "...",
response = requests.get(url)
print "OK!"
content = response.content
status_code = response.status_code
soup = BeautifulSoup(content, "html.parser")
links = soup.findAll("a")
for link in links:
    try:
        dstURL = link['href']
        if (dstURL.startswith("http://") or dstURL.startswith("https://")) and dstURL.startswith("http://www.baidu.com/link?url=") :
            result_url = requests.get(dstURL).url
            file = open(resultFileName, "a+")
            file.write(result_url + "\r\n")
            file.close()
            print result_url
    except Exception as e:
        pass
