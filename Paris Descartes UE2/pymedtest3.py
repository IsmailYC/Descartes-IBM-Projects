import pymedtermino
from pymedtermino.all import *
pymedtermino.LANGUAGE = "en"

listOfBacteria=[SNOMEDCT["80166006"],
    SNOMEDCT["9861002"],
    SNOMEDCT["112283007"],
    SNOMEDCT["44470000"],
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
    print(bacteria)
    for disorder in bacteria.INVERSE_causative_agent:
        if(disorder.is_a(SNOMEDCT[91302008])):
            print(disorder);
    print("********************");
