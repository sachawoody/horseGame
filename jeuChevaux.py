########PGM PRINCIPAL !!

###Afficher les règles du jeu à base de print !



def Jeu() :

    

    #Initialisation des variables

    liste_position1=[]

    liste_position2=[]

    liste_chevaux_ecuries=[]

    liste_murs = []

    joueur_actif = 0

    Couleurs = ["Rouge", "Jaune", "Bleu", "Vert"]

    #Listes positions

    listePosR=[[0,0],[0,0],[0,0],[0,0]]

    listePosJ=[[0,0],[0,0],[0,0],[0,0]]

    listePosB=[[0,0],[0,0],[0,0],[0,0]]

    listePosV=[[0,0],[0,0],[0,0],[0,0]]

    listePos=[listePosR,listePosJ,listePosB,listePosV]

    #Liste chevaux

    listeR=["R1","R2","R3","R4"]

    listeJ=["J1","J2","J3","J4"]

    listeB=["B1","B2","B3","B4"]

    listeV=["V1","V2","V3","V4"]

    listeJoueurs=[listeR,listeJ,listeB,listeV]

    #Compteurs chevaux

    liste_Compteurs=[4,4,4,4]

    #Ecuries

    liste_positions_ecuries=[5,11,17,23]

    #Cases secu

    liste_secu = [2,8,14,20]

    #Compteur points

    compteurVal=[0,0,0,0]

    

    

    #Création du Plateau

    nombre_joueurs = nb_joueurs()

    creation_listeP1(liste_position1,liste_position2, nombre_joueurs)

    noms_joueurs = presentation_joueurs(nombre_joueurs)

    

    #Affichage de début 

    print("Plateau \n", liste_position1,"\n", liste_position2)

    for i in range(nombre_joueurs) : 

        print(noms_joueurs[i], "Joue avec les chevaux", Couleurs[i]+"s")

        

    input("Cliquez sur entrée pour continuer\n")

    

    

    while 4 not in compteurVal:

        tour_joueur(joueur_actif,nombre_joueurs, liste_position1, liste_position2, liste_Compteurs, compteurVal, noms_joueurs, liste_positions_ecuries, Couleurs, listeJoueurs, listePos, liste_murs, liste_secu, compteurVal)

        joueur_actif = (joueur_actif+1)%nombre_joueurs

        input("\nAppuyez sur entrée pour continuer\n")

        

    fin_du_jeu(compteurVal, noms_joueurs)





    

    

####Tour joueur :

