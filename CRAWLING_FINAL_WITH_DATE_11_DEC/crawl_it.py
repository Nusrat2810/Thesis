import requests
from bs4 import BeautifulSoup

saveit = open('crawl_it_output.txt','w',encoding='utf8')

crawled = []


def mySpider(max_pages):

    page = 1
    while page < max_pages:
        news_no = 1
        url = "http://www.prothomalo.com/bangladesh/article/?tags=234&page=" + str(page)
        #print('page no is: ', page)
        if(url in crawled):
            continue
        crawled.append(url)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class':"link_overlay"}):
            if news_no > 20:
                break
            # print('[News_no: ', news_no , ' page_no :', page, ']')
            news_no += 1
            href = "http://www.prothomalo.com" + link.get('href')
            #print(href)
            sec_source = requests.get(href)
            sec_plain = sec_source.text
            sec_soup = BeautifulSoup(sec_plain)
            #for only_news in sec_soup.findAll('div', {'class':'right_part'}):
            for seclink in sec_soup.findAll('h1',{'class':'title mb10'}):
                tp = news_no

                saveit.write(seclink.string)
                saveit.write("\n")

            for secNews in sec_soup.findAll('div',  {'itemprop':'articleBody'}):
                for paragraph in secNews.findAll('p'):
                    saveit.write(str(paragraph))
                    saveit.write(" ")

            saveit.write("\n")

            for time in sec_soup.findAll('span'):
                if time.has_attr('content'):
                    saveit.write(str(time))
                    saveit.write(' ')
                    break
            saveit.write("\n")
        page += 1

mySpider(602)
