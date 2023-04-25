#box parcel service program

liczba_przesylek=input("Ile przesylek chcesz wyslac?    ")
liczba_przesylek=int(liczba_przesylek)
paczka = 0
paczka = int(paczka)
maxpojemnosc_paczki = 20
maxpojemnosc_paczki = int(maxpojemnosc_paczki)

for waga_przesylki in range(liczba_przesylek):
    waga_przesylki = int(input("Podaj wage przesylki min 1kg - max 10kg:   "))
    if waga_przesylki <1 or waga_przesylki >10:
        print("Twoje przesylki wyslano, poza ostatnia")
        break

    elif waga_przesylki >1 or waga_przesylki <10:
        paczka += waga_przesylki
        if not paczka > 20:
            print(paczka)
        else:
            print("Do pierwszej paczki zapakowano {} kg, nie wykorzystano {} kg".format(paczka, maxpojemnosc_paczki-paczka))








