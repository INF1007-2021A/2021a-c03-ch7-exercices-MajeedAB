#!/usr/bin/env python
# -*- coding: utf-8 -*-
import statistics

def order(values: list = None) -> list:
    if values is None:
        values = []
        # TODO: demander les valeurs ici
        for i in range(10):
            values.append(float(input("Valeur "+str(i)+"\n")))
    # print(values)
    values.sort()
    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        words = []
        words.append(input("premier mot"+"\n"))
        words.append(input("deuxieme mot"+"\n"))
    for lettre in words[0]:
        if (lettre in words[1]):
            words[1] = words[1].replace(lettre,'',1)
        else: #la lettre n'est pas dans l'autre mot, donc pas des anagrames
            print("Pas des anagrames!")
            return False
    #fini de parcourir mot 1:
    if(words[1]==""): #il ne reste plus de lettres dans le 2e mot, donc reelement des anagrames
        print("OUI, anagrames!")
        return True
    else: #il y a plus de lettres dans le 2e mot
        print("Pas des anagrames!")
        return False


def contains_doubles(items: list) -> bool:
    ensemble = {item for item in items}
    return not len(ensemble)==len(items) #si len sont egaux alors uniques, donc ne contient PAS de doublons


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne

    # best = {}
    # best_av = 0
    # best_av_person = ""
    # for name in student_grades:
    #     av = 0
    #     for grade in student_grades[name]:
    #         av += grade
    #     av/=len(student_grades[name])
    #     if(av>=best_av):
    #         best_av = av
    #         best_av_person = name
    # best = {best_av_person:best_av}
    # return best

    # print("\n----\n")
    # print(student_grades)
    # print(student_grades.items())
    # print( sorted(student_grades.items(),key = lambda x: statistics.mean(x[1])) )
    # print("\n----\n")

    return {sorted(student_grades.items(),key = lambda x: statistics.mean(x[1]))[0][0]:student_grades[sorted(student_grades.items(),key = lambda x: statistics.mean(x[1]))[0][0]]}
    return None


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    lettres_frequentes = {}
    for lettre in sentence:
        # if(sentence.count(lettre)>5):
        lettres_frequentes[lettre]=sentence.count(lettre)
    
    lettres_ordonnees = dict(sorted(lettres_frequentes.items(),key= lambda x:-x[1]))
    # for lettre in lettres_ordonnees:
    #     print(lettre,"apparait ",lettres_ordonnees[lettre],"fois")
    # print(lettres_ordonnees)
    return lettres_ordonnees

recipes = {}
def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom = input("nom de la recette:\n")
    nb = int(input("combien d'ingredients?\n"))
    recipes[nom]=[]
    for i in range(nb):
        recipes[nom].append(input("Ingredient:\n"))


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = input("quel recette cherche-tu?\n")
    if(not nom in recipes):
        print("on n'a pas cette recette")
    else:
        print("La recette de",nom,"a pour ingredients:")
        for ing in recipes[nom]:
            print(ing)


def main() -> None:
    # print(f"On essaie d'ordonner les valeurs...")
    # print(order())

    # print(f"On vérifie les anagrammes...")
    # anagrams()

    # my_list = [3, 3, 5, 6, 1, 1]
    # print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    # sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    # frequence(sentence)

    # print("On enregistre les recettes...")
    # recipes = get_recipes()

    # print("On affiche une recette au choix...")
    # print_recipe(recipes)


if __name__ == '__main__':
    main()
