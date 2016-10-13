import numpy as np
import rpy2
import pandas as pd
import random
import math
import readline
import rpy2.robjects as robjects
import rpy2.robjects as ro
from  rpy2.robjects import r
from rpy2.robjects.packages import importr
from rpy2.robjects import IntVector, Formula
from rpy2 import *
import pandas.rpy.common as com
import os

def get_path(*args):    
    output_dir = "/home/rajendra/workspace/Prisma/"    
    for a in args:
        output_dir = os.path.join(output_dir,a)
    return output_dir

#Read dictionaries
def tranformdata(transformDF):
    mf = transformDF #pd.read_csv('/home/rajendra/workspace/Prisma/data/processed_data.csv')
    feature_all = pd.read_csv(get_path('data','feature_list_all.csv')) 
    category_dictionary = pd.read_csv(get_path('dictionaries','category_dic11.csv')) 
    category_dictionary_cluster = pd.read_csv(get_path('dictionaries','category_dic12.csv'))
    numeric_dictionary = pd.read_csv(get_path('dictionaries','numeric_dic.csv'))
    procedure_dictionary = pd.read_csv(get_path('dictionaries','procedure_dic.csv'))
    selected_featured_vif = pd.read_csv(get_path('dictionaries','vif_selected_feat.csv'))

    mf.fillna('MISSING', inplace=True)
    mf = mf.replace([' ','','_','UNKNOWN','NA'],'MISSING')


    #Create additional Variables

    # create Number of nephrotoxic medications
    mf['no_nephrotoxic_meds'] = mf["aminog_adm"]+mf["diuret_adm"]+mf["vanco_adm"]+mf["ace_adm"]+mf["nsaids_adm"]+mf["inot_pres_adm"]

    mf.ix[mf['nsaids_adm'] == 0 ,'nephtox_adm'] = 0
    mf.ix[mf['nsaids_adm'] == 1 ,'nephtox_adm'] = 1
    mf.ix[(mf['nephtox_adm'] == 1) & ((mf['aminog_adm'] ==1) | (mf['diuret_adm']==1) | (mf['vanco_adm']==1)),'nephtox_adm'] = 2
    #df['nephtox_adm'] = np.where(((df['nephtox_adm'] == 1) & (df['aminog_adm'] ==1 | df['diuret_adm']==1 | df['vanco_adm']==1)),2,1)

    # grouping Urine Protein
    mf.ix[mf['max_PROTUR_gr2'] == ">=300" ,'max_PROTUR_gr2'] = 2
    mf.ix[mf['max_PROTUR_gr2'] == "TR-30-100" ,'max_PROTUR_gr2'] = 1
    mf.ix[mf['max_PROTUR_gr2'] != "TR-30-100" ,'max_PROTUR_gr2'] = 0

# grouping urinal hemoglobin
    mf.ix[mf['max_PROTUR_gr2'] == ">=300" ,'max_PROTUR_gr2'] = 2
    mf.ix[mf['max_PROTUR_gr2'] == "TR-30-100" ,'max_PROTUR_gr2'] = 1
    mf.ix[mf['max_PROTUR_gr2'] != "TR-30-100" ,'max_PROTUR_gr2'] = 0

# grouping urinal hemoglobin
    mf.ix[mf['max_HGBUR_gr'] == "LARGE" ,'max_HGBUR_gr'] = 2
    mf.ix[(mf['max_HGBUR_gr'] == "MISSING") |  (mf['max_HGBUR_gr'] == 'NEGATIVE' ),'max_HGBUR_gr'] = 0
    mf.ix[(mf['max_HGBUR_gr'] != "MISSING") &  (mf['max_HGBUR_gr'] != 'NEGATIVE' ),'max_HGBUR_gr'] = 1

