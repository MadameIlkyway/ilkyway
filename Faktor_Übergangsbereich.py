print()
print("SV-Beitragsrechner")
print("-------------------------------")
print()

entgelt = int(input("Eingabe Entgelt: "))
KVZusatz = float(input("Zusatzbeitrag Krankenkasse: "))
kinderlos = input("Über 23 Jahre ohne Kind (j/n): ")
print()

KVZhalb = KVZusatz/2

if kinderlos == "j":
    PVZusatz = 0.6
else:
    PVZusatz = 0    

if entgelt > 538 and entgelt < 2000.01:
    print("Es liegt der Übergangsbereich vor. SV müssen mittels Faktorrechnung ermittelt werden.")
    BBGAN = round(1.351351351 * entgelt - 702.7027027, 2)
    print("Die geminderte Beitragsbemessungsgrundlage liegt bei: ", BBGAN, "Euro.")
    kv = round((7.3 + KVZhalb) * BBGAN / 100, 2)
    pv = round((1.7 + PVZusatz) * BBGAN / 100, 2)
    rv = round(9.3 * BBGAN / 100, 2)
    av = round(1.3 * BBGAN / 100, 2)
    print()
    print("Die SV-Beiträge lauten: ")  
    print("KV: ", kv, "Euro")
    print("PV: ", pv, "Euro")
    print("RV: ", rv, "Euro")
    print("AV: ", av, "Euro")


else :
    if entgelt < 520:
        print("Entgelt unter 538 Euro. Es sind die Regeln für geringfügige Beschäftigung zu prüfen.") 
    else :
        print("Hier ist der Halbteilungsgrundsatz anzuwenden. Bemessungsgrundlage:", entgelt, "Euro.")
        print()
        kv = round((7.3 + KVZhalb) * entgelt / 100, 2)
        pv = round((1.7 + PVZusatz) * entgelt / 100, 2)
        rv = round(9.3 * entgelt / 100, 2)
        av = round(1.3 * entgelt / 100, 2)
        print("Die SV-Beiträge lauten: ")  
        print("KV: ", kv, "Euro")
        print("PV: ", pv, "Euro")
        print("RV: ", rv, "Euro")
        print("AV: ", av, "Euro")

    