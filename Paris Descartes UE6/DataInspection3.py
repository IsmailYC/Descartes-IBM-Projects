import pandas as pd

staysDF = pd.read_csv('sejours.csv',delimiter='\t',dtype={"id_sejour": int, "age": float, "sexe_masculin": bool, "ghm": str, "sortie_deces": bool, "diag_principal":str, "nb_RUM":int,"duree":int,"sortie_transfert":bool,"entree_transfert":bool,"entree_urgences":bool});
biologieDF = pd.read_csv('biologie.csv',delimiter='\t',encoding ='latin1',dtype={"id_sejour": int, "date_mesure":int, "type_mesure":str,"valeur":float,"unite":str,"borne_inf":str,"borne_sup":str});
actsDF = pd.read_csv('actes.csv',delimiter='\t',dtype={"id_sejour": int,"acte":str,"date_realisation":int});
diagnosticsDF = pd.read_csv('diagnostics.csv',delimiter='\t',dtype={"id_sejour": int,"diagnostic":str});
drugsDF = pd.read_csv('medicaments_administres.csv',delimiter='\t',encoding ='latin1',dtype={"id_sejour": int,"medicament_nom":str, "medicament_atc":str, "date_administration":int, "dose":str,"unite":str,"voie_administration":str});
anomalyStays=[];
targetBiologieDF= biologieDF[(biologieDF.type_mesure == 'Potassium') & (biologieDF.valeur >= 5.5)];
targetBiologieNoDuplicateDF= targetBiologieDF[~targetBiologieDF.id_sejour.duplicated(keep='first')];
staysIdList= targetBiologieNoDuplicateDF[targetBiologieNoDuplicateDF.columns[0]].values.tolist();
for stayId in staysIdList:
    ok=False;
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
    if(not(potassiumSparingAgentDrugDF.empty) and potassiumSparingAgentAfterFirstOccuranceDrugDF.empty):
        ok=True;
    if(not(potassiumSupplementDrugDF.empty) and potassiumSupplementAfterFirstOccuranceDrugDF.empty):
        ok=True
    if(not(hyperkalimiaTreatementDrugDF.empty)):
        ok=True;
    if(not(targetActsDF.empty)):
        ok=True;
    if(not(ok)):
        anomalyStays.append(stayId);
print(len(anomalyStays))
print(anomalyStays)