def tour_joueur(joueur_actif, nombre_joueurs, liste_position1, liste_position2, liste_Compteurs, compteurVal, noms_joueurs, liste_positions_ecuries, Couleurs, listeJoueurs, listePos, liste_murs, liste_secu, listeVal):

    de=lancer_de()

    print("")

    print("~~~~~~C'est à",noms_joueurs[joueur_actif]," de jouer !~~~~~~")

    print("")

    print("La valeur du dé est :",de,"!")

    print("")

    

    

    #Cas ou le joueur a des chevaux en ecurie et sur le plateau, et qu'il a la place de sortir un cheval

    if de == 6 and liste_Compteurs[joueur_actif] > 0 and liste_Compteurs[joueur_actif]<4 and (liste_position2[liste_positions_ecuries[joueur_actif]]== "_ " or (liste_position1[liste_positions_ecuries[joueur_actif]][0] != Couleurs[joueur_actif][0] or liste_position2[liste_positions_ecuries[joueur_actif]][0] != Couleurs[joueur_actif][0])) :

        print("Tapez \n1 pour sortir un cheval\n2 pour avancer un cheval\n3 pour passer votre tour")

        choix = input("-> ")

        while choix not in ["1", "2", "3"] :

            choix = input("Cette réponse n'est pas valide.\nTapez \n1 pour sortir un cheval\n2 pour avancer un cheval\n3 pour passer votre tour\n-> ")

        choix = int(choix)

        

        if choix == 1 :

            if liste_position2[liste_positions_ecuries[joueur_actif]]== "_ " :

                sortir_cheval(joueur_actif, liste_position1, liste_position2, liste_positions_ecuries, liste_Compteurs, Couleurs, listeJoueurs, listePos, liste_murs)

            else :

                sortir_en_mangeant(joueur_actif, liste_position1, liste_position2, liste_positions_ecuries, liste_Compteurs, Couleurs, listeJoueurs, listePos, liste_murs)

        elif choix == 2 :

            avancer_cheval(de, joueur_actif, liste_position1, liste_position2, liste_positions_ecuries, liste_Compteurs, Couleurs, listeJoueurs, listePos, liste_murs, liste_secu, compteurVal)

            

    #Cas ou le joueur a des chevaux en ecurie mais pas sur le plateau (tous les chevaux ont soit gagné soit pas sortis) et qu'il a la place de sortir un cheval

    elif de == 6 and liste_Compteurs[joueur_actif] > 0 and liste_Compteurs[joueur_actif]+compteurVal[joueur_actif] == 4 and liste_position2[liste_positions_ecuries[joueur_actif]] == "_ " : 

        print("Tapez \n1 pour sortir un cheval\n2 pour passer votre tour")

        choix = input("-> ")



        while choix not in ["1", "2"] :

            choix = input("Cette réponse n'est pas valide.\nTapez \n1 pour sortir un cheval\n2 pour passer votre tour\n-> ")

        choix = int(choix)

        

        if choix == 1 :

            sortir_cheval(joueur_actif, liste_position1, liste_position2, liste_positions_ecuries, liste_Compteurs, Couleurs, listeJoueurs, listePos, liste_murs)

            

    #Cas ou le joueur a pas de chevaux sur le plateau et ne fais pas de 6 

    elif de != 6 and liste_Compteurs[joueur_actif]+compteurVal[joueur_actif] == 4 :

        print("Vous ne pouvez pas jouer ce tour...")

        

    #Cas le plus banal, pas un 6 et le joueur a un cheval au moins sur le plateau ou qu'il n'a pas la place de sortir un cheval

    else : 

        print("Tapez\n1 pour avancer un cheval\n2 pour passer votre tour")

        choix = input("->")



        while choix not in ["1", "2"] :

            choix = input("Cette réponse n'est pas valide.\nTapez\n1 pour avancer un cheval\n2 pour passer votre tour\n-> ")

        choix = int(choix)

        

        if choix == 1 :

            avancer_cheval(de, joueur_actif, liste_position1, liste_position2, liste_positions_ecuries, liste_Compteurs, Couleurs, listeJoueurs, listePos, liste_murs, liste_secu, compteurVal)

            

    #Affichage

    print("\nPlateau :")

    print(liste_position1)

    print(liste_position2)

    print("Murs, cases sécurité (S) et écuries :")

    liste_murs_et_ecuries = [" _" for i in range(len(liste_position1))]

    for i in range(len(liste_position1)) :

        if i in liste_murs :

            liste_murs_et_ecuries[i] = "mur"

        elif i in liste_positions_ecuries :

            j = liste_positions_ecuries.index(i)

            liste_murs_et_ecuries[i] = "E"+Couleurs[j][0]

        elif i in liste_secu :

            liste_murs_et_ecuries[i] = "S "

    print(liste_murs_et_ecuries)

    

    print("Rappel positions des écuries :\n",liste_positions_ecuries[:nombre_joueurs])

    print("Rappel positions des cases securité :\n",liste_secu[:nombre_joueurs])

    if liste_murs != [] :

        liste_murs.sort()

        print("Rappel positions des murs :")

        affiche_liste_plus1(liste_murs)

    else :

        print("Il n'y a pas de mur")







## Fonctions

#Création liste position 1 et 2 :

def creation_listeP1(liste_position1, liste_position2, nombre_joueurs):

    for i in range(6*nombre_joueurs):

        liste_position1.append("_ ")

        liste_position2.append("_ ")

        

def presentation_joueurs(nombre_joueurs) :

    liste_noms = []

    for i in range(nombre_joueurs) :

        print("Quel est le nom du joueur",i+1,"?")

        nom = input()

        liste_noms.append(nom)

    return liste_noms







##Sortir un cheval:

