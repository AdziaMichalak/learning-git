print("lista zakupów".capitalize())
lista = {
    "piekarnia".capitalize(): ["chleb".capitalize(), "bułki".capitalize(), "pączek".capitalize()],
    "warzywniak".capitalize(): ["marchew".capitalize(), "seler".capitalize(), "rukola".capitalize()],
}

for sklep, rzeczy in lista.items():
    print("idę do %s i kupuję tam: %s".capitalize() % (sklep, rzeczy))
   
lista1 = lista ["Piekarnia"]
lista2 = lista ["Warzywniak"]
print(f"w sumie kupuję {len(lista1) + len(lista2)} produktów".capitalize())

print("Hello to ja drugi programista")

print("mam ochotę na pączka z różą")
print("mam zagadkę: jak blondynki robią dżem?")
print()
print("Nie wiem")
print("obierają pączki")

print("hello")
print("dawno mnie tu nie było, więc nadrabiam zaległości")
