# -*- coding:utf-8 -*-
import json, requests, datetime
import urllib, http.cookiejar
from bs4 import BeautifulSoup

def teachers():

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
		"Cookie":"choon=choon; ci_session=e78823c829625c3b349369bd886e1b565f14003c"
	}
	teachers =''
	for n in range(1,54):
		url = 'http://admin.gangchoo.thebe.co.kr/teacher/?&search_word=&page='+str(n)
		req = urllib.request.Request(url,headers=header)
		res = urllib.request.urlopen(req).read()
		data = BeautifulSoup(str(res,'utf-8'),'html.parser')
		tcList = data.select('tbody')[0].select('tr')
		for t in range(len(tcList)): teachers = teachers + tcList[t].select('td')[1].text + tcList[t].select('td')[3].text
		print('n')	




# def teachers():
# 	url = "http://api.gangchoo.thebe.co.kr/teacher/list"
# 	querystring = {"page_size":"2000"}
# 	payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"member_id\"\r\n\r\nsoungbeom@gmail.com\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"member_key\"\r\n\r\nfca2786db7027a4aa40c4af256e2995e\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"course_list\"\r\n\r\nON,OFF\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"page\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"page_size\"\r\n\r\n2000\r\n-----011000010111000001101001--"
# 	headers = {
# 	    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
# 	    'academy_code': "null",
# 	    'category_code': "null",
# 	    'course_type': "null",
# 	    'sort_type': "null",
# 	    'page': "null",
# 	    'page_size': "null",
# 	    'cache-control': "no-cache",
# 	    'postman-token': "6588c8fc-42a5-ed13-3cf9-e22e27fee969"
# 	    }
# 	tdict ={}
# 	res = json.loads(requests.request("POST", url, data=payload, headers=headers, params=querystring).text)['list']
# 	for n in range(len(res)): tdict.update({res[n]['teacher_title']:res[n]['teacher_code']})
# 	return tdict





def subjects():
	url = "http://api.gangchoo.thebe.co.kr/common/filter/course" #공통 > __필터_강좌선택 
	payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"category_code\"\r\n\r\nSB001\r\n-----011000010111000001101001--"
	headers = {
	    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
	    'language_code': "LG01",
	    'cache-control': "no-cache",
	    'postman-token': "392910d1-c403-b430-30f8-fb1747f13a0d"
	    } 
	res = json.loads(requests.request("POST", url, data=payload, headers=headers).text)
	SUBJ_dics = res['list']

	subjects ={} #과목명 -> 과목코드값 구하기
	for n in range(len(SUBJ_dics)):
		SUBJ_dic = SUBJ_dics[n]
		subjects.update({SUBJ_dic['category_name']:SUBJ_dic['category_code']})
	return subjects


def level(category):
	code = subjects()[category] 
	url = "http://api.gangchoo.thebe.co.kr/common/filter/level"
	payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"category_code\"\r\n\r\n"+code+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"course_type\"\r\n\r\n\r\n-----011000010111000001101001--"
	headers = {
	    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
	    'cache-control': "no-cache",
	    'postman-token': "334ae7f5-6dd4-2831-5dc2-9e2a4f1259c3"
	    }
	res = json.loads(requests.request("POST", url, data=payload, headers=headers).text)
	
	lv_header=[]
	for n in range(len(res['list'])): lv_header.append(res['list'][n]['code_name'])		
	return lv_header


def type(category):
	code = subjects()[category] 
	url = "http://api.gangchoo.thebe.co.kr/common/filter/class"
	payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"category_code\"\r\n\r\n"+code+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"course_type\"\r\n\r\n\r\n-----011000010111000001101001--"
	headers = {
	    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
	    'cache-control': "no-cache",
	    'postman-token': "b436239d-6b1a-eea5-418e-db2ff6e66b8c"
	    }
	res = json.loads(requests.request("POST", url, data=payload, headers=headers).text)
	
	tp_header=[]
	for n in range(len(res['list'])): tp_header.append(res['list'][n]['code_name'])		
	return tp_header


