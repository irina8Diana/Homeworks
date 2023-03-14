# 1. Clasa Factura Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie),
# număr, nume_produs, cantitate, pret_buc Constructor: toate atributele, fara serie
# Metode: ● schimbă_cantitatea(cantitate) ● schimbă_prețul(pret) ● schimbă_nume_produs(nume) ● generează_factura() - va printa tabelar dacă reușiți
from datetime import date


class Factura:
    serie = 'F123'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self._numar = numar
        self._nume_produs = nume_produs
        self._cantitate = cantitate
        self._pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self._cantitate = cantitate
        print(f'Noua cantitate este {self._cantitate} ')

    def schimba_pretul(self, pret):
        self._pret_buc = pret
        print(f'Noul pret este {self._pret_buc}')

    def schimba_nume_produs(self, nume):
        self._nume_produs = nume
        return self._nume_produs

    def genereaza_factura(self):
        print(f'Factura seria {self.serie}, numar {self._numar}')
        print(f'Data {date.today()}')
        print(f'Produs  | Cantitate | Pret_buc | Total')
        print(f'{self._nume_produs}, | {self._cantitate},     | {self._pret_buc},       | '
              f'{self._pret_buc * self._cantitate} ')


factura = Factura(5, 'Ardei', 5, 100)
factura.genereaza_factura()

'''2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e negativă-eroare, daca viteza e mai mare decat viteza_max 
- masina va accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0 '''


class Masina:
    culoare = 'gri'
    viteza_actuala = 0
    culori_disponibile = {'rosu', 'verde', 'albastru', 'galben', 'roz'}
    inmatriculata = False
    marca = 'Toyota'

    def __init__(self, model, viteza_maxima):
        self._model = model
        self._viteza_maxima = viteza_maxima

    def descrie(self):
        print(
            f'Masina {self.marca}, inmatriculata {self.inmatriculata}, are culoarea {self.culoare}, viteza {self.viteza_actuala}')

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
            print(f'Noua culoare va fi {self.culoare}')
        else:
            print(f' {culoare} nu se regaseste in lista de culori disponibile" ')

    def accelereaza(self, vit):
        if vit < 0:
            print('Error')
        elif vit > self._viteza_maxima:
            vit = self._viteza_maxima
            print(f'Se va accelera pana la {vit}')
        else:
            print(f'Acceleram la {vit}')

    def franeaza(self):
        print(f'Masina s-a oprit, viteza este {self.viteza_actuala}')


masina = Masina('Opel', 150)
masina.descrie()
masina.vopseste('rosu')
masina.accelereaza(50)
masina.franeaza()

'''3. Clasa TodoList Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea) La început nu avem taskuri,
 dict e gol și nu avem nevoie de constructor
Metode:

● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict'''


class ToDo:
    dictionary = {}

    def adauga_task(self, nume, descriere):
        self.dictionary.update({nume:descriere})
        print(self.dictionary)

    def finalizeaza_task(self, nume):
       nume = todo.adauga_task(nume)


    #def afiseaza_to_do_list(self):

    #def afiseaza_detalii_suplimentare(self, nume_task):
     #   if nume_task in self.dictionary:
      #      print()
todo= ToDo()
todo.adauga_task('curat','trebuie sa faci curat')
todo.finalizeaza_task('curat')