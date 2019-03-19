file = open('all_bangla_output.txt', 'r', encoding='utf=8')
# file = open('temp.txt', 'r', encoding='utf=8')
out = open('all_bangla_AVRO.txt', 'w', encoding='utf=8')

file = file.read().split('\n')

mp_dot = { 'ব': 'র', 'ড':'ড়','ঢ':'ঢ়','য':'য়'}


for line in file:
    # print(line)
    have_words = False
    line = line.split(' ')
    str1 = ''
    ok = 0
    for word in line:
        # print(word)
        str2 = ""
        for i in range(0, len(word), 1):
            ch = word[i]
            if ch == '়' or ch == 'ৗ':
                continue

            if ch == 'া':
                if word[i-1] == 'ে':
                    continue

            if word[i] in mp_dot:
                if i+1 < len(word):
                    if word[i+1] == '়':
                        ch = mp_dot[ch]

            if word[i] in 'ে':
                if i+1 < len(word):
                    if word[i+1] == 'ৗ':
                        ch = 'ৌ'

            if word[i] in 'ে':
                if i+1 < len(word):
                    if word[i+1] == 'া':
                        ch = 'ো'

            str2 = str2 + str(ch)

        if ok == 1:
            out.write(' ')

        if len(str2)> 1:
            have_words = True

        out.write(str(str2))
        ok = 1

    out.write('\n')
