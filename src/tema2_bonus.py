''' 1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
inputuri urmatoarele informatii:
a. Varsta
b. Insotit de mama
c. Insotit de tata
d. Pasaport
e. Act permisiune mama
f. Act permisiune tata
Conditii de imbarcare:
1. Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
si are permisiune in scris de la celalat parinte

Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.

'''
varsta = int(input('Introdu varsta:'))
mama = False
tata=True
ins_mama = False
ins_tata=False
pasaport = True
act_mama=True
act_tata = True

if varsta >=18 and pasaport:
    print('Se poate imbarca')
elif varsta<18 and pasaport and mama and tata:
    print('Se poate imbarca')
elif varsta<18 and pasaport:
    if ins_mama or ins_mama:
        print('Se poate imbarca')
    else:
        print('nu se poate imbarca')
else:
    print('nu se poate imbarca')

