#coding:utf-8
#__author__ ='dell'

import re

f1=open('log.txt','r' ,encoding='utf-8')
data1=f1.readlines()
# print data1
f1.close()
results = []
f2 = open('loss.txt', 'w')
f3 = open('score','w')

# 利用正则表达式

for line in data1:
	data2=line.split()
	print(data2)
	for i in data2:
		n = re.findall(r"Saving", i)
		m=	re.findall(r"Evaluate", i)
		if n:
			# print line
			f2.writelines(line)
		if m :
			f3.writelines(line)
f2.close()
f3.close()
f1.close()