def sortir_cheval(joueur_actif, liste_position1, liste_position2, liste_positions_ecuries, liste_Compteurs, Couleurs, listeJoueurs, listePos, liste_murs):

    choix_cheval=input("Quel est le numéro du cheval que vous voulez sortir ?\n")

    



    #Securité, cas ou l'utilisateur entre n'importe quoi ou un cheval déjà sorti

    choix_valide = False 

    while choix_valide == False :

        while choix_cheval not in ["1", "2", "3", "4"] :

            choix_cheval=input("Ce cheval n'existe pas !\nQuel est le numéro du cheval que vous voulez sortir ?\n")

        if listePos[joueur_actif][int(choix_cheval)-1][1] == 0 :

            choix_valide = True

        else : 

            choix_cheval = input("Ce cheval a déjà été sorti !\nQuel est le numéro du cheval que vous voulez sortir?\n")

    

    

    num_cheval = int(choix_cheval) - 1 #On decale pcq le premier indice d'une liste est 0

    

    if liste_position1[liste_positions_ecuries[joueur_actif]] == "_ " :  #Si la case est vide sur liste 1

        liste_position1[liste_positions_ecuries[joueur_actif]] = listeJoueurs[joueur_actif][num_cheval] 

        listePos[joueur_actif][num_cheval][0] = liste_positions_ecuries[joueur_actif] #Met a jour case 

        listePos[joueur_actif][num_cheval][1] = 1 #Met a jour plateau

    else :  #Sinon, elle l'est nécessairement sur liste 2, deux options se présentent, on s'ajoute ou on mange

        if liste_position1[liste_positions_ecuries[joueur_actif]][0] == Couleurs[joueur_actif][0] : #si meme couleur :

            liste_position2[liste_positions_ecuries[joueur_actif]] = listeJoueurs[joueur_actif][num_cheval]

            listePos[joueur_actif][num_cheval][0] = liste_positions_ecuries[joueur_actif]

            listePos[joueur_actif][num_cheval][1] = 2

            liste_murs.append(liste_positions_ecuries[joueur_actif])

        else : #Sinon, le cheval sur le plateau 1 est d'une autre couleur, on mange :

            cheval_a_manger = liste_position1[liste_positions_ecuries[joueur_actif]]

            if cheval_a_manger[0] == "R" :

                num_proprietaire = 0

            elif cheval_a_manger[0] == "J" :

                num_proprietaire = 1

            elif cheval_a_manger[0] == "B" :

                num_proprietaire = 2

            else :

                num_proprietaire = 3

            listePos[num_proprietaire][int(cheval_a_manger[1])-1][0] = liste_positions_ecuries[num_proprietaire]

            listePos[num_proprietaire][int(cheval_a_manger[1])-1][1] = 0

            liste_Compteurs[num_proprietaire] = liste_Compteurs[num_proprietaire] + 1

            print("Le cheval", cheval_a_manger,"a été mangé !")

            liste_position1[liste_positions_ecuries[joueur_actif]] = listeJoueurs[joueur_actif][num_cheval]#On sort le cheval en 1

            listePos[joueur_actif][num_cheval][0] = liste_positions_ecuries[joueur_actif] #Met a jour case 

            listePos[joueur_actif][num_cheval][1] = 1 #Met a jour plateau

                

    

    #Dans les deux cas, on met à jour le compteur

    liste_Compteurs[joueur_actif] = liste_Compteurs[joueur_actif] - 1 

    print("Le compteur de l'écurie est maintenant passé à:",liste_Compteurs[joueur_actif],"!\n")

    

## Sortir en mangeant

