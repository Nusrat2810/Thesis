#import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

file = open('tf_idf_input.txt','r',encoding='utf8')
querys = open('without_heading_output.txt','r',encoding='utf8')
final_result = open('cosine_similarity_output.txt','w',encoding='utf8')
RA_out = open('road_accident_cosine.txt','w',encoding='utf8')
file = file.read().split('\n')
querys = querys.read().split('\n')
file = file[:-1]
#fixedFile = file

def isRoadAccidentMatched(val):
    listOfRoadAccident = [0, 9, 11, 14, 16, 17, 18, 21, 22, 31, 32, 33, 34, 37, 38, 42, 44, 49, 50, 53, 55, 56, 57, 58, 59, 60, 64, 68, 71, 73, 75, 77, 80, 81, 84, 87, 92, 95, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282]

    if val in listOfRoadAccident:
        return True
    else:
        return False

def CosineSimiWorks(tmp, queryId):
    myvec = TfidfVectorizer(tokenizer=lambda x : x.split())
    myvec_mat = myvec.fit_transform(tmp)
    ##print(myvec.get_feature_names())
    cosine = cosine_similarity(myvec_mat[queryId], myvec_mat)
    ##print('Cosine: ',cosine, ' ',type(cosine))
    return cosine


def getMaxSimiId(cosineMat):
    mx = 0
    mxSimiId = 0
    ##print(cosineMat)
    for i in range(0, len(file)-1):
        if cosineMat[0][i] > mx :
            mx = cosineMat[0][i]
            mxSimiId = i
    return mxSimiId


for id in range(0, len(querys)):
    news = querys[id]
    if len(news) < 1:
        continue
    file.append(news)
    queryId = len(file) - 1
    cosineMat = CosineSimiWorks(file, queryId)

    final_result.write(news)
    final_result.write('\n')
    mxId = -1
    mxId = getMaxSimiId(cosineMat)
    if isRoadAccidentMatched(mxId):
        final_result.write('Road Accident ')
        final_result.write('\n')
        RA_out.write(news)
        RA_out.write('\n')

    else:
        final_result.write("Others ")
        final_result.write('\n')

    file = file[:-1]