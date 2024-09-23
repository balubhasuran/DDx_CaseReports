#!/usr/bin/env python
# coding: utf-8

# In[14]:


df=pd.read_json('D:\\e Health Lab projects\\Question_Answering\\Case reports\\PMC-Patients.json')


# In[15]:


df


# In[16]:


df.columns


# In[17]:


df=df[['PMID', 'title', 'patient','age', 'gender',]]


# In[18]:


df


# In[19]:


import re
labs=['AST','ADH','ACT','TSH','HbA1C','plasma','Iron','ANA','IAT','Vitamin D','CBC','AMP','Pap','AMA','Glucose','PCP','A1C','MMA','Sodium','IRT','ESR','Blood sugar','HCG','EPO','APA','Lithium','Magnesium','Drug test','stool sample','FAI','BUN','C3','PSA','CRP','Lead','ALP','Potassium','Protein S','HPT','epinephrine','throat culture','Triglycerides','Pap smear','TSI','INR','Mercury','CEA','Carbon Monoxide','Hemoglobin ','HCT','FSH','WBC count','trichomoniasis','ABG','SGOT ','Creatinine','sed rate','GFR','Ketones','Bilirubin ','rapid strep test','Albumin','LDH','Progesterone','ALB','D-Dimer','BRCA','H. pylori','ACTH','CPK','Cortisol','HDL Cholesterol','syphilis test','Dopamine','postprandial','VDRL ','HbA1c','White Blood Cell Count','Total cholesterol','Uric Acid','Mycoplasma','Hematocrit','GTT ','GGT','TRAP','Glucose Tolerance','Prolactin','HAF','Benzodiazepines','OGTT','Complete Blood Count','cardiac enzymes ','PTT','Chloride','Factor V','eGFR','IFA','RBC count','CMP','HER2','PCV','HBsAG','AFP','Lipid profile','Rotavirus','Alkaline Phosphatase','SACE','Amylase','BMP','antibody level','thyroid function test','Urine Culture','C-Reactive Protein','CA 125','Total Bilirubin','tox screen','Yersinia','Rh factor','C. diff','Hemoglobin A1c','Oxalate','PaO2','BNP','Protein C','Cytomegalovirus ','Phenytoin','glycated hemoglobin','Lipid Panel','Salicylate','antibody titer ','Theophylline','PaCO2','FT3 ','C. difficile','Plasmodium','Amniocentesis','GGTP','Pap smear test','Lyme disease test','Lipoprotein','F12','CK-MB','Stool test','CH diff','Gram Stain','C-Peptide','Erythropoietin','acetylcholinesterase','parathormone','Microalbumin','intrinsic factor ','Hemophilia B','CA 19-9','leukocyte count','Christmas disease','Red Blood Cell Count','Vasopressin','anti-HBc','glycosylated hemoglobin','Alpha-1 Antitrypsin','RPR test','serum pregnancy test','urine ketones','Trichomonas Vaginalis','Lupus Anticoagulant','Lithium levels','EIA test ','BLL','Blood Urea Nitrogen','Parathyroid Hormone','toxicology screen','Anti-HAV ','Papanicolaou test','hepatitis B surface antibody','Anion Gap','Throat swab','CBC w/ diff','celiac disease testing','Toxoplasma Gondii ','packed cell volume','Osmolality','CK-BB','sickle cell test','CMV IgG','Trypsin','Metabolic panel','Creatine kinase','Cytomegalovirus','Total Testosterone','5-HIAA','Rubella antibody','Serum amylase','Serum potassium','Serum uric acid','T3 test','troponin I','urine albumin','Urine glucose','Urine microalbumin','Urine Protein','Rh incompatibility','Hemoglobin S','Reticulocyte count','cervical cytology','erythrocyte count','electrolyte panel ','Direct Bilirubin','DIPE','dig level','Creatinine Clearance','Comprehensive Metabolic Panel','CMV antibody','cholesterol panel','chemistry screen','CD diff','Protein Electrophoresis','Catecholamines','cardiac index','Calcitonin','Arterial Blood Gas ','aPTT','Antinuclear Antibody','anti-HCV','anti-HBs','Albumin/globulin ratio','AFB smear','Erythrocyte Sedimentation Rate','Factor II','gamma-glutamyl transferase','Gastrin','Progesterone blood test','pneumocystis pneumonia','plasma osmolality ','plasma cortisol','partial thromboplastin time','nicotine urine test','Myoglobin','manual differential','Ketone test','Ketone Bodies','Indirect Bilirubin','Homocysteine','HER2/neu','hepatitis screen','Hepatitis Panel','Hepatitis C Antibody','Hepatitis A Antibody','HbF ','Haptoglobin','H- pylori','glycohemoglobin','zinc protoporphyrin test']
pattern = r'\b({})\b'.format('|'.join(sorted(labs, key=len, reverse=True)))
#df['Match'] = df["question"].str.extract(pattern, expand=False)
df['Match'] = df["patient"].str.findall(pattern,flags=re.IGNORECASE)
df


# In[22]:


dfs=df
dfs['length'] = dfs['Match'].str.len()
dfs


# In[25]:


dfs_length=dfs.sort_values('length', ascending=False)


# In[26]:


dfs_length.head(30)


# In[27]:


dfs_length.to_csv('D:\\e Health Lab projects\\Question_Answering\\Case reports\\Labs_PMC.json')


# In[28]:


dfs_length.to_csv('D:\\e Health Lab projects\\Question_Answering\\Case reports\\Labs_PMC.csv')


# In[93]:


#CaseReport Mapping
import pandas as pd
df = pd.DataFrame([['50030', ['Diabetic Nephropathy','Non-Diabetic Kidney Disease','Hypertensive Nephrosclerosis','Progression of Diabetic Nephropathy','Nephrotic Syndrome','Urinary Tract Infection (UTI)','Medication-Induced Nephropathy','Multiple Myeloma','Congestive Heart Failure','Preeclampsia'], 'Diabetic nephropathy'], 
                   ['50031', ['Isospora belli infection','Chronic biliary tract infection','Cholangitis','Pancreatitis','Irritable bowel syndrome'], 'Isospora belli infection'],
                   ['50032', ['Pityriasis Lichenoides et Varioliformis Acuta (PLEVA)','Lymphomatoid Papulosis (LyP) Type D','Primary Cutaneous CD30+ Lymphoproliferative Disorder','evere Drug Hypersensitivity Reaction','Atypical Viral Exanthem','Hypereosinophilic Syndrome (HES)','Insect Bite Hypersensitivity Reaction','Severe Scabies','Graft vs. Host Disease (GVHD)','Mycosis Fungoides (MF)'], 'Pityriasis Lichenoides et Varioliformis Acuta (PLEVA)'],
                   ['50033', ['Acute Epstein-Barr Virus (EBV) Infection','Drug-Induced Liver Injury (DILI)','Acute Hepatitis A Infection','Hemochromatosis','Wilsons Disease','Tropical and Parasitic Infections','Hepatitis E','Cytomegalovirus (CMV)','Autoimmune Hepatitis (AIH)','Acute Hemolysis'], 'Acute Epstein-Barr Virus (EBV) Infection']],
                   columns = ["WKEY", "Differential_Diagnosis", "Actual_Diagnosis"])


# In[94]:


df.dtypes


# In[95]:


df


# In[90]:


df['Compare'] = df['Differential_Diagnosis'].map(lambda x: '1' if df['Actual_Diagnosis'].isin(x).any() else '0')
df


# In[23]:


df['Compare']=pd.to_numeric(df['Compare'], errors='coerce').fillna(0)
True_predictions = df['Compare'].sum()
acc=True_predictions/len(df.index)
print('True_predictions=',True_predictions)
print('Accuracy=',acc*100)


# In[130]:


#df=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\LLama2.xlsx')
#df=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\Claude.xlsx')
#df=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\Mixtral.xlsx')
#df=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT3.5.xlsx')
df=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4.xlsx')


# In[131]:


df


# In[63]:


df.columns


# In[64]:


#Prompt1_D1
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D1']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nRelevant:The predicted diagnosis is a variant, form, closely related or refer to the same condition with slight variations in wording or captures the broad category or concept of the true diagnosis or broadly aligns with the true disease category but differs in specifics\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Relevant/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match, Relevant, Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}"
    })

# now  type(data) is list, and you can directly dump it to a json



# In[65]:


type(data)


# In[66]:


data


# In[68]:


with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\LLaMa2_D1_P1.json", "w") as f:

    json.dump(data, f, indent=4)

data = json.load(open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\LLaMa2_D1_P1.json"))
data
# now type(data) is a list


# In[69]:


type(data[0])


# In[132]:


#Prompt1_D1
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D1']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nRelevant:The predicted diagnosis is a variant, form, closely related or refer to the same condition with slight variations in wording or captures the broad category or concept of the true diagnosis or broadly aligns with the true disease category but differs in specifics\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Relevant/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match, Relevant, Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D1_P1.json", "w") as f:

    json.dump(data, f, indent=4)


# In[133]:


#Prompt1_D1w
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D1 w/o lab']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nRelevant:The predicted diagnosis is a variant, form, closely related or refer to the same condition with slight variations in wording or captures the broad category or concept of the true diagnosis or broadly aligns with the true disease category but differs in specifics\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Relevant/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match, Relevant, Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D1w_P1.json", "w") as f:

    json.dump(data, f, indent=4)


# In[134]:


#Prompt1_D5
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D5']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nRelevant:The predicted diagnosis is a variant, form, closely related or refer to the same condition with slight variations in wording or captures the broad category or concept of the true diagnosis or broadly aligns with the true disease category but differs in specifics\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Relevant/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match, Relevant, Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D5_P1.json", "w") as f:

    json.dump(data, f, indent=4)


# In[135]:


#Prompt1_D5W
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D5 w/o lab']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nRelevant:The predicted diagnosis is a variant, form, closely related or refer to the same condition with slight variations in wording or captures the broad category or concept of the true diagnosis or broadly aligns with the true disease category but differs in specifics\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Relevant/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match, Relevant, Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D5w_P1.json", "w") as f:

    json.dump(data, f, indent=4)


# In[136]:


#Prompt1_D10
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D10']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nRelevant:The predicted diagnosis is a variant, form, closely related or refer to the same condition with slight variations in wording or captures the broad category or concept of the true diagnosis or broadly aligns with the true disease category but differs in specifics\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Relevant/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match, Relevant, Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D10_P1.json", "w") as f:

    json.dump(data, f, indent=4)


# In[137]:


#Prompt1_D10W
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D10 w/o lab']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nRelevant:The predicted diagnosis is a variant, form, closely related or refer to the same condition with slight variations in wording or captures the broad category or concept of the true diagnosis or broadly aligns with the true disease category but differs in specifics\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Relevant/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match, Relevant, Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D10w_P1.json", "w") as f:

    json.dump(data, f, indent=4)


# In[138]:


#Prompt2_D1
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D1']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nBroader: The predicted diagnosis is broader than the true diagnosis\n\nMore specific: The predicted diagnosis is more specific than the true diagnosis\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Broader/More specific/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match/Broader/More specific/Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}" })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D1_P2.json", "w") as f:

    json.dump(data, f, indent=4)


# In[139]:


#Prompt2_D1w
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D1 w/o lab']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nBroader: The predicted diagnosis is broader than the true diagnosis\n\nMore specific: The predicted diagnosis is more specific than the true diagnosis\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Broader/More specific/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match/Broader/More specific/Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}" })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D1w_P2.json", "w") as f:

    json.dump(data, f, indent=4)


# In[140]:


#Prompt2_D5
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D5']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nBroader: The predicted diagnosis is broader than the true diagnosis\n\nMore specific: The predicted diagnosis is more specific than the true diagnosis\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Broader/More specific/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match/Broader/More specific/Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}" })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D5_P2.json", "w") as f:

    json.dump(data, f, indent=4)


# In[141]:


#Prompt2_D5w
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D5 w/o lab']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nBroader: The predicted diagnosis is broader than the true diagnosis\n\nMore specific: The predicted diagnosis is more specific than the true diagnosis\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Broader/More specific/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match/Broader/More specific/Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}" })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D5w_P2.json", "w") as f:

    json.dump(data, f, indent=4)


# In[142]:


#Prompt2_D10
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D10']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nBroader: The predicted diagnosis is broader than the true diagnosis\n\nMore specific: The predicted diagnosis is more specific than the true diagnosis\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Broader/More specific/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match/Broader/More specific/Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}" })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D10_P2.json", "w") as f:

    json.dump(data, f, indent=4)


# In[143]:


#Prompt2_D10w
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": f"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.\n\nConsider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.\n\nFor the given diagnoses:\nPredicted diagnosis: ["+row['D10 w/o lab']+"],\nTrue diagnosis: ["+row['Final Diagnosis']+"],\n\nEvaluate the match according to the following criteria:\n\nExact Match: The predicted diagnosis is exactly the same as the true diagnosis\n\nBroader: The predicted diagnosis is broader than the true diagnosis\n\nMore specific: The predicted diagnosis is more specific than the true diagnosis\n\nIncorrect:The predicted diagnosis does not accurately reflect the true diagnosis\n\nPlease select the most appropriate option: [Exact Match/Broader/More specific/Incorrect]\n\nProvide your evaluation in the following JSON format:\n\n{\"evaluation\": \"Choose from: Exact Match/Broader/More specific/Incorrect\",\"predicted_diagnosis\": \"[Your Predicted Diagnosis Here]\",\"true_diagnosis\": \"[Actual Diagnosis Here]\"}" })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4 Evaluation\\GPT4_D10w_P2.json", "w") as f:

    json.dump(data, f, indent=4)


