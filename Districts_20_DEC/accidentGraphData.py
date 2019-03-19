def accidentGraph():

    file = open('districts_with_data.txt', 'r', encoding='utf8')
    dis_file = open('districts.txt', 'r', encoding='utf8')
    out = open('districts_accident_final.txt', 'w', encoding='utf8')

    file = file.read().split('\n')
    dis_file = dis_file.read().split('\n')
    districts = []

    for i in range(0,len(dis_file),4):
        jhela = dis_file[i]
        if jhela not in districts:
            districts.append(jhela)

    cnt = 0
    for i in range(0, len(districts)-1, 1):
        (cnt_13_14, cnt_15_16, cnt_17_18) = (0, 0, 0)
        for j in range(0, len(file)-1, 1):
            data = file[j].split(' ')
            if data[0] == districts[i]:
                str2 = data[1]
                if str2 == '২০১৩' or str2 == '২০১৪':
                    cnt_13_14 += 1
                if str2 == '২০১৫' or str2 == '২০১৬':
                    cnt_15_16 += 1
                if str2 == '২০১৭' or str2 == '২০১৮':
                    cnt_17_18 += 1
        out.write(districts[i])
        out.write("\n 2013 - 2014 => ")
        out.write(str(cnt_13_14))
        out.write("\n 2015 - 2016 => ")
        out.write(str(cnt_15_16))
        out.write("\n 2017 - 2018 => ")
        out.write(str(cnt_17_18))
        out.write("\n")
        cnt += cnt_13_14 + cnt_15_16 + cnt_17_18

    print("Total accident = " + str(cnt))