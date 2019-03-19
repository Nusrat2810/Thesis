from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# news class
class news:
    def __init__(self, data, target, target_name):
        self.data = data
        self.target = target
        self.target_name = target_name


# reading train data
f = open('train_svm.txt','r',encoding='utf8')
f = f.read().split('\n')

data = []
target = []

for i in range(0,len(f)-1,2):
    data.append(f[i])
    if f[i+1] == 'positive':
        target.append(1)
    else:
        target.append(0)

target_name = ['negative', 'positive']
SVM_train_my = news(data, target, target_name)

# vectorizing of train

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(SVM_train_my.data)

tfidf_trainsformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tfidf_trainsformer.transform(X_train_counts)


tfidf_trainsformer = TfidfTransformer()  
X_train_tfidf = tfidf_trainsformer.fit_transform(X_train_counts)


clf = MultinomialNB().fit(X_train_tfidf, SVM_train_my.target)
# test data reading

testfile = open('without_heading_output.txt','r',encoding='utf8')
test_data = testfile.read().split('\n')

# tf idf for test data
X_test_counts = count_vect.transform(test_data)
X_test_tfidf = tfidf_trainsformer.transform(X_test_counts)

# predicting with tf idf it't not need here
# predicted = clf.predict(X_test_tfidf)

# creating a pipeline
from sklearn.pipeline import Pipeline

# connecting with  pipeline
# text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
# text_clf.fit(SVM_train_my.data, SVM_train_my.target)  # fitting train and class

# SGDClassifier for SVM
from sklearn.linear_model import SGDClassifier

# connecting with  pipeline 
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier(loss='hinge', penalty='l2',
                          alpha=1e-3, random_state=42,
                          max_iter=5, tol=None)),
])

text_clf.fit(SVM_train_my.data, SVM_train_my.target) # fitting train and class
predicted = text_clf.predict(test_data)  # predict the class for testData


out = open('svm_out.txt','w',encoding='utf8')
out_w_head = open('road_accident_SVM.txt','w',encoding='utf8')


cnt = 0  # cnt for counting RA

for i in range(0, len(test_data)):
    out.write(test_data[i])
    out.write('\n')
    if predicted[i] == 1:
        cnt += 1
        out_w_head.write(test_data[i])
        out_w_head.write('\n')
        out.write('Road Accident')
    else:
        out.write('Others')
    out.write('\n')
#print('total accident: ',cnt)
