import math

def createStringFromRandomness():
    #Δημιουργία μια λίστας με 20 τυχαίους δεκαεξαδικούς αριθμούς από το  https://www.cloudflare.com/en-gb/leagueofentropy/
    # Η τελευταία κλήρωση που χρησιμοποιήθηκε ήταν η κλήρωση με αριθμό 1641102. Επιλέχθηκαν οι τελευταίες 20 τιμές.
    nums=['d818ec70b12e9f90fe6fee1266101eda181c944a4acc5f363a850900ad0ad47d',
            'b1c37af6ebc0e549a79e6c0bee0f238d7c1f95a045283eeabe10eef0212a9be2',
            '4e20d479c1e66910ab156db8dab87e405daceaabe81d8064e47d498aaa91d410',
            '3a926b215aa2f7d168276a4caee3c450623c820ee39d046375fecb3006544c26',
            '9ac60661e9149dcfe7c3deae8d1e595302810ff8f4a1b98ef7e71c08926b53a3',
            'c79d891d53765c77a884f59c2ba431e52e055cef42d08c4f7ef67f201e76a899',
            '5e8531b1c08e38be804fbc4da6a718ec5c6185be238795120ae90f4a5112d7d7',
            '2983ebf4bc22dd61d123bb17e28c428af38ccbd9093c5c78c848fe0791dbaee1',
            'fe68602fed95aef245a977461d2e50c959e3ed27ff66e00ef3ca21a5525dcff6',
            '7f91b3daf5102f155d18fa3267d2a5c5bed2161741cd2f0c0a6b3cf5f8336c21',
            'e4851073494ce3e7b4c585479aedde9603bd7c459700a700663ee330f8788bd9',
            'f5b3a0ec72e8935f4ff519a9bc7cfbc2fc26d538af8059942172d0adfaad2b27',
            'a7e228959bdd90f21d333e9075564af83659925a315501d3ba092538aa5326ef',
            'c8c6e18a07cf88ffcbebafeeb4405a8bd1459bbf923a494976699fb4150bcea7',
            '7656105e8408948a16be7995bf2f5c1788bb2ebb5a85102110b780be7bde8cf1',
            'ddb370d837f17e7ca8af89d7d922d8b84ca435a8446af85ae862399fdfcf82d3',
            '76ab5a1c58779d70af7aa5d92e76885e9255f0fb43b9e645a00f4fe2bf634155',
            '90f6324dd2406d2747a7e1bd280418ffdb22c5ba6b43753390f48ba8f1cd1157',
            '1845427cea7144687d072e64e971d37910fc7756ceffd9d2fecb9232a6a7b2f5',
            '23bd4409c09e3224a00eb849d140d59b9e46dfdf074a26b1b98bbbb6e7db74cf']
    str=''
    for x in nums:
        str +=x
    return str


def createDictFromStr(str):
    #Δέχεται ένα χαρακτήρα με ψηφία του δεκαεξαδικού συστήματος και δημιουργεί ένα λεξικό στο οποίο
    #αποθηκεύει τη συχνότητα εμφάνισης κάθε ενός ψηφίου
    dict={}
  
    for x in '0123456789abcdef':
        dict[x]=0
    
    for x in str:
        dict[x]+=1

    return dict

def calcEntropia(dict,N):
    #Δέχεται ένα λεξικό με τη συχνότητα εμφάνισης των ψηφίων του δεκαεξαδικού συστήματος αρίθμησης και έναν
    #αριθμό που δείχνει το συνολικό πλήθος των ψηφίων από τα οποία προέκευψε το παραπάνω λεξικό.
    #Υπολογίζει την εντροπία του.
    s=0
    for x in '0123456789abcdef':
        if dict[x]!=0:
            prop=dict[x]/N
            s += prop*math.log(prop)
    s=s*(-1)
    return s


str=createStringFromRandomness()
N=len(str)
dict=createDictFromStr(str)
entropia=calcEntropia(dict,N)
print('H εντροπία του κειμένου είναι: ',entropia)
