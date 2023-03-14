'''1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
teren
- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
de rezerva
- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
variabilelor voastre)
Daca jucatorul pe care vrem sa il schimbam nu e in teren:
- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Altfel, afisati ecran: ‘mai aveti z schimbari’
Google search hint: “how to check if item is in list python”'''
lista_jucatori_teren = ["Ionel", "Costel", "Dan", "Andrei", "Marius"]
lista_jucatori_rezerva = ["Vlad", "Robert", "Andrei", "Ion", "Tudor"]
lista_jucatori_scosi = []
schimbari_efectuate = -3
SCHIMBARI_MAX = 3
jucator_scos = "Ionel"
jucator_intrat = "Vlad"
nr_schimbari_ramase = SCHIMBARI_MAX - abs(schimbari_efectuate)
if jucator_scos in lista_jucatori_teren:
    if nr_schimbari_ramase > 0:
        if jucator_intrat in lista_jucatori_rezerva and jucator_intrat not in lista_jucatori_teren:
            lista_jucatori_teren.remove(jucator_scos)
            lista_jucatori_scosi.append(jucator_scos)
            lista_jucatori_rezerva.remove(jucator_intrat)
            lista_jucatori_teren.append(jucator_intrat)
            print(lista_jucatori_teren)
            print(lista_jucatori_rezerva)
            print(lista_jucatori_scosi)
            schimbari = SCHIMBARI_MAX - schimbari_efectuate
            print(f'A intrat {jucator_intrat}, a iesit {jucator_scos}. Mai aveti {schimbari} schimbari')
        else:
            print('Jucatorul este in teren')
    else:
        print('Nu se mai pot efectua schimbari')
else:
    print(f'nu se poate efectua schimbarea deoarece jucatorul {jucator_scos} nu e in teren')
