from random import*

## Initialisation
tour=0
couleurs_affiché='Couleurs: J (jaune), B (Bleu), R (Rouge), V (Vert), W (Blanc), N (Noir)'

## Menu du jeu
def menu():
    '''
    Sortie: list, contient le nombre de couleur à deviné et le nombre de tour ainsi que l'informarion du nombre
    de joueur
    '''
    arg=[4, 12]
    auto_mode=False
    print('Mode auto : 0')
    print("Jouer Seul : 1")
    print("Jouer à deux : 2")
    print("Menu des Options : 3")
    seul=int(input("Valeur : "))
    print('')
    if seul==0:
        auto_mode=True
        seul+=1
    if seul==3:
        arg=options()
        return arg
    else:
        arg.append(seul)
        arg.append(auto_mode)
        return arg

def options():
    '''
    Sortie: list, contient le nombre de couleur à deviné et le nombre de tour ainsi que l'informarion du nombre
    de joueur
    '''
    print("Par défaut : 0")
    nb_pions=int(input("Nombre de Pions : "))
    nb_tours=int(input("Nombre de Tours : "))
    if nb_pions==0:
        nb_pions=4
    if nb_tours==0:
        nb_tours=12
    seul=int(input("Jouer Seul : 1 ; à deux joueurs : 2 : "))
    print()
    return [nb_pions, nb_tours, seul, False]

## Mise en place
def creation(seul, pions):
    '''
    seul: int, 1 ou 2 correspondant au nombre de joueur
    pions: int, nombre correspondant au nombre de couleur à deviner
    Sortie: tuple, contient des str correspondant aux couleurs à deviner
    '''
    combinaison=[]
    if seul==1:
        clefs=['J', 'B', 'R', 'V', 'W', 'N']
        for case in range(pions):
            combinaison.append(clefs[randint(0, len(clefs)-1)])
    else:
        print(couleurs_affiché)
        print()
        couleur=str(input(f"Combinaison de {pions} couleurs à deviner : "))
        combinaison=valable(couleur)
        for loop in range(35):
            print()
    return tuple(combinaison)

def valable(majuscule):
    '''
    majuscule: str,
    Sortie: list, contient des str correspondant aux couleurs à deviner après avoir été éventuellement mise en majuscule
    '''
    resultat=[]
    maj=(66, 74, 78, 82, 86, 87)
    minu=(98, 106, 110, 114, 118, 119)
    for i, element in enumerate(majuscule):
        while ord(element) not in minu and ord(element) not in maj:
              element=str(input(f"Couleur {i+1} inéxistante ! : "))
        if ord(element) in maj:
            resultat.append(element)
        elif ord(element) in minu:
            resultat.append(chr(ord(element)-32))
    return resultat

## Jeu (Variante)
def proposition(pions):
    '''
    pions: int, nombre correspondant au nombre de couleur à deviner
    Sortie: tuple , contient des str correspondant à differentes couleurs après avoir été éventuellement
    mise en majuscule
    '''
    prop=[]
    print(couleurs_affiché)
    print(f'tour : {tour+1}')
    couleur=str(input(f"Proposez une combinaison de {pions} pions : "))
    prop=valable(couleur)
    return tuple(prop)

def verification(prop, combinaison):
    '''
    prop: tuple, contient des str correspondant à des couleurs
    combinaison: tuple, contient des str correspondant à des couleurs
    Sortie: list, renvoie des entiers correspondant aux bonnes ou mauvaises positions de couleurs
    '''
    vérif=[0, 0, []]
    dict_image = {'J':0, 'B':0, 'R':0, 'V':0, 'W':0, 'N':0}
    for elt in combinaison:
        dict_image[elt] += 1
    for i, elem in enumerate(prop):
        if elem == combinaison[i]:
            vérif[0] += 1
            vérif[2].append(i)
            dict_image[elem] -= 1
    for i, elem in enumerate(prop):
        if dict_image[elem] != 0 and i not in vérif[2]:
            vérif[1]+=1
            dict_image[elem] -= 1
    return vérif

def gagne(verif):
    '''
    verif: list, entiers correspondant aux bonnes ou mauvaises positions de couleurs
    Sortie: Bool, renvoie True si la longueur de la combinaison correspond aux nombre de bonne position de prop
    '''
    if vérif[0]==len(combinaison):
        return True
    else:
        return False

## Affichage
def affichage(prop):
    '''
    prop: tuple, contient des str correspondant à des couleurs
    Sortie: None, print dans la console les differentes propositions
    '''
    cases=[prop]
    largeur = len(cases[0])
    print("  ", end="")
    for i in range(1, largeur+1):
        num = str(i)
        k = True
    print()

    print("   "+"_"*(largeur*(6)-1))
    for ligne in cases:
        print("  |"+(" "*5+"|")*largeur, f' Bonne position    : {vérif[0]}')
        print("  |", end="")
        for carac in ligne:
            k = True
            while len(carac) < 3:
                if k:
                    carac = " " + carac
                else:
                    carac = carac + " "
                k = not(k)
            print(" "+carac+" |", end="")
        print()
        print("  |"+("_"*(5)+"|")*largeur, f' Mauvaise position : {vérif[1]}')
    print()
    print()

##Auto-mode et Main
def auto(prop, verif, tour):
    '''
    prop: tuple, contient des str correspondant à des couleurs
    verif: list, entiers correspondant aux bonnes ou mauvaises positions de couleurs
    tour: int, numéro du tour en cours
    '''
    table_couleurs=['J', 'B', 'R', 'V', 'W', 'N']
    if tour==0:
        return ['J', 'J', 'J', 'J']
    elif tour<5 and (verif[0]+verif[1])<2:
        return ['J', 'J', table_couleurs[tour], table_couleurs[tour]]
    elif (verif[0]+verif[1])==3:
        return [table_couleurs[randint(1, 5)], 'J', prop[2], prop[3]]
    elif (verif[0]+verif[1])==4:
        if verif[1]==3:
            return [prop[3], prop[2], prop[1], prop[0]]
        if verif[1]==4:
            i_prop=[]
            while len(i_prop)!=len(prop):
                i_elem=randint(0, 4)
                while i_elem in i_prop:
                    i_elem=randint(0, 4)
                i_prop.append(i_elem)
            return [prop[i_prop[0]], prop[i_prop[1]], prop[i_prop[2]], prop[i_prop[3]]]
        if verif[0]==3:
            return [prop[0], prop[2], prop[3], prop[1]]
        else:
            return[prop[0], prop[2], prop[1], prop[3]]
    elif verif[0]==2:
        return [table_couleurs[randint(0, 5)], table_couleurs[randint(0, 5)], prop[2], prop[3]]
    else:
        return [table_couleurs[randint(0, 5)], table_couleurs[randint(0, 5)], table_couleurs[randint(0, 5)], table_couleurs[randint(0, 5)]]

if __name__ == '__main__':
    fin=False
    arg=menu()
    prop=[]
    vérif=[]
    combinaison=creation(arg[2], arg[0])
    print()
    print()
    while not fin and arg[1]!=tour:
        if arg[3]:
            prop=auto(prop, vérif, tour)
        else:
            prop=proposition(arg[0])
        vérif=verification(prop, combinaison)
        affichage(prop)
        fin=gagne(vérif)
        tour+=1
    if fin==False:
        print(f'Dommage nombre de tour épuisé ! La combinaison était {combinaison}')
    else:
        print(f'Bravo Vous avez deviné la combinaison en {tour} tours !')