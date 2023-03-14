# 1.Itereaza prin listă alte_numere.Populează corect celelalte liste Afișeaza cele 4 liste la final
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for num in alte_numere:
    if num >= 0:
        numere_pozitive.append(num)
    else:
        numere_negative.append(num)
    if num % 2 == 0:
        numere_pare.append(num)
    else:
        numere_impare.append(num)

print(f'Numerele pozitive sunt {numere_pozitive}')
print(f'Numerele negative sunt {numere_negative}')
print(f'Numerele impare sunt {numere_impare}')
print(f'Numerele pare sunt {numere_pare}')

# 2. Aceeași listă: Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici. https://www.youtube.com/watch?v=lyZQPjUT5B4

for i in range(len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
print(alte_numere)

'''3. Ghicitoare de număr: numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None  Folosind un while  User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!'''
numar_secret = int(input('Generati un numar intre 1 -30: '))
numar_ghicit = 9
while numar_secret != numar_ghicit:
    if numar_secret > numar_ghicit:
        print('Nr secret e mai mare')
    elif numar_secret < numar_ghicit:
        print('Nr secret e mai mic')
    break
else:
    print('Felicitari! Ai ghicit')

'''4. Alege un număr de la tastatură Ex: 7 Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333'''

nr = int(input('Alege un numar: '))
i = 0
for i in range(nr):
    for j in range(i + 1):
        print(i + 1, end="")
    print(" ")

'''5. tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)'''
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for tast in tastatura_telefon:
    for item in tast:
        print(f'Cifra curenta este {item}')

