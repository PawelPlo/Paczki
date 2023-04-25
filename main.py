#box parcel service program

liczba_paczek=input("Ile paczek chcesz wyslac?    ")
liczba_paczek=int(liczba_paczek)

for przesylka in range(liczba_paczek):
    waga_przesylki=int(input("Podaj wage przesylki min 1kg - max 10kg:   "))
    if waga_przesylki < 1 or waga_przesylki > 10:
        print("Wyslano wskazane przesylki bez ostatniej")
        break
    while waga_przesylki >= 20:
        waga_przesylki=int(input("Podaj wage przesylki min 1kg - max 10kg:   "))