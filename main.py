import numpy as np
import pandas as pd
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("Crop_recommendation.csv")

X = data.iloc[:,0:-1]
y = data.iloc[:,-1]

import sklearn.model_selection
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=2020)

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=100, criterion='gini')
classifier.fit(X_train, y_train)

classifier.score(X_test, y_test)

pickle.dump(classifier,open('model.pkl','wb'))

model=pickle.load(open('model.pkl','rb'))
