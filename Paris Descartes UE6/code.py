import pandas as pd

sejours_df = pd.read_csv('sejours.csv',delimiter='\t',dtype={"id_sejour": int, "age": float, "sexe_masculin": bool, "ghm": str, "sortie_deces": bool, "diag_principal":str, "nb_RUM":int,"duree":int,"sortie_transfert":bool,"entree_transfert":bool,"entree_urgences":bool});
biologies_df = pd.read_csv('biologie.csv',delimiter='\t',encoding ='latin1',dtype={"id_sejour": int, "date_mesure":int, "type_mesure":str,"valeur":float,"unite":str,"borne_inf":str,"borne_sup":str});
actes_df = pd.read_csv('actes.csv',delimiter='\t',dtype={"id_sejour": int,"acte":str,"date_realisation":int});
diagnostique_df = pd.read_csv('diagnostics.csv',delimiter='\t',dtype={"id_sejour": int,"diagnostic":str});
medicament_df = pd.read_csv('medicaments_administres.csv',delimiter='\t',encoding ='latin1',dtype={"id_sejour": int,"medicament_nom":str, "medicament_atc":str, "date_administration":int, "dose":str,"unite":str,"voie_administration":str});
list_id_sejours= sejours_df[sejours_df.columns[0]].values.tolist()
sejours_non_conforment=[];
types_anomalies=[];
for id_sejour in list_id_sejours:
    sejour_df_isole= sejours_df[(sejours_df.id_sejour==id_sejour)];
    biologies_df_isoles= biologies_df[(biologies_df.id_sejour==id_sejour) & (biologies_df.type_mesure == 'Potassium') & (biologies_df.valeur >= 5.5)];
    diagnostique_df_isoles= diagnostique_df[(diagnostique_df.id_sejour==id_sejour) & (diagnostique_df.diagnostic.str.startswith('E875'))];
    diuretique_hyperkaliemiant_df_isoles= medicament_df[(medicament_df.id_sejour==id_sejour) & (medicament_df.medicament_atc.str.startswith('C03D'))];
    supplementation_en_potassium_df_isoles= medicament_df[(medicament_df.id_sejour==id_sejour) & (medicament_df.medicament_atc.str.startswith('A12B'))];    
    if(not(biologies_df_isoles.empty)):
        if(diagnostique_df_isoles.empty):
            sejours_non_conforment.append(id_sejour);
            types_anomalies.append("diagnostique hyperkaliemie E875 manquant");
        premiere_apparence= biologies_df_isoles.date_mesure.values[0];
        diuretique_hyperkaliemiant_df_isoles_non_conforment= diuretique_hyperkaliemiant_df_isoles[(diuretique_hyperkaliemiant_df_isoles.date_administration>premiere_apparence)];
        supplementation_en_potassium_df_isoles_non_conforment= supplementation_en_potassium_df_isoles[(supplementation_en_potassium_df_isoles.date_administration>premiere_apparence)];
        chelateur_potassium_df_isoles= medicament_df[(medicament_df.id_sejour==id_sejour) & (medicament_df.medicament_atc.str.startswith('V03AE') & medicament_df.date_administration>=premiere_apparence)];
        epuration_extra_renale_df_isoles= actes_df[(actes_df.id_sejour==id_sejour) & (actes_df.acte.str.startswith("JV") & actes_df.date_realisation>=premiere_apparence)];
        if(not(diuretique_hyperkaliemiant_df_isoles_non_conforment.empty)):
            sejours_non_conforment.append(id_sejour);
            types_anomalies.append("administration de diuretique hyperkaliemiant a un hyperkaliémie");
        if(not(supplementation_en_potassium_df_isoles_non_conforment.empty)):
            sejours_non_conforment.append(id_sejour);
            types_anomalies.append("administration de supplementation en potassium a un hyperkaliémie");
        if(diuretique_hyperkaliemiant_df_isoles.empty and supplementation_en_potassium_df_isoles.empty):
            if(chelateur_potassium_df_isoles.empty):
                if(epuration_extra_renale_df_isoles.empty):
                    sejours_non_conforment.append(id_sejour);
                    types_anomalies.append("aucune action n'est prise");
    elif(not(diagnostique_df_isoles.empty)):
        sejours_non_conforment.append(id_sejour);
        types_anomalies.append("hyperkaliémie non justifiée");
resultats = zip(sejours_non_conforment,types_anomalies);
colonnes = ['id_sejour', 'type'];
df_finale = pd.DataFrame.from_records(resultats, columns=colonnes);
df_finale.to_csv('resultats.csv', sep='\t');
