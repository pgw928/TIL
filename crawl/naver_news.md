# 네이버 뉴스 크롤링

> 네이버 뉴스를 크롤링하는 python 코드에 대해서 알아본다.





* #### 파이썬 패키지

  ```python
  import requests
  from lxml import html
  import time
  ```

  

* #### 저장할 .txt 파일 만드는 함수

  ```python
  def fmake_file(keyword):
      output_file_name = f"naver_news_{keyword}_{time.strftime('%y%m%d_%H%M%S')}.txt"
      output_file = open(output_file_name, 'w', encoding='utf-8')
      output_file.write("페이지\t키워드\t제목\turl\n")
      output_file.close()
      return output_file_name
  
  ```

  * `output_file_name` : 파일이름을 현재시간 관련해 만들어준다.



* #### .txt 파일 쓰는 함수

  ```python
  def fwrite_news(i, keyword, news_title_clean, news_url, output_file_name):
      output_file = open(output_file_name, 'a', encoding='utf-8')
      output_file.write(f"{i}\t{keyword}\t{news_title_clean}\t{news_url}\n")
      output_file.close()
  ```

  * `open` 을 꼭 `'a'` 조건을 넣어준다.`w`로 하면 기존 작성된 내용을 모두 지운다.



* #### 크롤링 코드

  ```python
  def fcrawl_news(i, keyword, output_file_name):
      page_num = (i - 1) * 10 + 1
  
      url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&sort=1&photo=0&field=0&pd=3&ds=2021.01.01&de=2021.04.30&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:dd,p:from20210101to20210430,a:all&start={page_num}'
      print(url)
      headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
      html_req = requests.get(url, headers=headers)
      tree = html.fromstring(html_req.content)
      bodies = tree.xpath("//ul[@class='list_news']/li")
      results = []
      for body in bodies:
          news_title = body.xpath(".//a[@class='news_tit']/@title")[0]
          news_title_clean = news_title.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')
          try:
              news_url = body.xpath(".//a[@class='info']/@href")[0]
          except:
              news_url = ''
          results.append([keyword, news_title_clean, news_url])
          fwrite_news(i, keyword, news_title_clean, news_url, output_file_name)
      return results
  ```

  * `page_num` : 기사가 한 페이지에 10개씩 등장한다. 여기서 `i`가 페이지 숫자이다.
  * `url` : 2 page를 클릭해 정확한 url 주소를 알아낸다.
  * `bodies` : 모든 페이지에 대한 각각의 기사를 덩어리채로 가져온다.
  * `try` ~ `except` 문 : 네이버뉴스 링크가 존재하지 않는 경우가 존재하기 때문에 사용한다.
  * `news_title_clean` : 공백 한칸으로 바꾸는 이유는 공백 마저 없앨시 붙지 말아야 할 부분이 붙는 경우가 생김
  * `results` : print문을 찍기 위함이다.



* #### 메인 함수

  ```python
  def fmain():
      for keyword in keywords:
          output_file_name = fmake_file(keyword)
          for i in range(1, 4):
              results = fcrawl_news(i, keyword, output_file_name)
              print(results)
              time.sleep(6)
  ```



* #### 실행 부분

  ```python
  keywords = ['킥보드', '자전거']
  fmain()
  ```

  

