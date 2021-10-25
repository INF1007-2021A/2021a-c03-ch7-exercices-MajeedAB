#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import turtle as t
from exercice_ancien import frequence
import random

# TODO: Définissez vos fonction ici
def volume_masse_ellipsoide(a,b,c):
    return 4/3*math.pi*a*b*c

def tri(phrase):
    lettres = frequence(phrase)
    return sorted(lettres,key = lambda cle:lettres[cle], reverse=True)[0]

def fractale(niv=0,taille=0,angle=0):
    coef = 2/3
    if(niv==0):
        return None
    t.down()
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.forward(taille)
    t.left(angle)
    fractale(niv-1,taille*coef,angle)
    t.right(2*angle)
    fractale(niv-1,taille*coef,angle)
    t.left(angle)
    t.backward(taille)

def sequence_valide(sequence):
    if(type(sequence)==type("")):
        if(len(sequence)!=0):
            for i in sequence:
                if not i in "atgc": #des qu'il y a un caractere invalide, la sequence est invalide
                    return False
            #si on est passé a travers toute la sequence
            # et on a rencontré que des atcg, elle est valide
            return True
    return False

def saisir_chaine():
    while(True):
        chaine = input("chaine: ")
        if sequence_valide(chaine):
            break
        else:
            print("chaine invalide!")
    return chaine

def saisir_seq():
    while(True):
        sequence = input("sequence: ")
        if sequence_valide(sequence):
            break
        else:
            print("sequence invalide!")
    return sequence

def proportion(chaine,sequence):
    cpt = chaine.count(sequence)*len(sequence)/len(chaine)*100
    return cpt

def draw_fractales():
    t.speed(0)
    # print(t.color())
    t.colormode(255)
    t.up()
    for i in range(4):
        t.left(90)
        fractale(6,100,40)
    while(True):
        pass

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print("volume ellipsoide : ",volume_masse_ellipsoide(1,1,1))
    print("lettre max:   ",tri("abbbbbbbbbbbbbbbbhuejnwsajknedw"))

    # draw_fractales()
    chaine = saisir_chaine()
    seq = saisir_seq()
    print("Il y a "+str(proportion(chaine,seq))+'%'+" de "+str(seq))