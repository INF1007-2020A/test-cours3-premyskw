#!/usr/bin/env python
# -*- coding: utf-8 -*-

def majuscule(mot):
    resultat = ''
    for char in mot:
        if ord(char) >=65:
            resultat += chr(ord(char)-32)
    return resultat

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre',
        'yolo'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