def sortir_en_mangeant(joueur_actif, liste_position1, liste_position2, liste_positions_ecuries, liste_Compteurs, Couleurs, listeJoueurs, listePos, liste_murs) :

    """Dans cette fonction, on ne traite que le cas ou le cheval sort sachant que les deux cases devant lui sont prises, mais il y a au moins un des deux chevaux d'une couleur différente"""

    

    #Choix du cheval à sortir

    choix_cheval=input("Quel est le numéro du cheval que vous voulez sortir ?\n")

    

    #Securité, cas ou l'utilisateur entre n'importe quoi ou un cheval déjà sorti

    choix_valide = False 

    while choix_valide == False :

        while choix_cheval not in ["1", "2", "3", "4"] :

            choix_cheval=input("Ce cheval n'existe pas !\nQuel est le numéro du cheval que vous voulez sortir ?\n")

        if listePos[joueur_actif][int(choix_cheval)-1][1] == 0 :

            choix_valide = True

        else : 

            choix_cheval = input("Ce cheval a déjà été sorti !\nQuel est le numéro du cheval que vous voulez sortir?\n")

    

    

    num_cheval = int(choix_cheval) - 1 #On decale pcq le premier indice d'une liste est 0

    

    #Choix du cheval à manger 

    cheval_case_1 = liste_position1[liste_positions_ecuries[joueur_actif]]

    cheval_case_2 = liste_position2[liste_positions_ecuries[joueur_actif]]

    

    #Cas ou les deux chevaux sont de couleurs différentes, on choisit lequel manger

    if cheval_case_1[0] != Couleurs[joueur_actif][0] and cheval_case_2[0] != Couleurs[joueur_actif][0] :

        print("Quel cheval voulez vous manger ?", cheval_case_1,"ou",cheval_case_2)

        cheval_a_manger = input()

        while cheval_a_manger not in [cheval_case_1, cheval_case_2] :

            print("Cette réponse n'est pas valide.\nQuel cheval voulez vous manger ?", cheval_case_1,"ou",cheval_case_2)



    #Cas ou seul le cheval 1 est de couleur différente :

    elif cheval_case_1[0] != Couleurs[joueur_actif][0] :

        cheval_a_manger = cheval_case_1



    #Cas ou seul le cheval 2 est de couleur différente :

    elif cheval_case_1[0] != Couleurs[joueur_actif][0] : 

        cheval_a_manger = cheval_case_2



    #Recherche du propriétaire de cheval a manger 

    if cheval_a_manger[0] == "R" :

        num_proprietaire = 0

    elif cheval_a_manger[0] == "J" :

        num_proprietaire = 1

    elif cheval_a_manger[0] == "B" :

        num_proprietaire = 2

    else :

            num_proprietaire = 3

    #Le cheval se fait manger

    listePos[num_proprietaire][int(cheval_a_manger[1])-1][0] = liste_positions_ecuries[num_proprietaire]

    listePos[num_proprietaire][int(cheval_a_manger[1])-1][1] = 0

    liste_Compteurs[num_proprietaire] = liste_Compteurs[num_proprietaire] + 1

    print("Le cheval", cheval_a_manger,"a été mangé !")

    

    #Cas ou on mange le cheval 1, on sort le cheval en plateau 1

    if cheval_a_manger == cheval_case_1 : 

        liste_position1[liste_positions_ecuries[joueur_actif]] = listeJoueurs[joueur_actif][num_cheval]#On sort le cheval en 1

        listePos[joueur_actif][num_cheval][0] = liste_positions_ecuries[joueur_actif] #Met a jour case 

        listePos[joueur_actif][num_cheval][1] = 1 #Met a jour plateau

    #Cas ou on mange le cheval 2, on sort le cheval en plateau 2

    else :

        liste_position2[liste_positions_ecuries[joueur_actif]] = listeJoueurs[joueur_actif][num_cheval]#On sort le cheval en 1

        listePos[joueur_actif][num_cheval][0] = liste_positions_ecuries[joueur_actif] #Met a jour case 

        listePos[joueur_actif][num_cheval][1] = 2 #Met a jour plateau    

    





    





##Avancer un cheval :

