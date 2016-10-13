'''
Created on Oct 12, 2016

@author: rajendra
'''
import pandas as pd
import numpy as np

def cvcompDType(df):
    
    df[['zip5', 'County','admit_day1','Year_of_admission','attend_doc','Admitting_Service','pr1c','cci']] \
      = df[['zip5', 'County','admit_day1','Year_of_admission','attend_doc','Admitting_Service','pr1c','cci']].\
        astype(float)
    
    return df