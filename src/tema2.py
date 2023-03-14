'''1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
 #Un if else verifica daca o conditie este indeplinita si atunci se intrea pe ramura de if si se executa codul,
#daca nu este indeplinita se intra pe ramura de else si se executa codul'''

# 2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg mai mare ca 0)
x: int = int(input('Introdu x:'))
if x > 0:
    print(f' {x} este un numar natural mai mare ca 0')
else:
    print(f'{x} nu este un numar natural')

# 3 Verifica daca x este un numar pozitiv, negativ sau neutru
if x > 0:
    print(f' {x} este un numar pozitiv')
elif x < 0:
    print(f'{x} este nu numar negativ')
else:
    print(f'{x} este un numar neutru')

# 4 Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
if (x >= -2) and (x <= 13):
    print(f'{x} este in intervalul (-2;13)')
else:
    print(f'{x} nu este in intervalul (-2 ; 13)')

# 5 Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna cate numere sunt intre x si y,
# nu rezultatul diferentei intre x si y). Hint: Se va folosi functia abs
x1 = int(input('Introdu x1:'))
x2 = int(input('Introdu x2:'))
numbers =abs(x1 -x2)
if numbers < 5:
    print('Diferenta este mai mica ca 5')
else:
    print('Diferenta este mai mare ca 5')


# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
if x not in range(5, 27):
    print('not in range')
else:
    print('in range')

# 7.Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale, daca nu, afiseaza care din ele este mai mare
y = int(input('Introdu y:'))
if x == y:
    print('Valorile sunt egale')
elif x < y:
    print(f'{x} este mai mic ca {y}')
else:
    print(f'{x} este mia mare ca {y}')

# 8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).
l1 = int(input('Introdu l1:'))
l2 = int(input('Introdu l2:'))
l3 = int(input('Introdu ll3:'))
if l1 == l2 and l2 == l3:
    print('Triunghiul este echilateral')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Triunghiul este isoscel')
else:
    print('Triunghiul nu are nici o latura egala')

# 9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu.
# Atentie!Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
vocala = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
litera = input('Introdu litera:')
if litera in vocala:
    print(f'{litera} este vocala')
else:
    print(f'{litera} nu este vocala')

'''10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
urmeaza:
a. Peste 9 => A
b. Peste 8 => B
c. Peste 7 => C
d. Peste 6 => D
e. Peste 4 => E
f. 4 sau sub => F'''
nota = int(input('Introdu nota:'))
if nota >= 9:
    print('Nota este A')
elif nota >= 8 and nota < 9:
    print('Nota este B')
elif nota >= 7 and nota < 8:
    print('Nota este C')
elif nota >= 6 and nota < 7:
    print('Nota este D')
elif nota >= 4 and nota < 6:
    print('Nota este E')
elif nota <=4 and nota > 0:
    print('Nota este F')
else:
    print('Nota este incorecta')
