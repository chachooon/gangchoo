# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re, csv, datetime, requests, api

def mklevel(category, level):
	if category =='토익':
		lv1 = re.compile('600|기초|첫토익|내생토|내.생.토')
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
		lv2 = re.compile('')#5
		lv3 = re.compile('600|650')#6
		lv4 = re.compile('700|750|기출문제풀이|실전')
		lv5 = re.compile('800|850|기출문제풀이|실전')#800
	elif category == '아이엘츠':
		lv1 = re.compile('기초|입문')
		lv2 = re.compile('5.5|기초|입문')#5.5
		lv3 = re.compile('6.0')#6.0
		lv4 = re.compile('6.5')#6.5
		lv5 = re.compile('7.0')#7.0
	elif category == '일반영어':
		lv1 = re.compile('기초|초보')
		lv2 = re.compile('')
		lv3 = re.compile('중급')
		lv4 = re.compile('')
		lv5 = re.compile('고급|심화')
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
	institute = '파고다'
	branc_dict = {'04':'강남학원','01':'종로학원','02':'신촌학원','08':'여의도학원','12':'부평학원','30':'부산대학원','05':'서면학원','25':'대연학원'}
	categ_code_dict = {
		# '토익':['260'],
		# '토플':['250'], 
		# '토익스피킹':['251'],
		# '오픽':['391'],
		# '텝스':['270'],
		# '아이엘츠':['310'], 
		'일반영어':['110','120','200','210','220','230','240']
		}
	categ_bran_dict = {
		# '260':['04','01','02','08','12','30','05','25'],
		# '250':['04','01','02','12','05','30','25'], 
		# '251':['04','01','02','12','05','30','25'],
		# '391':['04','01','02','08','12','05','30','25'],
		# '270':['04','01','02','05','30'],
		# '310':['04','01','02','12','05','25'], 
		'110':['04','01','02','08','12','30','25'],
		'120':['04','01','02','08','12','30','05','25'],
		'200':['05','25'],
		'210':['04','01','02','08','12','30','05'],
		'220':['04','01','02','30','05'],
		'230':['04','01','02','12','05'],
		'240':['04','01']
		}
	
	# 과목별 파일생성
	categories = list(categ_code_dict.keys())
	for n in range(len(categories)):
		category = categories[n]
		mk_header = api.mk_header(category,'off')
		file_name = month+'_'+category+'_'+institute+'_'+strDate+'.csv'
		with open('/Users/choon/py3.5/'+file_name,'w',newline="\n", encoding="utf-8") as file: 
			file = csv.writer(file ,delimiter=',')
			file.writerow('')
			file.writerow(mk_header)
	
	for n in range(len(categories)): # 과목별 데이터 가공
		category = categories[n]
		categ_codes = categ_code_dict[category]
		for c in range(len(categ_codes)):
			subjcode = categ_codes[c]		
			brancodes = categ_bran_dict[subjcode]
			for b in range(len(brancodes)): # typecode 구하기
				brancode = brancodes[b]
				branch = branc_dict[brancode]
				BASE_URL = "http://m.pagoda21.com/m/register/class/step1Two.do?subjcode=" + subjcode +"&brancode=" + brancode 
				data = BeautifulSoup(requests.get(BASE_URL).text, 'html.parser')	
				typecode_list = data.select('ul.accordion_list')[0].select('li')
				print(category+branch+'_'+str(len(typecode_list))+'typecodes')

				for t in range(len(typecode_list)):
					typecode = typecode_list[t]['id'].split('_')[-1]

					data2 = requests.post(
						'http://m.pagoda21.com/m/register/class/ajax/getTimeMobile.do',
						data={
							'yymm':yymm,
							'schedule':yymm,
							'branch':brancode,
							'subjcode':subjcode,
							'classterm':'all',
							'courses':yymm+'/'+brancode+'/aaaa/all/N',
							'typecode':typecode,
							'schgubun':'lectgb',
							'mobileChk':'Y',
							'ordergubun':'time'
							}
						)	
					data2 = BeautifulSoup(data2.text, 'html.parser')
					lects = data2.select('.lect_area > ul > li')
					for num in range(len(lects)):
						lect = lects[num].select('.cn_box')[0]
						link= lect.select('a')[0]['href'].replace("'","").split(",")
						if len(link)<5: print('url_error')
						else:
							sale_id = brancode + link[2]+link[3]+link[4]+link[5]
							url='http://m.pagoda21.com/m/lecture/detail/'+sale_id+'?yymm='+yymm
							if len(lect.select('.class_tit'))>0:
								title = lect.select('.class_tit')[0].text.replace(month+'월','['+month+'월] ')

								st_t = lect.select('.class_sch > span:nth-of-type(3)')[0].text.split('~')[0].strip().replace(':','')
								ed_t = lect.select('.class_sch > span:nth-of-type(3)')[0].text.split('~')[1].strip().replace(':','')	
								week = lect.select('.class_sch > span:nth-of-type(2)')[0].text				
								[w1,w2,w3,w4,w5,w6,w7] =['','','','','','','']
								if '월' in week: w1 = 'Y'
								if '화' in week: w2 = 'Y'
								if '수' in week: w3 = 'Y'
								if '목' in week: w4 = 'Y'
								if '금' in week: w5 = 'Y'
								if '토' in week: w6 = 'Y'
								if '일요반' in week: w7 = 'Y'
								if '토일' in week: w7 = 'Y'
								if '기타' in week: [w1,w2,w3,w4,w5,w6,w7] =['Y','Y','Y','Y','Y','','']
								if '주5일' in week: [w1,w2,w3,w4,w5,w6,w7] =['Y','Y','Y','Y','Y','','']
								wt = ''
								exc =['특별반','2주반','주4일']
								for e in range(len(exc)):	
									if exc[e] in week: 
										[w1,w2,w3,w4,w5,w6,w7] =['Y','Y','Y','Y','Y','','']
										wt = week
								wk_list= [w1,w2,w3,w4,w5,w6,w7,wt]

								price = lect.select('.txt_price')[0].text.replace('"','').replace(',','').replace('원','').strip()
								lv_list = mklevel(category, title)
								tp_list = mktype(category, title)	

								 #마감강의 걸러내기
								if 'ico_end' in str(lect): pass
									# with open('C:\\'+'마감강의.txt','a',encoding='utf-8') as endfile:
									# 	endfile.write(strDate+'-'+institute+'__'+title+'\n')			
								else:
									tc_txt=[]
									tc_code=[]
									teacher1 = lect.select('.img_name')[0].text.strip()
									if len(lect.select('.class_name'))>0: teacher2 = lect.select('.class_name')[0].text
									else: teacher2 =''
									
									if teacher2=='': 
										tc_name = teacher1
										if tc_name=='':tc_name = '-'
										tc = re.findall('TC.....'+tc_name,tc_data)	
										if len(tc) == 0: 
											tc_code = ''
											tc_txt = tc_name
										elif len(tc) == 1: 
											tc_code = tc[0][0:7]
											tc_txt = ''
										else: 
											tc_code = ''
											tc_txt = tc_name
											with open('/Users/choon/py3.5/'+'강사중복.txt','a',encoding='utf-8') as tcError:
												tcError.write(strDate+'-'+institute+'__'+tc_name+'__'+title+'\n')								

									else: 
										teachers = str(teacher2).split(',')
										for tcs in range(len(teachers)):
											tc_name = teachers[tcs].strip()
											if tc_name=='': tc_name='-'
											tc = re.findall('TC.....'+tc_name,tc_data)
											if len(tc) == 0: tc_txt.append(tc_name)
											elif len(tc) == 1: tc_code.append(tc[0][0:7])
											else: # 강사 중복 파일로 저장 
												tc_txt.append(tc_name)
												with open('/Users/choon/py3.5/'+'강사중복.txt','a',encoding='utf-8') as tcError:
													tcError.write(strDate+'-'+institute+'__'+tc_name+'__'+title+'\n')
										if len(tc_txt)==1: tc_txt = tc_txt[0]
										else: tc_txt ='//'.join(tc_txt)
										if len(tc_code)==1: tc_code = tc_code[0]
										else: tc_code ='//'.join(tc_code)

									file_name = month+'_'+category+'_'+institute+'_'+strDate+'.csv'
									with open('/Users/choon/py3.5/'+file_name,'a',newline="\n", encoding="utf-8") as file: 
										file = csv.writer(file ,delimiter=',')							
										file.writerow([branch, title, st_t, ed_t, tc_txt, tc_code, price, url] + wk_list + lv_list + tp_list)	

							else: print('no title')

off()




