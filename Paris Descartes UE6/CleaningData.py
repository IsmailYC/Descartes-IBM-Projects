import pandas as pd

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

attempt1DF = pd.read_csv('attempt1Results.csv',delimiter=',');
attempt2DF = pd.read_csv('attempt2Results.csv',delimiter=',');
attempt1StaysList= attempt1DF[attempt1DF.columns[1]].values.tolist();
attempt2StaysList= attempt2DF[attempt2DF.columns[1]].values.tolist();
attempt1UniqueStaysList= remove_duplicates(attempt1StaysList);
attempt2UniqueStaysList= remove_duplicates(attempt2StaysList);
total1=len(attempt1UniqueStaysList);
total2=len(attempt2UniqueStaysList);
attempt1NbrOfMissingICD10= attempt1DF[(attempt1DF.type=="Missing hyperkalemia diagnosis")].shape[0]
attempt1NbrOfPotassiumAgents= attempt1DF[(attempt1DF.type=="Giving Potassium-Sparing Agents to a patient with hyperkalemia")].shape[0]
attempt1NbrOfPotassiumSupp= attempt1DF[(attempt1DF.type=="Giving Potassium Supplements to a patient with hyperkalemia")].shape[0]
attempt1NbrOfNoAction= attempt1DF[(attempt1DF.type=="No action was taken")].shape[0]
attempt1NbrOfUnjustDialysis= attempt1DF[(attempt1DF.type=="Unjustified use of extrarenal purification")].shape[0]
attempt1NbrOfUnjustDiagnosis= attempt1DF[(attempt1DF.type=="Unjustified diagnosis with hyperkalemia")].shape[0]
attempt2NbrOfMissingICD10= attempt2DF[(attempt2DF.type=="Missing hyperkalemia diagnosis")].shape[0]
attempt2NbrOfPotassiumAgents= attempt2DF[(attempt2DF.type=="Giving Potassium-Sparing Agents to a patient with hyperkalemia")].shape[0]
attempt2NbrOfPotassiumSupp= attempt2DF[(attempt2DF.type=="Giving Potassium Supplements to a patient with hyperkalemia")].shape[0]
attempt2NbrOfNoAction= attempt2DF[(attempt2DF.type=="No action was taken")].shape[0]
attempt2NbrOfUnjustDialysis= attempt2DF[(attempt2DF.type=="Unjustified use of extrarenal purification")].shape[0]
attempt2NbrOfUnjustDiagnosis= attempt2DF[(attempt2DF.type=="Hyperkalemia while having normal potassium level")].shape[0]
attempt2NbrOfMissingTests= attempt2DF[(attempt2DF.type=="Missing potassium biologie results")].shape[0]
print(total1);
print(attempt1NbrOfMissingICD10)
print(attempt1NbrOfPotassiumAgents)
print(attempt1NbrOfPotassiumSupp)
print(attempt1NbrOfNoAction)
print(attempt1NbrOfUnjustDialysis)
print(attempt1NbrOfUnjustDiagnosis)
print("***************************")
print(total2);
print(attempt2NbrOfMissingICD10)
print(attempt2NbrOfPotassiumAgents)
print(attempt2NbrOfPotassiumSupp)
print(attempt2NbrOfNoAction)
print(attempt2NbrOfUnjustDialysis)
print(attempt2NbrOfUnjustDiagnosis)
print(attempt2NbrOfMissingTests)
print("***************************")
f1=attempt1DF[(attempt1DF.type=="Giving Potassium-Sparing Agents to a patient with hyperkalemia")]
f2=attempt1DF[(attempt1DF.type=="Giving Potassium Supplements to a patient with hyperkalemia")]
f3=attempt1DF[(attempt1DF.type=="No action was taken")]
f4=attempt2DF[(attempt2DF.type=="Giving Potassium-Sparing Agents to a patient with hyperkalemia")]
f5=attempt2DF[(attempt2DF.type=="Giving Potassium Supplements to a patient with hyperkalemia")]
f6=attempt2DF[(attempt2DF.type=="No action was taken")]
