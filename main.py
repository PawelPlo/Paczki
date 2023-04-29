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


for waga_przesylki in range(liczba_przesylek):
    waga_przesylki = int(input("Podaj wage przesylki nr {} min 1kg - max 10kg:   ".format(nr_przesylki)))
    if waga_przesylki <1 or waga_przesylki >10:
        print("Zla waga przesylki, koniec przyjmowania")
        break
    if waga_przesylki >1 or waga_przesylki <10:
        paczka += waga_przesylki
        nr_przesylki = nr_przesylki + 1
        if paczka > 20:
            paczka -= waga_przesylki
            pudelko = pudelko + 1
            print("wyslano 1 pudelko o wadze {}".format(paczka))
            print("W wyslanej paczce pozostalo {} wolnych kilogramow".format(poj_pudelka-paczka))
            paczka = 0 + waga_przesylki
            print("Do nastepnej paczki przeniesiono {} kg".format(paczka))
            continue
        if paczka == 20:
            pudelko = pudelko + 1
            print("wyslano 1 pudelko o wadze 20 kg")
            paczka=0
            print("W paczce pozostalo {} wolnych kilogramow".format(poj_pudelka - paczka))
            continue
    else:
        continue
pudelko = pudelko + 1
print("wyslano 1 pudelko o wadze {}".format(paczka))
print("W wyslanej paczce pozostalo {} wolnych kilogramow".format(poj_pudelka-paczka))
print("Wyslano {} sztuk pudelek o wadze {} kg".format(pudelko, paczka))


#   print("Do pierwszej paczki zapakowano {} kg, nie wykorzystano {} kg".format(paczka))



         #else:
         #   print("Do pierwszej paczki zapakowano {} kg, nie wykorzystano {} kg".format(paczka, maxpojemnosc_paczki-paczka))








