import requests
import json

#url = "http://www.eatsight.com/portal/searchDetail/result"
'''	'type04': 500,	#encodeURI

'type05': 1,	#영업점 체크박스1
	'type07': 1,	#PB센터 체크박스3
	'type08': 1,	#대여금고 체크박스4
	'type10': 5,	#pagesize
	'type24': 1,	#영업점방문상담여부13
	'type25': 1,	#디지털창구11
	'type26': 1,	#바이오인증12
	'type28': 0,	#영업시간특화점포여부14
	'type30': 1,	#영업점/자동화 15
	'type31': 1,	#출장소	16
	'type32': 1,	#대기업금융센터 17
	'type33': 1,	#복합점포 18
	'type34': '',		#검색명
	'type35': '',		#안내부점코드
	'type36': 596045,	#지도좌표 x left
	'type37': 598455,	#지도좌표 x right
	'type38': 793540,	#지도좌표 y bottom
	'type39': 795590,	#지도좌표 y top
	'type40': 597250,	#지도좌표 x center
	'type41': 794565,	#지도좌표 y center
	'USER_TYPE': '03'
'''
data = {
	'pageNum': 1,
	'pageSize': 5,
	'searchShopName':'' ,
	'searchSido': 30,
	'searchGugun': 3023,
	'searchDong': 30230109,
	'searchType':' ' ,
	'searchTypeService': 1,
	'searchTypeLotto': 0,
	'searchTypeToto': 0,
	'searchTypeCafe25': 0,
	'searchTypeBakery': 0,
	'searchTypeInstant': 0,
	'searchTypeDrug': 0,
	'searchTypeSelf25': 0,
	'searchTypePost': 0,
	'searchTypeBattery': 0,
	'searchTypeATM': 0,
	'searchTypeWithdrawal': 1, #인출
	'searchTypeTaxrefund': 0,
	'searchTypeGelasoft': 0,
	'searchTypeSmartAtm': 0,
	'searchTypeSelfCookingUtensils': 0

}
'''	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
	'Connection': 'keep-alive',
	'Content-Length': '264',

'Cookie': '_KB_RECENTLY_VIEW_COOKIE=20190102%3A%3ADP000013%3A%3A%uAD6D%uBBFC%uC544%uD30C%uD2B8%uC0DD%uD65C%uD1B5%uC7A5%3A%3A/quics%3Fpage%3DC016613%26cc%3Db061496%3Ab061645%3A%3A%3A%3A1%3A%3AN%3B%3B20190102%3A%3ADP000005%3A%3AKB%uC885%uD569%uD1B5%uC7A5%3A%3A/quics%3Fpage%3DC016613%26cc%3Db061496%3Ab061645%3A%3A/money/money/deposit20130801031.jpg%3A%3A1%3A%3AN%3B%3B20190102%3A%3ADP000356%3A%3AKB%uB098%uB77C%uC0AC%uB791%uC6B0%uB300%uD1B5%uC7A5%3A%3A/quics%3Fpage%3DC016613%26cc%3Db061496%3Ab061645%3A%3A/money/money/kookkun11990829257653988.jpg%3A%3A1%3A%3AN%3B%3B20190102%3A%3ADP000104%3A%3A%uC9C1%uC7A5%uC778%uC6B0%uB300%uC885%uD569%uD1B5%uC7A5%3A%3A/quics%3Fpage%3DC016613%26cc%3Db061496%3Ab061645%3A%3A/money/money/item_biz01.jpg%3A%3A1%3A%3AN%3B%3B20190102%3A%3ADP000375%3A%3AKB%20%uF95CStar%uD1B5%uC7A5%3A%3A/quics%3Fpage%3DC016613%26cc%3Db061496%3Ab061645%3A%3A/money/money/23_rockstar20151203.jpg%3A%3A1%3A%3AN%3B%3B20190102%3A%3ADP000186%3A%3AKB%20Star*t%20%uD1B5%uC7A5%3A%3A/quics%3Fpage%3DC016613%26cc%3Db061496%3Ab061645%3A%3A/money/money/12_start20151203.jpg%3A%3A1%3A%3AN%3B%3B; JSESSIONID=nGzvc8dB1fytzD8V2y2t1l8JjDLkX4GgPx0Ll3jG78NBvTy79QzZ!1507676342; QSID=6726&&QxCKc8dbHpLPblY9NLsJ2gMxdv6KWSGy015b9fg88MmVhhFLp0Ty!1169552880!1547459931816',
	'Host': 'omoney.kbstar.com',
	'''
headers = {
	

	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
	'Connection': 'keep-alive',
	'Content-Length': '420',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie': 's_fid=629A740DC4C46087-156ECF206777F5E3; _BS_GUUID=HeIJVRRUkOntfhf3M5r2jdAPT6Yvdg3VvLFqCxlX; _ga=GA1.3.218098969.1546803940; _ga=GA1.2.647712068.1546804013; JSESSIONID=14D89C8167A23FADD2DF7033C7CC807C.htomcat2; s_cc=true; _gid=GA1.3.2086264589.1547608993; _TRK_UID=f7aca2fde733b541fd7ec6961292d9bb:1:9.31777244212963:1547608993834; _TRK_CR22400=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fsm=top_hty%26fbm=1%26ie=utf8%26query=gs25; _TRK_EX22400=2; _TRK_SID=4814ad53b1cb6ea8a70170fe3f8176df; s_sq=gsretail-com-prd%3D%2526c.%2526a.%2526activitymap.%2526page%253D%2525EB%2525A7%2525A4%2525EC%25259E%2525A5%25252F%2525EC%252584%25259C%2525EB%2525B9%252584%2525EC%25258A%2525A4%25255E%2525EB%2525A7%2525A4%2525EC%25259E%2525A5%2525EA%2525B2%252580%2525EC%252583%252589%2526link%253D%2525EA%2525B2%252580%2525EC%252583%252589%2526region%253Dcontents%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253D%2525EB%2525A7%2525A4%2525EC%25259E%2525A5%25252F%2525EC%252584%25259C%2525EB%2525B9%252584%2525EC%25258A%2525A4%25255E%2525EB%2525A7%2525A4%2525EC%25259E%2525A5%2525EA%2525B2%252580%2525EC%252583%252589%2526pidt%253D1%2526oid%253Dhttp%25253A%25252F%25252Fgs25.gsretail.com%25252Fgscvs%25252Fko%25252Fstore-services%25252Flocations%252523%25253B%2526ot%253DA',
	'Host': 'gs25.gsretail.com',
	'Origin': 'http://gs25.gsretail.com',
	'Referer': 'http://gs25.gsretail.com/gscvs/ko/store-services/locations',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest'
} #post 전송방식
#params={
#	'asfilecode': 548565
#http://gs25.gsretail.com/gscvs/ko/store-services/locationList?CSRFToken=e5041d84-3c80-401d-8acd-20e3a2e290d1

#}
req = requests.post('http://gs25.gsretail.com/gscvs/ko/store-services/locationList?CSRFToken=e5041d84-3c80-401d-8acd-20e3a2e290d1', data =data,headers=headers)



#,params=params
#r = requests.head('https://omoney.kbstar.com/quics', data =json.dumps(data),headers=headers,params=params)
print(req.status_code)
#print("POST 주소확인 : " + req.url )
html = json.loads(req.text)
	
print(html)
