# -*- coding:utf-8 -*-
import re, datetime, requests, html.parser, json, urllib
import csv, api
from bs4 import BeautifulSoup

strDate = datetime.datetime.now().strftime("%y%m%d")
header ={
	"Host":'admin.gangchoo.thebe.co.kr',
	"Connection" : "keep-alive",
	"Content-Length" : '3997',
	"Cache-Control": 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0',
	"Content-Type" :'text/html; charset=UTF-8',
	"Referer" : "http://admin.gangchoo.thebe.co.kr/code",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
	"Accept-Encoding":"gzip, deflate, sdch",
	"Accept-Language":"en-US,en;q=0.8,ko;q=0.6",
	"Cookie":"" #코드 실행전 값입력하기
}
# teachers =''
log =0
for n in range(1,55):
	url = 'http://admin.gangchoo.thebe.co.kr/teacher/?&search_word=&page='+str(n)
	req = urllib.request.Request(url,headers=header)
	res = urllib.request.urlopen(req).read()
	data = BeautifulSoup(str(res,'utf-8'),'html.parser')
	tcList = data.select('tbody')[0].select('tr')
	teachers =''
	for t in range(len(tcList)): 
		tn = tcList[t].select('td')[3].text.replace(')','').replace('(',',').split(',')
		if len(tn)==1: teachers= teachers+ tcList[t].select('td')[1].text.strip() + tcList[t].select('td')[3].text.strip()
		else: 
			for ts in range(len(tn)): teachers = teachers+tcList[t].select('td')[1].text.strip() + tn[ts].strip() 
		log = log+1
	with open('/Users/choon/py3.5/gcrawler/'+'강사_'+strDate+'.txt','a',encoding='utf-8') as f:
		f.write(teachers+'\n')	
			
print(log)