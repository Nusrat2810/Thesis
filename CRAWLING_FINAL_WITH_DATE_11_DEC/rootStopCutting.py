rootfile = open('root.txt', 'r', encoding='utf8')
stopfile = open('stop.txt', 'r', encoding='utf8')
mainfile = open('all_bangla_AVRO.txt', 'r', encoding='utf8')
cleanData = open('clean_data.txt', 'w', encoding='utf8')

rootfile = rootfile.read().split('\n')
stopfile = stopfile.read().split('\n')
mainfile = mainfile.read().split('\n')

# print(len(mainfile))
root = {}
for x in rootfile:
    v = x.split(' ')
    if (len(v) != 2):
        continue
    a, b = v[0], v[1]
    if a not in root:
        root[a] = b

stop = []
for x in stopfile:
    if x not in stop:
        stop.append(x)


def cutStop(line):
    global stop
    global root
    line = line.split(' ')
    myLine = ''
    for word in line:
        if (len(word) > 0):
            if word not in stop:
                myLine += word
                myLine += ' '
    return myLine


def toRoot(line):
    global root
    line = line.split(' ')
    myline = ''
    for word in line:
        if len(word) < 1:
            continue
        if word in root:
            word = root[word]
        myline += word + ' '
    return cutStop(myline)


def this_is_okay(line):
    if len(line) == 0:
        return False
    for i in line:
        if i != ' ' and i != '\n':
            return True

    return False


# print(mainfile[len(mainfile)-2])

for i in range(0, len(mainfile), 3):

    eachLine = mainfile[i]
    eachNews = mainfile[i + 1]

    thisLine = cutStop(eachLine)
    thisLine = toRoot(thisLine)

    thisNews = cutStop(eachNews)
    thisNews = toRoot(thisNews)

    shouldPrint = this_is_okay(thisLine)
    shouldNewsPrint = this_is_okay(thisNews)

    if shouldPrint == 0 or shouldNewsPrint == 0:
        continue

    # cleanData.write('Heading ')
    cleanData.write(thisLine)

    cleanData.write('\n')
    # cleanData.write('News ')
    cleanData.write(thisNews)
    cleanData.write('\n')
    cleanData.write(mainfile[i + 2])
    cleanData.write('\n')