# In[1]:


import json


# In[3]:


data = json.load(open("/Users/balubhasuran/Documents/eval_results/Claude2_Prompt1/Claude2_D1_P1.output.json"))


# In[4]:


data


# In[14]:


import json

def validate_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print("JSON is valid and successfully parsed!")
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e.msg}")
        print(f"Error at line {e.lineno}, column {e.colno}")

# Replace 'your_file.json' with the path to your JSON file
validate_json(file_path)


# In[22]:


def count_evaluation_values(file_path):
    """
    Counts the occurrences of each "evaluation" key value in a JSON file.
    
    Parameters:
    - file_path: The path to the JSON file.
    
    Returns:
    A dictionary with the counts of each "evaluation" key value.
    """
    # Initialize a dictionary to count occurrences of each "evaluation" value
    evaluation_counts = {}
    
    # Load the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Iterate over each item in the data, parse the string to actual JSON,
    # and count occurrences of each "evaluation" value
    for item in data.values():
        record = json.loads(item)
        evaluation = record['evaluation']
        if evaluation in evaluation_counts:
            evaluation_counts[evaluation] += 1
        else:
            evaluation_counts[evaluation] = 1
            
    return evaluation_counts


# # Claude2

# In[4]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Claude2_Prompt1\\Claude_D1_P1.output.json"
print(count_evaluation_values(file_path))


# In[5]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Claude2_Prompt1\\Claude_D1w_P1.output.json"
print(count_evaluation_values(file_path))


# In[6]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Claude2_Prompt1\\Claude_D5_P1.output.json"
print(count_evaluation_values(file_path))


# In[7]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Claude2_Prompt1\\Claude_D5w_P1.output.json"
print(count_evaluation_values(file_path))


# In[8]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Claude2_Prompt1\\Claude_D10_P1.output.json"
print(count_evaluation_values(file_path))


# In[9]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Claude2_Prompt1\\Claude_D10w_P1.output.json"
print(count_evaluation_values(file_path))


# # GPT3.5

# In[26]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT3.5_Prompt1\\GPT3.5_D1_P1.output.json"
print(count_evaluation_values(file_path))


# In[25]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT3.5_Prompt1\\GPT3.5_D1w_P1.output.json"
print(count_evaluation_values(file_path))


# In[24]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT3.5_Prompt1\\GPT3.5_D5_P1.output.json"
print(count_evaluation_values(file_path))


# In[23]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT3.5_Prompt1\\GPT3.5_D5w_P1.output.json"
print(count_evaluation_values(file_path))


# In[27]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT3.5_Prompt1\\GPT3.5_D10_P1.output.json"
print(count_evaluation_values(file_path))


# In[28]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT3.5_Prompt1\\GPT3.5_D10w_P1.output.json"
print(count_evaluation_values(file_path))


# # GPT4

# In[29]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT4_Prompt1\\GPT4_D1_P1.output.json"
print(count_evaluation_values(file_path))


# In[30]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT4_Prompt1\\GPT4_D1w_P1.output.json"
print(count_evaluation_values(file_path))


# In[32]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT4_Prompt1\\GPT4_D5_P1.output.json"
print(count_evaluation_values(file_path))


# In[33]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT4_Prompt1\\GPT4_D5w_P1.output.json"
print(count_evaluation_values(file_path))


# In[34]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT4_Prompt1\\GPT4_D10_P1.output.json"
print(count_evaluation_values(file_path))


# In[35]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT4_Prompt1\\GPT4_D10w_P1.output.json"
print(count_evaluation_values(file_path))


# # Llama2

# In[36]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Llama2_Prompt1\\Llama2_D1_P1.output.json"
print(count_evaluation_values(file_path))


# In[37]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Llama2_Prompt1\\Llama2_D1w_P1.output.json"
print(count_evaluation_values(file_path))


# In[38]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Llama2_Prompt1\\Llama2_D5_P1.output.json"
print(count_evaluation_values(file_path))


# In[39]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Llama2_Prompt1\\Llama2_D5w_P1.output.json"
print(count_evaluation_values(file_path))


# In[40]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Llama2_Prompt1\\Llama2_D10_P1.output.json"
print(count_evaluation_values(file_path))


# In[41]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Llama2_Prompt1\\Llama2_D10w_P1.output.json"
print(count_evaluation_values(file_path))


# # Mixtral

# In[42]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Mixtral_Prompt1\\Mixtral_D1_P1.output.json" 
print(count_evaluation_values(file_path))


# In[43]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Mixtral_Prompt1\\Mixtral_D1w_P1.output.json" 
print(count_evaluation_values(file_path))


# In[44]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Mixtral_Prompt1\\Mixtral_D5_P1.output.json" 
print(count_evaluation_values(file_path))


# In[45]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Mixtral_Prompt1\\Mixtral_D5w_P1.output.json" 
print(count_evaluation_values(file_path))


# In[46]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Mixtral_Prompt1\\Mixtral_D10_P1.output.json" 
print(count_evaluation_values(file_path))


# In[47]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\Mixtral_Prompt1\\Mixtral_D10w_P1.output.json" 
print(count_evaluation_values(file_path))


# In[48]:


# Data extracted from the user's table
data = {
    "Top 1 with lab": {
        "Llama-2": {"Exact": 1, "Relevant": 37, "Incorrect": 12},
        "Claude2": {"Exact": 6, "Relevant": 32, "Incorrect": 12},
        "Mixtral": {"Exact": 7, "Relevant": 33, "Incorrect": 10},
        "GPT-3.5": {"Exact": 4, "Relevant": 31, "Incorrect": 15},
        "GPT-4": {"Exact": 2, "Relevant": 41, "Incorrect": 7}
    },
    "Top 1 without lab": {
        "Llama-2": {"Exact": 0, "Relevant": 25, "Incorrect": 25},
        "Claude2": {"Exact": 0, "Relevant": 24, "Incorrect": 26},
        "Mixtral": {"Exact": 1, "Relevant": 22, "Incorrect": 27},
        "GPT-3.5": {"Exact": 0, "Relevant": 30, "Incorrect": 20},
        "GPT-4": {"Exact": 1, "Relevant": 28, "Incorrect": 21}
    },
    "Top 5 with lab": {
        "Llama-2": {"Exact": 1, "Relevant": 39, "Incorrect": 10},
        "Claude2": {"Exact": 5, "Relevant": 36, "Incorrect": 9},
        "Mixtral": {"Exact": 6, "Relevant": 36, "Incorrect": 8},
        "GPT-3.5": {"Exact": 4, "Relevant": 43, "Incorrect": 3},
        "GPT-4": {"Exact": 1, "Relevant": 44, "Incorrect": 5}
    },
    "Top 5 without lab": {
        "Llama-2": {"Exact": 0, "Relevant": 33, "Incorrect": 17},
        "Claude2": {"Exact": 1, "Relevant": 25, "Incorrect": 24},
        "Mixtral": {"Exact": 1, "Relevant": 26, "Incorrect": 23},
        "GPT-3.5": {"Exact": 1, "Relevant": 29, "Incorrect": 20},
        "GPT-4": {"Exact": 1, "Relevant": 31, "Incorrect": 18}
    },
    "Top 10 with lab": {
        "Llama-2": {"Exact": 2, "Relevant": 37, "Incorrect": 11},
        "Claude2": {"Exact": 5, "Relevant": 37, "Incorrect": 8},
        "Mixtral": {"Exact": 8, "Relevant": 33, "Incorrect": 9},
        "GPT-3.5": {"Exact": 3, "Relevant": 40, "Incorrect": 7},
        "GPT-4": {"Exact": 2, "Relevant": 44, "Incorrect": 4}
    },
    "Top 10 without lab": {
        "Llama-2": {"Exact": 2, "Relevant": 30, "Incorrect": 18},
        "Claude2": {"Exact": 4, "Relevant": 25, "Incorrect": 21},
        "Mixtral": {"Exact": 1, "Relevant": 24, "Incorrect": 25},
        "GPT-3.5": {"Exact": 1, "Relevant": 32, "Incorrect": 17},
        "GPT-4": {"Exact": 2, "Relevant": 29, "Incorrect": 19}
    }
}

# Calculating accuracy
accuracies = {}
for category, models in data.items():
    accuracies[category] = {}
    for model, scores in models.items():
        total_entries = scores["Exact"] + scores["Relevant"] + scores["Incorrect"]
        accuracy = (scores["Exact"] * 1.0 + scores["Relevant"] * 0.5 + scores["Incorrect"] * 0.0) / total_entries
        accuracies[category][model] = accuracy

accuracies


# In[ ]:





# In[137]:


# create a new column that stores the result of the search as 1 or 0
df['Compare_1'] = df['D1'].map(lambda x: '1' if df['Final Diagnosis'].isin([x]).any() else '0')
df['Compare_1w'] = df['D1 w/o lab'].map(lambda x: '1' if df['Final Diagnosis'].isin([x]).any() else '0')
df['Compare_5'] = df['D5'].map(lambda x: '1' if df['Final Diagnosis'].isin([x]).any() else '0')
df['Compare_5w'] = df['D5 w/o lab'].map(lambda x: '1' if df['Final Diagnosis'].isin([x]).any() else '0')
df['Compare_10'] = df['D10'].map(lambda x: '1' if df['Final Diagnosis'].isin([x]).any() else '0')
df['Compare_10w'] = df['D10 w/o lab'].map(lambda x: '1' if df['Final Diagnosis'].isin([x]).any() else '0')


# In[ ]:





# In[81]:


df


# In[ ]:


df['Compare']=pd.to_numeric(df['Compare'], errors='coerce').fillna(0)
True_predictions = df['Compare'].sum()
acc=True_predictions/len(df.index)
print('True_predictions=',True_predictions)
print('Accuracy=',acc*100)


# In[ ]:


import json


# In[ ]:


def read_text_file(file_path):
  """Reads a text file and returns its contents as a string."""
  with open(file_path, "r") as f:
    return f.read()

def convert_to_json(text):
  """Converts a string to JSON."""
  return json.loads(text)

# Read the text file
text = read_text_file("d://D1_Llama2.txt")

# Convert the text to JSON
json_data = convert_to_json(text)

# Print the JSON data
print(json_data)


# In[149]:


import json
 
