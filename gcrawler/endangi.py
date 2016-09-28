# -*- coding:utf-8 -*-
import re, datetime, requests, html.parser, json, urllib
import csv, api
from bs4 import BeautifulSoup

def mklevel(category, level):
	lv_header = api.level(category)
	lv_txt =''
	[l1,l2,l3,l4,l5]=['','','','','']
	if category =='토익':
		lv1 = re.compile('68|126')
		lv2 = re.compile('68|69|126|127')
		lv3 = re.compile('69|70|128|127')
		lv4 = re.compile('70|71|129|128')
		lv5 = re.compile('71|129')
	elif category =='토플':
		lv1 = re.compile('72')
		lv2 = re.compile('72|73')
		lv3 = re.compile('73|74')
		lv4 = re.compile('74|75')
		lv5 = re.compile('75|76')		
	elif category =='토익스피킹':
		lv1 = re.compile('77')
		lv2 = re.compile('77|78')
		lv3 = re.compile('78|79')
		lv4 = re.compile('79|130')
		lv5 = re.compile('130|132')
	elif category =='오픽':
		lv1 = re.compile('00')
		lv2 = re.compile('80')
		lv3 = re.compile('81')
		lv4 = re.compile('82')
		lv5 = re.compile('00')
	elif category =='텝스':
		lv1 = re.compile('86')
		lv2 = re.compile('00')
		lv3 = re.compile('87')
		lv4 = re.compile('00')
		lv5 = re.compile('88')
	elif category =='일반영어':
		lv1 = re.compile('83')
		lv2 = re.compile('00')
		lv3 = re.compile('84')
		lv4 = re.compile('00')
		lv5 = re.compile('8 5')							
	else: pass

	lv_header = api.level(category)
	lv = ['','','','',''][0:len(lv_header)]
	lvr = [lv1,lv2,lv3,lv4,lv5][0:len(lv_header)]
	for n in range(len(lv)):
		if lvr[n].match(level): lv[n] = 'Y' 

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
		tp1 = re.compile('LC단과')
		tp2 = re.compile('RC단과')
		tp3 = re.compile('종합')
		tp4 = re.compile('CARE')
		tp5 = re.compile('문제')
		tp6 = re.compile('완성')
		tp7 = re.compile('대비')
		tp8 = re.compile('스마트')
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
		tp8 = re.compile('단기')
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
		tp2 = re.compile('CARE')
		tp3 = re.compile('문제')
		tp4 = re.compile('단기')
		tp5 = re.compile('인강')
		tp6 = re.compile('')
		tp7 = re.compile('')
		tp8 = re.compile('')
		tp9 = re.compile('')
		tp10= re.compile('')
	elif category == '텝스':
		tp1 = re.compile('독해')
		tp2 = re.compile('청취')
		tp3 = re.compile('Speaking')
		tp4 = re.compile('문법')
		tp5 = re.compile('어휘')
		tp6 = re.compile('CARE')
		tp7 = re.compile('문제')
		tp8 = re.compile('완성')
		tp9 = re.compile('')
		tp10= re.compile('')
	# elif category == '아이엘츠':
	# 	tp1 = re.compile('')
	# 	tp2 = re.compile('')
	# 	tp3 = re.compile('')
	# 	tp4 = re.compile('')
	# 	tp5 = re.compile('')
	# 	tp6 = re.compile('')
	# 	tp7 = re.compile('')
	# 	tp8 = re.compile('')
	# 	tp9 = re.compile('')
	# 	tp10= re.compile('')
	elif category == '일반영어':
		tp1 = re.compile('문법')
		tp2 = re.compile('어휘')
		tp3 = re.compile('독해')
		tp4 = re.compile('청취')
		tp5 = re.compile('회화|발음|스피킹')
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
	teachers = ''
	t = open('/Users/choon/py3.5/gcrawler/'+'강사.txt','r' ,encoding="utf-8")
	while True:
		line = t.readline()
		if not line: break
		teachers = teachers + line
	t.close()
	print(teachers)
	
	strDate = datetime.datetime.now().strftime("%y%m%d")
	now_y = datetime.date.today().year
	now_m = datetime.date.today().month
	
	if now_m == 12: months = ['12','1']
	else: months = [str(now_m), str(now_m+1)]

	institute = '영단기'
	branches = ['강남','부산본관']
	categs = {'11':'토익','12':'토플','13':'토스','28':'오픽','29':'회화/작문','30':'텝스'}
	br_categ = {'강남':['11','12','13','28','29','30'],'부산본관':['11','13','29']}	
	subject_ids = list(categs.keys())
	categories = list(categs.values())	

	# 과목별 파일 만들기	
	for m in range(len(months)):
		month = months[m]
		for n in range(len(categories)):
			category =categories[n]
			if category == '토스': category = '토익스피킹'
			if category == '회화/작문': category = '일반영어'
			mk_header = api.mk_header(category,'off')
			file_name = month+'_'+category+'_'+institute+'_'+strDate+'.csv'
			with open('/Users/choon/Documents/'+file_name,'w',newline="\n", encoding="utf-8") as file: 
				file = csv.writer(file ,delimiter=',')
				file.writerow('')
				file.writerow(mk_header)

	# 강의 리스트 데이터
	for b in range(len(branches)):
		branch = branches[b]
		subject_ids = br_categ[branch]
		for n in range(len(subject_ids)):
			subject_id = subject_ids[n]
			category = categs[subject_id]
			if category == '토스': category = '토익스피킹'
			if category == '회화/작문': category = '일반영어'

			if branch == '강남': 
				data = requests.post(
					'http://offeng.dangi.co.kr/m/registration/main/get_products',
					data={
						'subject_id':subject_id,
						'level_id':'',
						'store_category_ids':10,
						'course_week':'HHHHHHH',
						's_time':"01:59",
						'e_time':"23:59",
						'course_category':''
						}
					)	
			else: 
				data = requests.post(
					'http://eng.dangi.co.kr/m/busan/registration/main/get_products',
					data={
						'subject_id':subject_id,
						'level_id':'',
						'course_week':'HHHHHHH',
						's_time':"01:59",
						'e_time':"23:59",
						'course_category':''
						}
					)	
			products = json.loads(data.text)['dataset']['products']

			for num in range(len(products)):
				lect = products[num]
				title = str(BeautifulSoup(lect['sale_name'],'html.parser').text)
				title = title.replace('"','').replace(',','-').strip()
				price = lect['amt_list'][0]['display_sale_amt']
				# try:price = lect['amt_list'][0]['display_sale_amt']
				# except: print (lect['amt_list'])
				st_t = lect['lec_time'].split('~')[0].replace(':','')
				ed_t = lect['lec_time'].split('~')[1].replace(':','')
			 	# st_d = lect['cole_sdt'] 개강일
				# ed_d = lect['cole_edt'] 종강일
				saleinfo_id = lect['saleinfo_id']
				if branch == '강남':
					url = 'http://offeng.dangi.co.kr/m/registration/main/view?saleinfo_id='+ str(saleinfo_id)	
				else: url = 'http://eng.dangi.co.kr/m/busan/registration/main/view?saleinfo_id='+ str(saleinfo_id)
				
				week = lect['lec_week'].replace('"','').strip()
				wk_txt = '' 
				[w1,w2,w3,w4,w5,w6,w7]=['','','','','','','']
				if '월' in week: w1 = 'Y'
				if '화' in week: w2 = 'Y'
				if '수' in week: w3 = 'Y'
				if '목' in week: w4 = 'Y'
				if '금' in week: w5 = 'Y'
				if '토' in week: w6 = 'Y'
				if '일' in week: w7 = 'Y'	
				wk_list = [w1,w2,w3,w4,w5,w6,w7,wk_txt]

				level = str(lect['level_id'])
				lv_list = mklevel(category, level)
				tp_list = mktype(category, title)	

				if lect['sale_status'] =='HD':
					with open('/Users/choon/Documents/'+'마감강의.txt','a',encoding='utf-8') as endfile:
						endfile.write(strDate+'-'+institute+'__'+title+'\n')
				
				tc_txt=[]
				tc_code=[]
				if lect['team_yn']=='Y': # 강사 복수(팀)인 경우
					for tm in range(len(lect['team_detail'])): 
						tc_name = lect['team_detail'][tm]['tec_nm']
						tc = re.findall('TC.....'+tc_name,teachers)
						if len(tc) == 0: tc_txt.append(tc_name)
						elif len(tc) == 1: tc_code.append(tc[0][0:7])
						else: # 강사 중복 파일로 저장 
							tc_txt.append(tc_name)
							with open('/Users/choon/Documents/'+'강사중복.txt','a',encoding='utf-8') as tcError:
								tcError.write(strDate+'-'+institute+'__'+tc_name+'__'+title+'\n')
					if len(tc_txt)==1: tc_txt = tc_txt[0]
					else: tc_txt ='//'.join(tc_txt)
					if len(tc_code)==1: tc_code = tc_code[0]
					else: tc_code ='//'.join(tc_code)


				elif lect['team_yn']=='N': 
					tc_name = lect['teacher_name']
					tc = re.findall('TC.....'+tc_name,teachers)
					if len(tc) == 0: 
						tc_code = ''
						tc_txt = tc_name
					elif len(tc) == 1: 
						tc_code = tc[0][0:7]
						tc_txt = ''
					else: 
						tc_code = ''
						tc_txt = tc_name
						with open('/Users/choon/Documents/'+'강사중복.txt','a',encoding='utf-8') as tcError:
							tcError.write(strDate+'-'+institute+'__'+tc_name+'__'+title+'\n')
				else:pass


				if months[0]+'월' in title: file_name = months[0]+'_'+category+'_'+institute+'_'+strDate+'.csv' 
				else: file_name = months[1]+'_'+category+'_'+institute+'_'+strDate+'.csv'	
				with open('/Users/choon/Documents/'+file_name,'a',newline="\n", encoding="utf-8") as file: 
					file = csv.writer(file ,delimiter=',')	
					file.writerow([branch, title, st_t, ed_t, tc_txt, tc_code, price, url] + wk_list + lv_list + tp_list)		
				
off()