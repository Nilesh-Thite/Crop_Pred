
import pickle
path='model.pkl'
	   
f=open(path,'rb')
data=pickle.load(f)
 
print(data)
print(len(data))
