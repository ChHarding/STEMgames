#In this file, I will process the data from the reviews by searching for specific terms related to STEM domains. 
#Currently not sure if it is tokenizing correctly. 
# This allows importing of scripts, which are stored in a folder one level up
import sys
sys.path.append('..')
import numpy as np
import pandas as pd
from scripts import preprocessing
from string import punctuation
from nltk.corpus import stopwords

stopwords_list = stopwords.words('english') + list(punctuation) + ['`', '’', '…', '\n']


df = pd.read_pickle(r"C:\Users\UTEC\Desktop\hci584\HCI584 - STEM games\STEMgames\apps_ids.pkl')

