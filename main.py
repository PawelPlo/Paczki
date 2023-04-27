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

        if paczka >= 20:
            print("Waga twojej paczki przekroczyla 20 kg. Wyjmij ostatni element i dodaj do następnej paczki")
            ostatni_element=int(input("Podaj wage ostatniego elementu w kg:   "))
            paczka -= ostatni_element
            print("wyslano paczke o wadze {} kg".format(paczka))
            waga_przesylki = int(input("Podaj wage przesylki min 1kg - max 10kg:   "))

print(paczka)

#   print("Do pierwszej paczki zapakowano {} kg, nie wykorzystano {} kg".format(paczka))



         #else:
         #   print("Do pierwszej paczki zapakowano {} kg, nie wykorzystano {} kg".format(paczka, maxpojemnosc_paczki-paczka))








