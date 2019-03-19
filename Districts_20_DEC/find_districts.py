file = open('districts.txt','r',encoding='utf8')
dataFile = open('road_accident_naive.txt','r',encoding='utf8')
out = open('find_pattern.txt','w',encoding='utf8')
result = open('result_pattern.txt','w',encoding='utf8')
out_w_date = open('districts_with_data.txt','w',encoding='utf8')

file = file.read().split('\n')
dataFile = dataFile.read().split('\n')

districs = []
mp = {}

visited_news = []


def find(value):
    for i in range(0,len(districs)):
        if districs[i] == value:
            # print(value, end=' ')
            # print(i)
            return int(i/4) * 4
    return -1

def pattern1():    # If first word is the district in the news
    # print(len(dataFile))
    for id in range(1,len(dataFile), 3):
        news = dataFile[id]
        # print(news)
        word = news.split(' ');
        # print(word[0])
        x = find(word[0])
        # print(x)
        if x >= 0:
            if districs[x] not in mp:
                mp[districs[x]] = 0
            mp[districs[x]] += 1
            visited_news.append(id)
            dates = dataFile[id+1].split(' ')
            out_w_date.write(districs[x])
            out_w_date.write(" ")
            out_w_date.write(dates[2][0:4])
            out_w_date.write('\n')

def pattern2():    # If first word is the district in the news heading
    # print(len(dataFile))
    for id in range(0,len(dataFile), 3):
        i = id+1
        if i not in visited_news:
            news = dataFile[id]
            word = news.split(' ');
            # print(word[0])
            x = find(word[0])
            # print(x)
            if x >= 0:
                if districs[x] not in mp:
                    mp[districs[x]] = 0
                mp[districs[x]] += 1
                visited_news.append(i)
                if (id+2) < len(dataFile):
                    dates = dataFile[id + 2].split(' ')
                    out_w_date.write(districs[x])
                    out_w_date.write(" ")
                    out_w_date.write(dates[2][0:4])
                    out_w_date.write('\n')


def pattern3():    # If pattern look like ঢাকা আরিচা মহাড়কে

    fix = ['মহাসড়কে', 'মহাসড়ক', 'মহাসড়কের', 'মহাড়কে']

    for id in range(1, len(dataFile), 3):
        if id not in visited_news:
            news = dataFile[id]
            word = news.split(' ');
            for i in range(0, len(word)):
                if word[i] in fix:
                    if i-2 >= 0:
                        x = find(word[i-2])
                        if x >= 0:
                            if districs[x] not in mp:
                                mp[districs[x]] = 0
                            mp[districs[x]] += 1
                            visited_news.append(id)
                            dates = dataFile[id + 1].split(' ')
                            out_w_date.write(districs[x])
                            out_w_date.write(" ")
                            out_w_date.write(dates[2][0:4])
                            out_w_date.write('\n')


def check():

    for id in range(1, len(dataFile), 3):
        if id not in visited_news:
            out.write(dataFile[id-1])
            out.write('\n')
            out.write(dataFile[id])
            out.write('\n')




for word in file:
    districs.append(word)



# print(districs)

pattern1()
pattern2()
pattern3()
check()

cnt = 0
for word in mp:
    cnt = cnt + mp[word]
    result.write(word)
    result.write(" ")
    result.write(str(mp[word]))
    result.write('\n')

# print(mp)
# print(len(mp)-1)
print(cnt)

import accidentGraphData
accidentGraphData.accidentGraph()
