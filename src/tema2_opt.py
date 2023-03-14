# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
number = input('Introdu un numar:')
leng_nr = len(number)
if leng_nr == 4:
    print('Numarul are 4 cifre')
elif leng_nr > 4:
    print('Numarul are mai mult de 4 cifre')
else:
    print('Numarul are mai putin de 4 cifre')

# 2 Verifica daca x are exact 6 cifre
if leng_nr==6:
    print('Numarul are 6 cifre')
else:
    print('Numarul nu are 6 cifre')

#3. Verifica daca x este numar par sau impar
x = int(input('Introdu un numar x:'))
if x % 2 == 0:
    print (f'{x} este un numar par')
else:
    print(f'{x} este un numar impar')

#4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele
y = int(input('Introdu y:'))
z = int(input('Introdu z:'))
if x>y and x>z:
    print(f'{x} este mai mare ca {y} si {z}')
elif x==y and y==z:
    print (f'Numerele sunt egale {x} = {y}={z}')
elif y>x and y>z:
    print (f'{y} este mai mare ca {x} {z}')
else:
    print(f'{z} este mai mare ca {x} {y}')

#5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca triunghiul este valid sau nu
# (un triunghi este valid daca suma tuturor unghiurilor este de 180 de grade sau daca suma lungimilor a oricare doua laturi
# este mai mare decat lungimea celei de-a treia laturi)
x= 110
y=30
z=40
if x+y+z ==180:
    print('Triunghiul este valid')
else:
    print ('Triunghiul este invalid')

#6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de la tastatura un număr x de tip int și
# afișează stringul fără ultimele x caractere. ex: dacă ați ales 7 se va afisa urmatorul string:
# 'Coral is either the stupidest animal or the smarte'
text ='Coral is either the stupidest animal or the smartest rock'
nr = int(input('Introdu un numar:'))
print(text[:-nr])

#7 Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format din primele 5 caractere + ultimele 5
first = text[:5]
last = text[-5:]
print(f'{first} {last}')

#8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start al cuvântului rock
# - adică poziția in string la care începe cuvântul rock (hint: este o funcție care te ajuta sa faci asta).
# Folosind aceasta variabila + slicing, afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
# animal or the smartest '

index = text.index('rock')
print (index)
print(text[:index])

#9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se va folosi un assert.
#Atentie: se dorește ca programul sa fie case insensitive, adica 'apA' e acceptat ca un string in care primul si ultimul caracter
# este la fel (hint, te poti folosi de o functie pentru a face string-ul case insensitive)

text2 = input('Introdu un text:')
firstchar = text2[:1]
lastchar = text2[-1:]
assert(firstchar.casefold() == lastchar.casefold())

#10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)
list = ('0123456789')
nrpare = list[0::2]
print({nrpare})
nrimpare = list[1::2]
print({nrimpare})
