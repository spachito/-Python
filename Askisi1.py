import random

def addDiskInSkakiera(list,disk):
    #Δέχεται τη λίστα του παιχνιδιού (σκακιέρα 3Χ3) και το είδος του δίσκου που πρέπει να τοποθετήσει
    #Τοποθετεί τον δίσκο σε κάποια τυχαία θέση παράγοντας τυχαίους αριθμούς για τη γραμμή και τη στήλη.
    #Επιστρέφει τη λίστα μετά την τοποθέτηση καθώς και τον αριθμό γραμμής και στήλης στη οποία τοποθετήθηκε
    randRow=random.randint(0,2)
    randCol=random.randint(0,2)
    while (disk in list[randRow][randCol]):
        randRow=random.randint(0,2)
        randCol=random.randint(0,2)
    list[randRow][randCol].append(disk)
    return list, randRow, randCol


def checkRow(list,row,disk):
    # Δέχεται τη λίστα του παιχνιδιού τη γραμμή και το είδος δίσκου στην οποία τοποθετήθηκε ο τελευτάιος δακτύλιος
    # Ελέγχει αν αυτή η προσθήκη οδήγησε σε γραμμή που πληρεί τα κριτήρια για τερματισμό του προγράμματος.
    if(disk in list[row][0] and disk in list[row][1] and disk in list[row][2]):
        return True    #Ίδιοι δίσκοι σε μια γραμμή

    if('B' in list[row][1]):
        if ('A' in list[row][0] and 'C' in list[row][2]) or  ('A' in list[row][2] and 'C' in list[row][0]):
            return True   #Δίσκοι από τον μικρότερο στον μεγαλύτερο
    
    return False


def checkCol(list,col,disk):
    # Δέχεται τη λίστα του παιχνιδιού τη στήλη και το είδος του δίσκου στην οποία τοποθετήθηκε ο τελευταίος δακτύλιος
    # Ελέγχει αν αυτή η προσθήκη οδήγησε σε στήλη που πληρεί τα κριτήρια για τερματισμό του προγράμματος.

    # Έλεγχος αν υπάρχουν κάθετα τρεις ίδιοι δίσκοι
    if(disk in list[0][col] and disk in list[1][col] and disk in list[2][col]):
        return True

    # Έλεγχος αν στην στήλη υπάρχουν τρεις δίσκοι από τον μικρότερο στον μεγαλύτερο
    if('B' in list[1][col]):
        if ('A' in list[0][col] and 'C' in list[2][col]) or  ('A' in list[2][col] and 'C' in list[0][col]):
            return True
    return False

def checkDiag(list,disk):
    #Δέχεται τη λίστα και το είδος του δίσκου που μπήκε τελευταίος
    # και ελέγχει αν κάποια από τις κύριες διαγώνιες πληρεί τα κριτήρια τερματισμού.
  
    #Έλεγχος για ίδια στοιχεία σε κάποια από τις διαγώνιους
    if(disk in list[0][0] and disk in list[1][1] and disk in list[2][2]) or (disk in list[0][2] and disk in list[1][1] and disk in list[2][0]):
        return True
    
    if('B' in list[1][1]):
        if('A' in list[0][0] and 'C' in list[2][2]) or ('A' in list[2][2] and 'C' in list[0][0]):
            return True
        if ('A' in list[0][2] and 'C' in list[2][0]) or ('A' in list[2][0] and 'C' in list[0][2]):
            return True
    return False

def checkForEnd(list,row,col,disk):
    #Δέχεται την λίστα του παιχνιδιού, τη γραμμή, τη στήλη και το είδος του δίσκου που μπήκε τελευταίος.
    #Ελέγχει αν η προσθήκη αυτή οδηγεί σε τερματισμό του παιχνιδιού σύμφωνα με τα κριτήρια. 
    flag=checkRow(list,row,disk)  #Έλεγχος γραμμής
    if(not flag):
        flag=checkCol(list,col,disk) # Έλεγχος στήλης
    if(not flag) and (col==row or col+row==2):   # Έλεγχος διαγωνίων
            flag=checkDiag(list,disk)
    return flag  


def playGame():
    gameList=[[[],[],[]],[[],[],[]],[[],[],[]]]  #Λίστα 3X3 για την σκακιέρα 3Χ3
    disk_str='ABCABCABCABCABCABCABCABCABC' #Δίσκοι A (μικρότερος)-C(μεαλύτερος) 
    diskList=[] #Λίστα για την αναπαράσταση των δακτυλίων (Α μικρότερο και C μεγαλύτερο)
    for x in disk_str:
        diskList.append(x)

    endGame=False
    moves=0         
    while(not endGame):
        moves +=1
        randNum=random.randint(0,len(diskList)-1)  #Τυχαία επιλογή δίσκου
        disk=diskList.pop(randNum) # Αφαίρεση του δίσκου από τη λίστα
        gameList,row,col=addDiskInSkakiera(gameList,disk) #Προσθήκη του δίσκου σε τυχαία θέση
        endGame=checkForEnd(gameList,row,col,disk) #Έλεγχος για ολοκλήρωση του παιχνιδιού
    return moves   

        

#mail program
s=0
for i in range(100):
    moves=playGame()
    s+=moves
mo=s/100
mo_int=s//100
if mo-mo_int>=0.5:
    mo_int +=1
print('O μέσος όρος των βημάτων για την λήξη του παιχνιδιού ήταν: ',mo)
print ('ή περίπου', mo_int, 'βήματα')