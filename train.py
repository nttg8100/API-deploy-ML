import pickle
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

# Loading Iris Dataset
iris = load_iris()

# Getting features and targets from the dataset
X = iris.data
Y = iris.target

# Fitting our Model on the dataset
clf = GaussianNB()
clf.fit(X, Y)

# save the model to disk
filename = 'models/finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))