file = open('clean_data.txt','r',encoding='utf8')
out = open('final_data.txt','w',encoding='utf8')

file = file.read().split('\n')


def getNews(news):
    news = news.split(' ')
    tmpNews = news[0]
    for i in range(1, min(80, len(news))):
        tmpNews += ' ' + news[i]
    return  tmpNews


for news in file:
    myNews = getNews(news)
    #print(type(myNews))
    out.write(myNews)
    if len(myNews) > 1:
        out.write('\n')