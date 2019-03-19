file = open('crawl_it_output.txt','r',encoding='utf8')
out = open('cut_paragraph_output.txt','w',encoding='utf8')
file = file.read().split('\n')


for i in range(0, len(file), 1):

    lines = file[i]
    thisLine = lines.split(' ')
    flag = 0

    if (i % 3) == 2:
        check = 1
        str = ''
        for j in range(0, len(lines),1):
            if check == 0 and lines[j] == '<':
                break
            if lines[j] == '>':
                check = 0
                continue
            if check == 0:
                str += lines[j]
        out.write(str)
        out.write('\n')
        continue


    for word in thisLine:
        # print(word, end='*')

        if len(word) < 1:
            continue
        if(word == "<p><img" or word == "<p><iframe" or word == "</p><p><img" or word == "<br/><img" and flag == 0):
            # print('paise')
            # print('\n')
            flag = 1

        if(flag == 1):
            str = ''
            for alp in word:
                str += alp
                if(str == "width="):
                    flag = 0
                    break

        if(flag == 0):
            out.write(word)
            out.write(" ")
    out.write('\n')
