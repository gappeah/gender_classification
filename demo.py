#This is the simple data science project for the gender classification

from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier

clf = tree.DecisionTreeClassifier()

#create 3 more classifiers...




# [height, weight, shoe_size]

x = [[181, 80, 9], [177, 70, 8], [160, 60, 2], [154, 54, 5], [166, 65, 7], [190, 90, 8], [175, 64, 6]]

y = ['male', 'male', 'female', 'female', 'male', 'male', 'female']


clf = clf.fit(x,y)

prediction = clf.predict([[190, 70, 8]])

print(prediction)

