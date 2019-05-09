import pymedtermino
from pymedtermino.all import *
pymedtermino.LANGUAGE = "en"

def haveSepsis( bacteria ):
    for disorder in bacteria.INVERSE_causative_agent:
        if(disorder.is_a(SNOMEDCT[91302008])):
            return True;
    return False;

def icd10Code(bacteria):
    print(bacteria);
    if(bacteria.is_a(SNOMEDCT[58800005])):
       if(bacteria.is_a(SNOMEDCT[9861002])):
           return "A40.3";
       elif(bacteria.is_a(SNOMEDCT[55547008])):
           return "A40.2";
       elif(bacteria.is_a(SNOMEDCT[80166006])):
           return "A40.0";
       elif(bacteria.is_a(SNOMEDCT[42518002])):
           return "A40.1";
       elif(bacteria in list(SNOMEDCT[58800005].descendants_no_double())):
           return "A40.8";
       else:
           return "A40.9";
    else:
       if(bacteria.is_a(SNOMEDCT[59343002])):
           return "A41.4";
       elif(bacteria.is_a(SNOMEDCT[44470000])):
           return "A41.3";
       elif(bacteria.is_a(SNOMEDCT[65119002])):
           if(bacteria.is_a(SNOMEDCT[3092008])):
               return "A41.0";
           elif(bacteria in list(SNOMEDCT[65119002].descendants_no_double())):
               return "A41.1";
           else:
               return "A41.2";
       elif(bacteria.is_a(SNOMEDCT[81325006])):
           return "A41.5";
       elif(haveSepsis(bacteria)):
           return "A41.8";
       else:
           return "A41.9";
        
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
    SNOMEDCT["80771008"],
    SNOMEDCT[113381003],
    SNOMEDCT[57997003],
    SNOMEDCT[113985000],
    SNOMEDCT[44304009],
    SNOMEDCT[114264004]];
for bacteria in listOfBacteria:
    print(icd10Code(bacteria));
