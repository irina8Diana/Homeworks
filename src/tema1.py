#1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
"""
O variabila este o locatie de memorie unde se stocheaza informatii
"""
#2 Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabila:

fruct = 'Portocala'
varsta = 18
rez = 283.75
rezultat = True

#3 Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(fruct))
print(type(varsta))
print(type(rez))
print(type(rezultat))

#4 Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
rez=round(rez)
print(type(rez))
print(rez)

#5 Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile
print(f'Ana mananca o {fruct}')
print(f'Ana are varsta de: {varsta} ani')
print(f'Rezultatul adunarii este: {rez}')
print(f'Daca testul e negativ poate calatori {rezultat}')

#6. Citește de la tastatură:numele;prenumele. Afișează: 'Numele complet are x caractere'.
nume = input('Introdu numele:')
prenume = input('Introdu prenumele:')

lung_nume_complet=len(nume) +len(prenume)
print(f'Numele complet are {lung_nume_complet} caractere')

#7. Citește de la tastatură:lungimea;lățimea.Afișează: 'Aria dreptunghiului este x'.
lungime = int(input('Introdu lungimea:'))
latime = int(input('Introdu latimea:'))
arie_drep = lungime*latime
print(f'Aria dreptunghiului este {arie_drep}')

#8 Având stringul: 'Coral is either the stupidest animal or the smartest rock': afișează de câte ori apare cuvântul 'the';
#9 Același string.Afișează de câte ori apare cuvântul 'the';Printează rezultatul.
text = 'Coral is either the stupidest animal or the smartest rock'
count_word =text.count('the')
print(f'Number of occurrences of the word the is {count_word}')

#10 Folosiți un assert ca să verificați dacă acest string conține doar numere.
#print(pro.isnumeric())
#assert prop.isnumeric() == true
#text.isnumeric()
print (text.isnumeric())
assert text.isnumeric() != True


