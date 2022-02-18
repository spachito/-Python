def createListOfNums():
    #Δημιουργία λίστας με 100 τυχαίους δεκαεξαδικούς αριθμούς από  https://www.cloudflare.com/en-gb/leagueofentropy/.
    # Η τελευταία κλήρωση που χρησιμοποιήθηκε ήταν η κλήρωση με αριθμό 1632972 (9/2/2022). Χρησιμοποιήθηκαν οι
    #τελευταίοι 100 αριθμοί.
    hexnumbers=['a0a64512e287353bb4e4680f36646b618319d609ba88df50cd03034951e4e45f',
        '5868cbc893905a35c30ea987b7460f8dc178101c3aefcf88446172a9b97676fc',
        '77c60eaa843afd36d6f9d94c000e52f3871cfebc69b18bc22ce0f3dacc3705eb',
        '68686b86171881dc77a6809d3705af4df948add38825c97e4717059fc003d7e1',
        '005acfbd33702f1fa77b1a29c32564b2ebc6e93070b5fc20b66790a23bbc67c1',
        'da0606813d63eef2c384a1e74c02be24aad0e225c0f83eaf9cc5b8d7eaf2218a',
        '70761843d76b91a1530a8abf5c76c025ff554bd0d3c8b6ef21c55b076efae799',
        '10c25f7c091725b6428b7403f30981bc5a252e775b4ad15e8fec97bef0fabedf',
        '7780e1f40c19481d00d355c10c1e1372f7411c05bd7e0a820f3d280ced2fa0dd',
        '997d19b5ac5c19a4767c83b17184bb042601f74209493696fe190fb332f693dc',
        '01741b7289971f0cc2227fe34544f907e3852fb7a07513bcb74718775e730042',
        '68b20832f8a438ea4f1a24ef2d4f3b0ae2eb6f7986bd2568cafbb9e906f679a3',
        '10b559899daa7e25c0cddf4809bbc67b8a0319b95491ecdcf7ec0f9ec44885d4',
        '0ff73d56654b96cd34289137508d1d5f690c0ff250c33d1c0f7f3b592ad9af61',
        '251f4b8972e46b45efabfa4d62d220cafb5245b4084d348e6f4850d659119602',
        '31ae4342c4c86f7b9122ce16b0d6a2acd2b0f280152056b1626f80eb203f363b',
        '545acaea21f75cc2570f82562d58e497f0b6ee7ed859efc73bb41af29aced0a5',
        '4b62dd6b238d4e0b10637ea14e49f670f9f3078e6c3c720a36cff3a11d473e12',
        'c72d007d3783157dffb66dfcdae2e0538eff620c6bf488cfed9eefc455298bc8',
        '11dde943bc31dd43846df51b74f5203db9ae6989e4c20551de2c568d9ee9725d',
        '47e696c62a6df9179f220499c0bb43378da029b77221a9fe9deeb87856f35522',
        '8186dcc01ea83e9fdd7909328ac655113be84989c6421ba7012b412316f3b031',
        '1a94864dfcc9fb58c4b17241d163b0080a94600d7def751d0682f4307484c44a',
        '43622445d3852ad3b9c847d9896efa7893d20738f67fef5711d625fe887e2eb1',
        'ce06c6539448e8e779db59a1eeb106f4ee2c8d67c6e2a0a329896df5a19c2476',
        '7c6b51888d4cf5a66f6662748b37e4a6b67d18b4141363314ea0652c760edec8',
        'bc3510ca44803820e5040c1cc0ae3142e682ce6fab56e7c828451b0e51732cef',
        '47f8ba537f5ffd648b86473ab179fddd12e575a12a8cb2dd3c76557fed725219',
        '141d0183fbd82a0325f49b28f8acfa7c7fd8deff964c82f0a1d2c87bcd23b155',
        'f3cddec87ffdfeb7a1d84cb11da24fa886307e7da6fc89efdba7b06a911cedb1',
        '42c81719ef07ccc2199ac1ecf1aa70c5f3a886c6c5e2aeb2e98519fd7f1ef385',
        'dae8e1c251fd5e8a8c7f689cda66bc556278e9afc26c3c53da0860461b9ce44a',
        '1c15a43f49b81d946944a8202e0fa73f090ba79ccd447c868b53a1d0de28f676',
        'a3db6e17534e25d1f13c1fab7981dddfbc50405aaea4c81433ce2b86ed340437',
        'c369e03b853e791755d9f8dadc2e5ee06a09952166cbf97aecca350b9ee8e29b',
        '9225e3b8a9f1f63b567296a390e62a60177bd5a6f5569f4292cc5fd34356076d',
        '4dc585bf1f3c2daf142977b62fbfd6fc428ab9402d10430a210043e70723a5e5',
        '97afc922176c5887aad47175a53164315ca72e649935ed6c100898bb7cff876b',
        '8498efac28b62fc6e4303f965e6d4fd599558a8d4cfe8d2b0a59ca3ff547df1e',
        '21d4309448e43f5d1f3642c795799823b8208d0bd1e595401e748515f15e555e',
        '65e9237c067be64a7c5519e7c4bc7210311a4467d6d9eb1bdabe906256996f29',
        '2c426270fe47c4b70c9dc671d672624d2e7d1cf4d0b8c2cc7929a0bbb00cb318',
        'd7ba8d68b1fa90165dd115b35056b9e5651732efb5e9f397f3f5f17c7bc29de7',
        'ce7410585b6d3f6728afbe99731ec31f90d48e735cc870dd5bdb4cc72285bf95',
        '7cf35ba7b7e068c1e011fc931d696a43de27f70e35a69d16a53d55260725ae8d',
        '6fe009336dfe60f0caeaee7dce22ff403b0c2be131cb6d8fdb8c0949c81eeba8',
        'c9d5792aacc3ddeada1e180eac49085d33b771de411359c8b7bfca5af396bee6',
        'e8ca53296ea0d384ce6b7834033e0f2eccb4fe4244138879f3068c0145ae964d',
        '9a0fa3ec06b7eac452598a08d8a27112e0658eadfc27717110f0d83486f77a71',
        'ad9b4c1cb3fd262f7f5aa1cf22f96a0a9827af90057ec2c4fdefe5e11d8c6ab9',
        '81929bdaf8573127c7d9febcfff6fa0dc65579fa2ddead0d818bdfa5811711f3',
        'cfa2ec254cd10dc91ee8d7bd43febd6309ab23aa620678f82484f2af5f84ea4d',
        '063c5284483483778bedd7149e5e1077601d304260bb212b8daa3c6b10f3c872',
        '36d35591e1b7fe7038f4540d5c955ae0fdd51def6af7711cad77f269242531f0',
        '1a4b6a0e6a1a3bdb00e230b3b5e8bdabd3d3da4ce4fcd06c1ac70ae617514f68',
        '83601ef7ffac9d54084eda559bc673ab281712bd0970ce7920e7d0c510e07559',
        'dabb439bb485855780286b081e19da13c69e69a851d9814bc333efa17367faad',
        'e4879b150d4e3bff7d8172f9220538967a0dddd9d3aa954428976782974162da',
        'fec2b3b2e281bf465c77d7b4ffc48255abb2fe2a807de18191fafcaba0c404a5',
        '88d35f0c847e02a8e063c58cc9653a81e6a3245bb6c2a5976676b6accab49b4b',
        'a1e91ed0304603fa80adcea85129bf4c13518655c4c50c3b2aac4d5277b2934e',
        '84ef6170c954e7395df77a82adf83071410d64d3ca26957055a19e4d9fda55eb',
        '040118268e269637e470f322908f822b586ff413c5efdfb17b7f71ab7f2faed4',
        '3b5fcc207a18af751a1139713f0a344ba1f40607db716e942ae4965365ef6e87',
        '3ef26c9602a25fefd5ba5988cafc876c9fbfc4ab4d3c10d5fab5bd0e92189f6f',
        'ce5485225aff0f75f4ebd50797b55c9c9b8b68ee17cc66882560660145de3fb0',
        'd632d595c97abcf0c1183aabcbd847dea743283563e2dfa6ef4dab4ceebf878e',
        '72fb64851018188caad8af4993c177b25b119219e5b240cf8b90f47322e68754',
        'dc200cfae0057ec1a1e9599c74d150e87ba162a93c860cfc9da6926a719b95f3',
        '478bb4830a9753b788965c2e028eeac8b37dfeeebd7c14941f80805f78df729b',
        '809c7f513375c9d3217816cddaa5b644a476e679b76f25af4f87114f59bba2cd',
        'a3fb7531a6dfb7217d1cae90a05c959c9c983432c68292f127b4a62e2426f96c',
        'e4b9d0ba87d2b618040186fb210a69055b9c12b8a5c50f816b255fb1e5020761',
        'caf92a6d0e1c47cd7549d123be106a1f58800365e9d206bf58425835683c61b1',
        'b6dc69331afcbb418db8a447efe777b611ddc9c4405957c9d768a61cfc1044bb',
        'edd05919a201bfd89cb803bf8b4781529839781e74d50986f07327d7ae74f962',
        'd556a7642d8fae189b868e627e92ceb19807c4d790f82567103998503363e6c4',
        'e816477fc69cb5fb04102dff8d81de60e6dd371ccb9e35e44f5fc9a4ec66e3b5',
        'f36d0296d3f99e84c11763ec30c7c9ec89036c6b4974f6e089d61d4263453244',
        'ff2615f38ac3fc45e6217c286a0c6beb92d175711ae717d642da31995b05abcf',
        'cf2469185d969f9bba97e4850498109592ec449a63fa622791d7727e1a3e4823',
        '5e1e01de436c345c84a5fdf0d6e73721dddd9156ce2cbf343a68544095df58b9',
        '0583cf494660c48023d72cbcfba2d03717abc4fadeb6975f6520178b5df7d492',
        '875eabd6c1392e872f2893432fdb6460f6134c0bda7b489d0c141d316aefb6a4',
        'f10477a574322d4ac9342a5c750dda8a933f34d80e1ac5aa628fd182829e9a2f',
        'b0abecc8ffdc05797a1b89681738078663559cefaa22259d5140cdc0b07b1b07',
        'dbe1cd10e824c3014f7e7774bcad4b870f70159f46f4faf30406d73ded4de9f1',
        'd4c8b234f379b6e74393ad04c8c19712447ecc0d0f8114d80552631e7a7867f1',
        '40f02ffddc1dbef8c8909a7abdf98c20c6a4364a258a588715d4da339ddba475',
        '5d8b6841860f838168109386522d8e62fbab62851c3433515e52e915dd7560ca',
        '9f25880691d02c0ecb9dbc746928dafe8aa18d13fb516909e3551b87131cce3a',
        'd43c33db0a8afe1a528f32f5cae536196c077ca7dbf44ba6ea6c0def1de4b3ed',
        '023daefe047a7559498722316307290942c144f4d57f24dc8f52e9530b6d4506',
        '23b368e4c6865386641b5ecd3e3fb5f8c50a5e917e6f89c5df16acd414085f20',
        'be7214637f58979cbf96aeb2a6807488cdcdd4bd3f9513e314f6baeb481f6892',
        '3a79892d53dfa8b0eeb83e0a1fb72efeb0757653fdfaff9a4c6132ca164f346d',
        '4453182c65bf48f45778bbfe6ca0d1e2ae04210044e3153cf9636b7e2c43f562',
        '2dc8318afd7d385797826d699421da48d235ef776a27a438d9f3a8c92ed681bc',
        'cce597bf98534f746ee21a8938013a5aae9e2f02c977ebc78e364ccef5777496',
        'f6fefcfaa8d4aa54e17f6f6afd3c7e6bbfe1c3699786ff194ae9eebc9c09eebb'
    ]
    return hexnumbers

