#This is the simple data science project for the gender classification

from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

clf_tree = tree.DecisionTreeClassifier()

# Create a K-Nearest Neighbors Classifier
clf_knn = KNeighborsClassifier()

# Create a Random Forest Classifier
clf_rf = RandomForestClassifier()

# Create a Support Vector Machine Classifier
clf_svm = SVC()

# [height, weight, shoe_size]

x = [[181, 80, 9], [177, 70, 8], [160, 60, 2], [154, 54, 5], [166, 65, 7], [190, 90, 8], [175, 64, 6]]

y = ['male', 'male', 'female', 'female', 'male', 'male', 'female']


clf_tree.fit(x, y)
clf_knn.fit(x, y)
clf_rf.fit(x, y)
clf_svm.fit(x, y)

# Make a prediction using the Decision Tree Classifier
prediction = clf_tree.predict([[190, 70, 8]])
print("Decision Tree Prediction:", prediction)

