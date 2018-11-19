import os

from cv2 import imread, resize, cvtColor, COLOR_BGR2GRAY

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

########################## READING AND PROCESSING IMAGE DATA ##########################

num_list = os.listdir('data/train')
train_img = []
test_img = []
train_lab = []
test_lab = []

for num in num_list:
    for img in os.listdir('data/train/{}'.format(num)):
        img_path = 'data/train/{0}/{1}'.format(num, img)
        image = imread(img_path)
        image = cvtColor(image, COLOR_BGR2GRAY)
        image = resize(image, (64,64))
        
        train_img.append(image.flatten())
        train_lab.append(int(num))

for num in num_list:
    for img in os.listdir('data/test/{}'.format(num)):
        img_path = 'data/test/{0}/{1}'.format(num, img)
        image = imread(img_path)
        image = cvtColor(image, COLOR_BGR2GRAY)
        image = resize(image, (64,64))
        
        test_img.append(image.flatten())
        test_lab.append(int(num))

########################## LOGISTIC REGRESSION ##########################

clf = LogisticRegression(random_state=0,
                         solver = 'lbfgs', 
                         multi_class='multinomial')
clf.fit(train_img, train_lab)
pred = clf.predict(test_img)

print('Logistic Regression Accuracy:', accuracy_score(test_lab, pred))

########################## DECISSION TREE ##########################

clf = DecisionTreeClassifier()
clf.fit(train_img, train_lab)
pred = clf.predict(test_img)

print('DecisionTree Accuracy:', accuracy_score(test_lab, pred))

########################## RANDOM FOREST ##########################

clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=0)
clf.fit(train_img, train_lab)
pred = clf.predict(test_img)
print('RandomForest Accuracy:', accuracy_score(test_lab, pred))

########################## SUPPORT VECTOR MACHINES ##########################

clf = LinearSVC()
clf.fit(train_img, train_lab)
pred = clf.predict(test_img)
print('SVM Accuracy:', accuracy_score(test_lab, pred))