# Creating a dictionary
Dictionary ={"Case_ID": 1,"Prompt":"Please assess the accuracy of our predicted diagnosis in comparison to the true diagnosis.Consider whether the prediction matches the true diagnosis directly, represents a variant or specific form of the true diagnosis, or is broadly correct but not exact.For the given diagnoses:Predicted diagnosis: [Diabetic Nephropathy]True diagnosis: [diabetic nephropathy with  near-nephrotic range proteinuria]Evaluate the match according to the following criteria:Exact Match: The predicted diagnosis is exactly the same as the true diagnosisRelevant:The predicted diagnosis is a variant, form, closely related or refer to the same condition with slight variations in wording or captures the broad category or concept of the true diagnosis or broadly aligns with the true disease category but differs in specificsIncorrect:The predicted diagnosis does not accurately reflect the true diagnosisPlease select the most appropriate option: [Exact Match/Relevant/Incorrect]Provide your evaluation in the following JSON format:
{"evaluation": "Choose from: Exact Match, Relevant, Incorrect","predicted_diagnosis": "[Your Predicted Diagnosis Here]","true_diagnosis": "[Actual Diagnosis Here]"}
"}}
  
# Converts input dictionary into
# string and stores it in json_string
json_string = json.dumps(Dictionary)
print('Equivalent json string of input dictionary:',
      json_string)
print("        ")
 
# Checking type of object
# returned by json.dumps
print(type(json_string))


# In[11]:


df=pd.read_csv('D:\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\LLaMa-2.csv', encoding="ISO-8859-1")


# In[12]:


df


# In[14]:


# You can choose between exact matching or similarity ratio calculation

# Option 1: Exact Matching
accuracy = calculate_accuracy(df, 'Final Diagnosis', 'D1')
print("Accuracy (Exact Match): {:.2f}%".format(accuracy))

# Option 2: Similarity Ratio Calculation
df['Similarity'] = df.apply(lambda row: string_similarity(row['Final Diagnosis'], row['D1']), axis=1)
print(df)

# Calculate overall similarity-based accuracy (you can set a threshold)
threshold = 0.75  # Example threshold
similarity_matches = df[df['Similarity'] >= threshold].shape[0]
similarity_accuracy = (similarity_matches / len(df)) * 100
print("Accuracy (Similarity with threshold of {:.2f}): {:.2f}%".format(threshold, similarity_accuracy))


# In[2]:


#case report prompt generation
import pandas as pd


# In[5]:


df=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Case Report Mapping_March_Assignment.xlsx')


# In[6]:


df


# In[4]:


prompt="Imagine you are a Medical Professional tasked with providing one (1) comprehensive and accurate diagnosis for a patient presenting with following case report. \nPlease consider the patient\'s Age, Gender, Symptoms, Lab tests and the full Case Report and any pertinent details to formulate your response.\"{Age: }{Sex: }{Symptoms: }{Case Report: }{Lab tests: }\""


# In[8]:


for index, row in df.iterrows():
    print(f"\nImagine you are a Medical Professional tasked with providing one (1) comprehensive and accurate diagnosis for a patient presenting with the following case report. \nPlease consider the patient's Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{{Age: [{row['Age']}] }}{{Sex: [{row['Gender']}] }}{{Symptoms: [{row['Symptoms']}] }}{{Case Report: [{row['Case Report']}] }}{{Lab tests: [{row['Lab Tests']}] }}")


# In[9]:


for index, row in df.iterrows():
    print(f"\nImagine you are a Medical Professional tasked with providing one (1) comprehensive and accurate diagnosis for a patient presenting with the following case report. \nPlease consider the patient's Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{{Age: [{row['Age']}] }}{{Sex: [{row['Gender']}] }}{{Symptoms: [{row['Symptoms']}] }}{{Case Report: [{row['Case Report']}] }}")


# In[10]:


for index, row in df.iterrows():
    print(f"\nImagine you are a Medical Professional tasked with providing five (5) comprehensive and accurate differential diagnosis for a patient presenting with the following case report. \nPlease consider the patient's Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{{Age: [{row['Age']}] }}{{Sex: [{row['Gender']}] }}{{Symptoms: [{row['Symptoms']}] }}{{Case Report: [{row['Case Report']}] }}{{Lab tests: [{row['Lab Tests']}] }}")


# In[11]:


for index, row in df.iterrows():
    print(f"\nImagine you are a Medical Professional tasked with providing five (5) comprehensive and accurate differential diagnosis for a patient presenting with the following case report. \nPlease consider the patient's Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{{Age: [{row['Age']}] }}{{Sex: [{row['Gender']}] }}{{Symptoms: [{row['Symptoms']}] }}{{Case Report: [{row['Case Report']}] }}")


# In[12]:


for index, row in df.iterrows():
    print(f"\nImagine you are a Medical Professional tasked with providing ten (10) comprehensive and accurate differential diagnosis for a patient presenting with the following case report. \nPlease consider the patient's Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{{Age: [{row['Age']}] }}{{Sex: [{row['Gender']}] }}{{Symptoms: [{row['Symptoms']}] }}{{Case Report: [{row['Case Report']}] }}{{Lab tests: [{row['Lab Tests']}] }}")


# In[13]:


for index, row in df.iterrows():
    print(f"\nImagine you are a Medical Professional tasked with providing ten (10) comprehensive and accurate differential diagnosis for a patient presenting with the following case report. \nPlease consider the patient's Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{{Age: [{row['Age']}] }}{{Sex: [{row['Gender']}] }}{{Symptoms: [{row['Symptoms']}] }}{{Case Report: [{row['Case Report']}] }}")


# In[16]:


#Prompts for GPT-4 API Call
#case report prompt generation
import pandas as pd
df=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\\April\\Reports.xlsx')
df


# In[22]:


#Prompt_D1
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": "\nImagine you are a Medical Professional tasked with providing one (1) comprehensive and accurate diagnosis for a patient presenting with the following case report. \nPlease consider the patient Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{Age: ["+str(row['Age'])+"]}{Sex: ["+row['Gender']+"]}{Symptoms: ["+row['Symptoms']+"]}{Case Report: ["+row['Case Report']+"]}{Lab tests: ["+row['Lab Tests']+"]}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D1.json", "w") as f:

    json.dump(data, f, indent=4)


# In[23]:


#Prompt_D1 without lab
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": "\nImagine you are a Medical Professional tasked with providing one (1) comprehensive and accurate diagnosis for a patient presenting with the following case report. \nPlease consider the patient Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{Age: ["+str(row['Age'])+"]}{Sex: ["+row['Gender']+"]}{Symptoms: ["+row['Symptoms']+"]}{Case Report: ["+row['Case Report']+"]}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D1_withoutLab.json", "w") as f:

    json.dump(data, f, indent=4)


# In[24]:


#Prompt_D5
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": "\nImagine you are a Medical Professional tasked with providing five (5) comprehensive and accurate differential diagnosis for a patient presenting with the following case report. \nPlease consider the patient Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{Age: ["+str(row['Age'])+"]}{Sex: ["+row['Gender']+"]}{Symptoms: ["+row['Symptoms']+"]}{Case Report: ["+row['Case Report']+"]}{Lab tests: ["+row['Lab Tests']+"]}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D5.json", "w") as f:

    json.dump(data, f, indent=4)


# In[25]:


#Prompt_D5 without lab
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": "\nImagine you are a Medical Professional tasked with providing five (5) comprehensive and accurate differential diagnosis for a patient presenting with the following case report. \nPlease consider the patient Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{Age: ["+str(row['Age'])+"]}{Sex: ["+row['Gender']+"]}{Symptoms: ["+row['Symptoms']+"]}{Case Report: ["+row['Case Report']+"]}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D5_withoutLab.json", "w") as f:

    json.dump(data, f, indent=4)


# In[26]:


#Prompt_D10
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": "\nImagine you are a Medical Professional tasked with providing ten (10) comprehensive and accurate differential diagnosis for a patient presenting with the following case report. \nPlease consider the patient Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{Age: ["+str(row['Age'])+"]}{Sex: ["+row['Gender']+"]}{Symptoms: ["+row['Symptoms']+"]}{Case Report: ["+row['Case Report']+"]}{Lab tests: ["+row['Lab Tests']+"]}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D10.json", "w") as f:

    json.dump(data, f, indent=4)


# In[27]:


#Prompt1_D10 without lab
i=0
data = []
# Initial string
result_string = ""
for index, row in df.iterrows():
    i=i+1

    data.append({
        "ID": i,"prompt": "\nImagine you are a Medical Professional tasked with providing ten (10) comprehensive and accurate differential diagnosis for a patient presenting with the following case report. \nPlease consider the patient Age, Gender, Symptoms, Lab tests, and the full Case Report and any pertinent details to formulate your response.\n{Age: ["+str(row['Age'])+"]}{Sex: ["+row['Gender']+"]}{Symptoms: ["+row['Symptoms']+"]}{Case Report: ["+row['Case Report']+"]}"
    })

# now  type(data) is list, and you can directly dump it to a json
with open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D10_withoutLab.json", "w") as f:

    json.dump(data, f, indent=4)


# In[31]:


import os
import openai
#api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = 'your key'


# In[32]:


dataset = json.load(open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D1.json"))


# In[35]:


dataset[0]


# In[46]:


for entry in dataset:
    prompt = entry["prompt"] + "\n"
    messages = [{"role": "system", "content": prompt},{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(model="gpt-4",messages=messages,temperature=0)
    output = response.choices[0].message.content
    print("Case Report"+str( entry["ID"])+" ")
    print(output)


# In[47]:


dataset = json.load(open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D1_withoutLab.json"))
for entry in dataset:
    prompt = entry["prompt"] + "\n"
    messages = [{"role": "system", "content": prompt},{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(model="gpt-4",messages=messages,temperature=0)
    output = response.choices[0].message.content
    print("Case Report"+str( entry["ID"])+" ")
    print(output)


# In[48]:


dataset = json.load(open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D5.json"))
for entry in dataset:
    prompt = entry["prompt"] + "\n"
    messages = [{"role": "system", "content": prompt},{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(model="gpt-4",messages=messages,temperature=0)
    output = response.choices[0].message.content
    print("Case Report"+str( entry["ID"])+" ")
    print(output)


# In[49]:


dataset = json.load(open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D5_withoutLab.json"))
for entry in dataset:
    prompt = entry["prompt"] + "\n"
    messages = [{"role": "system", "content": prompt},{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(model="gpt-4",messages=messages,temperature=0)
    output = response.choices[0].message.content
    print("Case Report"+str( entry["ID"])+" ")
    print(output)


# In[50]:


dataset = json.load(open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D10.json"))
for entry in dataset:
    prompt = entry["prompt"] + "\n"
    messages = [{"role": "system", "content": prompt},{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(model="gpt-4",messages=messages,temperature=0)
    output = response.choices[0].message.content
    print("Case Report"+str( entry["ID"])+" ")
    print(output)


# In[51]:


dataset = json.load(open("C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\D10_withoutLab.json"))
for entry in dataset:
    prompt = entry["prompt"] + "\n"
    messages = [{"role": "system", "content": prompt},{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(model="gpt-4",messages=messages,temperature=0)
    output = response.choices[0].message.content
    print("Case Report"+str( entry["ID"])+" ")
    print(output)


# In[52]:


def extract_diagnoses(file_path):
    diagnoses = []
    with open(file_path, 'r') as file:
        current_case = []
        for line in file:
            if line.startswith('Case Report'):
                if current_case:  # Save the current case and start a new one
                    diagnoses.append(current_case)
                    current_case = []
            elif line.strip():
                # Extract the diagnosis name up to the first colon
                diagnosis = line.split(':')[0].strip().split('. ')[-1]
                current_case.append(diagnosis)
        if current_case:  # Add the last case
            diagnoses.append(current_case)
    return diagnoses

def main():
    file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\D5w.txt'  # Adjust the file path if necessary
    case_reports = extract_diagnoses(file_path)
    for report in case_reports:
        print(",".join(report))

main()


# In[53]:


def extract_diagnoses(file_path):
    diagnoses = []
    with open(file_path, 'r') as file:
        current_case = []
        for line in file:
            if line.startswith('Case Report'):
                if current_case:  # Save the current case and start a new one
                    diagnoses.append(current_case)
                    current_case = []
            elif line.strip():
                # Extract the diagnosis name up to the first colon
                diagnosis = line.split(':')[0].strip().split('. ')[-1]
                current_case.append(diagnosis)
        if current_case:  # Add the last case
            diagnoses.append(current_case)
    return diagnoses

def main():
    file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\D10.txt'  # Adjust the file path if necessary
    case_reports = extract_diagnoses(file_path)
    for report in case_reports:
        print(",".join(report))

main()


# In[54]:


def extract_diagnoses(file_path):
    diagnoses = []
    with open(file_path, 'r') as file:
        current_case = []
        for line in file:
            if line.startswith('Case Report'):
                if current_case:  # Save the current case and start a new one
                    diagnoses.append(current_case)
                    current_case = []
            elif line.strip():
                # Extract the diagnosis name up to the first colon
                diagnosis = line.split(':')[0].strip().split('. ')[-1]
                current_case.append(diagnosis)
        if current_case:  # Add the last case
            diagnoses.append(current_case)
    return diagnoses

def main():
    file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\D10w.txt'  # Adjust the file path if necessary
    case_reports = extract_diagnoses(file_path)
    for report in case_reports:
        print(",".join(report))

main()


# In[2]:


#Error Analysis
import pandas as pd

# Path to the Excel file
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results from 5 LLM_DDx.xlsx'

# Load the Excel file
excel_file = pd.ExcelFile(file_path)

# Print the sheet names
print("Sheet names:", excel_file.sheet_names)

# Read each sheet into a dictionary of DataFrames
sheets_dict = {sheet_name: excel_file.parse(sheet_name) for sheet_name in excel_file.sheet_names}




# In[3]:


# Read each sheet into a DataFrame and assign it to a variable named after the sheet
for sheet_name in excel_file.sheet_names:
    # Replace spaces with underscores in sheet names for valid variable names
    variable_name = sheet_name.replace('-', '_')
    globals()[variable_name] = pd.read_excel(file_path, sheet_name=sheet_name)


# In[4]:


GPT_4['LLM']='GPT-4'
GPT_35['LLM']='GPT-3.5'
Mixtral['LLM']='Mixtral'
Claude2['LLM']='Claude2'
Llama_2['LLM']='Llama2'


# In[5]:


LLM_Prediction = pd.concat([GPT_4, GPT_35, Mixtral,Claude2,Llama_2], ignore_index=True)


# In[6]:


# Column to move to the first position
column_to_move = 'LLM'

# Create new column order
new_column_order = [column_to_move] + [col for col in LLM_Prediction.columns if col != column_to_move]

# Reorder the DataFrame columns
LLM_Prediction = LLM_Prediction[new_column_order]
LLM_Prediction


# In[7]:


df = pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Case Report Mapping.xlsx')


# In[8]:


dfs=df.iloc[:, :6]
dfs


# In[9]:


df=pd.merge(dfs,LLM_Prediction,on='PMID', how='right')


# In[13]:


dfk=df[['PMID', 'Case Report','Age', 'Gender', 'Lab tests', 'Symptoms', 'LLM',
       'Final Diagnosis', 'D1', 'D1 w/o lab', 'D5', 'D5 w/o lab', 'D10','D10 w/o lab' ]]


# In[14]:


dfk.to_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\600_evaluations.xlsx')


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the new Excel file
new_file_path = '/mnt/data/Clinicain_300_Evaluations.xlsx'
new_excel_data = pd.ExcelFile(new_file_path)

# Load the data from the first sheet of the new file
new_data = pd.read_excel(new_file_path, sheet_name='Sheet1')

# Apply the conversion function to the new data
new_data['D1_Clinican Comment'] = new_data['D1_Clinican Comment'].fillna('')
new_data['D1 w/o_Clinican Comment'] = new_data['D1 w/o_Clinican Comment'].fillna('')
new_data['D5_Clinican Comment'] = new_data['D5_Clinican Comment'].fillna('')
new_data['D5 w/o_Clinican Comment'] = new_data['D5 w/o_Clinican Comment'].fillna('')
new_data['D10_Clinican Comment'] = new_data['D10_Clinican Comment'].fillna('')
new_data['D10 w/o_Clinican Comment'] = new_data['D10 w/o_Clinican Comment'].fillna('')

# Define the function to convert comments to numerical scores
def convert_to_numerical(comment):
    comment = comment.lower()
    if "exact match" in comment:
        return 1
    elif "relevant" in comment:
        return 0.5
    else:
        return 0

# Apply the conversion function to the relevant columns
new_data['D1_Clinican Comment Score'] = new_data['D1_Clinican Comment'].apply(convert_to_numerical)
new_data['D1 w/o_Clinican Comment Score'] = new_data['D1 w/o_Clinican Comment'].apply(convert_to_numerical)
new_data['D5_Clinican Comment Score'] = new_data['D5_Clinican Comment'].apply(convert_to_numerical)
new_data['D5 w/o_Clinican Comment Score'] = new_data['D5 w/o_Clinican Comment'].apply(convert_to_numerical)
new_data['D10_Clinican Comment Score'] = new_data['D10_Clinican Comment'].apply(convert_to_numerical)
new_data['D10 w/o_Clinican Comment Score'] = new_data['D10 w/o_Clinican Comment'].apply(convert_to_numerical)

# Define the categories
categories = [
    'D1_Clinican Comment Score',
    'D1 w/o_Clinican Comment Score',
    'D5_Clinican Comment Score',
    'D5 w/o_Clinican Comment Score',
    'D10_Clinican Comment Score',
    'D10 w/o_Clinican Comment Score'
]

# Calculate the mean scores for the new data
new_mean_scores = new_data.groupby('LLM').mean().reset_index()

# Function to highlight the best and second best models
def highlight_best(df, column):
    sorted_df = df.sort_values(by=column, ascending=False)
    best_model = sorted_df.iloc[0]['LLM']
    second_best_model = sorted_df.iloc[1]['LLM']
    return best_model, second_best_model

# Dictionary to hold the best and second best models for each category in the new data
new_best_models = {category: highlight_best(new_mean_scores, category) for category in categories}

# Plot the new scores and highlight the best and second best models
plt.figure(figsize=(14, 12))

for idx, category in enumerate(categories, 1):
    plt.subplot(3, 2, idx)
    sns.barplot(x='LLM', y=category, data=new_mean_scores, palette="viridis")
    plt.title(category.replace('_', ' '))
    plt.xticks(rotation=45)
    
    # Highlight the best and second best models
    best_model, second_best_model = new_best_models[category]
    plt.gca().patches[new_mean_scores[new_mean_scores['LLM'] == best_model].index[0]].set_edgecolor('gold')
    plt.gca().patches[new_mean_scores[new_mean_scores['LLM'] == second_best_model].index[0]].set_edgecolor('silver')

plt.tight_layout()
plt.show()

# Plot the performance of each model across all categories in the new dataset
models = new_mean_scores['LLM'].unique()

plt.figure(figsize=(14, 12))

for idx, model in enumerate(models, 1):
    model_data = new_mean_scores[new_mean_scores['LLM'] == model]
    
    plt.subplot(3, 2, idx)
    scores = model_data.iloc[0, 1:]  # Get scores for this model
    scores.plot(kind='bar', color='skyblue', edgecolor='black')
    
    plt.title(f'Performance of {model}')
    plt.ylim(0, 1.1)
    plt.ylabel('Score')
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Claude2

# In[4]:


#300 evaluation from GPT4
import json

# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Claude2_Prompt1\\Claude2_D1_P1.output.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# IDs for which to extract evaluations
ids = [1, 3, 5, 7, 8, 9, 10, 11, 12, 13]

# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]

# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[5]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Claude2_Prompt1\\Claude2_D1w_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[37]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Claude2_Prompt1\\Claude2_D5_P1.output.json'

# Open and read the file
with open(file_path, 'r') as file:
    content = file.read()

# Handling multiple JSON objects if concatenated directly into the file
try:
    # Try to parse the file as normal JSON
    data = json.loads(content)
except json.JSONDecodeError:
    # If fails, attempt to fix common JSON concatenation issues
    # This assumes that extra data errors are due to multiple JSON objects appended one after another without comma separation
    # Fixing by wrapping multiple JSON objects into an array
    corrected_content = "[" + content.replace('}\n{', '},{') + "]"
    data = json.loads(corrected_content)

evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]

# Print the evaluations as a comma-separated list
print('\n'.join(evaluations))


# In[7]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Claude2_Prompt1\\Claude2_D5w_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[8]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Claude2_Prompt1\\Claude2_D10_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[9]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Claude2_Prompt1\\Claude2_D10w_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# GPT3.5

# In[10]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D1_P1.output.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# IDs for which to extract evaluations
ids = [1, 3, 5, 7, 8, 9, 10, 11, 12, 13]

# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]

# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[12]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D1w_P1.output.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]

# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[13]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D5_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[14]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D5w_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[15]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D10_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[16]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D10w_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# GPT4

# In[17]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT4_Prompt1\\GPT4_D1_P1.output.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# IDs for which to extract evaluations
ids = [1, 3, 5, 7, 8, 9, 10, 11, 12, 13]

# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]

# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[18]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT4_Prompt1\\GPT4_D1w_P1.output.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]

# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[19]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT4_Prompt1\\GPT4_D5_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[20]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT4_Prompt1\\GPT4_D5w_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[21]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT4_Prompt1\\GPT4_D10_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[22]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT4_Prompt1\\GPT4_D10w_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# Llama2

# In[23]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Llama2_Prompt1\\Llama2_D1_P1.output.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# IDs for which to extract evaluations
ids = [1, 3, 5, 7, 8, 9, 10, 11, 12, 13]

# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]

# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[24]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Llama2_Prompt1\\Llama2_D1w_P1.output.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]

# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[25]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Llama2_Prompt1\\Llama2_D5_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[26]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Llama2_Prompt1\\Llama2_D5w_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[27]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Llama2_Prompt1\\Llama2_D10_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[28]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Llama2_Prompt1\\Llama2_D10w_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# Mixtral

# In[29]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Mixtral_Prompt1\\Mixtral_D1_P1.output.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# IDs for which to extract evaluations
ids = [1, 3, 5, 7, 8, 9, 10, 11, 12, 13]

# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]

# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[30]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Mixtral_Prompt1\\Mixtral_D1w_P1.output.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]

# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[31]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Mixtral_Prompt1\\Mixtral_D5_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[32]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Mixtral_Prompt1\\Mixtral_D5w_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[33]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Mixtral_Prompt1\\Mixtral_D10_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[34]:


# File path
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\Mixtral_Prompt1\\Mixtral_D10w_P1.output.json'
# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)
# Extract evaluations, parsing the string data for each ID
evaluations = [json.loads(data[str(id)])['evaluation'] for id in ids if str(id) in data]
# Print the evaluations without ID keys
print('\n'.join(evaluations))


# In[38]:


import pandas as pd

# Load the Excel file
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\Clinician Evaluation\\Clinicain_300_Evaluations[66].xlsx'
data = pd.read_excel(file_path)

# Filter and sort the necessary columns
columns_of_interest = [
    "LLM", 
    "D1_Clinican Comment", 
    "D1 w/o_Clinican Comment", 
    "D5_Clinican Comment", 
    "D5 w/o_Clinican Comment", 
    "D10_Clinican Comment", 
    "D10 w/o_Clinican Comment"
]
filtered_data = data[columns_of_interest]

# Group by 'LLM' and sort the data within each group
grouped_data = filtered_data.groupby('LLM').apply(lambda x: x.sort_values(by='LLM'))

# Display the grouped data for verification before further formatting
grouped_data.head(20)


# In[41]:


grouped_data.to_csv('D:\\mapped.csv')


# In[48]:


import pandas as pd


# In[49]:


# Load the Excel file
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\Clinician Evaluation\\Comparison.xlsx'  # Update this path as needed
data = pd.read_excel(file_path)

# Define the pairs of columns to compare
column_pairs = [
    ('GPT-4 Prediction_Claude', 'Clinician Comments_Claude'),
    ('GPT-4 Prediction_GPT3.5', 'Clinician Comments_GPT3.5'),
    ('GPT-4 Prediction_GPT4', 'Clinician Comments_GPT4'),
    ('GPT-4 Prediction_LLaMa2', 'Clinician Comments_LLaMa2'),
    ('GPT-4 Prediction_Mixtral', 'Clinician Comments_Mixtral')
]

# Create new columns for evaluation scores
for i, (col1, col2) in enumerate(column_pairs, start=1):
    data[f'Evaluation_{i}'] = (data[col1] == data[col2]).astype(int)

# Calculate the overall accuracy
overall_accuracy = data[[f'Evaluation_{i}' for i in range(1, 6)]].mean().mean()

# Output the first few rows of the modified DataFrame and the overall accuracy
data.head()



# In[50]:


print(f'Overall accuracy: {overall_accuracy:.2f}')


# In[51]:


# Correcting the potential issue with column names
# Ensure we are using the exact column names provided by data.columns

# Update column_pairs based on the exact names from the DataFrame
column_pairs = [
    ('GPT-4 Prediction_Claude', 'Clinician Comments_Claude'),
    ('GPT-4 Prediction_GPT3.5', 'Clinician Comments_GPT3.5'),
    ('GPT-4 Prediction_GPT4', 'Clinician Comments_GPT4'),
    ('GPT-4 Prediction_LLaMa2', 'Clinician Comments_LLaMa2'),
    ('GPT-4 Prediction_Mixtral', 'Clinician Comments_Mixtral')
]

# Recalculate the statistics using the corrected column names
stats_corrected = {}

for i, (pred_col, comm_col) in enumerate(column_pairs, start=1):
    matches = data[pred_col] == data[comm_col]
    total_rows = len(data)
    match_count = matches.sum()
    mismatch_count = total_rows - match_count
    match_percentage = (match_count / total_rows) * 100
    mismatch_percentage = (mismatch_count / total_rows) * 100
    
    # Store the corrected statistics
    stats_corrected[f'Pair {i} ({pred_col} vs {comm_col})'] = {
        'Match Count': match_count,
        'Mismatch Count': mismatch_count,
        'Match Percentage': match_percentage,
        'Mismatch Percentage': mismatch_percentage
    }

# Convert the corrected statistics to a DataFrame for better visualization
stats_df_corrected = pd.DataFrame.from_dict(stats_corrected, orient='index')
stats_df_corrected


# In[52]:


# Load the Excel file
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\Clinician Evaluation\\Comparison.xlsx'  # Update this path as needed
data = pd.read_excel(file_path)

# Define the pairs of columns to compare
column_pairs = [
    ('GPT-4 Prediction_Claude', 'KG Evaluation_Claude'),
    ('GPT-4 Prediction_GPT3.5', 'KG Evaluation_GPT3.5'),
    ('GPT-4 Prediction_GPT4', 'KG Evaluation_GPT4'),
    ('GPT-4 Prediction_LLaMa2', 'KG Evaluation_LLaMa2'),
    ('GPT-4 Prediction_Mixtral', 'KG Evaluation_Mixtral')
]

# Create new columns for evaluation scores
for i, (col1, col2) in enumerate(column_pairs, start=1):
    data[f'Evaluation_{i}'] = (data[col1] == data[col2]).astype(int)

# Calculate the overall accuracy
overall_accuracy = data[[f'Evaluation_{i}' for i in range(1, 6)]].mean().mean()

# Output the first few rows of the modified DataFrame and the overall accuracy
data.head()


# In[53]:


print(f'Overall accuracy: {overall_accuracy:.2f}')


# In[54]:


# Correcting the potential issue with column names
# Ensure we are using the exact column names provided by data.columns

# Update column_pairs based on the exact names from the DataFrame
column_pairs = [
    ('GPT-4 Prediction_Claude', 'KG Evaluation_Claude'),
    ('GPT-4 Prediction_GPT3.5', 'KG Evaluation_GPT3.5'),
    ('GPT-4 Prediction_GPT4', 'KG Evaluation_GPT4'),
    ('GPT-4 Prediction_LLaMa2', 'KG Evaluation_LLaMa2'),
    ('GPT-4 Prediction_Mixtral', 'KG Evaluation_Mixtral')
]

# Recalculate the statistics using the corrected column names
stats_corrected = {}

for i, (pred_col, comm_col) in enumerate(column_pairs, start=1):
    matches = data[pred_col] == data[comm_col]
    total_rows = len(data)
    match_count = matches.sum()
    mismatch_count = total_rows - match_count
    match_percentage = (match_count / total_rows) * 100
    mismatch_percentage = (mismatch_count / total_rows) * 100
    
    # Store the corrected statistics
    stats_corrected[f'Pair {i} ({pred_col} vs {comm_col})'] = {
        'Match Count': match_count,
        'Mismatch Count': mismatch_count,
        'Match Percentage': match_percentage,
        'Mismatch Percentage': mismatch_percentage
    }

# Convert the corrected statistics to a DataFrame for better visualization
stats_df_corrected = pd.DataFrame.from_dict(stats_corrected, orient='index')
stats_df_corrected


# In[55]:


# Load the Excel file
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\Clinician Evaluation\\Comparison.xlsx'  # Update this path as needed
data = pd.read_excel(file_path)

# Define the pairs of columns to compare
column_pairs = [
    ('Clinician Comments_Claude', 'KG Evaluation_Claude'),
    ('Clinician Comments_GPT3.5', 'KG Evaluation_GPT3.5'),
    ('Clinician Comments_GPT4', 'KG Evaluation_GPT4'),
    ('Clinician Comments_LLaMa2', 'KG Evaluation_LLaMa2'),
    ('Clinician Comments_Mixtral', 'KG Evaluation_Mixtral')
]

# Create new columns for evaluation scores
for i, (col1, col2) in enumerate(column_pairs, start=1):
    data[f'Evaluation_{i}'] = (data[col1] == data[col2]).astype(int)

# Calculate the overall accuracy
overall_accuracy = data[[f'Evaluation_{i}' for i in range(1, 6)]].mean().mean()

# Output the first few rows of the modified DataFrame and the overall accuracy
data.head()


# In[56]:


print(f'Overall accuracy: {overall_accuracy:.2f}')


# In[57]:


# Correcting the potential issue with column names
# Ensure we are using the exact column names provided by data.columns

# Update column_pairs based on the exact names from the DataFrame
column_pairs = [
    ('Clinician Comments_Claude', 'KG Evaluation_Claude'),
    ('Clinician Comments_GPT3.5', 'KG Evaluation_GPT3.5'),
    ('Clinician Comments_GPT4', 'KG Evaluation_GPT4'),
    ('Clinician Comments_LLaMa2', 'KG Evaluation_LLaMa2'),
    ('Clinician Comments_Mixtral', 'KG Evaluation_Mixtral')
]

# Recalculate the statistics using the corrected column names
stats_corrected = {}

for i, (pred_col, comm_col) in enumerate(column_pairs, start=1):
    matches = data[pred_col] == data[comm_col]
    total_rows = len(data)
    match_count = matches.sum()
    mismatch_count = total_rows - match_count
    match_percentage = (match_count / total_rows) * 100
    mismatch_percentage = (mismatch_count / total_rows) * 100
    
    # Store the corrected statistics
    stats_corrected[f'Pair {i} ({pred_col} vs {comm_col})'] = {
        'Match Count': match_count,
        'Mismatch Count': mismatch_count,
        'Match Percentage': match_percentage,
        'Mismatch Percentage': mismatch_percentage
    }

# Convert the corrected statistics to a DataFrame for better visualization
stats_df_corrected = pd.DataFrame.from_dict(stats_corrected, orient='index')
stats_df_corrected


# In[83]:


#Combine the results from GPT-4 and KG by taking the average
# Load the Excel file
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\Clinician Evaluation\\Comparison_clinician_GPT4_KG.xlsx'  # Update this path as needed
df= pd.read_excel(file_path)
# Identify columns with values 'Relevant', 'Exact Match', and 'Incorrect'
df_replaced=df
columns_to_convert = df_replaced.columns[df_replaced.isin(['Relevant', 'Exact Match', 'Incorrect']).any()]

# Create a mapping to convert the string values to floats
mapping = {'Relevant': 0.5, 'Exact Match': 1.0, 'Incorrect': 0.0}

# Strip whitespace from all string values in the dataframe
df_replaced = df_replaced.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Apply the mapping and convert the data type to float
df_replaced[columns_to_convert] = df_replaced[columns_to_convert].applymap(lambda x: mapping.get(x, x)).astype(float)

# Output the data types of the modified dataframe
df_replaced.dtypes


# In[84]:


# Define the column pairs
column_pairs = [
    ('GPT-4 Prediction_Claude', 'KG Evaluation_Claude'),
    ('GPT-4 Prediction_GPT3.5', 'KG Evaluation_GPT3.5'),
    ('GPT-4 Prediction_GPT4', 'KG Evaluation_GPT4'),
    ('GPT-4 Prediction_LLaMa2', 'KG Evaluation_LLaMa2'),
    ('GPT-4 Prediction_Mixtral', 'KG Evaluation_Mixtral')
]

# Calculate the average of the column pairs and add them as new columns
for col1, col2 in column_pairs:
    new_col_name = f'Average_{col1}_{col2}'
    df_replaced[new_col_name] = df_replaced[[col1, col2]].mean(axis=1)


# Output the data types of the modified dataframe
df_replaced.head(5)



# In[85]:


new_df=df_replaced


# In[86]:


new_df['Average_GPT-4 Prediction_Claude_KG Evaluation_Claude'].value_counts()


# In[87]:


new_df['Average_GPT-4 Prediction_GPT3.5_KG Evaluation_GPT3.5'].value_counts()


# In[88]:


new_df['Average_GPT-4 Prediction_GPT4_KG Evaluation_GPT4'].value_counts()


# In[89]:


new_df['Average_GPT-4 Prediction_LLaMa2_KG Evaluation_LLaMa2'].value_counts()


# In[90]:


new_df['Average_GPT-4 Prediction_Mixtral_KG Evaluation_Mixtral'].value_counts()


# In[92]:


new_df = new_df.replace(1.0, 'Exact Match')
new_df = new_df.replace(0.75, 'Exact Match')
new_df = new_df.replace(0.50, 'Relevant')
new_df = new_df.replace(0.25, 'Relevant')
new_df = new_df.replace(0.0, 'Incorrect')
new_df


# In[93]:


data=new_df
# Define the pairs of columns to compare
column_pairs = [
    ('Clinician Comments_Claude', 'Average_GPT-4 Prediction_Claude_KG Evaluation_Claude'),
    ('Clinician Comments_GPT3.5', 'Average_GPT-4 Prediction_GPT3.5_KG Evaluation_GPT3.5'),
    ('Clinician Comments_GPT4', 'Average_GPT-4 Prediction_GPT4_KG Evaluation_GPT4'),
    ('Clinician Comments_LLaMa2', 'Average_GPT-4 Prediction_LLaMa2_KG Evaluation_LLaMa2'),
    ('Clinician Comments_Mixtral', 'Average_GPT-4 Prediction_Mixtral_KG Evaluation_Mixtral')
]

# Create new columns for evaluation scores
for i, (col1, col2) in enumerate(column_pairs, start=1):
    data[f'Evaluation_{i}'] = (data[col1] == data[col2]).astype(int)

# Calculate the overall accuracy
overall_accuracy = data[[f'Evaluation_{i}' for i in range(1, 6)]].mean().mean()

# Output the first few rows of the modified DataFrame and the overall accuracy
data.head()


# In[94]:


print(f'Overall accuracy: {overall_accuracy:.2f}')


# In[95]:


# Correcting the potential issue with column names
# Ensure we are using the exact column names provided by data.columns

# Update column_pairs based on the exact names from the DataFrame
column_pairs = [
    ('Clinician Comments_Claude', 'Average_GPT-4 Prediction_Claude_KG Evaluation_Claude'),
    ('Clinician Comments_GPT3.5', 'Average_GPT-4 Prediction_GPT3.5_KG Evaluation_GPT3.5'),
    ('Clinician Comments_GPT4', 'Average_GPT-4 Prediction_GPT4_KG Evaluation_GPT4'),
    ('Clinician Comments_LLaMa2', 'Average_GPT-4 Prediction_LLaMa2_KG Evaluation_LLaMa2'),
    ('Clinician Comments_Mixtral', 'Average_GPT-4 Prediction_Mixtral_KG Evaluation_Mixtral')
]

# Recalculate the statistics using the corrected column names
stats_corrected = {}

for i, (pred_col, comm_col) in enumerate(column_pairs, start=1):
    matches = data[pred_col] == data[comm_col]
    total_rows = len(data)
    match_count = matches.sum()
    mismatch_count = total_rows - match_count
    match_percentage = (match_count / total_rows) * 100
    mismatch_percentage = (mismatch_count / total_rows) * 100
    
    # Store the corrected statistics
    stats_corrected[f'Pair {i} ({pred_col} vs {comm_col})'] = {
        'Match Count': match_count,
        'Mismatch Count': mismatch_count,
        'Match Percentage': match_percentage,
        'Mismatch Percentage': mismatch_percentage
    }

# Convert the corrected statistics to a DataFrame for better visualization
stats_df_corrected = pd.DataFrame.from_dict(stats_corrected, orient='index')
stats_df_corrected


# In[65]:


# Counting the occurrences of 'Relevant' and 'Incorrect' in the dataframe
df=data
# Create a dictionary to hold the counts for each column
results = {}

# Iterate through the columns and count the values
for column in df.columns:
    if df[column].dtype == 'object':  # Only consider string columns
        exact_count = df[column].str.count('Exact Match').sum()
        relevant_count = df[column].str.count('Relevant').sum()
        incorrect_count = df[column].str.count('Incorrect').sum()
        results[column] = {'Exact Match':exact_count,'Relevant': relevant_count, 'Incorrect': incorrect_count}

results_df = pd.DataFrame(results).transpose()
filtered_df = results_df[(results_df['Relevant'] != 0) | (results_df['Incorrect'] != 0)]
filtered_df


# In[66]:


df = df.replace('Exact Match', 'Relevant')
# Create a dictionary to hold the counts for each column
results = {}

# Iterate through the columns and count the values
for column in df.columns:
    if df[column].dtype == 'object':  # Only consider string columns
        exact_count = df[column].str.count('Exact Match').sum()
        relevant_count = df[column].str.count('Relevant').sum()
        incorrect_count = df[column].str.count('Incorrect').sum()
        results[column] = {'Exact Match':exact_count,'Relevant': relevant_count, 'Incorrect': incorrect_count}

results_df = pd.DataFrame(results).transpose()
filtered_df = results_df[(results_df['Relevant'] != 0) | (results_df['Incorrect'] != 0)]
filtered_df


# In[67]:


data=df
# Define the pairs of columns to compare
column_pairs = [
    ('GPT-4 Prediction_Claude', 'Clinician Comments_Claude'),
    ('GPT-4 Prediction_GPT3.5', 'Clinician Comments_GPT3.5'),
    ('GPT-4 Prediction_GPT4', 'Clinician Comments_GPT4'),
    ('GPT-4 Prediction_LLaMa2', 'Clinician Comments_LLaMa2'),
    ('GPT-4 Prediction_Mixtral', 'Clinician Comments_Mixtral')
]

# Create new columns for evaluation scores
for i, (col1, col2) in enumerate(column_pairs, start=1):
    data[f'Evaluation_{i}'] = (data[col1] == data[col2]).astype(int)

# Calculate the overall accuracy
overall_accuracy = data[[f'Evaluation_{i}' for i in range(1, 6)]].mean().mean()

# Output the first few rows of the modified DataFrame and the overall accuracy
data.head()


# In[68]:


print(f'Overall accuracy: {overall_accuracy:.2f}')


# In[69]:


# Correcting the potential issue with column names
# Ensure we are using the exact column names provided by data.columns

# Update column_pairs based on the exact names from the DataFrame
column_pairs = [
    ('GPT-4 Prediction_Claude', 'Clinician Comments_Claude'),
    ('GPT-4 Prediction_GPT3.5', 'Clinician Comments_GPT3.5'),
    ('GPT-4 Prediction_GPT4', 'Clinician Comments_GPT4'),
    ('GPT-4 Prediction_LLaMa2', 'Clinician Comments_LLaMa2'),
    ('GPT-4 Prediction_Mixtral', 'Clinician Comments_Mixtral')
]

# Recalculate the statistics using the corrected column names
stats_corrected = {}

for i, (pred_col, comm_col) in enumerate(column_pairs, start=1):
    matches = data[pred_col] == data[comm_col]
    total_rows = len(data)
    match_count = matches.sum()
    mismatch_count = total_rows - match_count
    match_percentage = (match_count / total_rows) * 100
    mismatch_percentage = (mismatch_count / total_rows) * 100
    
    # Store the corrected statistics
    stats_corrected[f'Pair {i} ({pred_col} vs {comm_col})'] = {
        'Match Count': match_count,
        'Mismatch Count': mismatch_count,
        'Match Percentage': match_percentage,
        'Mismatch Percentage': mismatch_percentage
    }

# Convert the corrected statistics to a DataFrame for better visualization
stats_df_corrected = pd.DataFrame.from_dict(stats_corrected, orient='index')
stats_df_corrected


# In[70]:


data=df
# Define the pairs of columns to compare
column_pairs = [
    ('GPT-4 Prediction_Claude', 'KG Evaluation_Claude'),
    ('GPT-4 Prediction_GPT3.5', 'KG Evaluation_GPT3.5'),
    ('GPT-4 Prediction_GPT4', 'KG Evaluation_GPT4'),
    ('GPT-4 Prediction_LLaMa2', 'KG Evaluation_LLaMa2'),
    ('GPT-4 Prediction_Mixtral', 'KG Evaluation_Mixtral')
]

# Create new columns for evaluation scores
for i, (col1, col2) in enumerate(column_pairs, start=1):
    data[f'Evaluation_{i}'] = (data[col1] == data[col2]).astype(int)

# Calculate the overall accuracy
overall_accuracy = data[[f'Evaluation_{i}' for i in range(1, 6)]].mean().mean()

# Output the first few rows of the modified DataFrame and the overall accuracy
data.head()


# In[71]:


print(f'Overall accuracy: {overall_accuracy:.2f}')


# In[72]:


# Correcting the potential issue with column names
# Ensure we are using the exact column names provided by data.columns

# Update column_pairs based on the exact names from the DataFrame
column_pairs = [
    ('GPT-4 Prediction_Claude', 'KG Evaluation_Claude'),
    ('GPT-4 Prediction_GPT3.5', 'KG Evaluation_GPT3.5'),
    ('GPT-4 Prediction_GPT4', 'KG Evaluation_GPT4'),
    ('GPT-4 Prediction_LLaMa2', 'KG Evaluation_LLaMa2'),
    ('GPT-4 Prediction_Mixtral', 'KG Evaluation_Mixtral')
]

# Recalculate the statistics using the corrected column names
stats_corrected = {}

for i, (pred_col, comm_col) in enumerate(column_pairs, start=1):
    matches = data[pred_col] == data[comm_col]
    total_rows = len(data)
    match_count = matches.sum()
    mismatch_count = total_rows - match_count
    match_percentage = (match_count / total_rows) * 100
    mismatch_percentage = (mismatch_count / total_rows) * 100
    
    # Store the corrected statistics
    stats_corrected[f'Pair {i} ({pred_col} vs {comm_col})'] = {
        'Match Count': match_count,
        'Mismatch Count': mismatch_count,
        'Match Percentage': match_percentage,
        'Mismatch Percentage': mismatch_percentage
    }

# Convert the corrected statistics to a DataFrame for better visualization
stats_df_corrected = pd.DataFrame.from_dict(stats_corrected, orient='index')
stats_df_corrected


# In[73]:


# Define the pairs of columns to compare
column_pairs = [
    ('Clinician Comments_Claude', 'KG Evaluation_Claude'),
    ('Clinician Comments_GPT3.5', 'KG Evaluation_GPT3.5'),
    ('Clinician Comments_GPT4', 'KG Evaluation_GPT4'),
    ('Clinician Comments_LLaMa2', 'KG Evaluation_LLaMa2'),
    ('Clinician Comments_Mixtral', 'KG Evaluation_Mixtral')
]

# Create new columns for evaluation scores
for i, (col1, col2) in enumerate(column_pairs, start=1):
    data[f'Evaluation_{i}'] = (data[col1] == data[col2]).astype(int)

# Calculate the overall accuracy
overall_accuracy = data[[f'Evaluation_{i}' for i in range(1, 6)]].mean().mean()

# Output the first few rows of the modified DataFrame and the overall accuracy
data.head()


# In[74]:


print(f'Overall accuracy: {overall_accuracy:.2f}')


# In[75]:


# Correcting the potential issue with column names
# Ensure we are using the exact column names provided by data.columns

# Update column_pairs based on the exact names from the DataFrame
column_pairs = [
    ('Clinician Comments_Claude', 'KG Evaluation_Claude'),
    ('Clinician Comments_GPT3.5', 'KG Evaluation_GPT3.5'),
    ('Clinician Comments_GPT4', 'KG Evaluation_GPT4'),
    ('Clinician Comments_LLaMa2', 'KG Evaluation_LLaMa2'),
    ('Clinician Comments_Mixtral', 'KG Evaluation_Mixtral')
]

# Recalculate the statistics using the corrected column names
stats_corrected = {}

for i, (pred_col, comm_col) in enumerate(column_pairs, start=1):
    matches = data[pred_col] == data[comm_col]
    total_rows = len(data)
    match_count = matches.sum()
    mismatch_count = total_rows - match_count
    match_percentage = (match_count / total_rows) * 100
    mismatch_percentage = (mismatch_count / total_rows) * 100
    
    # Store the corrected statistics
    stats_corrected[f'Pair {i} ({pred_col} vs {comm_col})'] = {
        'Match Count': match_count,
        'Mismatch Count': mismatch_count,
        'Match Percentage': match_percentage,
        'Mismatch Percentage': mismatch_percentage
    }

# Convert the corrected statistics to a DataFrame for better visualization
stats_df_corrected = pd.DataFrame.from_dict(stats_corrected, orient='index')
stats_df_corrected


# In[96]:


#Combine the results from GPT-4 and KG by taking the average
#Combine the results from GPT-4 and KG by taking the average
# Load the Excel file
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\Clinician Evaluation\\Comparison_clinician_GPT4_KG.xlsx'  # Update this path as needed
df= pd.read_excel(file_path)
# Identify columns with values 'Relevant', 'Exact Match', and 'Incorrect'
df_replaced=df
columns_to_convert = df_replaced.columns[df_replaced.isin(['Relevant', 'Exact Match', 'Incorrect']).any()]

# Create a mapping to convert the string values to floats
mapping = {'Relevant': 1.0, 'Exact Match': 1.0, 'Incorrect': 0.0}

# Strip whitespace from all string values in the dataframe
df_replaced = df_replaced.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Apply the mapping and convert the data type to float
df_replaced[columns_to_convert] = df_replaced[columns_to_convert].applymap(lambda x: mapping.get(x, x)).astype(float)

# Define the column pairs
column_pairs = [
    ('GPT-4 Prediction_Claude', 'KG Evaluation_Claude'),
    ('GPT-4 Prediction_GPT3.5', 'KG Evaluation_GPT3.5'),
    ('GPT-4 Prediction_GPT4', 'KG Evaluation_GPT4'),
    ('GPT-4 Prediction_LLaMa2', 'KG Evaluation_LLaMa2'),
    ('GPT-4 Prediction_Mixtral', 'KG Evaluation_Mixtral')
]

# Calculate the average of the column pairs and add them as new columns
for col1, col2 in column_pairs:
    new_col_name = f'Average_{col1}_{col2}'
    df_replaced[new_col_name] = df_replaced[[col1, col2]].mean(axis=1)


df_replaced = df_replaced.replace(1.0, 'Relevant')
df_replaced = df_replaced.replace(0.75, 'Relevant')
df_replaced = df_replaced.replace(0.50, 'Relevant')
df_replaced = df_replaced.replace(0.25, 'Relevant')
df_replaced = df_replaced.replace(0.0, 'Incorrect')

df=df_replaced
df = df.replace('Exact Match', 'Relevant')
data=df
# Define the pairs of columns to compare
column_pairs = [
    ('Clinician Comments_Claude', 'Average_GPT-4 Prediction_Claude_KG Evaluation_Claude'),
    ('Clinician Comments_GPT3.5', 'Average_GPT-4 Prediction_GPT3.5_KG Evaluation_GPT3.5'),
    ('Clinician Comments_GPT4', 'Average_GPT-4 Prediction_GPT4_KG Evaluation_GPT4'),
    ('Clinician Comments_LLaMa2', 'Average_GPT-4 Prediction_LLaMa2_KG Evaluation_LLaMa2'),
    ('Clinician Comments_Mixtral', 'Average_GPT-4 Prediction_Mixtral_KG Evaluation_Mixtral')
]

# Create new columns for evaluation scores
for i, (col1, col2) in enumerate(column_pairs, start=1):
    data[f'Evaluation_{i}'] = (data[col1] == data[col2]).astype(int)

# Calculate the overall accuracy
overall_accuracy = data[[f'Evaluation_{i}' for i in range(1, 6)]].mean().mean()


# In[97]:


print(f'Overall accuracy: {overall_accuracy:.2f}')


# In[98]:


# Correcting the potential issue with column names
# Ensure we are using the exact column names provided by data.columns

# Update column_pairs based on the exact names from the DataFrame
column_pairs = [
    ('Clinician Comments_Claude', 'Average_GPT-4 Prediction_Claude_KG Evaluation_Claude'),
    ('Clinician Comments_GPT3.5', 'Average_GPT-4 Prediction_GPT3.5_KG Evaluation_GPT3.5'),
    ('Clinician Comments_GPT4', 'Average_GPT-4 Prediction_GPT4_KG Evaluation_GPT4'),
    ('Clinician Comments_LLaMa2', 'Average_GPT-4 Prediction_LLaMa2_KG Evaluation_LLaMa2'),
    ('Clinician Comments_Mixtral', 'Average_GPT-4 Prediction_Mixtral_KG Evaluation_Mixtral')
]

# Recalculate the statistics using the corrected column names
stats_corrected = {}

for i, (pred_col, comm_col) in enumerate(column_pairs, start=1):
    matches = data[pred_col] == data[comm_col]
    total_rows = len(data)
    match_count = matches.sum()
    mismatch_count = total_rows - match_count
    match_percentage = (match_count / total_rows) * 100
    mismatch_percentage = (mismatch_count / total_rows) * 100
    
    # Store the corrected statistics
    stats_corrected[f'Pair {i} ({pred_col} vs {comm_col})'] = {
        'Match Count': match_count,
        'Mismatch Count': mismatch_count,
        'Match Percentage': match_percentage,
        'Mismatch Percentage': mismatch_percentage
    }

# Convert the corrected statistics to a DataFrame for better visualization
stats_df_corrected = pd.DataFrame.from_dict(stats_corrected, orient='index')
stats_df_corrected


# In[99]:


# Load the Excel file
file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\Clinician Evaluation\\Comparison_clinician_GPT4_KG.xlsx'  # Update this path as needed
df= pd.read_excel(file_path)
# Identify columns with values 'Relevant', 'Exact Match', and 'Incorrect'
df_replaced=df
columns_to_convert = df_replaced.columns[df_replaced.isin(['Relevant', 'Exact Match', 'Incorrect']).any()]

# Create a mapping to convert the string values to floats
mapping = {'Relevant': 0.5, 'Exact Match': 1.0, 'Incorrect': 0.0}

# Strip whitespace from all string values in the dataframe
df_replaced = df_replaced.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Apply the mapping and convert the data type to float
df_replaced[columns_to_convert] = df_replaced[columns_to_convert].applymap(lambda x: mapping.get(x, x)).astype(float)
df_replaced


# In[101]:


df_replaced.to_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\Clinician Evaluation\\Comparison_clinician_GPT4_KG_plot.xlsx')


# In[111]:


new_data=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\Clinician Evaluation\\Comparison_clinician_GPT4_KG_plot.xlsx')


# In[112]:


new_data


# In[117]:


# Filter only the numeric columns for the aggregation
numeric_cols = ['GPT-4 Prediction', 'Clinician Prediction', 'Knowledge Graph Prediction']
llm_groups_new = new_data.groupby('LLM')[numeric_cols].mean()

# Create a bar plot comparing prediction scores for each LLM using updated data
plt.figure(figsize=(12, 6))
llm_groups_new.plot(kind='bar', figsize=(12, 6))

plt.title('Average Prediction Scores for Each LLM (Updated Data)')
plt.xlabel('LLM')
plt.ylabel('Average Prediction Score')
plt.xticks(rotation=45)
plt.legend(title='Prediction Source')
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()


# In[119]:


# Define a few color themes for the bar plot
color_themes = {
    "Theme 1": ['#4c72b0', '#55a868', '#c44e52'],
    "Theme 2": ['#8172b2', '#ccb974', '#64b5cd'],
    "Theme 3": ['#e24a33', '#348abd', '#988ed5'],
}

# Create bar plots for each color theme
for theme_name, colors in color_themes.items():
    plt.figure(figsize=(12, 6))
    llm_groups_new.plot(kind='bar', figsize=(12, 6), color=colors)
    
    plt.title(f'Average Prediction Scores for Each LLM ')
    plt.xlabel('LLM')
    plt.ylabel('Average Prediction Score')
    plt.xticks(rotation=45)
    plt.legend(title='Prediction Source')
    plt.grid(True)
    
    # Show the plot
    plt.tight_layout()
    plt.show()


# In[124]:


# Filter the data from the relevant sheet (Sheet1) as per the provided diagnoses
diagnoses_new = ['DDx 1', 'DDx 1 without Lab', 'DDx 5', 'DDx 5 without Lab', 'DDx 10', 'DDx 10 without Lab']
filtered_data_new = sheet1_data[sheet1_data['DDx'].isin(diagnoses_new)]

import matplotlib.pyplot as plt
import seaborn as sns

# Plot similar figures for each diagnosis using updated data
fig, axes = plt.subplots(3, 2, figsize=(14, 12), sharey=True)
fig.suptitle('Clinician Scores by Differential Diagnosis with and without Lab from 5 LLMs')

# Flatten the axes for easier iteration
axes = axes.flatten()

for idx, diagnosis in enumerate(diagnoses_new):
    subset = filtered_data_new[filtered_data_new['DDx'] == diagnosis]
    sns.barplot(ax=axes[idx], data=subset, x='LLM', y='Clinician Prediction', palette='viridis')
    axes[idx].set_title(f'{diagnosis} Clinician Score')
    axes[idx].set_xlabel('LLM')
    axes[idx].set_ylabel(f'{diagnosis} Clinician Score')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# In[125]:


# Define the diagnoses to plot using updated data
diagnoses_new = ['DDx 1', 'DDx 1 without Lab', 'DDx 5', 'DDx 5 without Lab', 'DDx 10', 'DDx 10 without Lab']

# Filter the data for the specific diagnoses using updated data
filtered_data_new = new_data[new_data['DDx'].isin(diagnoses_new)]

# Plot similar figures for each diagnosis using updated data
fig, axes = plt.subplots(3, 2, figsize=(14, 12), sharey=True)
fig.suptitle('GPT-4 Scores by Differentail Diagnosis with and without Lab from 5 LLMs')

# Flatten the axes for easier iteration
axes = axes.flatten()

for idx, diagnosis in enumerate(diagnoses_new):
    subset = filtered_data_new[filtered_data_new['DDx'] == diagnosis]
    sns.barplot(ax=axes[idx], data=subset, x='LLM', y='GPT-4 Prediction', palette='viridis')
    axes[idx].set_title(f'{diagnosis} GPT-4 Score')
    axes[idx].set_xlabel('LLM')
    axes[idx].set_ylabel(f'{diagnosis} GPT-4 Score')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# In[126]:


# Define the diagnoses to plot using updated data
diagnoses_new = ['DDx 1', 'DDx 1 without Lab', 'DDx 5', 'DDx 5 without Lab', 'DDx 10', 'DDx 10 without Lab']

# Filter the data for the specific diagnoses using updated data
filtered_data_new = new_data[new_data['DDx'].isin(diagnoses_new)]

# Plot similar figures for each diagnosis using updated data
fig, axes = plt.subplots(3, 2, figsize=(14, 12), sharey=True)
fig.suptitle('Knowledge Graph Scores by Differentail Diagnosis with and without Lab from 5 LLMs')

# Flatten the axes for easier iteration
axes = axes.flatten()

for idx, diagnosis in enumerate(diagnoses_new):
    subset = filtered_data_new[filtered_data_new['DDx'] == diagnosis]
    sns.barplot(ax=axes[idx], data=subset, x='LLM', y='Knowledge Graph Prediction', palette='viridis')
    axes[idx].set_title(f'{diagnosis} Knowledge Graph Score')
    axes[idx].set_xlabel('LLM')
    axes[idx].set_ylabel(f'{diagnosis} Knowledge Graph Score')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# In[130]:


# Plot similar figures for each diagnosis using updated data without error bars
filtered_data = new_data[new_data['DDx'].isin(diagnoses_new)]
fig, axes = plt.subplots(3, 2, figsize=(14, 12), sharey=True)
fig.suptitle('Clinician Scores by Differential Diagnosis with and without Lab from 5 LLMs (Updated)')

# Flatten the axes for easier iteration
axes = axes.flatten()

for idx, diagnosis in enumerate(diagnoses_new):
    subset = filtered_data[filtered_data['DDx'] == diagnosis]
    sns.barplot(ax=axes[idx], data=subset, x='LLM', y='Clinician Prediction', palette='viridis', errorbar=None)
    axes[idx].axhline(0.5, ls='--', color='red')  # Adding a horizontal line at y=0.5 for reference
    axes[idx].set_title(f'{diagnosis} Clinician Score')
    axes[idx].set_xlabel('LLM')
    axes[idx].set_ylabel(f'{diagnosis} Clinician Score')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# In[131]:


# Plot similar figures for each diagnosis using updated data without error bars
filtered_data = new_data[new_data['DDx'].isin(diagnoses_new)]
fig, axes = plt.subplots(3, 2, figsize=(14, 12), sharey=True)
fig.suptitle('Clinician Scores by Differential Diagnosis with and without Lab from 5 LLMs')

# Flatten the axes for easier iteration
axes = axes.flatten()

for idx, diagnosis in enumerate(diagnoses_new):
    subset = filtered_data[filtered_data['DDx'] == diagnosis]
    sns.barplot(ax=axes[idx], data=subset, x='LLM', y='GPT-4 Prediction', palette='viridis', errorbar=None)
    axes[idx].axhline(0.5, ls='--', color='red')  # Adding a horizontal line at y=0.5 for reference
    axes[idx].set_title(f'{diagnosis} GPT-4 Score')
    axes[idx].set_xlabel('LLM')
    axes[idx].set_ylabel(f'{diagnosis} GPT-4 Score')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# In[132]:


# Plot similar figures for each diagnosis using updated data without error bars
filtered_data = new_data[new_data['DDx'].isin(diagnoses_new)]
fig, axes = plt.subplots(3, 2, figsize=(14, 12), sharey=True)
fig.suptitle('Clinician Scores by Differential Diagnosis with and without Lab from 5 LLMs')

# Flatten the axes for easier iteration
axes = axes.flatten()

for idx, diagnosis in enumerate(diagnoses_new):
    subset = filtered_data[filtered_data['DDx'] == diagnosis]
    sns.barplot(ax=axes[idx], data=subset, x='LLM', y='Knowledge Graph Prediction', palette='viridis', errorbar=None)
    axes[idx].axhline(0.5, ls='--', color='red')  # Adding a horizontal line at y=0.5 for reference
    axes[idx].set_title(f'{diagnosis} Knowledge Graph Score')
    axes[idx].set_xlabel('LLM')
    axes[idx].set_ylabel(f'{diagnosis} Knowledge Graph Score')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# In[2]:


#Generating full reports for KG evaluation
import pandas as pd
import re
dfl=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\LLama2.xlsx')
dfc=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\Claude.xlsx')
dfm=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\Mixtral.xlsx')
dfg=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT3.5.xlsx')
dfg4=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4.xlsx')


# In[4]:


dfl['LLM']='LLaMa2'
dfc['LLM']='Claude'
dfm['LLM']='Mixtral'
dfg['LLM']='GPT3.5'
dfg4['LLM']='GPT4'


# In[6]:


# Concatenate the data frames
concatenated_df = pd.concat([dfl, dfc, dfm, dfg, dfg4], ignore_index=True)
concatenated_df.columns


# In[7]:


df_30_900=concatenated_df[['PMID', 'LLM', 'Final Diagnosis', 'D1', 'D1 w/o lab', 'D5', 'D5 w/o lab',
       'D10', 'D10 w/o lab']]
df_30_900


# In[11]:


dfl=pd.read_csv('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\LLaMa-2.csv',encoding='latin-1')
dfc=pd.read_csv('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\Claude.csv' ,encoding='latin-1')
dfm=pd.read_csv('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\Mixtral.csv',encoding='latin-1')
dfg=pd.read_csv('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-3.5.csv',encoding='latin-1')
dfg4=pd.read_csv('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Results\\GPT-4.csv',encoding='latin-1')
dfl['LLM']='LLaMa2'
dfc['LLM']='Claude'
dfm['LLM']='Mixtral'
dfg['LLM']='GPT3.5'
dfg4['LLM']='GPT4'
concatenated_df = pd.concat([dfl, dfc, dfm, dfg, dfg4], ignore_index=True)
concatenated_df


# In[12]:


df_20_600=concatenated_df[['PMID', 'LLM', 'Final Diagnosis', 'D1', 'D1 w/o lab', 'D5', 'D5 w/o lab',
       'D10', 'D10 w/o lab']]
df_20_600


# In[50]:


concatenated_df = pd.concat([df_20_600, df_30_900], ignore_index=True)
# Assuming your DataFrame is named `concatenated_df`
# Modify the 'PMID' column only if the value contains 'PMID'
concatenated_df['PMID'] = concatenated_df['PMID'].apply(lambda x: x.replace('PMID ', '') if isinstance(x, str) and 'PMID' in x else x)
concatenated_df


# In[34]:


concatenated_df.to_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\1500_predictions.xlsx')


# In[36]:


df=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\1500_predictions_cleaned.xlsx')


# In[37]:


df


# In[38]:


# List of PMIDs to remove
pmids_to_remove = ['19162360', '23415437', '23975921', '29033779', '30186097', 
                   '31380008', '31497118', '31497445', '32864246', '33763324']

# Removing rows where the 'PMID' column contains any of the PMIDs in the list
df_filtered = df[~df['PMID'].astype(str).isin(pmids_to_remove)]

# Saving the filtered DataFrame back to Excel
df_filtered.to_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\1200_predictions_cleaned.xlsx')
df_filtered


# In[52]:


report=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\Reports.xlsx')
concatenated_df=pd.read_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\1500_predictions.xlsx')
report.columns


# In[53]:


report


# In[55]:


report=report[['PMID', 'Age', 'Gender', 'Lab Tests', 'Symptoms', 'Case Report']]
# Remove any leading or trailing spaces
concatenated_df['PMID'] = concatenated_df['PMID'].astype(str)
report['PMID'] = report['PMID'].astype(str)
concatenated_df['PMID'] = concatenated_df['PMID'].str.strip()
report['PMID'] = report['PMID'].str.strip()


final_df=pd.merge(concatenated_df,report,on='PMID',how='left')
final_df.to_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\test.xlsx')


# In[58]:


final_df.columns


# In[59]:


final_df=final_df[['PMID', 'Age', 'Gender', 'Lab Tests',
       'Symptoms', 'Case Report','LLM', 'Final Diagnosis', 'D1', 'D1 w/o lab', 'D5',
       'D5 w/o lab', 'D10', 'D10 w/o lab', ]]
final_df.to_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\1500_predictions_final.xlsx')


# In[60]:


# List of PMIDs to remove
pmids_to_remove = ['19162360', '23415437', '23975921', '29033779', '30186097', 
                   '31380008', '31497118', '31497445', '32864246', '33763324']

# Removing rows where the 'PMID' column contains any of the PMIDs in the list
df_filtered = final_df[~final_df['PMID'].astype(str).isin(pmids_to_remove)]

# Saving the filtered DataFrame back to Excel
df_filtered.to_excel('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\1200_predictions_final.xlsx')
df_filtered


# In[62]:


import matplotlib.pyplot as plt

# Data for categories and their counts
categories = [
    "Endocrine/Metabolic",
    "Cardiovascular",
    "Hematologic/Oncologic",
    "Infectious Diseases",
    "Neurological Disorders",
    "Gastrointestinal and Hepatic Conditions",
    "Renal Conditions",
    "Urological Conditions",
    "Toxicological Conditions",
    "Musculoskeletal Disorders",
    "Autoimmune Disorders",
    "Hematologic/Coagulation Disorders"
]

# Number of diseases in each category based on the previous classification
disease_counts = [
    8, 1, 4, 10, 2, 17, 4, 1, 2, 1, 1, 2
]

# Plotting the bar chart
plt.figure(figsize=(10, 8))
plt.barh(categories, disease_counts, color='skyblue')
plt.xlabel('Number of Diseases')
plt.title('Number of Diseases in Each Category')
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
# Save the figure
plt.tight_layout()
plt.savefig('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\Figures\\diseases_category_plot_300dpi.png', dpi=300)
# Display the plot
plt.tight_layout()
plt.show()


# In[80]:


#1500 full evaluation GPT4 and KG
import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
excel_file = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\KG evaluation\\300match.xlsx'

# Read all sheets from the Excel file
all_sheets = pd.read_excel(excel_file, sheet_name=None)

# Assign each sheet to a separate DataFrame
for sheet_name, df in all_sheets.items():
    # Dynamically create a variable for each sheet
    globals()[f'df_{sheet_name}'] = df
    print(f"DataFrame created for sheet: {sheet_name}")


# In[81]:


df0_300=df_D1
df1_300=df_D1_wo_lab
df2_300=df_D5
df3_300=df_D5_wo_lab
df4_300=df_D10
df5_300=df_D10_wo_lab
df0_300


# In[82]:


columns_to_select=['PMID','LLM','Score']
df0_300=df0_300[columns_to_select]
df1_300=df1_300[columns_to_select]
df2_300=df2_300[columns_to_select]
df3_300=df3_300[columns_to_select]
df4_300=df4_300[columns_to_select]
df5_300=df5_300[columns_to_select]
df0_300['PMID'] = df0_300['PMID'].str.replace('PMID ', '')
df1_300['PMID'] = df1_300['PMID'].str.replace('PMID ', '')
df2_300['PMID'] = df2_300['PMID'].str.replace('PMID ', '')
df3_300['PMID'] = df3_300['PMID'].str.replace('PMID ', '')
df4_300['PMID'] = df4_300['PMID'].str.replace('PMID ', '')
df5_300['PMID'] = df5_300['PMID'].str.replace('PMID ', '')
df4_300


# In[83]:


# Replace 'your_file.xlsx' with the path to your Excel file
excel_file = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\Manuscript\\KG evaluation\\1200match.xlsx'

# Read all sheets from the Excel file
all_sheets = pd.read_excel(excel_file, sheet_name=None)

# Assign each sheet to a separate DataFrame
for sheet_name, df in all_sheets.items():
    # Dynamically create a variable for each sheet
    globals()[f'df_{sheet_name}'] = df
    print(f"DataFrame created for sheet: {sheet_name}")
	
df0_1200=df_D1
df1_1200=df_D1_wo_lab
df2_1200=df_D5
df3_1200=df_D5_wo_lab
df4_1200=df_D10
df5_1200=df_D10_wo_lab
columns_to_select=['PMID','LLM','Score']
df0_1200=df0_1200[columns_to_select]
df1_1200=df1_1200[columns_to_select]
df2_1200=df2_1200[columns_to_select]
df3_1200=df3_1200[columns_to_select]
df4_1200=df4_1200[columns_to_select]
df5_1200=df5_1200[columns_to_select]
df4_1200


# In[87]:


# Assuming the DataFrames df0_300, df1_300, ..., df5_300 and df0_1200, df1_1200, ..., df5_1200 are already defined

# List of DataFrames to concatenate and their corresponding score names
df_300_list = [df0_300, df1_300, df2_300, df3_300, df4_300, df5_300]
df_1200_list = [df0_1200, df1_1200, df2_1200, df3_1200, df4_1200, df5_1200]
score_names = ['score_D1', 'score_D1_wo', 'score_D5', 'score_D5_wo', 'score_D10', 'score_D10_wo']

# Mapping of score values to their corresponding labels
score_mapping = {0: 'Incorrect', 1: 'Relevant', 2: 'Relevant', 3: 'Exact Match'}

# Initialize an empty DataFrame to store the merged results
merged_df = pd.DataFrame()

# Concatenate each pair of DataFrames, rename the score column, apply the mapping, and merge into the final DataFrame
for i in range(len(df_300_list)):
    # Rename the score columns before concatenating
    df_300_list[i] = df_300_list[i].rename(columns={'Score': score_names[i]})
    df_1200_list[i] = df_1200_list[i].rename(columns={'Score': score_names[i]})
    
    # Replace score values with the corresponding labels
    df_300_list[i][score_names[i]] = df_300_list[i][score_names[i]].map(score_mapping)
    df_1200_list[i][score_names[i]] = df_1200_list[i][score_names[i]].map(score_mapping)
    
    # Concatenate the corresponding DataFrames
    concatenated_df = pd.concat([df_300_list[i], df_1200_list[i]], ignore_index=True)
    
    # Merge the concatenated DataFrame into the final DataFrame
    if merged_df.empty:
        merged_df = concatenated_df
    else:
        merged_df = pd.merge(merged_df, concatenated_df, on=['PMID', 'LLM'], how='outer')

# Display the final merged DataFrame
merged_df



# In[89]:


merged_df.to_csv('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\1500_KG_Sep.csv')


# In[90]:


merged_df['score_D1'].value_counts()


# In[91]:


merged_df['score_D1_wo'].value_counts()


# In[92]:


merged_df['score_D5'].value_counts()


# In[93]:


merged_df['score_D5_wo'].value_counts()


# In[95]:


merged_df['score_D10'].value_counts()


# In[94]:


merged_df['score_D10_wo'].value_counts()


# In[3]:


#GPT-4 Prediction of 1500
import json

def print_evaluation_values(file_path):
    """
    Prints the "evaluation" key value from each entry in the JSON file.
    
    Parameters:
    - file_path: The path to the JSON file.
    """
    # Load the JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Iterate over each item in the data, parse the string to actual JSON,
    # and print the "evaluation" value
    for item in data.values():
        record = json.loads(item)
        evaluation = record['evaluation']
        print(f"{evaluation}")



# In[59]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D1_P1.output.json"
print_evaluation_values(file_path)


# In[60]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D1w_P1.output.json"
print_evaluation_values(file_path)


# In[61]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D5_P1.output.json"
print_evaluation_values(file_path)


# In[62]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D5w_P1.output.json"
print_evaluation_values(file_path)


# In[63]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D10_P1.output.json"
print_evaluation_values(file_path)


# In[64]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\20 cases\\GPT-4 Evaluation\\GPT3.5_Prompt1\\GPT3.5_D10w_P1.output.json"
print_evaluation_values(file_path)


# In[65]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT3.5_Prompt1\\GPT3.5_D1_P1.output.json"
print_evaluation_values(file_path)


# In[66]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT3.5_Prompt1\\GPT3.5_D1w_P1.output.json"
print_evaluation_values(file_path)


# In[71]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT4_Prompt1\\GPT4_D5_P1.output.json"
print_evaluation_values(file_path)


# In[72]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT4_Prompt1\\GPT4_D5w_P1.output.json"
print_evaluation_values(file_path)


# In[74]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT4_Prompt1\\GPT4_D10_P1.output.json"
print_evaluation_values(file_path)


# In[73]:


file_path="C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\April\\GPT4\\30 Cases\\30 Cases\\GPT4_Prompt1\\GPT4_D10w_P1.output.json"
print_evaluation_values(file_path)


# In[116]:


import pandas as pd

# Load the CSV and Excel files
kg_file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\1500_KG_Sep.csv'
llm_file_path = 'C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\1500_LLM_Sep.xlsx'

# Load the data
kg_df = pd.read_csv(kg_file_path)
llm_df = pd.read_excel(llm_file_path)

# Mapping for accuracy and lenient accuracy
accuracy_mapping = {'Relevant': 0.5, 'Exact Match': 1.0, 'Incorrect': 0.0}

# Apply the mappings to both the KG and LLM dataframes for accuracy and lenient accuracy
kg_df_replaced_acc = kg_df.applymap(lambda x: accuracy_mapping.get(x, x))
llm_df_replaced_acc = llm_df.applymap(lambda x: accuracy_mapping.get(x, x))

# Ensure that the columns are aligned for merging
common_columns = ['PMID', 'LLM', 'score_D1', 'score_D1_wo', 'score_D5', 'score_D5_wo', 'score_D10', 'score_D10_wo']

# Function to calculate the average of values between KG and LLM for accuracy and lenient accuracy
def calculate_average(kg_df, llm_df, columns):
    merged_df = pd.DataFrame()
    merged_df['PMID'] = kg_df['PMID']
    merged_df['LLM'] = kg_df['LLM']
    
    for col in columns:
        merged_df[f'avg_{col}'] = (kg_df[col] + llm_df[col]) / 2  # Take the average of corresponding values from KG and LLM
        
    return merged_df

# Calculate the average for accuracy and lenient accuracy
merged_df_acc = calculate_average(kg_df_replaced_acc, llm_df_replaced_acc, common_columns[2:])

# Replace numerical values with 'Exact', 'Relevant', and 'Incorrect'
def replace_values_with_labels(df):
    df_replaced = df.replace(1.0, 'Exact')  # Replacing float values, not strings
    df_replaced = df_replaced.replace(0.75, 'Exact')
    df_replaced = df_replaced.replace(0.50, 'Relevant')
    df_replaced = df_replaced.replace(0.25, 'Relevant')
    df_replaced = df_replaced.replace(0.00, 'Incorrect')
    return df_replaced


# Apply the label replacement to the averaged dataframe
df_to_acc = replace_values_with_labels(merged_df_acc)
df_to_acc.to_csv('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\1500_Sep.csv')
df_to_acc




# In[117]:


# Update the function to calculate the new definitions of Accuracy and Lenient Accuracy
def calculate_scores_updated(data):
    # Initialize an empty list to store the results
    results = []

    # Iterate over each unique LLM
    for llm in data['LLM'].unique():
        llm_data = data[data['LLM'] == llm]

        # For each score column, count Exact, Relevant, and Incorrect
        for col in ['avg_score_D1', 'avg_score_D1_wo', 'avg_score_D5', 'avg_score_D5_wo', 'avg_score_D10', 'avg_score_D10_wo']:
            total = 50
            exact_matches = sum(llm_data[col] == 'Exact')
            relevant_matches = sum(llm_data[col] == 'Relevant')
            incorrect_matches = sum(llm_data[col] == 'Incorrect')

            # Calculate new Accuracy and Lenient Accuracy
            accuracy = (exact_matches * 1 + 0.5 * relevant_matches) / total
            

            # Append the results to the list
            results.append({
                'LLM': llm,
                'Score_Type': col,
                'Exact Match': exact_matches,
                'Relevant': relevant_matches,
                'Incorrect': incorrect_matches,
                'Accuracy': accuracy * 100,
                
            })

    # Convert the results to a DataFrame
    results_df = pd.DataFrame(results)
    return results_df

# Calculate the updated scores and display the table
accuracy = calculate_scores_updated(df_to_acc)
accuracy.to_csv('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\1500_Sep_acc_res.csv')
accuracy


# In[118]:


# Update the function to calculate the new definitions of Accuracy and Lenient Accuracy
def calculate_scores_updated(data):
    # Initialize an empty list to store the results
    results = []

    # Iterate over each unique LLM
    for llm in data['LLM'].unique():
        llm_data = data[data['LLM'] == llm]

        # For each score column, count Exact, Relevant, and Incorrect
        for col in ['avg_score_D1', 'avg_score_D1_wo', 'avg_score_D5', 'avg_score_D5_wo', 'avg_score_D10', 'avg_score_D10_wo']:
            total = 50
            exact_matches = sum(llm_data[col] == 'Exact')
            relevant_matches = sum(llm_data[col] == 'Relevant')
            incorrect_matches = sum(llm_data[col] == 'Incorrect')

            # Calculate new Accuracy and Lenient Accuracy
            #accuracy = (exact_matches * 1 + 0.5 * relevant_matches) / total
            lenient_accuracy = (exact_matches * 1 +1 * relevant_matches) / total

            # Append the results to the list
            results.append({
                'LLM': llm,
                'Score_Type': col,
                'Exact Match': exact_matches + relevant_matches,
                'Incorrect': incorrect_matches,
                'Lenient Accuracy': lenient_accuracy * 100,
                
            })

    # Convert the results to a DataFrame
    results_df = pd.DataFrame(results)
    return results_df

# Calculate the updated scores and display the table
lenient_accuracy = calculate_scores_updated(df_to_acc)
lenient_accuracy.to_csv('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\1500_Sep_len_acc_res.csv')
lenient_accuracy


# In[119]:


# Update the function to calculate the new definitions of Accuracy and Lenient Accuracy
def calculate_scores_updated(data):
    # Initialize an empty list to store the results
    results = []

    # Iterate over each unique LLM
    for llm in data['LLM'].unique():
        llm_data = data[data['LLM'] == llm]

        # For each score column, count Exact, Relevant, and Incorrect
        for col in ['avg_score_D1', 'avg_score_D1_wo', 'avg_score_D5', 'avg_score_D5_wo', 'avg_score_D10', 'avg_score_D10_wo']:
            total = 50
            exact_matches = sum(llm_data[col] == 'Exact')
            relevant_matches = sum(llm_data[col] == 'Relevant')
            incorrect_matches = sum(llm_data[col] == 'Incorrect')

            # Calculate new Accuracy and Lenient Accuracy
            #accuracy = (exact_matches * 1 + 0.5 * relevant_matches) / total
            lenient_accuracy = ((exact_matches * 1) +(0.75 * relevant_matches)) / total

            # Append the results to the list
            results.append({
                'LLM': llm,
                'Score_Type': col,
                'Exact Match': exact_matches,
                'Relevant':  relevant_matches,
                'Incorrect': incorrect_matches,
                'Lenient Accuracy': lenient_accuracy * 100,
                
            })

    # Convert the results to a DataFrame
    results_df = pd.DataFrame(results)
    return results_df

# Calculate the updated scores and display the table
lenient_accuracy = calculate_scores_updated(df_to_acc)
#lenient_accuracy.to_csv('C:\\D\\e Health Lab projects\\Question_Answering\\Case reports\\1500_Sep_len_acc_res.csv')
lenient_accuracy


# In[ ]:




