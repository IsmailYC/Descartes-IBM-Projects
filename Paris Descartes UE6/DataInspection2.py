import pandas as pd

staysDF = pd.read_csv('sejours.csv',delimiter='\t',dtype={"id_sejour": int, "age": float, "sexe_masculin": bool, "ghm": str, "sortie_deces": bool, "diag_principal":str, "nb_RUM":int,"duree":int,"sortie_transfert":bool,"entree_transfert":bool,"entree_urgences":bool});
biologieDF = pd.read_csv('biologie.csv',delimiter='\t',encoding ='latin1',dtype={"id_sejour": int, "date_mesure":int, "type_mesure":str,"valeur":float,"unite":str,"borne_inf":str,"borne_sup":str});
actsDF = pd.read_csv('actes.csv',delimiter='\t',dtype={"id_sejour": int,"acte":str,"date_realisation":int});
diagnosticsDF = pd.read_csv('diagnostics.csv',delimiter='\t',dtype={"id_sejour": int,"diagnostic":str});
drugsDF = pd.read_csv('medicaments_administres.csv',delimiter='\t',encoding ='latin1',dtype={"id_sejour": int,"medicament_nom":str, "medicament_atc":str, "date_administration":int, "dose":str,"unite":str,"voie_administration":str});
anomalyStays=[];
anomalyTypes=[];
targetBiologieDF= biologieDF[(biologieDF.type_mesure == 'Potassium') & (biologieDF.valeur >= 5.5)];
targetBiologieNoDuplicateDF= targetBiologieDF[~targetBiologieDF.id_sejour.duplicated(keep='first')];
staysIdList= targetBiologieNoDuplicateDF[targetBiologieNoDuplicateDF.columns[0]].values.tolist();
print(len(targetBiologieDF[targetBiologieNoDuplicateDF.columns[0]].values.tolist()));
print(len(staysIdList));
for stayId in staysIdList:
    targetStaysDF= staysDF[(staysDF.id_sejour==stayId)];
    tempTargetBiologieDF= targetBiologieDF[(targetBiologieDF.id_sejour==stayId)];
    potassiumSparingAgentDrugDF= drugsDF[(drugsDF.id_sejour==stayId) & (drugsDF.medicament_atc.str.startswith('C03D'))];
    potassiumSupplementDrugDF= drugsDF[(drugsDF.id_sejour==stayId) & (drugsDF.medicament_atc.str.startswith('A12B'))];    
    firstOccurance= tempTargetBiologieDF.date_mesure.values[0];
    potassiumSparingAgentAfterFirstOccuranceDrugDF= potassiumSparingAgentDrugDF[(potassiumSparingAgentDrugDF.date_administration>=firstOccurance)];
    potassiumSupplementAfterFirstOccuranceDrugDF= potassiumSupplementDrugDF[(potassiumSupplementDrugDF.date_administration>=firstOccurance)];
    hyperkalimiaTreatementDrugDF= drugsDF[(drugsDF.id_sejour==stayId) & (drugsDF.medicament_atc.str.startswith('V03AE')) & (drugsDF.date_administration>=firstOccurance)];
    targetActsDF= actsDF[(actsDF.id_sejour==stayId) & (actsDF.acte.str.startswith('JV')) & (actsDF.date_realisation>=firstOccurance)];
    targetDiagnosticsDF= diagnosticsDF[(actsDF.id_sejour==stayId) & (diagnosticsDF.diagnostic.str.startswith('E875'))];
    if(targetDiagnosticsDF.empty):
            anomalyStays.append(stayId);
            anomalyTypes.append("Missing hyperkalemia diagnosis");
    if(not(potassiumSparingAgentAfterFirstOccuranceDrugDF.empty)):
        anomalyStays.append(stayId);
        anomalyTypes.append("Giving Potassium-Sparing Agents to a patient with hyperkalemia");
    if(not(potassiumSupplementAfterFirstOccuranceDrugDF.empty)):
        anomalyStays.append(stayId);
        anomalyTypes.append("Giving Potassium Supplements to a patient with hyperkalemia");
    if(potassiumSupplementDrugDF.empty and potassiumSparingAgentDrugDF.empty):
        if(not(hyperkalimiaTreatementDrugDF.empty)):
            if(targetActsDF.empty):
                anomalyStays.append(stayId);
                anomalyTypes.append("No action was taken");
            elif(not(targetStaysDF.entree_transfert.values[0])):
                anomalyStays.append(stayId);
                anomalyTypes.append("Unjustified use of extrarenal purification");
                
targetDiagnosticsDF= diagnosticsDF[(diagnosticsDF.diagnostic.str.startswith('E875'))];
staysIdList= targetDiagnosticsDF[targetDiagnosticsDF.columns[0]].values.tolist();
print(len(staysIdList));
for stayId in staysIdList:
    targetStaysDF= staysDF[(staysDF.id_sejour==stayId)];
    targetBiologieDF= biologieDF[(targetBiologieDF.id_sejour==stayId) & (biologieDF.type_mesure == 'Potassium')];
    targetBiologieLessDF= targetBiologieDF[(targetBiologieDF.valeur >= 5.5)]
    if(not(targetStaysDF.entree_transfert.values[0])):
        if(targetBiologieDF.empty):
            anomalyStays.append(stayId);
            anomalyTypes.append("Missing potassium biologie results");
        elif(targetBiologieLessDF.empty):
            anomalyStays.append(stayId);
            anomalyTypes.append("Hyperkalemia while having normal potassium level");
lists = zip(anomalyStays,anomalyTypes);
labels = ['id_sejour', 'type'];
saveDF = pd.DataFrame.from_records(lists, columns=labels);
saveDF.to_csv('attempt2Results.csv', sep=',');
