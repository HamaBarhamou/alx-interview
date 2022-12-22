#!/usr/bin/python3


def pascal_triangle(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    elif n == 3:
        return [[1], [1, 1], [1, 2, 1]]
    else:
        liste = [[1], [1, 1], [1, 2, 1]]
        for __ in range(4, n+1, 1):
            endliste = liste[len(liste) - 1]
            new_liste = [1]
            for i in range(1, len(endliste), 1):
                new_liste.append(endliste[i-1] + endliste[i])
            new_liste.append(1)
            liste.append(new_liste)
        return liste
