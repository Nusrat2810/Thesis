file = open('naive_train_input.txt','r',encoding='utf8')
file_w_head = open('final_data.txt','r',encoding='utf8')
query = open('without_heading_output.txt','r',encoding='utf8')
testQuery = open('naive_output.txt','w',encoding='utf8')
RAfile = open('road_accident_naive.txt','w',encoding='utf8')

file_w_head = file_w_head.read().split('\n')

file = file.read()
file = file.split('\n')
query = query.read().split('\n')
word_cnt_pos = {}
word_cnt_neg = {}
class_cnt = {'positive':0, 'negative':0}
distinct_cnt = 0

def class_counting_function():
    id=0
    global class_cnt

    while(id<len(file)-1):
        sentence = file[id]
        sentence_class = file[id+1]
        id += 2
        #print(sentence_class)
        class_cnt[sentence_class]+=1

def prior_():

    class_counting_function()
    global class_cnt
    posNum = class_cnt['positive']
    negNum = class_cnt['negative']
    totalDoc = posNum + negNum
    priorPos = posNum/(totalDoc*1.0)
    priorNeg = negNum/(totalDoc*1.0)
    #print(posNum,negNum)
    #print(totalDoc)
    #print(priorPos,priorNeg)
    return priorPos,priorNeg

#priorPos, priorNeg = prior_()

#end of prior probability


def word_counting_function():
    id=0

    global distinct_cnt
    global  sentence_class
    global  word_cnt_neg
    global  word_cnt_pos

    while(id< len(file)-2):
        sentence = file[id]
        sentence_class = file[id+1]
        id += 2
        word_part = sentence.split(' ')
        for word in word_part:
            #print(word)
            if sentence_class == 'positive':
                if word not in word_cnt_pos:
                    word_cnt_pos[word]=0
                    if word not in word_cnt_neg:
                         distinct_cnt =  distinct_cnt+ 1
                word_cnt_pos[word] += 1
                #print(word)
                #print(distinct_cnt)

            elif sentence_class == 'negative':
                if word not in word_cnt_neg:
                    word_cnt_neg[word]=0
                    if word not in word_cnt_pos:
                         distinct_cnt =  distinct_cnt + 1
                word_cnt_neg[word] += 1
                #print(word)
                #print(distinct_cnt)
    #print(distinct_cnt)


def class_total_word():
    posWord=0
    negWord=0
    global  word_cnt_pos
    global  word_cnt_neg
    for word in word_cnt_pos:
        posWord += word_cnt_pos[word]
    for word in word_cnt_neg:
        negWord += word_cnt_neg[word]
    return posWord,negWord


def conditional_prob(word):
    global distinct_cnt
    posWord,negWord=class_total_word()
    #print(posWord,negWord)
    posOcc,negOcc =0,0

    if word in word_cnt_pos:
        posOcc += word_cnt_pos[word]
    if word in word_cnt_neg:
        negOcc += word_cnt_neg[word]
    posPost = (posOcc+ 1.00)/ (posWord +  distinct_cnt)
    negPost = (negOcc+ 1.00)/ (negWord +  distinct_cnt)
    #print(word,posPost,negPost)
    return posPost,negPost


def posteriorProbability(query):
    postPos,postNeg = prior_()
    #print('pos, neg here : ',postPos,postNeg)
    query_words = query.split(' ')
    boroValue = 10 ** (len(query_words)/2)
    #print('q = ' ,query)
    postPos = postPos *boroValue
    postNeg = postNeg * boroValue

    #print('      PosteriorPos   posterior neg      conditionalwordPos  conditionalwordNeg\n')
    for word in query_words:
        #print(word)
        condiPos, condiNeg = conditional_prob(word)
        postPos *= condiPos
        postNeg *= condiNeg
        #print(word, ' ', postPos,'  ',postNeg, condiPos, condiNeg)

    return postPos,postNeg

r_a_cnt = 0
def Naive_bayes(test):
    positive_probability, negative_probability = posteriorProbability(test)
    global  r_a_cnt

    #print('pos, neg ', positive_probability, ' ',negative_probability)
    if positive_probability > negative_probability:
        #print('Road Accident')
        r_a_cnt += 1
        testQuery.write('Road Accident')
        return True
    else:
        testQuery.write('Others')
        #print('Others')
        return  False



word_counting_function()
#print(query)

for id in range(0, len(query)):
    test = query[id]
    if len(test) > 0:
        #print(test)
        testQuery.write(test)
        testQuery.write('\n')
        okay = Naive_bayes(test)
        testQuery.write('\n')

        if okay:
            RAfile.write(file_w_head[id*3])
            RAfile.write('\n')
            RAfile.write(file_w_head[id*3 + 1])
            RAfile.write('\n')
            RAfile.write(file_w_head[id*3 + 2])
            RAfile.write('\n')


#total_accident = r_a_cnt
#total_not_accident = len(query) - total_accident


