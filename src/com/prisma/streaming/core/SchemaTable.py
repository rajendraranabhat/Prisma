'''
Created on Oct 11, 2016

@author: rajendra
'''
from pyspark.sql.types import *

schema_data = StructType([
                StructField("acc", IntegerType(), True),
                StructField("age", IntegerType(), True),
                StructField("Gender", StringType(), True),
                StructField("race2", StringType(), True),
                StructField("zip5", IntegerType(), True),
                StructField("pay_grp", IntegerType(), True),
                StructField("County", StringType(), True),
                StructField("rural", IntegerType(), True),
                StructField("total", IntegerType(), True),
                StructField("Med_inc", IntegerType(), True),
                StructField("prop_black", DoubleType(), True),
                StructField("prop_hisp", DoubleType(), True),
                StructField("Prop_pov", DoubleType(), True),
                StructField("zipdist2", DoubleType(), True),
                StructField("admit_day1", StringType(), True),
                StructField("admit_mth", IntegerType(), True),
                StructField("Year_of_admission", IntegerType(), True),
                StructField("weekend_adm", IntegerType(), True),
                StructField("attend_doc", IntegerType(), True),
                StructField("Admission_Source", StringType(), True),
                StructField("Admitting_Service", StringType(), True),
                StructField("Admitting_type", StringType(), True),
                StructField("emergent", IntegerType(), True),
                StructField("pr1_day", IntegerType(), True),
                StructField("service1", StringType(), True),
                StructField("pr1c", StringType(), True),
                StructField("cci", IntegerType(), True),
                StructField("NDX", IntegerType(), True),
                StructField("MDC", StringType(), True),
                StructField("imi", IntegerType(), True),
                StructField("ichf", IntegerType(), True),
                StructField("ipvd", IntegerType(), True),
                StructField("icvd", IntegerType(), True),
                StructField("icpd", IntegerType(), True),
                StructField("liverd", IntegerType(), True),
                StructField("diabetes", IntegerType(), True),
                StructField("icancer", IntegerType(), True),
                StructField("imcancer", IntegerType(), True),
                StructField("cancer", IntegerType(), True),
                StructField("VALVE", IntegerType(), True),
                StructField("HYPOTHY", IntegerType(), True),
                StructField("COAG", IntegerType(), True),
                StructField("OBESE", IntegerType(), True),
                StructField("WGHTLOSS", IntegerType(), True),
                StructField("LYTES", IntegerType(), True),
                StructField("alc_drug", IntegerType(), True),
                StructField("anemia", IntegerType(), True),
                StructField("DEPRESS", IntegerType(), True),
                StructField("HTN_C", IntegerType(), True),
                StructField("CKD_corr", IntegerType(), True),
                StructField("esrd_corr", IntegerType(), True),
                StructField("PARA", IntegerType(), True),
                StructField("NEURO", IntegerType(), True),
                StructField("no_meds_on_adm", IntegerType(), True),
                StructField("aminog_adm", IntegerType(), True),
                StructField("bicarb_adm", IntegerType(), True),
                StructField("diuret_adm", IntegerType(), True),
                StructField("steroi_adm", IntegerType(), True),
                StructField("vanco_adm", IntegerType(), True),
                StructField("ace_adm", IntegerType(), True),
                StructField("nsaids_adm", IntegerType(), True),
                StructField("asa_adm", IntegerType(), True),
                StructField("antiemetic_adm", IntegerType(), True),
                StructField("betablockers_adm", IntegerType(), True),
                StructField("statin_adm", IntegerType(), True),
                StructField("inot_pres_adm", IntegerType(), True),
                StructField("eGFR_epi_new", DoubleType(), True),
                StructField("ratio_firstCr_mdrd", DoubleType(), True),
                StructField("min_HGB", DoubleType(), True),
                StructField("max_PROTUR_gr2", StringType(), True),
                StructField("max_HGBUR_gr", StringType(), True),
                StructField("max_GLUURN_gr", StringType(), True),
                StructField("count_HGBn", IntegerType(), True),
                StructField("count_PROTURn", IntegerType(), True),
                StructField("BLDLOSS", IntegerType(), True),
                StructField("ANEMDEF", IntegerType(), True),
                StructField("ALCOHOL", IntegerType(), True),
                StructField("DRUG", IntegerType(), True),
                StructField("frailty_score_all50", StringType(), True),
                StructField("aki_recov_corr", StringType(), True),
                StructField("ckd_stage_gr", StringType(), True),
                StructField("ckd_stage", StringType(), True),
                StructField("GR_renal5_newest", StringType(), True),
                StructField("grp8_CORR", StringType(), True),
                StructField("kdigo_corr", IntegerType(), True),
                StructField("aki_kdigo_corr", IntegerType(), True),
                StructField("rrt_corr", IntegerType(), True),
                StructField("Died", StringType(), True),
                StructField("icu_days2", IntegerType(), True),
                StructField("ICU_comp", IntegerType(), True),
                StructField("MV_days", IntegerType(), True),
                StructField("sepsis", IntegerType(), True),
                StructField("septic_shock", IntegerType(), True),
                StructField("severe_sepsis", IntegerType(), True),
                StructField("postop_inf_new", IntegerType(), True),
                StructField("wound_comp_new", IntegerType(), True),
                StructField("proc_comp_new", IntegerType(), True),
                StructField("cv_comp_new", IntegerType(), True),
                StructField("pulm_comp_new", IntegerType(), True),
                StructField("vte_new", IntegerType(), True),
                StructField("gi_comp_new", IntegerType(), True),
                StructField("neurocom_new", IntegerType(), True),
                StructField("delirium_new", IntegerType(), True),
                StructField("proc_wound_inf", IntegerType(), True),
                StructField("neuro_delirium", IntegerType(), True),
                StructField("cv_inot_pres", IntegerType(), True),
                StructField("ltostatus_new", IntegerType(), True),
                StructField("censor", IntegerType(), True),
                StructField("mort_status_90d", IntegerType(), True),
                StructField("mort_status_30d", IntegerType(), True),
                StructField("time", DoubleType(), True),
                StructField("ICD_CODE", StringType(), True),
                StructField("cod_cancer_Gans", IntegerType(), True),
                StructField("cod_Cardiovascular_Gans", IntegerType(), True),
                StructField("status_cardio_Gans", IntegerType(), True)
        ])

