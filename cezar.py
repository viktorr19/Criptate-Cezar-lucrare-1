alfabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"


def validare_text(text):
    for caracter in text:
        if caracter != " " and caracter.upper() not in alfabet:
            return False
    return True


def criptare_cezar(text, cheie):
    text = text.upper().replace(" ", "")
    rezultat = ""

    for litera in text:
        pozitie = alfabet.index(litera)
        pozitie_noua = (pozitie + cheie) % len(alfabet)
        rezultat += alfabet[pozitie_noua]

    return rezultat


def decriptare_cezar(text, cheie):
    text = text.upper().replace(" ", "")
    rezultat = ""

    for litera in text:
        pozitie = alfabet.index(litera)
        pozitie_noua = (pozitie - cheie) % len(alfabet)
        rezultat += alfabet[pozitie_noua]
    
    return rezultat


print("CIFRUL CEZAR")
print("1 - Criptare")
print("2 - Decriptare")

operatie = input("Alegeti operatia: ")

while operatie != "1" and operatie != "2":
    print("Introduceti 1 pentru criptare sau 2 pentru decriptare.")
    operatie = input("Alegeti operatia: ")


cheie = input("Introduceti cheia (1-30): ")

while not cheie.isdigit() or int(cheie) < 1 or int(cheie) > 30:
    print("Cheia trebuie sa fie un numar intre 1 si 30.")
    cheie = input("Introduceti cheia (1-30): ")

cheie = int(cheie)


text = input("Introduceti textul: ")

while not validare_text(text):
    print("Textul poate contine doar litere ale alfabetului roman si spatii.")
    text = input("Introduceti textul: ")


if operatie == "1":
    rezultat = criptare_cezar(text, cheie)
    print("Criptograma:", rezultat)
else:
    rezultat = decriptare_cezar(text, cheie)
    print("Mesajul decriptat:", rezultat)