def avancer_cheval(de, joueur_actif, liste_position1, liste_position2, liste_positions_ecuries, liste_Compteurs, Couleurs, listeJoueurs, listePos, liste_murs, liste_secu, compteurVal):

    choix_cheval=input("Quel est le numéro du cheval que vous shouaitez avancer ?\n")

    

    #Securite, le choix est il valide ?

    choix_valide = False 

    while choix_valide == False :

        while choix_cheval not in ["1", "2", "3", "4"] :

            choix_cheval=input("Ce cheval n'existe pas !\nQuel est le numéro du cheval que vous souhaitez avancer ?\n")

        if listePos[joueur_actif][int(choix_cheval)-1][1] in [1,2] :

            choix_valide = True

        else : 

            choix_cheval = input("Ce cheval n'est pas sur le plateau !\nQuel est le numéro du cheval que vous voulez sortir?\n")

            

    num_cheval = int(choix_cheval) - 1

    

    #On cherche la nouvelle case

    anc_case = listePos[joueur_actif][num_cheval][0]

    nouv_case = (listePos[joueur_actif][num_cheval][0]+de)

    

    #On cherche si il y a un mur ou non et si le cheval passe par une écurie 

    Mur_sur_la_route = False 

    liste_cases_traversees = []

    if nouv_case <= len(liste_position1) - 1 :

        for i in range(anc_case + 1, (nouv_case + 1)) :

            liste_cases_traversees.append(i)

            if i in liste_murs :

                Mur_sur_la_route = True

    else : 

        nouv_case = nouv_case%len(liste_position1)

        for i in range(anc_case+1, len(liste_position1)) :

            liste_cases_traversees.append(i)

            if i in liste_murs :

                Mur_sur_la_route = True

        for i in range(0, (nouv_case + 1)) :

            liste_cases_traversees.append(i)

            if i in liste_murs :

                Mur_sur_la_route = True

    

    #Si le cheval passe par son ecurie, on le fait reculer a la place 

    if liste_positions_ecuries[joueur_actif] in liste_cases_traversees :

        recul = nouv_case - liste_positions_ecuries[joueur_actif]

        if recul < 0 : 

            recul = recul + len(liste_position1)

        nouv_case = (liste_positions_ecuries[joueur_actif] - recul)%len(liste_position1)

        

    

    

    # Differents cas possibles Mur ? Superposition ? Manger ? 



    

    #Si il n'y a pas de mur, ou s'il y en a un, que le de est 5 et que le cheval ne tombe pas pile sur le mur : on avance

    if (Mur_sur_la_route == False) or (de == 5 and nouv_case not in liste_murs) : 

        

        #Si la case d'arrivée est vide

        if liste_position1[nouv_case] == "_ " : 

            avancer_sans_manger(liste_position1,liste_position2,num_cheval,joueur_actif,listeJoueurs,nouv_case,anc_case, compteurVal, liste_positions_ecuries, listePos, listeJoueurs, liste_murs)

        

        #Sinon si la case d'arrivée n'est pas vide, mais que le cheval est de la même couleur ou que c'est une case sécurité ou que le cheval est sur son ecurie ET qu'il n'y a qu'un seul cheval

        elif ((liste_position1[nouv_case][0] == Couleurs[joueur_actif][0]) or (nouv_case in liste_secu) or (liste_position1[nouv_case][0] == "R" and nouv_case == liste_positions_ecuries[0]) or (liste_position1[nouv_case][0] == "J" and nouv_case == liste_positions_ecuries[1]) or (liste_position1[nouv_case][0] == "B" and nouv_case == liste_positions_ecuries[2]) or (liste_position1[nouv_case][0] == "V" and nouv_case == liste_positions_ecuries[3])) and liste_position2[nouv_case] == "_ " : 

            superposition_chevaux(anc_case, nouv_case, liste_position1, liste_position2, joueur_actif, Couleurs, num_cheval, compteurVal, listePos, liste_positions_ecuries, liste_murs, listeJoueurs)

        

        #Dernier Cas ou la case n'est pas vide, il y a un unique cheval dessus, de couleur différente, et pas de case sécurité 

        elif liste_position2[nouv_case] == "_ " :

            manger_cheval(anc_case, nouv_case, liste_position1, liste_position2, joueur_actif, Couleurs, num_cheval, compteurVal, listePos, liste_positions_ecuries, liste_murs, liste_Compteurs)

     

        

     #Sinon, cas ou le cheval ne peut pas avancer à cause d'un mur ou parce que les deux cases sont déja prises par deux chevaux de la même couleurs par exemple

    elif (Mur_sur_la_route == True and de!= 5) or (liste_position2[nouv_case]!="_ ") : 

        print("Desole mais ce mouvement n'est pas possible !\nVous passez donc votre tour...")

    

    

        

    

##Manger un cheval :

