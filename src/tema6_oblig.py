# 1.Clasa Cerc Atribute: raza, culoare Constructor pentru ambele atribute
# Metode:● descrie_cerc() - va PRINTA culoarea și raza ● aria() - va RETURNA aria● diametru()● circumferinta()

class Circle:

    def __init__(self, raza, culoare):
        self._raza = raza
        self._culoare = culoare

    def descrie_cerc(self):
        print(f'{self._raza}, {self._culoare}')

    def aria(self):
        return self._raza ** 2 * 3.14

    def diametru(self):
        diametru = self._raza * 2
        return diametru

    def circumferinta(self):
        circumferinta = 3.14 * 2 * self._raza
        return circumferinta


circle1 = Circle(170, 'pink')

print(circle1.descrie_cerc())
print(circle1.aria())
print(circle1.diametru())
print(circle1.circumferinta())

'''2. Clasa DreptunghiAtribute: lungime, latime, culoareConstructor pentru toate atributele
Metode:● descrie()● aria()● perimetrul() ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().'''


class Dreptunghi:

    def __init__(self, lungime, latime, culoare):
        self._lungime = lungime
        self._latime = latime
        self._culoare = culoare

    def descrie_dreptunghi(self):
        print(
            f'Lungimea dreptunghiului este {self._lungime}, si are latimea {self._latime} si culoarea {self._culoare}')

    def aria_dreptunghi(self):
        aria = self._lungime * self._latime
        return aria

    def perimetru(self):
        perimetru = self._lungime * 2 + self._latime * 2
        return perimetru

    def schimba_culoarea(self, noua_culoare):
        self._culoare = noua_culoare


dreptunghi1 = Dreptunghi(8, 5, 'blue')
print(dreptunghi1.descrie_dreptunghi())
print(dreptunghi1.aria_dreptunghi())
print(dreptunghi1.perimetru())
dreptunghi1.schimba_culoarea('red')
print(dreptunghi1.descrie_dreptunghi())


# 3. Clasa Angajat Atribute: nume, prenume, salariu Constructor pt toate atributele
# Metode:● descrie() ● nume_complet() ● salariu_lunar() ● salariu_anual() ● marire_salariu(procent)

class Angajat:

    def __init__(self, nume, prenume, salariu):
        self._nume = nume
        self._prenume = prenume
        self._salariu = salariu

    def descrie_angajat(self):
        print(f' Angajatul cu numele {self._nume} si prenumele {self._prenume} are salariul: {self._salariu}')

    def nume_complet(self):
        print(f'Numele complet este {self._nume} {self._prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar este {self._salariu}')

    def salariu_anual(self):
        salariu_anual = self._salariu * 10
        return salariu_anual

    def marire_salariu(self, procent):
        marire_salariu = self._salariu + (procent * self._salariu / 100)
        return marire_salariu


angajat = Angajat('Popescu', 'Ionel', 10000)
angajat.descrie_angajat()
angajat.nume_complet()
angajat.salariu_lunar()
print(f'Salariul anual este {angajat.salariu_anual()}')
print(f'Salariul marit va fi  {angajat.marire_salariu(10)}')


# 4.Clasa Cont Atribute: iban, titular_cont, soldConstructor pentru toate atributele
# Metode:● afisare_sold() - Titularul x are în contul y suma de n lei● debitare_cont(suma)● creditare_cont(suma)
class Cont:
    def __init__(self, iban, titular_cont, soldConstructor):
        self._iban = iban
        self._titular_cont = titular_cont
        self._soldConstructor = soldConstructor

    def afisare_sold (self):
        print(f'Titularul {self._titular_cont} are in contul {self._iban} suma de {self._soldConstructor}')

    def debitare_cont(self, suma):
        if self._soldConstructor > suma:
            self._soldConstructor = self._soldConstructor - suma
            print(f'Noul sold este {self._soldConstructor}')
        else:
            print ('Nu aveti fonduri suficiente')

    def creditare_cont(self, suma):
        sold_nou = self._soldConstructor + suma
        print (f'Noul sold este {sold_nou}')

cont = Cont( 'Ro100RBR1230', 'Popescu Daniel', 10000)
print(cont.afisare_sold())
cont.debitare_cont(900)
cont.creditare_cont(100)