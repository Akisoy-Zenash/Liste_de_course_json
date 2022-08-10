import json
import os

chemin_fichier = "C:/Users/stell/Desktop/Python/script/liste_de_course.json"



COURSE = []

CHOIX = """Choissisez parmi les 5 options suivantes :
    1: Ajouter un élément à la liste de course
    2: Retirer un élément de la liste de course
    3: Afficher les éléments de la liste de course
    4: Vider la liste de course
    5: Quitter le programme"""
OUI = ["1", "2", "3", "4", "5"]
while True:
    with open(chemin_fichier, "r") as fichier :
        COURSE = json.load(fichier)

    print(CHOIX)
    entrer = input("Votre choix : ")
    if entrer not in OUI:
        print("Veuiller choisir une option valide...")
        continue
    else:
        entrer = int(entrer)
        if entrer == 1 :
            ajoute = input("Que voulez-vous ajouter ? : ")
            COURSE.append(ajoute)
            print(f"{ajoute} à bien été ajouter a votre liste")
            with open(chemin_fichier, "w") as fichier :
                json.dump(COURSE, fichier, indent=4)
        elif entrer == 2 :
            retire = input("Que voulez-vous retirer ? : ")
            if retire in COURSE :
                COURSE.remove(retire)
                print(f"{retire} à bien été supprimé de la liste")
                with open(chemin_fichier, "w") as fichier :
                    json.dump(COURSE, fichier, indent=4)
            else:
                print(f"{retire} n'est pas dans la liste")
        elif entrer == 3 :
            if COURSE == []:
                print("Votre liste ne contien aucun element")
            else :
                print("voici le contenu de la liste :")
                for i in COURSE:
                    print(COURSE.index(i) +1, end=' ')
                    print(" ",i)
        elif entrer == 4 :
            COURSE.clear()
            print("votre liste a bien été vider !")
            with open(chemin_fichier, "w") as fichier :
                json.dump(COURSE, fichier, indent=4)
        elif entrer == 5 :
            print("A Bientôt !")
            with open(chemin_fichier, "w") as fichier:
                json.dump(COURSE, fichier, indent = 4)
            break
    print("-"*50)
