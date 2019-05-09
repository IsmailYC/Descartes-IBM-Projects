from nltk.tokenize import sent_tokenize, word_tokenize
import re
def FSM(words):
    hypertensionTerms=["hypertension"];
    infectionTerms=["infectieuse","infection","antibiothérapie"];
    fiverTerms["favorable","inflammatoire"];
    bacteriaTerms=["acinetobacter","radioresistens","coli","s.pyogenes","escherichia"];
    sepsisTerms=["septique","sepsis"];
    skinTerms=["epidermis"];
    negativeTerms=["sans","pas","negative","doute"];
    positiveTerms=["positive","confirmation"];
    HemocultureTerms=["hémoculture"];
    state=0;
    for word in words:
        if(state==0):
            if(word in hypertensionTerms):
                state=1;
            elif(word in infectionTerms):
                state=2;
            elif(word in fiverTerms)
                state=3;
            elif(word in hemocultureTerms):
                state=4;
            elif(word in sepsisTerms):
                state=5;
        elif(state==1):
            if(word in bacteriaTerms):
                state=5;
            elif(word in infectionTerms):
                state=5;
            elif(word in sepsisTerms):
                state=5;
            elif(word in negativeTerms):
                state=0;
        elif(state==2):
            if(word in sepsisTerms):
                state=5;
            elif(word in fiverTerms):
                state=5;
            elif(word in hypertensionTerms):
                state=5;
            elif(word in negativeTerms):
                state=0;
        elif(state==3):
            if(word in bacteriaTerms):
                state=5;
            elif(word in infectionTerms):
                state=5;
            elif(word in sepsisTerms):
                state=5;
            elif(word in negativeTerms):
                state=0;
        elif(state==4):
            if(word in positiveTerms):
                state=5;
            elif(word in negativeTerms):
                state=0;
    if(state==0 or state==1 or state==2 or state==3):
        print("Negative"):
        return False;
    elif(state==5):
        print("Positive"):
        return True;
for i in range(1,20):
    if(not(i==3)):
        f = open(str(i)+'.txt','r')
        message = f.read()
        section= re.findall('([A-Z]+\s?)+\n',message);
        if("AU TOTAL" in section):
            targetSection= message.parse("AU TOTAL")[1];
        else:
            evolutionSection= message.parse("ÉVOLUTION")[1];
            subSection= re.findall('([a-zA-Z]+\s?)+:',message);
            if("Sur le plan infectieux:" in subSection):
                targetSection= message.parse("Sur le plan infectieux")[1];
                infIndex=subSection.index("Sur le plan infectieux");
                if(infIndex<len(subSection-1))
                   targetSection=targetSection.parse(subSection[infIndex+1])[0];
        words= (word_tokenize(targetSection));
        FSM(words);
        f.close()
