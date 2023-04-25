#box parcel service program

liczba_przesylek=input("Ile przesylek chcesz wyslac?    ")
liczba_przesylek=int(liczba_przesylek)
paczka = 0
paczka = int(paczka)

for waga_przesylki in range(liczba_przesylek):
    waga_przesylki = int(input("Podaj wage przesylki min 1kg - max 10kg:   "))
    if waga_przesylki <1 or waga_przesylki >10:
        print("Twoje przesylki wyslano, poza ostatnia")
        break

    elif waga_przesylki >1 or waga_przesylki <10:
         paczka += waga_przesylki
         print(paczka)

    if paczka > 20:
        print("cos")
        break








