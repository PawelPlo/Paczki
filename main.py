#box parcel service program

liczba_przesylek=input("Ile przesylek chcesz wyslac?    ")
liczba_przesylek=int(liczba_przesylek)
nr_przesylki=1
pudelko = 0
paczka = 0
poj_pudelka = 20
waga_paczki = []
laczna_waga_paczek = 0
najlzejsza_paczka = 0
waga_najlzejszej_paczki = 0
nr_najlzejszej_paczki = 0


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
            if poj_pudelka-paczka >= najlzejsza_paczka:
                najlzejsza_paczka = poj_pudelka-paczka
                waga_najlzejszej_paczki = najlzejsza_paczka
                nr_najlzejszej_paczki = nr_najlzejszej_paczki + 1
            paczka = 0 + waga_przesylki
            print("Do nastepnej paczki przeniesiono {} kg".format(paczka))
            continue
        if paczka == poj_pudelka:
            pudelko = pudelko + 1
            print("wyslano 1 paczke o wadze 20 kg")
            waga_paczki.append(poj_pudelka)
            if poj_pudelka - paczka >= najlzejsza_paczka:
                najlzejsza_paczka = poj_pudelka - paczka
                waga_najlzejszej_paczki = najlzejsza_paczka
                nr_najlzejszej_paczki = nr_najlzejszej_paczki + 1
            paczka=0
            continue
if paczka > 0:
    pudelko = pudelko + 1
    waga_paczki.append(paczka)
    if poj_pudelka - paczka >= najlzejsza_paczka:
        najlzejsza_paczka = poj_pudelka - paczka
        waga_najlzejszej_paczki = najlzejsza_paczka
        nr_najlzejszej_paczki = nr_najlzejszej_paczki + 1
print("PODSUMOWANIE")
print("Wyslano {} sztuk pudelek o wadze {} kg".format(pudelko, waga_paczki))
print("Wyslano w sumie {} kg".format(laczna_waga_paczek))
print("Wyslano {} pustych kilogramow".format(pudelko*poj_pudelka-laczna_waga_paczek))
for najlzejsza_paczka in range(1, pudelko + 1):
    print("Najwiecej pustych kilogramow to {}.".format(waga_najlzejszej_paczki))
    print("Nr najlzejszej paczki to: {}.".format(nr_najlzejszej_paczki))
    break











