file = open('final_data.txt','r',encoding='utf8')
out_file = open('without_heading_output.txt','w', encoding='utf8')
file = file.read()

file = file.split('\n')

for i in range(1,len(file),3):
    #print(i,end = ' ')
    out_file.write(file[i])
    out_file.write('\n')