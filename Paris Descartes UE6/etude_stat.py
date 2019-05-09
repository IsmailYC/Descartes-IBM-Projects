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

df = pd.read_csv('resultats.csv',delimiter='\t');
list_sejours= df[df.columns[1]].values.tolist();
list_sejours_unique= remove_duplicates(list_sejours);
nom_sejours_non_conforment=len(list_sejours_unique);
df1= df[(df.type=="diagnostique hyperkaliemie E875 manquant")]
nom_diagnostique_manquant= df1.shape[0]
df2=df[(df.type=="administration de diuretique hyperkaliemiant a un hyperkaliémie")]
nom_administration_diuretique= df2.shape[0]
df3= df[(df.type=="administration de supplementation en potassium a un hyperkaliémie")]
nom_administration_supplementation= df3.shape[0]
df4=df[(df.type=="aucune action n'est prise")]
nom_aucune_action= df4.shape[0]
df5=df[(df.type=="hyperkaliémie non justifiée")]
nom_hyperkaliemie_non_justifiee= df5.shape[0]
print("nombre de sejours non conforment: "+str(nom_sejours_non_conforment));
print(list_sejours_unique)
print("nombre de diagnostique hyperkaliemie E875 manquant: "+str(nom_diagnostique_manquant))
print(df1[df1.columns[1]].values.tolist());
print("nombre de administration de diuretique hyperkaliemiant a un hyperkaliémie: "+str(nom_administration_diuretique));
print(df2[df2.columns[1]].values.tolist());
print("nombre de administration de supplementation en potassium a un hyperkaliémie: "+str(nom_administration_supplementation));
print(df3[df3.columns[1]].values.tolist());
print("nombre de sejours avec aucune action: "+str(nom_aucune_action));
print(df4[df4.columns[1]].values.tolist());
print("nombre de hyperkaliémie non justifiée: "+str(nom_hyperkaliemie_non_justifiee));
print(df5[df5.columns[1]].values.tolist());
c=input("Continue...")