* #### 결과

  * `naver_news_자전거_210630_020419.txt`

    ```
    페이지	키워드	제목	url
    1	자전거	천안시의회 육종영 의원, 일자리 창출, 농업인 지원 촉구	
    1	자전거	의대생 삶 앗아간 무서운 한강 “안전은 어디에?”	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=103&oid=296&aid=0000049752
    1	자전거	자전거 탄 초등학생, 좌회전 승용차와 충돌…병원 이송 후 사망	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=421&aid=0005324829
    1	자전거	서울 길음동에서 차량·자전거 충돌...초등학생 사망	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=052&aid=0001582434
    1	자전거	자전거 타던 초등학생, 아파트 나오던 승용차와 충돌해 사망	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=469&aid=0000601491
    1	자전거	노인 변비, ‘노쇠 신호’일 수 있어 주의해야	
    1	자전거	성북구서 좌회전 차량과 자전거 충돌…초등학생 숨져	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=056&aid=0011036151
    1	자전거	서울 길음동에서 차량·자전거 충돌...초등학생 사망	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=052&aid=0001582423
    1	자전거	성북구서 자전거 타던 초등생, 승용차와 정면충돌…사망	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=079&aid=0003499218
    1	자전거	좌회전 차량과 초등생 자전거 충돌…초등생 사망	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=055&aid=0000891351
    2	자전거	이재정 의원, 특별조정교부금 11억 5천만원 확보"	
    2	자전거	서울시설공단, 따릉이 정비 효율 높이는 작업대 6개 정비센터에 배치	
    2	자전거	자전거 타던 초등생 차량 충돌로 사망···어린이보호구역은 아냐	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=011&aid=0003904688
    2	자전거	성북구서 좌회전 차량과 자전거 충돌…초등생 사망	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=001&aid=0012366445
    2	자전거	내리막길 자전거 타던 초등생, 승용차 정면충돌 사망	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=003&aid=0010476832
    2	자전거	개불 생태계 파괴 '빠라뽕' 사용 못한다	
    2	자전거	[백운기의 뉴스와이드] 이춘희 "세종시, 행정도시 결정 났고, 이미 반 이상 건설…행정수도 활용이 옳은 일"	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=057&aid=0001572962
    2	자전거	[B tv 한빛뉴스][데스크 노트] 위험천만 공유 킥보드 해법은 없나?	
    2	자전거	[Opinion] 풍경은 가고 사람은 남는다 [여행]	
    2	자전거	[팝업★]문희준♥소율 딸 잼잼이, 생애 첫 자전거 타기.."처음 맞아?"	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=106&oid=112&aid=0003428166
    3	자전거	문희준♥소율 딸, 기특하게 벌써 자전거도 타네..엄빠 빼다박은 인형	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=106&oid=112&aid=0003428143
    3	자전거	대전시 다함께돌봄원스톱통합지원센터, 거점온돌방 출범식	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=008&aid=0004581196
    3	자전거	[MAY 2021 ] Fortune	
    3	자전거	[IT오늘] SK텔레콤, AI 활용 의료 진단 보조 솔루션 개발…KT, 디즈니·해리포터 등 가정의 달 이벤트	
    3	자전거	포스코건설, '더샵 양평리버포레' 30일 견본주택 개관	
    3	자전거	코로나로 바깥활동 줄어든 자녀에게 '어린이날 선물' 자전거 어때요~	
    3	자전거	[메아리] 나쁜 버블, 좋은 버블	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=110&oid=469&aid=0000601437
    3	자전거	포스코건설 '더샵 양평리버포레' 견본주택 개관	
    3	자전거	나만의 취향대로 즐기는 4색 캠핑 라이프	
    3	자전거	고양시, 공유자전거 ‘타조’ 내달부터 1천대 정식 운영	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=005&aid=0001435560
    
    ```

  * `naver_news_킥보드_210630_020400.txt`

    ```
    페이지	키워드	제목	url
    1	킥보드	[B tv 한빛뉴스][데스크 노트] 위험천만 공유 킥보드 해법은 없나?	
    1	킥보드	팅크웨어, 전동 킥보드 아이나비 스포츠 로드 기어 GT 출시	
    1	킥보드	빔모빌리티와 부산교통공사, 부산지역 모빌리티 활성화 위한 업무협약 체결	
    1	킥보드	'빨대퀸' 홍현희, 공유 킥보드 충전..역대급 생고생에 멘붕	
    1	킥보드	'빨대퀸' 홍현희, 촬영하다 강제 다이어트?!…'공유 킥보드 충전 도전'	
    1	킥보드	백원킥보드 쓩, 2021년 형 MAX 킥보드 공급 통한 안정성 모색	
    1	킥보드	"킥보드, 안전 또 안전"...업계·지자체·경찰, 환경개선 총력	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=105&oid=092&aid=0002220832
    1	킥보드	세븐일레븐, 가정의달 맞이 ‘가족사랑 선물세트’ 출시	
    1	킥보드	‘빨대퀸’ 홍현희, 역대급 힘든 N잡에 멘붕..촬영 중 강제 다이어트?	
    1	킥보드	공유 킥보드 디어 ‘1분 90원’ 배민커넥터 발 된다	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=016&aid=0001829519
    2	킥보드	'빨대퀸' 홍현희, 촬영하다 강제 다이어트... 역대급 N잡	
    2	킥보드	디어, 배민커넥트와 달린다	
    2	킥보드	세븐일레븐, 가정의 달 맞아 ‘가족사랑 선물세트’ 선봬	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=018&aid=0004917130
    2	킥보드	'빨대퀸' 홍현희, 공유 킥보드 충격에 멘붕..월수입 1천만 원에 '깜짝'	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=106&oid=112&aid=0003428002
    2	킥보드	‘빨대퀸’ 홍현희, 방전된 킥보드 찾아 삼만리	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=106&oid=144&aid=0000733885
    2	킥보드	'빨대퀸' 홍현희, 킥보드 충전=월수입 천만원?...역대급 생고생	
    2	킥보드	'빨대퀸' 홍현희, 촬영하다 강제 다이어트?	
    2	킥보드	[스토리 포토]당당한 "짐 맡아주세요!"...이것이 공유서비스	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=648&aid=0000000777
    2	킥보드	유아킥보드 켈리앤스테판, 초등학생 위한 킥보드 '마스터미니' 출시	
    2	킥보드	한국인공지능협회 참여 기업, 서울형 뉴딜 일자리 AI 학습 데이터 구축사업 인턴십 착수	
    3	킥보드	세븐일레븐, 가정의 달 맞아 '가족사랑 선물세트' 선봬	
    3	킥보드	세븐일레븐, 5월 가정의 달 ‘가족사랑 선물세트’ 선봬	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=014&aid=0004630829
    3	킥보드	수원시, 개인형 이동장치 활성화·안전성 '두 마리 토끼' 잡는다	
    3	킥보드	팅크웨어, 중장거리형 전동 킥보드 ‘아이나비 스포츠 로드 기어 GT’ 출시	
    3	킥보드	팅크웨어, 중장거리형 전동 킥보드 '아이나비 스포츠 로드 기어 GT' 2종 출시	
    3	킥보드	[포토] 공유 킥보드 주‧정차 금지구역 지정…현실은 '유명무실'	
    3	킥보드	헬멧 안쓰고 인도로 질주…전동킥보드 10명중 9명 '위법'	
    3	킥보드	세븐일레븐, 가정의 달 맞아 '가족사랑 선물세트' 선봬	
    3	킥보드	세븐일레븐 "편의점서 '가정의 달' 선물 준비하세요"	https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=008&aid=0004580784
    3	킥보드	[오늘e유통] 홈플러스, 가정의 달 맞이 '키즈 페스티벌' 개최 外	
    
    ```

    

  

