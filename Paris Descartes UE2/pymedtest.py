import pymedtermino
from pymedtermino.all import *
pymedtermino.LANGUAGE = "en"
listOfSepsis= list(SNOMEDCT[91302008].descendants_no_double());
listOfBacteria=[SNOMEDCT["80166006"],
    SNOMEDCT["9861002"],
    SNOMEDCT["112283007"],
    SNOMEDCT["27784005"],
    SNOMEDCT["58800005"],
    SNOMEDCT["3092008"],
    SNOMEDCT["68704007"],
    SNOMEDCT["21927003"],
    SNOMEDCT["60875001"],
    SNOMEDCT["55247009"],
    SNOMEDCT["52499004"],
    SNOMEDCT["73457008"],
    SNOMEDCT["80897008"],
    SNOMEDCT["80771008"]];
for bacteria in listOfBacteria:
    print(bacteria);
    for sepsis in listOfSepsis:
        listOfCauses=list(sepsis.causative_agent)
        if(bacteria in listOfCauses):
            print(sepsis);
    print("***********************************");
