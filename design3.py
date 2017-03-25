from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
x =[]
y =[]
for i in range(100):
    x.append([i%9]*10)
    y.append(str(i%9)+'a')

param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
clf = clf.fit(x, y)
print clf.predict([3]*10)