def convertHexNumToBin(r,num):
    #Μετατροπή ενός δεκαεξαδικού αριθμού σε δυαδικό. Η παράμετρος num καθορίζει ότι αν είναι 1 τότε
    #για κάθε δεκαεξαδικό ψηφίο θα έχουμε 4 δυαδικά ψηφία για την αναπάραστασή του. 
    # Έτσι όταν η num είναι 1 το δεκαεξαδικό ψηφίο 3 θα είναι το 0011 (στο δυαδικό), ενώ διαφορετικά θα είναι το 11 (στο δυαδικό)
    str=''
    for n in r:
        intNum=int(n,16)
        binStr=bin(intNum)[2:]
        if num==1:
            binStr=binStr.zfill(4)
        str +=binStr
    return str


def convertHexListToBinList(hexList,num):
    #Δέχεται μια λίστα με δεκαεξαδικούς αριθμούς (σε μορφή string) και επιστρέφει μια λίστα με τους αντίστοιχους
    #δυαδικούς τους. Η μετατροπή του δεκαεξαδικού σε δυαδικό γίνεται ανάλογα με την παράμετρο num.
    strlist=[]
    for hexNum in hexList:
        strBin=convertHexNumToBin(hexNum,num)
        strlist.append(strBin)
    return strlist
    


