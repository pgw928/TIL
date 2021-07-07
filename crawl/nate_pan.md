# 네이트판 훈훈한 이야기 크롤링 연습





* ### 페이지, 제목, url 수집

  ```python
  import requests
  from lxml import html
  import time
  
  keywords = ['c20048']
  categories = {keywords[0]:'훈훈한 이야기'}
  def fmake_file(keyword):
      output_file_name = 'nate_pan_' + keyword + '_' + time.strftime('%y%m%d_%H%M%S') + '.txt'
      output_file = open(output_file_name, 'w', encoding='utf-8')
      output_file.write(f'카테고리\t페이지\t제목\turl\n')
      output_file.close()
      return output_file_name
  
  def fwrite_contents(page_num, keyword, title_clean,url, output_file_name):
      output_file = open(output_file_name, 'a', encoding='utf-8')
      output_file.write(f'{categories[keyword]}\t{page_num}\t{title_clean}\t{url}\n')
      output_file.close()
  
  def fcrawl_contents(page_num, keyword, output_file_name):
      url = f'https://pann.nate.com/talk/{keyword}?page={page_num}'
      headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
      html_req = requests.get(url, headers=headers)
      tree = html.fromstring(html_req.content)
      print(tree.text)
      bodies = tree.xpath("//table[@class='talk_list']/tbody/tr")
      results = []
      # print(bodies)
      for body in bodies:
          title = body.xpath(".//td[@class='subject']/a/text()")
          title_clean = title[0].strip().replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')
          url = 'https://pann.nate.com/' + body.xpath(".//td[@class='subject']/a/@href")[0]
          results.append((categories[keyword], title_clean, url))
          fwrite_contents(page_num, keyword, title_clean, url, output_file_name)
      return results
  
  def fmain():
      for keyword in keywords:
          output_file_name = fmake_file(keyword)
          for page_num in range(1, 30):
              results = fcrawl_contents(page_num, keyword, output_file_name)
              print(results)
              time.sleep(6)
  
  fmain()
  ```

  

* ### 날짜, 아이디, 본문 수집

  ```python
  import requests
  from lxml import html
  import time
  
  keyword = 'c20048'
  categories = {'c20048':'훈훈한 이야기'}
  
  input_file_name = f'nate_pan_{keyword}_210628_142508.txt'
  
  headers = { 'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
  
  
  def fmake_file(keyword):
      output_file_main_name = f'nate_pan_{keyword}_page' + '_' + time.strftime('%y%m%d_%H%M%S') + '.txt'
      output_file_main = open(output_file_main_name, 'w', encoding='utf-8')
      output_file_main.write('페이지번호\t카테고리\t날짜\turl\t아이디\t제목\t본문\n')
      output_file_main.close()
      return output_file_main_name
  
  def fget_list():
      input_file = open(input_file_name, 'r', encoding='utf-8')
      lines = input_file.readlines()
      arr = []
      for line in lines:
          if not line:
              break
          tmp = line.strip().split('\t')
          page_num, title, url = tmp[1], tmp[2], tmp[3]
          arr.append([page_num, title, url])
      input_file.close()
      return arr[1:]
  
  
  def fwrite_contents_main(page_num, keyword, date, url, user, title_clean, content, output_file_name):
      output_file = open(output_file_name, 'a', encoding='utf-8')
      output_file.write(f'{page_num}\t{categories[keyword]}\t{date}\t{url}\t{user}\t{title_clean}\t{content}\n')
      output_file.close()
  
  def fcrawl_contents_main(page_num, title, url, output_file_main_name):
      html_req = requests.get(url, headers=headers)
      tree = html.fromstring(html_req.content)
      try:
          user = tree.xpath("//div[@class='post-tit-info']/div[@class='info']/a[@class='writer']/text()")[0]
      except:
          user = ''
      try:
          date = tree.xpath("//div[@class='post-tit-info']/div[@class='info']/span[@class='date']/text()")[0]
      except:
          date = ''
      try:
          content = tree.xpath("//div[@id='espresso_editor_view']/descendant-or-self::text()[not(ancestor::script)]")
      except:
          content = ''
      print(content)
      content = ' '.join(content).replace('\xa0', ' ').replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').strip()
      fwrite_contents_main(page_num, keyword, date, url, user, title, content, output_file_main_name)
  
  def fmain():
      arr = fget_list()
      output_file_main_name = fmake_file(keyword)
      for tmp in arr:
          page_num, title, url = tmp
          fcrawl_contents_main(page_num, title, url, output_file_main_name)
          time.sleep(6)
  
  fmain()
  ```

  

