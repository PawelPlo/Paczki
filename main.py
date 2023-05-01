#box parcel service program

liczba_przesylek=input("Ile przesylek chcesz wyslac?    ")
liczba_przesylek=int(liczba_przesylek)
nr_przesylki=1
nr_przesylki=int(nr_przesylki)
pudelko = 0
pudelko = int(pudelko)
paczka = 0
paczka = int(paczka)
poj_pudelka = 20
poj_pudelka = int(poj_pudelka)
waga_paczki = []
laczna_waga_paczek = 0
laczna_waga_paczek = int(laczna_waga_paczek)
puste_kilogramy = 0
puste_kilogramy = int(puste_kilogramy)
najlzejsza_paczka = 0
najlzejsza_paczka = int(najlzejsza_paczka)
nr_najlzejszej_paczki = 0
nr_najlzejszej_paczki = int(nr_najlzejszej_paczki)

for waga_przesylki in range(liczba_przesylek):
    waga_przesylki = int(input("Podaj wage przesylki nr {} min 1kg - max 10kg:   ".format(nr_przesylki)))
    if waga_przesylki <1 or waga_przesylki >10:
        print("Zla waga przesylki, koniec przyjmowania")
        break
    if waga_przesylki >=1 or waga_przesylki <=10:
        paczka += waga_przesylki
        laczna_waga_paczek += waga_przesylki
        nr_przesylki = nr_przesylki + 1
        if paczka > poj_pudelka:
            paczka -= waga_przesylki
            pudelko = pudelko + 1
            print("wyslano 1 paczke o wadze {}".format(paczka))
            waga_paczki.append(paczka)
            print("W wyslanej paczce pozostalo {} wolnych kilogramow".format(poj_pudelka-paczka))
            if poj_pudelka-paczka>najlzejsza_paczka:
                najlzejsza_paczka = poj_pudelka-paczka
                nr_najlzejszej_paczki = nr_najlzejszej_paczki + 1
            paczka = 0 + waga_przesylki
            print("Do nastepnej paczki przeniesiono {} kg".format(paczka))
            continue
        if paczka == poj_pudelka:
            pudelko = pudelko + 1
            print("wyslano 1 paczke o wadze 20 kg")
            waga_paczki.append(poj_pudelka)
            nr_najlzejszej_paczki = nr_najlzejszej_paczki + 1
            paczka=0
            continue
if paczka > 0:
    pudelko = pudelko + 1
    waga_paczki.append(paczka)
    nr_najlzejszej_paczki = nr_najlzejszej_paczki + 1
    if poj_pudelka - paczka > najlzejsza_paczka:
        najlzejsza_paczka = poj_pudelka - paczka

print("PODSUMOWANIE")
print("Wyslano {} sztuk pudelek o wadze {} kg".format(pudelko, waga_paczki))
print("Wyslano w sumie {} kg".format(laczna_waga_paczek))
print("Wyslano {} pustych kilogramow".format(pudelko*poj_pudelka-laczna_waga_paczek))
if pudelko > 1:
    print("Paczka nr {} ma najwiecej pustych kilogramow: {} kg".format(nr_najlzejszej_paczki, najlzejsza_paczka))










