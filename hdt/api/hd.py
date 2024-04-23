import pickle
import os

def pred(ob):
    pkl_filename= "Heart_disease_prediction.sav"
    pkl_filename= os.path.dirname(__file__)+ "/"+pkl_filename
    with open(pkl_filename, 'rb') as file:
        model=pickle.load(file)
    prediction = model.predict([ob])
    return prediction