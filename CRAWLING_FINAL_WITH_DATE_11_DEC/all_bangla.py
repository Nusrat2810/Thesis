o9file = open('cut_paragraph_output.txt','r',encoding='utf8')
out = open('all_bangla_output.txt','w',encoding='utf8')
file = file.read().split('\n')


def inrange(a):
    if ord(a) >= 2433 and ord(a) <= 2543:
        return 1
    return 0


def getit(s):
    tp= ' '
    s = s.split(' ')
    for x in s:
        if len(x):
            if len(tp):
                if (tp[-1]!=' '):
                    tp += ' '
            tp += x
        else:
            if len(tp):
                if (tp[-1]!=' '):
                    tp += ' '
    return tp


def getLine(s):
    #print(s)
    tmpstr = ''
    #mapping = []
    s = s.split(' ')
    for each in s:

        if len(each)>0:
            #if each not in mapping:
            if len(tmpstr) > 0:
                 tmpstr += ' '
            tmpstr += each
            # print('nai, ', each)
            #mapping.append(each)
    return tmpstr

#print(len(file))


for i in range(0, len(file), 1):
    if(i%3) == 2:
        out.write(file[i])
        out.write('\n')
        continue
    lines = file[i]
    # out.write(lines)
    # out.write('\n')
    thisLine = lines.split(' ')
    myLine = ''
    for word in thisLine:
        if len(word) < 1:
            continue
        if word[-1] == '।':
            word = word[:-1]
        myWord = ''
        for thisChar in word:
            if not inrange(thisChar):
                thisChar = ' '
            myWord += thisChar
        myWord = getit(myWord)

        if len(myWord) > 0:
            if myWord[-1] !=' ':
                myWord += ' '
        myLine += myWord


    myLine = getLine(myLine)
    if(len(myLine)>1):
        out.write(myLine)
        out.write('\n')
