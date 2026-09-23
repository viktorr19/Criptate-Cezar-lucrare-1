


alfabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"


def validare_text(text):
    for caracter in text:
        if caracter != " " and caracter.upper() not in alfabet:
            return False
    return True


def validare_cheie2(cheie2):
    if len(cheie2) < 7:
        return False

    for caracter in cheie2:
        if caracter.upper() not in alfabet:
            return False

    return True


def creare_alfabet_nou(cheie2):
    cheie2 = cheie2.upper()
    alfabet_nou = ""

    for litera in cheie2:
        if litera not in alfabet_nou:
            alfabet_nou += litera

    for litera in alfabet:
        if litera not in alfabet_nou:
            alfabet_nou += litera

    return alfabet_nou


def criptare_cezar(text, cheie1, alfabet_nou):
    text = text.upper().replace(" ", "")
    rezultat = ""

    for litera in text:
        pozitie = alfabet_nou.index(litera)
        pozitie_noua = (pozitie + cheie1) % len(alfabet_nou)
        rezultat += alfabet_nou[pozitie_noua]

    return rezultat


def decriptare_cezar(text, cheie1, alfabet_nou):
    text = text.upper().replace(" ", "")
    rezultat = ""

    for litera in text:
        pozitie = alfabet_nou.index(litera)
        pozitie_noua = (pozitie - cheie1) % len(alfabet_nou)
        rezultat += alfabet_nou[pozitie_noua]

    return rezultat


print("CIFRUL CEZAR CU 2 CHEI")
print("1 - Criptare")
print("2 - Decriptare")

operatie = input("Alegeti operatia: ")

while operatie != "1" and operatie != "2":
    print("Introduceti 1 pentru criptare sau 2 pentru decriptare.")
    operatie = input("Alegeti operatia: ")


cheie1 = input("Introduceti cheia 1 (1-30): ")

while not cheie1.isdigit() or int(cheie1) < 1 or int(cheie1) > 30:
    print("Cheia 1 trebuie sa fie un numar intre 1 si 30.")
    cheie1 = input("Introduceti cheia 1 (1-30): ")

cheie1 = int(cheie1)


cheie2 = input("Introduceti cheia 2 (minimum 7 litere): ")

while not validare_cheie2(cheie2):
    print("Cheia 2 trebuie sa contina doar litere ale alfabetului roman si minimum 7 caractere.")
    cheie2 = input("Introduceti cheia 2: ")


alfabet_nou = creare_alfabet_nou(cheie2)

print("Alfabetul initial :", alfabet)
print("Alfabetul permutat:", alfabet_nou)


text = input("Introduceti textul: ")

while not validare_text(text):
    print("Textul poate contine doar litere ale alfabetului roman si spatii.")
    text = input("Introduceti textul: ")


if operatie == "1":
    rezultat = criptare_cezar(text, cheie1, alfabet_nou)
    print("Criptograma:", rezultat)
else:
    rezultat = decriptare_cezar(text, cheie1, alfabet_nou)
    print("Mesajul decriptat:", rezultat)