def manger_cheval(anc_case, nouv_case, liste_position1, liste_position2, joueur_actif, Couleurs, num_cheval, compteurVal, listePos, liste_positions_ecuries, liste_murs, liste_Compteurs):

    """Dans cette fonction, on ne traite que le cas ou le cheval peut avancer et arrive sur une case ou il y a un autre cheval à manger."""

    print("manger cheval")

    cheval_a_bouger = Couleurs[joueur_actif][0] + str(num_cheval+1)

    cheval_a_manger = liste_position1[nouv_case]

    

    #Supression du cheval à l'ancienne case 

    if cheval_a_bouger in liste_position1 :

        liste_position1[anc_case] = "_ "

        if liste_position2[anc_case] != "_ " :

            if liste_position2[anc_case][0] == "R" :

                num_proprietaire = 0

            elif liste_position2[anc_case][0] == "J" :

                num_proprietaire = 1

            elif liste_position2[anc_case][0] == "B" :

                num_proprietaire = 2

            elif liste_position2[anc_case][0] == "V" :

                num_proprietaire = 3

            listePos[num_proprietaire][int(liste_position2[anc_case][1])-1][1] = 1 #On indique qu'on remet le cheval sur le plateau 1

            liste_position1[anc_case]=liste_position2[anc_case]

            liste_position2[anc_case]="_ "

            

    else :

        liste_position2[anc_case] = "_ "



    

    #Mangeage du cheval 

    if cheval_a_manger[0] == "R" :

        num_proprietaire = 0

    elif cheval_a_manger[0] == "J" :

        num_proprietaire = 1

    elif cheval_a_manger[0] == "B" :

        num_proprietaire = 2

    else :

        num_proprietaire = 3

    listePos[num_proprietaire][int(cheval_a_manger[1])-1][0] = liste_positions_ecuries[num_proprietaire]

    listePos[num_proprietaire][int(cheval_a_manger[1])-1][1] = 0

    liste_position1[nouv_case] = "_ "

    liste_Compteurs[num_proprietaire] = liste_Compteurs[num_proprietaire] + 1

    print("Le cheval",cheval_a_manger,"a été mangé !")

    

    #Deplacement du cheval

    liste_position1[nouv_case] = cheval_a_bouger

    listePos[joueur_actif][num_cheval][0] = nouv_case

    listePos[joueur_actif][num_cheval][1] = 1

    

    

    #Cas ou le cheval est arrivé au bout et a gagné

    if nouv_case == liste_positions_ecuries[joueur_actif] :

        print("Le cheval est revenu à son écurie !")

        compteurVal[joueur_actif] = compteurVal[joueur_actif] + 1 

        print("Vous avez", compteurVal[joueur_actif], "points !")

        listePos[joueur_actif][num_cheval][1] = 3 #3 signifie que le cheval a gagné

        liste_position1[nouv_case] = "_ "



    #Cas ou on a cassé un mur 

    if liste_position2[nouv_case] == "_ " and nouv_case in liste_murs :

        liste_murs.remove(nouv_case)

    if liste_position2[anc_case] == "_ " and anc_case in liste_murs:

        liste_murs.remove(anc_case)

    

    

    

##Avancer_sans_manger :

def avancer_sans_manger(liste_position1,liste_position2,num_cheval,joueur_actif,listJoueur,nouv_case,anc_case, compteurVal, liste_positions_ecuries, listePos, listeJoueurs, liste_murs) :

    """Dans cette fonction, on ne traite que le cas ou le cheval peut avancer librement et arrive sur une case vide"""

    print("Avancer_sans_manger")

    

    

    if liste_position1[anc_case] == listeJoueurs[joueur_actif][num_cheval]:

        liste_position1[nouv_case]=listeJoueurs[joueur_actif][num_cheval]

        liste_position1[anc_case]="_ "

        if liste_position2[anc_case] !="_ ":

            if liste_position2[anc_case][0] == "R" :

                num_proprietaire = 0

            elif liste_position2[anc_case][0] == "J" :

                num_proprietaire = 1

            elif liste_position2[anc_case][0] == "B" :

                num_proprietaire = 2

            elif liste_position2[anc_case][0] == "V" :

                num_proprietaire = 3

            listePos[num_proprietaire][int(liste_position2[anc_case][1])-1][1] = 1 #On indique qu'on remet le cheval sur le plateau 1

            liste_position1[anc_case]=liste_position2[anc_case]

            liste_position2[anc_case]="_ "

            

    

    elif liste_position2[anc_case]== listeJoueurs[joueur_actif][num_cheval]:

        liste_position1[nouv_case]=listeJoueurs[joueur_actif][num_cheval]

        liste_position2[anc_case]="_ "



    

    listePos[joueur_actif][num_cheval][0] = nouv_case

    listePos[joueur_actif][num_cheval][1] = 1

    

    #Cas ou le cheval est arrivé au bout et a gagné

    if nouv_case == liste_positions_ecuries[joueur_actif] :

        print("Le cheval est revenu à son écurie !")

        compteurVal[joueur_actif] = compteurVal[joueur_actif] + 1 

        print("Vous avez", compteurVal[joueur_actif], "points !")

        listePos[joueur_actif][num_cheval][1] = 3 #3 signifie que le cheval a gagné

        liste_position1[nouv_case] = "_ "



    #Cas ou on a cassé un mur 

    if liste_position2[nouv_case] == "_ " and nouv_case in liste_murs :

        liste_murs.remove(nouv_case)

    if liste_position2[anc_case] == "_ " and anc_case in liste_murs:

        liste_murs.remove(anc_case)

    

