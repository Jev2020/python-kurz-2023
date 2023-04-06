#Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

sklad = {
  "1N4148":250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = ["1N4148", "BAV21", "KC147", "2N7002", "BC547C"]

# Pokud zadaný kód není ve slovníku, není součástka skladem.
# Vypiš tedy zprávu, že součástka není skladem.

kod_soucastky = input("Zadej kod soucastky:")

if kod_soucastky in sklad:
    pocet_soucastek = int(input("Zadejte pocet soucastek:"))

    if pocet_soucastek > sklad[kod_soucastky]:
        print("Lze prodat pouze omezene mnozstvi kusu.")
        pocet_soucastek = sklad.pop(kod_soucastky)
    else:
        print("Poptavku lze uspokojit v plne vysi.")
        sklad[kod_soucastky] -= pocet_soucastek

else:
    print("Soucastka neni skladem.")
