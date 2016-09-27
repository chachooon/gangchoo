# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re, datetime, requests, csv, api, json, html.parser
import urllib.parse as up
def mklevel(category, level):
	if category =='토익':
		lv1 = re.compile('600|기초|첫토익|내생토')
		lv2 = re.compile('650|700')
		lv3 = re.compile('700|750')
		lv4 = re.compile('800|850|실전')
		lv5 = re.compile('900|950|실전')
	elif category == '토플':
		lv1 = re.compile('기초')
		lv2 = re.compile('70')
		lv3 = re.compile('80')
		lv4 = re.compile('90')
		lv5 = re.compile('100')
	elif category == '토익스피킹':
		lv1 = re.compile('Lv[.]5')
		lv2 = re.compile('Lv[.]6|Lv[.]6.7')
		lv3 = re.compile('Lv[.]6.7|Lv[.]7')
		lv4 = re.compile('Lv[.]7')
		lv5 = re.compile('고득점|Lv[.]8')
	elif category == '오픽':
		lv1 = re.compile('IM\D{1,3}IH|IM')
		lv2 = re.compile('IM\D{1,3}IH|IM2.{1,3}IH|IM2.{1,3}AL|IM2')
		lv3 = re.compile('IM\D{1,3}IH|IM2.{1,3}IH|IM2.{1,3}AL|IM3.{1,3}AL|IM3')
		lv4 = re.compile('IM\D{1,3}IH|IM2.{1,3}IH|IM2.{1,3}AL|IM3.{1,3}AL|IH.{1,3}AL|IH')
		lv5 = re.compile('IM2.{1,3}AL|IM3.{1,3}AL|IH.{1,3}AL|AL')
	elif category == '텝스':
		lv1 = re.compile('')
		lv2 = re.compile('')
		lv3 = re.compile('')
		lv4 = re.compile('')
		lv5 = re.compile('')
	elif category == '아이엘츠':
		lv1 = re.compile('')
		lv2 = re.compile('')
		lv3 = re.compile('')
		lv4 = re.compile('')
		lv5 = re.compile('')
	elif category == '일반영어':
		lv1 = re.compile('')
		lv2 = re.compile('')
		lv3 = re.compile('')
		lv4 = re.compile('')
		lv5 = re.compile('')
	else: pass
	
	lv_header = api.level(category)
	lv = ['','','','',''][0:len(lv_header)]
	lvr = [lv1,lv2,lv3,lv4,lv5][0:len(lv_header)]
	for n in range(len(lv)):
		if lvr[n].search(level): lv[n] = 'Y' 

	if len(''.join(lv)) == 0:
		for n in range(len(lv)): lv[n] = 'Y'
		lv_txt =''
	elif len(''.join(lv)) == 1:
		for n in range(len(lv)):
			if lv[n] == 'Y': lv_txt = lv_header[n]+'+' 
	elif len(''.join(lv)) == 2:
		lv_txt =[]
		for n in range(len(lv)):
			if lv[n] == 'Y': lv_txt.append(lv_header[n])
		lv_txt = '~'.join(lv_txt)+'+'
	else: lv_txt =''

	return [lv_txt] + lv

	
