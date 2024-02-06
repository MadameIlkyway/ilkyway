print("Faktorrechnung Übergangsbereich")
print("_______________________________")
entgelt = int(input("Eingabe Entgelt: "))

if entgelt > 520 and entgelt < 2000.01:
    print("Es liegt der Übergangsbereich vor. SV müssen mittels Faktorrechnung ermittelt werden.")
    BBGAN = round(1.351351351 * entgelt - 702.7027027, 2)
    kv = 9.1 * BBGAN / 100
    pv = 1.525 * BBGAN / 100
    rv = 9.3 * BBGAN / 100
    av = 1.3 * BBGAN / 100
    print("Die SV-Beiträge sind: ", kv, pv, rv, av)  

else :
    if entgelt < 520:
        print("Kein Übergangsbereich. Es sind die Regeln für geringfügige Beschäftigung zu prüfen.") 
    else :
        print("Kein Übergangsbereich. Es ist der Halbteilungsgrundsatz anzuwenden.")

    