def mk_header(category,onoff):
	strDate = datetime.datetime.now().strftime("%y%m%d")
	code = subjects()[category] 
	lv_header = []
	url = "http://api.gangchoo.thebe.co.kr/common/filter/level"
	payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"category_code\"\r\n\r\n"+code+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"course_type\"\r\n\r\n\r\n-----011000010111000001101001--"
	headers = {
	    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
	    'cache-control': "no-cache",
	    'postman-token': "334ae7f5-6dd4-2831-5dc2-9e2a4f1259c3"
	    }
	res = json.loads(requests.request("POST", url, data=payload, headers=headers).text)['list']
	for n in range(len(res)): lv_header.append('F-'+res[n]['sys_code'])
	tp_header = []
	url = "http://api.gangchoo.thebe.co.kr/common/filter/class"
	payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"category_code\"\r\n\r\n"+code+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"course_type\"\r\n\r\n\r\n-----011000010111000001101001--"
	headers = {
	    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
	    'cache-control': "no-cache",
	    'postman-token': "b436239d-6b1a-eea5-418e-db2ff6e66b8c"
	    }
	res = json.loads(requests.request("POST", url, data=payload, headers=headers).text)['list']
	for n in range(len(res)): tp_header.append('G-'+res[n]['sys_code'])

	def off(lv_header, tp_header):
		mk_header =['BRANCH_NAME','TITLE','START','END','TEACHER_STRING','TEACHER','PRICE','URL','W1','W2','W3','W4','W5','W6','W7','W8','LEVEL_MEMO']+lv_header+tp_header
		return(mk_header)
	def on(lv_header, tp_header):
		mk_header =['TITLE','TEACHER_STRING','TEACHER','PRICE','URL','T1','T2','T3','T4','T5','T6', 'TERM_MEMO','LEVEL_MEMO']+lv_header+tp_header
		return(mk_header)

	if onoff == 'off': mk_header= off(lv_header, tp_header)
	else:mk_header= on(lv_header, tp_header)
	return mk_header



def institutes():
	url = "http://api.gangchoo.thebe.co.kr/academy/list" #학원 > 목록(검색)
	payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"member_id\"\r\n\r\nsoungbeom@gmail.com\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"member_key\"\r\n\r\nfca2786db7027a4aa40c4af256e2995e\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"local_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"page\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"page_size\"\r\n\r\n50\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sort_type\"\r\n\r\n\r\n-----011000010111000001101001--"
	headers = {
	    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
	    'cache-control': "no-cache",
	    'postman-token': "55c60cf1-3a04-6bf3-b6dd-64285d8a74d2"
	    }
	res = requests.request("POST", url, data=payload, headers=headers).text
	res = json.loads(res)
	INST_dics = res['list']
	institutes = {}
	for n in range(len(INST_dics)):
		INST_dic = INST_dics[n]
		institutes.update({INST_dic['academy_title'] : INST_dic['academy_code']})
	return institutes

def branches():
	url = "http://api.gangchoo.thebe.co.kr/academy/list" #학원 > 목록(검색)
	payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"member_id\"\r\n\r\nsoungbeom@gmail.com\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"member_key\"\r\n\r\nfca2786db7027a4aa40c4af256e2995e\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"local_code\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"page\"\r\n\r\n1\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"page_size\"\r\n\r\n50\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"sort_type\"\r\n\r\n\r\n-----011000010111000001101001--"
	headers = {
	    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
	    'cache-control': "no-cache",
	    'postman-token': "55c60cf1-3a04-6bf3-b6dd-64285d8a74d2"
	    }
	res = requests.request("POST", url, data=payload, headers=headers).text
	res = json.loads(res)
	BRAN_dics = res['list']
	branches ={}

	for n in range(len(BRAN_dics)):
		BRAN_dic = BRAN_dics[n]
		# 지점명 -> 학원명 구하기 
		branches.update({BRAN_dic['branch_title'] : [BRAN_dic['branch_idx'], BRAN_dic['academy_title']]})

	return branches




