import numpy as np
import rpy2
import pandas as pd
import random
import math
import readline
import rpy2.robjects as robjects
from  rpy2.robjects import r
from rpy2.robjects.packages import importr
from rpy2.robjects import IntVector, Formula
from rpy2 import *
import pandas.rpy.common as com
import os
from prediction import tranformdata

def get_path(*args):    
    output_dir = "/home/rajendra/workspace/Prisma/"    
    for a in args:
        output_dir = os.path.join(output_dir,a)
    return output_dir

def predict(predDF):
    mgcv = rpy2.robjects.packages.importr('mgcv')
    base = rpy2.robjects.packages.importr('base')
    statsf = rpy2.robjects.packages.importr('stats',robject_translations = {'format_perc': 'format_dot_perc'})
    
    model_dict = tranformdata(predDF)
    mf = predDF #pd.read_csv('/home/rajendra/workspace/Prisma/data/processed_data1.csv')
    rdata =  pd.read_csv(get_path('output','cvcomp_data.csv')) #model_dict['cvcomp_data']
    tdf = com.convert_to_r_dataframe(rdata)
    robjects.globalenv['tdf'] = tdf
    r_cvco =r.load(get_path('model','Cv-Comp.RData'))
    robjects.r("datresults<-predict(max_auc_model_cvcomp,tdf,type=\"response\")")
    results = robjects.globalenv['datresults']
    mf['score_cvcomp'] = results
    
    rdata = pd.read_csv(get_path('output','mvcomp_data.csv'))
    tdf = com.convert_to_r_dataframe(rdata)
    robjects.globalenv['tdf'] = tdf
    r_cvco =r.load(get_path('model','Mv-CoMP.RData'))
    robjects.r("datresults<-predict(max_auc_model_mvcomp,tdf,type=\"response\")")
    results = robjects.globalenv['datresults']
    mf['score_mvcomp'] = results    
    
    rdata = pd.read_csv(get_path('output','icucomp_data.csv'))
    tdf = com.convert_to_r_dataframe(rdata)
    robjects.globalenv['tdf'] = tdf
    r_cvco =r.load(get_path('model','Icu-Comp.RData'))
    robjects.r("datresults<-predict(max_auc_model_ICU_comp,tdf,type=\"response\")")
    results = robjects.globalenv['datresults']
    mf['score_icucomp'] = results    
    
    rdata = pd.read_csv(get_path('output','woundcomp_data.csv'))
    tdf = com.convert_to_r_dataframe(rdata)
    robjects.globalenv['tdf'] = tdf
    r_cvco =r.load(get_path('model','Proc_wound_inf.RData'))
    robjects.r("datresults<-predict(max_auc_model_cvcomp,tdf,type=\"response\")")
    results = robjects.globalenv['datresults']
    mf['score_woundcomp'] = results
    
    rdata = pd.read_csv(get_path('output','neuro_delirium_data.csv'))
    tdf = com.convert_to_r_dataframe(rdata)
    robjects.globalenv['tdf'] = tdf
    r_cvco =r.load(get_path('model','Neuro_delirium.RData'))
    robjects.r("datresults<-predict(max_auc_model_cvcomp,tdf,type=\"response\")")
    results = robjects.globalenv['datresults']
    mf['score_neuro_delirium'] = results    
    
    rdata = pd.read_csv(get_path('output','sepsis_data.csv'))
    tdf = com.convert_to_r_dataframe(rdata)
    robjects.globalenv['tdf'] = tdf
    r_cvco =r.load(get_path('model','Sepsis.RData'))
    robjects.r("datresults<-predict(max_auc_model_cvcomp,tdf,type=\"response\")")
    results = robjects.globalenv['datresults']
    mf['score_sepsis'] = results
    
    rdata = pd.read_csv(get_path('output','vtenew_data.csv'))
    tdf = com.convert_to_r_dataframe(rdata)
    robjects.globalenv['tdf'] = tdf
    r_cvco =r.load(get_path('model','Vte.RData'))
    robjects.r("datresults<-predict(max_auc_model_cvcomp,tdf,type=\"response\")")
    results = robjects.globalenv['datresults']
    mf['score_vte'] = results
    
    rdata = pd.read_csv(get_path('output','aki_data.csv'))
    tdf = com.convert_to_r_dataframe(rdata)
    robjects.globalenv['tdf'] = tdf
    r_cvco =r.load(get_path('model','Kdigo.RData'))
    robjects.r("datresults<-predict(max_auc_model_cvcomp,tdf,type=\"response\")")
    results = robjects.globalenv['datresults']
    mf['score_aki'] = results
        
    mf.to_csv(get_path('scores','scores.csv'))
    #exit()
    os.remove(get_path('output','icucomp_data.csv'))
    os.remove(get_path('output','cvcomp_data.csv'))
    os.remove(get_path('output','aki_data.csv'))
    os.remove(get_path('output','sepsis_data.csv'))
    os.remove(get_path('output','woundcomp_data.csv'))
    os.remove(get_path('output','mvcomp_data.csv'))
    os.remove(get_path('output','vtenew_data.csv'))
    os.remove(get_path('output','neuro_delirium_data.csv'))
    
    return mf