# grouping urinal glucose
    mf.ix[mf['max_GLUURN_gr'] == "LARGE" ,'max_GLUURN_gr'] = 2
    mf.ix[(mf['max_GLUURN_gr'] == "MISSING") |  (mf['max_GLUURN_gr'] == 'NEGATIVE' ),'max_GLUURN_gr'] = 0
    mf.ix[(mf['max_GLUURN_gr'] != "MISSING") &  (mf['max_GLUURN_gr'] != 'NEGATIVE' ),'max_GLUURN_gr'] = 1

# grouping of No of complete blood count tests
    mf.ix[mf['count_HGBn'] > 1 ,'count_HGBn'] = "2 or more"
    
    model_dict = {}

    models_all = ["cvcomp" ,"mvcomp","aki","icucomp","neuro_delirium","vtenew","woundcomp","sepsis"]
    for mod in range(0,len(models_all)):
        model = models_all[mod]
        df = mf.copy()
        print(model)
        # subset on model
        sub_category_dictionary = category_dictionary[category_dictionary['Model'] == model]
        sub_category_dictionary_cluster = category_dictionary_cluster[category_dictionary_cluster['Model'] == model]
        sub_numeric_dictionary = numeric_dictionary[numeric_dictionary['Model'] == model]
        sub_procedure_dictionary = procedure_dictionary[procedure_dictionary['Model'] == model]
        selected_features_vif_selection = selected_featured_vif[selected_featured_vif['Model'] == model]
        sub_category_dictionary['Vocabulary'] = sub_category_dictionary['Vocabulary'].apply(lambda x: str(x))
        test = sub_category_dictionary[sub_category_dictionary['Feature'] == 'zip5']

        for index,row in df.iterrows():

            for ind , feat in feature_all.iterrows():
                if(feat['feature_type'] == 'cat'):
                    if(feat['feature_name'] == 'pr1c'):

                        lrow = sub_procedure_dictionary[sub_procedure_dictionary['original'] == row[feat['feature_name']]]
                        if not (lrow.empty):
                            df.ix[index ,feat['feature_name']] = float(lrow['transformed'].values[0])
                        else:
                            df.ix[index, feat['feature_name']] = 0
                            
                    else :
                        df.ix[index, feat['feature_name']] = str(row[feat['feature_name']])
                        lrow = sub_category_dictionary[(sub_category_dictionary['Feature'] == feat['feature_name'])]
                        lrow = lrow[lrow['Vocabulary'] == str(row[feat['feature_name']])]

                        if not (lrow.empty) :
                            df.ix[index, feat['feature_name']] = float(lrow['p'].values[0])
                        else :
                            crow = sub_category_dictionary_cluster[sub_category_dictionary_cluster['Feature'] == feat['feature_name']]
                            if not (crow.empty):
                                if(str(crow['cl_vocabulary'].values[0]) == row[feat['feature_name']]):
                                    df.ix[index, feat['feature_name']] = crow['cl_p'].values[0]
                                else :
                                    df.ix[index, feat['feature_name']] = crow['cl_p'].values[1]
                else:
                    lrow = sub_numeric_dictionary[sub_numeric_dictionary['Feature'] == feat['feature_name']]
                    if not (lrow.empty):
                        if(row[feat['feature_name']] == 'MISSING'):
                            df.ix[index, feat['feature_name']]  = lrow['mean'].values[0]
                        elif(row[feat['feature_name']] > lrow['higher_sig'].values[0]) :
                            df.ix[index, feat['feature_name']] = lrow['quartile3'].values[0]
                        elif(row[feat['feature_name']] < lrow['lower_sig'].values[0]):
                            df.ix[index, feat['feature_name']] = lrow['quartile1'].values[0]

        rdata = pd.DataFrame()
        for ft in selected_features_vif_selection['Feature'].values :
            rdata[ft] = df[ft]

        #filename = "/home/rajendra/workspace/Prisma/output/"+ model + "_data.csv"
        filename = model + "_data.csv"
        
        #print "filename: "+filename
        df.to_csv(get_path('output',filename))
        
        model_dict[filename] = df
                       
    return model_dict
        
        
