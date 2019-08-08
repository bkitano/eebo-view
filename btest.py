import pandas as pd
import numpy as np
import pickle

with open('./d.p', 'rb') as fp:
    D = pickle.load(fp)

def model_view_topic(topic):
    if topic >= 50:
        return "Topic id does not exist."
    
    ww = [i[1] for d in D[:,topic] for i in d]
    bb = [ww[i:i+15] for i in range(0, len(ww), 15)]
    p = pd.DataFrame(bb).transpose()
    p.columns = range(1473, 1820, 20)
    return p.to_json()