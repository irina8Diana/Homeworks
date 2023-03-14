
#1. Citește de la tastatură un string de dimensiune impară; Afișează caracterul din mijloc.
import stdiomask as stdiomask
from pwinput import pwinput

text = input('Introdu textul dorit:')
middle = text[len(text)//2]
print(middle)

# 2. Folosind assert, verifică dacă un string este palindrom.

str = input('Introdu textul dorit:')
x = str[::-1]
print(x)
assert (str == x)

# 3. Folosind o singură linie de cod :citește un string de la tastatură (ex: 'alabala portocala');
#salvează fiecare cuvânt într-o variabilă; printează ambele variabile pentru verificare.

word1, word2 = input('Enter first word:'), input ('Enter second word')
print (word1 , word2)

#4. Exercițiu: citește un string de la tastatură (ex: alabala portocala);
#- salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
#capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

prop = input ('Enter a string:')
x = prop[0];
print (x)
import re
prop = re.sub(x,x.upper(),prop)
print (prop)
print (prop[0].lower() + prop[1:] + prop[len(prop)-1].lower())

'''5.Exercițiu: citește un user de la tastatură;citește o parolă;
# afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect. eg: parola abc => *** parola abcd => ****
'''
user = input('Enter a user:')
password = input('Enter your password:')
leng_pass= len(password)
star='*'
leng_star= len(star)
leng_star=leng_pass
password1=password.replace(password,'*' *leng_star)
print(f'Password for user: {user} is {password1} and has {leng_pass} characters')




