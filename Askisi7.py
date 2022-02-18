import ast

def chooseKey(dict):
    for d in dict:
        print(d)
    key=input('Choose one of the above key:')
    while(key not in dict):
        print('Wrong choice')
        key=input('Choose one of the above key: ')
    print ('You choose as key:', key)
    return key

def printResults(list, k):
    D={}
    maxi=list[0]
    mini=list[0]
    for x in list:
        if x in D:
            D[x]+=1
        else:
            D[x]=1
        if x>maxi:
            maxi=x
        elif x<mini:
            mini=x
    
    popul=-1
   
    for key in D:
        if D[key]>popul:
            popul=D[key]
    print ('Δηοφιλέστερη τιμή για το κλειδί ', k, 'είναι:')
    for key in D:
        if D[key]== popul:
            print (key)

    print ('H μικρότερη τιμή  για το κλειδί ', k, 'είναι:', mini)
    print ('H μεγαλύτερη τιμή  για το κλειδί ', k, 'είναι:', maxi)


f = open('Askisi7.txt', 'r')
flag=True #Σημαία που είναι αληθής μόνο στην πρώτη γραμμή του αρχείου txt
for x in f:
    dictionary = ast.literal_eval(x) # Συνάρτηση μετατροπής της γραμμής του αρχείου σε Λεξικό
    if(flag):
            # Συνάρτηση επιλογής του κλειδιού από τα διαθέσιμα κλειδιά στο πρώτο λεξικό
        key=chooseKey(dictionary)
        values=[]
        flag=False
    values.append(dictionary[key])
# Συνάρτηση εμφάνισης των αποτελεσμάτων
printResults(values, key)
f.close()