def mktype(category, title):		
	if category =='토익':
		tp1 = re.compile('LC')
		tp2 = re.compile('RC')
		tp3 = re.compile('종합')
		tp4 = re.compile('스터디|밀착')
		tp5 = re.compile('문제')
		tp6 = re.compile('완성')
		tp7 = re.compile('시험')
		tp8 = re.compile('무료|인강')
		tp9 = re.compile('')
		tp10= re.compile('')		
	elif category == '토플':
		tp1 = re.compile('Reading')
		tp2 = re.compile('Listening')
		tp3 = re.compile('Writing')
		tp4 = re.compile('Speaking')
		tp5 = re.compile('문법|어휘')
		tp6 = re.compile('종합')
		tp7 = re.compile('문제|모의')
		tp8 = re.compile('완성')
		tp9 = re.compile('유학')
		tp10= re.compile('')
	elif category == '토익스피킹':
		tp1 = re.compile('문제|모의')
		tp2 = re.compile('완성')
		tp3 = re.compile('')
		tp4 = re.compile('')
		tp5 = re.compile('')
		tp6 = re.compile('')
		tp7 = re.compile('')
		tp8 = re.compile('')
		tp9 = re.compile('')
		tp10= re.compile('')
	elif category == '오픽':
		tp1 = re.compile('단과')
		tp2 = re.compile('스터디|밀착')
		tp3 = re.compile('문제|모의')
		tp4 = re.compile('완성')
		tp5 = re.compile('무료|인강')
		tp6 = re.compile('')
		tp7 = re.compile('')
		tp8 = re.compile('')
		tp9 = re.compile('')
		tp10= re.compile('')
	elif category == '텝스':
		tp1 = re.compile('Reading')
		tp2 = re.compile('Listening')
		tp3 = re.compile('Speaking')
		tp4 = re.compile('Grammar')
		tp4 = re.compile('Vocabulary')
		tp5 = re.compile('스터디|밀착')
		tp6 = re.compile('문제|모의')
		tp7 = re.compile('완성')
		tp8 = re.compile('')
		tp9 = re.compile('')
		tp10= re.compile('')
	elif category == '아이엘츠':
		tp1 = re.compile('Reading')
		tp2 = re.compile('Listening')
		tp3 = re.compile('Writing')
		tp4 = re.compile('Speaking')
		tp5 = re.compile('General')
		tp6 = re.compile('Academic')
		tp7 = re.compile('문제|모의')
		tp8 = re.compile('완성')
		tp9 = re.compile('무료|인강')
		tp10= re.compile('')
	elif category == '일반영어':
		tp1 = re.compile('문법')
		tp2 = re.compile('어휘')
		tp3 = re.compile('독해')
		tp4 = re.compile('청취')
		tp5 = re.compile('회화')
		tp6 = re.compile('영작')
		tp7 = re.compile('비지니스')
		tp8 = re.compile('기초')
		tp9 = re.compile('')
		tp10= re.compile('')
	else: pass

	tp_header = api.type(category)
	tp = ['','','','','','','','','',''][0:len(tp_header)]
	tpr = [tp1,tp2,tp3,tp4,tp5,tp6,tp7,tp8,tp9,tp10][0:len(tp_header)]
	for n in range(len(tp)):
		if tpr[n].search(title): tp[n] = 'Y' 

	return tp