def find_max(list,digit):
    # H συνάρτηση δέχεται μια λίστα με δυαδικούς αριθμούς και βρίσκει την μεγαλύτερη ακολουθία με συνεχόμμενα 
    # ψηφία 0 ή 1 ανάλογα με την παράμετρο digit.
    maxi=-1
    for hex in list:
        s=0
        for x in hex:
            if x==digit:
                s+=1
            else:
                if s>maxi:
                    maxi=s
                s=0
        if x==digit:
            if s>maxi:
                maxi=s
    return maxi


# main program
randomness=createListOfNums() # Δημιουργία της λίστας με τους δεκαεξαδικούς αριθμούς
stringRandom4digit=convertHexListToBinList(randomness,1) #Λίστα με τους αντίστοιχους δυαδικούς αριθμούς 
                                                            #(4 ψηφία για κάθε ένα δεκαεξαδικό ψηφίο)
stringRandom=convertHexListToBinList(randomness,2)

print('Σε περίπτωση που για κάθε δεκαεξαδικό ψηφίο χρησιμοποιούμε 4bit για την αναπαράσταση του σε δυαδικό:')
print('Το μήκος της μέγιστης ακολουθίας με συνεχόμενα 1 είναι: ', find_max(stringRandom4digit,'1'))
print('Το μήκος της μέγιστης ακολουθίας με συνεχόμενα 0 είναι: ', find_max(stringRandom4digit,'0'))
print('')
print('Αλλιώς')
print('Το μήκος της μέγιστης ακολουθίας με συνεχόμενα 1 είναι: ', find_max(stringRandom,'1'))
print('Το μήκος της μέγιστης ακολουθίας με συνεχόμενα 0 είναι: ', find_max(stringRandom,'0'))