##Superposer : 

def superposition_chevaux(anc_case, nouv_case, liste_position1, liste_position2, joueur_actif, Couleurs, num_cheval, compteurVal, listePos, liste_positions_ecuries, liste_murs, listeJoueurs) :

    """Dans cette fonction, on ne traite que le cas ou le cheval arrive sur une case déjà occupée par un unique cheval mais ne peut pas le manger. Il se place donc sur la case équivalente du deuxième plateau"""

    print("Superposition chevaux")

    cheval_a_bouger = listeJoueurs[joueur_actif][num_cheval]

    if cheval_a_bouger in liste_position1 :

        liste_position1[anc_case] = liste_position2[anc_case]

        liste_position2[anc_case] = "_ "

        

    else : 

        liste_position2[anc_case] = "_ "

        

    

    liste_position2[nouv_case] = cheval_a_bouger  

    listePos[joueur_actif][num_cheval][0] = nouv_case  #On met a jour la case

    listePos[joueur_actif][num_cheval][1] = 2  #On met a jour le plateau 

    liste_murs.append(nouv_case) #La nouvelle case devient un mur 

    

    #Cas ou le cheval est arrivé au bout et a gagné

    if nouv_case == liste_positions_ecuries[joueur_actif] :

        print("Le cheval est revenu à son écurie !")

        compteurVal[joueur_actif] = compteurVal[joueur_actif] + 1 

        print("Vous avez", compteurVal[joueur_actif], "points !")

        listePos[joueur_actif][num_cheval][1] = 3 #3 signifie que le cheval a gagné

        liste_position2[nouv_case] = "_ "

        

    #Cas très particulier ou le cheval revient à sa propre position par rebond

    if liste_position1[nouv_case] == "_ " :

        liste_position1[nouv_case] = liste_position2[nouv_case]

        liste_position2[nouv_case] = "_ "

    

    

    #Cas ou on a cassé un mur 

    if liste_position2[nouv_case] == "_ " and nouv_case in liste_murs :

        liste_murs.remove(nouv_case)

    if liste_position2[anc_case] == "_ " and anc_case in liste_murs:

        liste_murs.remove(anc_case)

    

        

    



    

##Fin du Jeu 

def fin_du_jeu(compteurVal, noms_joueurs) :

    i = 0

    while compteurVal[i] < 4 : 

        i = i+1

    

    print("Bravo au joueur", i+1, noms_joueurs[i],"!")

    print("Tu as gagné la partie !")







###Lancé le dé :

import random

def lancer_de():

    de = random.randint(1,6)

    return de



###Nombre de joueurs

def nb_joueurs():

    nombreDeJoueurs=input("Combien y a-t-il de joueurs ?\n")

    while nombreDeJoueurs not in ["1","2","3","4"] :

        nombreDeJoueurs = input("Cette réponse n'est pas valide.\nCombien y a-t-il de joueurs ?\n")

    return int(nombreDeJoueurs)

###Qui joue ?

def qui_joue():

    quiJoue=int(input("Quel joueur joue ?"))

    return quiJoue

    

##Affiche listes +1 

def affiche_liste_plus1(Liste) :

    """Cette fonction affiche tous les éléments d'une liste Plus 1"""

    Liste_plus1 = []

    for i in Liste :

        Liste_plus1.append(i+1)

    print(Liste_plus1)











Jeu()