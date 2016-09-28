# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re, datetime, requests, html.parser, api, csv

def mklevel(category, level):
	if category =='토익':
		lv1 = re.compile('기초|왕초보|필수|입문')
		lv2 = re.compile('기본')
		lv3 = re.compile('중급')
		lv4 = re.compile('정규')
		lv5 = re.compile('실전')
	elif category == '토플':
		lv1 = re.compile('기초|왕초보|필수|입문')
		lv2 = re.compile('기본|베이직|Grammar Start|Academic Writing')
		lv3 = re.compile('중급|intermediate|베이직|영문분석')
		lv4 = re.compile('정규|Hackers LC|Hackers RC|Hackers Writing|Hackers Speaking|Hackers Grammar|영문분석')
		lv5 = re.compile('실전|영문분석')
	elif category == '토익스피킹':
		lv1 = re.compile('입문')
		lv2 = re.compile('기본')
		lv3 = re.compile('기본|중급')
		lv4 = re.compile('중급|실전')
		lv5 = re.compile('실전')
	elif category == '오픽':
		lv1 = re.compile('입문')
		lv2 = re.compile('기본')
		lv3 = re.compile('중급')
		lv4 = re.compile('중급|실전')
		lv5 = re.compile('실전')
	elif category == '텝스':
		lv1 = re.compile('기초|왕초보|필수|입문')
		lv2 = re.compile('기본|베이직|Grammar Start|Academic Writing')
		lv3 = re.compile('중급|intermediate|베이직|영문분석')
		lv4 = re.compile('정규|Hackers LC|Hackers RC|Hackers Writing|Hackers Speaking|Hackers Grammar|영문분석')
		lv5 = re.compile('실전|영문분석')
	elif category == '아이엘츠':
		lv1 = re.compile('기초|왕초보|필수|입문')
		lv2 = re.compile('기본|베이직|Grammar Start|Academic Writing')
		lv3 = re.compile('중급|intermediate|베이직|영문분석')
		lv4 = re.compile('정규|Hackers LC|Hackers RC|Hackers Writing|Hackers Speaking|Hackers Grammar|영문분석')
		lv5 = re.compile('실전|영문분석')
	elif category == '일반영어':
		lv1 = re.compile('기초|왕초보|필수|입문')
		lv2 = re.compile('기본|베이직|Grammar Start|Academic Writing')
		lv3 = re.compile('중급|intermediate|베이직|영문분석')
		lv4 = re.compile('정규|Hackers LC|Hackers RC|Hackers Writing|Hackers Speaking|Hackers Grammar|영문분석')
		lv5 = re.compile('실전|영문분석')
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
		tp2 = re.compile('RC|Reading')
		tp3 = re.compile('종합')
		tp4 = re.compile('소수|밀착|스터디')
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
		tp2 = re.compile('소수|밀착|스터디')
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
	with open('/Users/choon/py3.5/gcrawler/'+'강사.txt','r' ,encoding="utf-8") as file: 
		tc_data =file.read().replace('\\n','')
	print(tc_data)

	strDate = datetime.datetime.now().strftime("%y%m%d")
	# now_y = datetime.date.today().year
	# now_m = datetime.date.today().month
	# monthes = [str(now_m), str(now_m+1)]
	month = '10'
	institute = '해커스'
	branc_dict = {'1':'강남역캠퍼스','2':'종로캠퍼스','3':'대구캠퍼스'}       
	branc_categ_dict = {
		'1':{'토플':'1','토익':'2','텝스':'3','토스&오픽':'4','일반영어':'5','아이엘츠':'7'},
		'2':{'토플':'11','토익':'12','토스&오픽':'13','일반영어':'14'},
		'3':{'토익':'21','토스&오픽':'22'}
		}
	m_branc_categ_dict = {
		'1':{'토플':'1','토익':'4','텝스':'6','토스&오픽':'11','일반영어':'9','아이엘츠':'7'},
		'2':{'토플':'1','토익':'4','토스&오픽':'11','일반영어':'9'},
		'3':{'토익':'4','토스&오픽':'11'}
		}
	'''
	모바일은 가격정보 등 리스트에 정보가 부족해 PC에서 데이터 수집
	'''	
	# 과목별 파일 만들기
	categories = list(branc_categ_dict['1'].keys())
	# for m in range(len(monthes)):
	# 	month = monthes[m]
	for n in range(len(categories)):
		category = categories[n]
		if category == '토스&오픽':
			for category in ['토익스피킹', '오픽']:
				mk_header = api.mk_header(category,'off')
				file_name = month+'_'+category+'_'+institute+'_'+strDate+'.csv'
				with open('/Users/choon/Documents/'+file_name,'w',newline="\n", encoding="utf-8") as file: 
					file = csv.writer(file ,delimiter=',')
					file.writerow('')
					file.writerow(mk_header)
		mk_header = api.mk_header(category,'off')
		file_name = month+'_'+category+'_'+institute+'_'+strDate+'.csv'
		with open('/Users/choon/Documents/'+file_name,'w',newline="\n", encoding="utf-8") as file: 
			file = csv.writer(file ,delimiter=',')
			file.writerow('')
			file.writerow(mk_header)


	bran_codes = list(branc_dict.keys()) # 학원지점번호 리스트
	for n in range(len(bran_codes)): 
		bran_code = bran_codes[n] # 학원지점번호
		branch = branc_dict[bran_code] # 학원지점명
		bran_categs = list(branc_categ_dict[bran_code].keys()) # 지점별과목 리스트
		
		for num in range(len(bran_categs)):
			category = bran_categs[num] #과목명
			categ_code = branc_categ_dict[bran_code][category] #과목코드
			m_categ_code = m_branc_categ_dict[bran_code][category] #모바일 과목코드
			SEED_URL = "http://www.hackers.ac/site/?st=lecture&idx=201&no="+categ_code+"&loc="+bran_code
			data = requests.get(SEED_URL)
			data = BeautifulSoup(data.text, 'html.parser', from_encoding="utf-8")
			data = html.parser.HTMLParser().unescape(data)
			lects = data.select('.table-base')[0].select('table')[0].select('tbody')[0].select('tr')
			for nm in range(len(lects)):
				lect = lects[nm]
				title = lect.select('td')[0].text.strip().replace('"','').replace(',','.')
				
				if category == '토스&오픽':
					if '토익스피킹' in title: category = '토익스피킹'
					else: category = '오픽'
				if lect.select('td')[4].text.strip().replace(' ','') == '마감': pass
				else:
					wtime = lect.select('td')[1].text.replace(' ','').strip().split()
					[w1,w2,w3,w4,w5,w6,w7] =['','','','','','','']
					week = wtime[0]
					w = week.replace('월~금','월,화,수,목,금')				
					if '월' in w: w1 = 'Y'
					if '화' in w: w2 = 'Y'
					if '수' in w: w3 = 'Y'
					if '목' in w: w4 = 'Y'
					if '금' in w: w5 = 'Y'
					if '토' in w: w6 = 'Y'
					if '일' in w: w7 = 'Y'
					if '[' in week: wk_txt = week
					elif '(' in week: wk_txt = week
					else: wk_txt = ''
					wk_list = [w1,w2,w3,w4,w5,w6,w7,wk_txt]
					time = wtime[1]#.split('<')[0].replace('>','').strip().replace(':','')
					st_t = time.split('~')[0].replace(':','')
					ed_t = time.split('~')[1].replace(':','')
					
					price = lect.select('td')[3]
					if price.select('span') == []: price = price.text.replace('원','').replace(',','').strip()	
					else: price = price.select('span')[-1].text.replace('원','').replace(',','').strip()
					
					sale_id = str(lect.select('td')[0].a).split('="')[1].split('">')[0].replace('s','')
					url = 'http://m.hackers.ac/dev/lecture/view.php?location='+bran_code+'&menu_no='+m_categ_code+'&num=&lecture_no='+sale_id
				
					lv_list = mklevel(category, title)
					tp_list = mktype(category, title)		
					
					tc_list=[]
					tc_txt=[]
					tc_code=[]
					teachers = lect.select('td.tr_name')[0].select('a')

					if len(teachers) == 0 : 
						teachers = lect.select('td.tr_name')[0].font.contents[::2]
						for tc in range(len(teachers)): tc_list.append(teachers[tc].strip())
					else: 
						for tc in range(len(teachers)): tc_list.append(teachers[tc].text)				

					if len(tc_list) > 1 :
						for tc in range(len(tc_list)):
							tc_name = tc_list[tc]
							if tc_name=='':tc_name = '-'
							tcsearch = re.findall('TC.....'+tc_name,tc_data)
							if len(tcsearch) == 0: tc_txt.append(tc_name)
							elif len(tcsearch) == 1: tc_code.append(tcsearch[0][0:7])
							else:
								tc_txt.append(tc_name)
								with open('/Users/choon/Documents/'+'강사중복.txt','a',encoding='utf-8') as tcError:
									tcError.write(strDate+'-'+institute+'__'+tc_name+'__'+title+'\n')						
						if len(tc_txt)==1: tc_txt = tc_txt[0]
						else: tc_txt ='//'.join(tc_txt)
						if len(tc_code)==1: tc_code = tc_code[0]
						else: tc_code ='//'.join(tc_code)

					else: 
						tc_name = tc_list[0]
						if tc_name=='':tc_name = '-'
						tcsearch = re.findall('TC.....'+tc_name,tc_data)
						if len(tcsearch) == 0: 
							tc_code = ''
							tc_txt = tc_name
						elif len(tcsearch) == 1: 
							tc_code = tcsearch[0][0:7]
							tc_txt = ''
						else: 
							tc_code = ''
							tc_txt = tc_name
							with open('/Users/choon/Documents/'+'강사중복.txt','a',encoding='utf-8') as tcError:
								tcError.write(strDate+'-'+institute+'__'+tc_name+'__'+title+'\n')

					file_name = month+'_'+category+'_'+institute+'_'+strDate+'.csv'
					with open('/Users/choon/Documents/'+file_name,'a',newline="\n", encoding="utf-8") as file: 
						file = csv.writer(file ,delimiter=',')							
						file.writerow([branch, title, st_t, ed_t, tc_txt, tc_code, price, url] + wk_list + lv_list + tp_list)	

off()