def off():
	with open('/Users/choon/py3.5/gcrawler/'+'강사.txt','r' ,encoding="utf-8") as file: tc_data =file.read().replace('\\n','')
	strDate = datetime.datetime.now().strftime("%y%m%d")
	now_y = datetime.date.today().year
	now_m = datetime.date.today().month
	if len(str(now_m)) == 1: yymm = str(now_y)+'0'+str(now_m)
	else: yymm = str(now_y)+str(now_m)
	# if now_m == 12: months = ['12','1']
	# else: months = [str(now_m), str(now_m+1)]
	month = '8'
	institute = 'YBM'
	branc_dict =  {
		'1':'종로센터',
		'12':'종로e4u센터',
		'2':'강남센터',
		'5':'강남대로센터',
		'4':'신촌센터',
		'3':'영등포센터',
		'28':'구로센터',
		'41':'건대센터',
		'25':'분당센터',
		'27':'부평센터',
		'6':'주안센터',
		'11':'대전센터',
		'7':'대구범어동센터',
		'8':'대구동성로센터',
		'10':'부산서면센터',
		'9':'부산광복센터',
		'39':'부산대센터'
		}
	categ_dict = {
		'1031686':'토익', 
		'1031688':'토플', 
		'1031687':'토익스피킹', 
		'1031689':'오픽', 
		'1031691':'텝스', 
		'1031690':'아이엘츠', 
		'1031692':'일반영어',
		'1031693':'일반영어'
		}	
	sNames = {
		'1031686':'TOEIC', 
		'1031688':'TOEFL', 
		'1031687':'TOEIC+Speaking', 
		'1031689':'OPIc', 
		'1031691':'TEPS', 
		'1031690':'IELTS', 
		'1031692':'영문법/영작문/청취/취업대비',
		'1031693':'한인회화/원어민회화/어학연수/Business English'
		}	

	sCodes = list(branc_dict.keys())
	branches = list(branc_dict.values())

	# 과목별 파일생성
	categories = ['토익','토플','토익스피킹','오픽','텝스','아이엘츠','일반영어']
	for n in range(len(categories)):
		category = categories[n]
		mk_header = api.mk_header(category,'off')
		file_name = month+'_'+category+'_'+institute+'_'+strDate+'.csv'
		with open('/Users/choon/py3.5/'+file_name,'w',newline="\n", encoding="utf-8") as file: 
			file = csv.writer(file ,delimiter=',')
			file.writerow('')
			file.writerow(mk_header)
	
	# 강의 리스트 데이터
	BASE_URL = 'http://m.ybmedu.com/config/hakwonJSON/txtToJson.asp?code=reg'
	data = json.loads(requests.get(BASE_URL).text)
	redata =[]
	for n in range(len(data)):
		if data[n]['bgSeq'] in list(sNames.keys()):
			if data[n]['sCode'] in sCodes: 
				if data[n]['cnt'] != '0': redata.append(data[n])
	for n in range(len(redata)):
		pt_seq = redata[n]['pt_seq']		
		sCode = redata[n]['sCode']
		bgSeq = redata[n]['bgSeq']
		category = categ_dict[bgSeq]
		part_name = redata[n]['part_name']
		lecdata = requests.post(
			'http://m.ybmedu.com/register/class_list_json.asp',
			data={
				'pt_seq':pt_seq,
				'sCode':sCode,
				'orgCheck':'0'
				}
			)
		lecdata = json.loads(lecdata.text)	
		branch = branc_dict[sCode]
		for num in range(len(lecdata)):
			#book = lecdata[num]['bookName']
			sj_seq = lecdata[num]['sj_seq']
			tit = html.parser.HTMLParser().unescape(lecdata[num]['sjt_name'])
			title = '['+month+'월] '+ tit.split(',')[0].replace('[','(').replace(']',')')
			
			lectable = requests.post(
				'http://m.ybmedu.com/register/teacher_time_table_json.asp',
				data={
					'sj_seq':sj_seq,
					'sCodeVal':sCode,
					'orgCheck':'0'
				}
			)
			lectable = json.loads(lectable.text)['classInfo'][0]['classDetail']
			for lt in range(len(lectable)):
				lect = lectable[lt]
				#마감여부 체크
				if lect['state'] == '마감': pass
				else:
					sale_id = lect['cl_seq']
					level = lect['level']
					price = lect['pay'].replace(',','')
					time = lect['time'].replace(' ','').replace(':','').split('~')
					st_t = time[0]
					ed_t = time[1]
					url = 'http://m.ybmedu.com/register/register_view.asp?sCode='+sCode+'&pt_seq='+pt_seq+'&sj_seq='+sj_seq+'&orgCheck=0'+'&bgSeq='+bgSeq+'&mode=cate'

					
					week = lect['weekend']
					[w1,w2,w3,w4,w5,w6,w7] =['','','','','','','']
					if '주5일' in week: week = '월화수목금'
					if '월' in week: w1 = 'Y'
					if '화' in week: w2 = 'Y'
					if '수' in week: w3 = 'Y'
					if '목' in week: w4 = 'Y'
					if '금' in week: w5 = 'Y'
					if '토' in week: w6 = 'Y'
					if '일' in week: w7 = 'Y'
					wk_txt = ''
					if 'Y' not in [w1,w2,w3,w4,w5,w6,w7]:wk_txt = week
					wk_list = [w1,w2,w3,w4,w5,w6,w7,wk_txt]
				
					lv_list = mklevel(category, level)
					tp_list = mktype(category, tit)
				
					tc_txt=[]
					tc_code=[]
					teachers = lect['teacher']
					if len(teachers) == 1: 
						tcnames = html.parser.HTMLParser().unescape(teachers[0]['name'])
						tc_name = tcnames.split('(')[0]
						if tc_name in tcdict: 
							tc_code = tcdict[tc_name]
							tc_txt = ''
						else: 
							tc_txt = tc_name
							tc_code =''
					else:
						tcnames =[]
						for t in range(len(teachers)):
							tcname = html.parser.HTMLParser().unescape(teachers[t]['name'])
							tcnames.append(tcname)
							tc_name = tcname.split('(')[0]
							if tc_name in tcdict:
								if tcdict[tc_name] not in tc_code: tc_code.append(tcdict[tc_name])
							else:
								if tc_name not in tc_txt: tc_txt.append(tc_name)
						tcnames = ' '.join(tcnames)
						tc_txt = '//'.join(tc_txt)
						tc_code = '//'.join(tc_code)

					

				
				
					

					file_name = month+'_'+category+'_'+institute+'_'+strDate+'.csv'
					with open('/Users/choon/py3.5/'+file_name,'a',newline="\n", encoding="utf-8") as file: 
						file = csv.writer(file ,delimiter=',')							
						file.writerow([branch, title, st_t, ed_t, tc_txt, tc_code, price, url] + wk_list+ lv_list + tp_list)	

off()
