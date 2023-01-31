class Chaine:
    def __init__(self, chaineDeCaractere):
        self.chaineDeCaractere = chaineDeCaractere

    def afficher(self):
        return self.chaineDeCaractere

    def renvoit_miroir(self):
        return self.chaineDeCaractere[::-1]

    def est_palindrome(self):
        return self.chaineDeCaractere == self.chaineDeCaractere[::-1]

class Salutation(Chaine):
    def afficher(self):
        return "Bonjour " + super().afficher()

class Aurevoir(Chaine):
    def afficher(self):
        return super().afficher() + " Au revoir"

class Palindrome(Chaine):
    def afficher(self):
        chaineDeCaractere = super().afficher()
        if self.est_palindrome():
            chaineDeCaractere += " Bien dit"
        return chaineDeCaractere

# def main():
#     chaineDeCaractere = input("Entrez une chaîne de caractere: ")
#     c = Palindrome(chaineDeCaractere)
#     c= Aurevoir(c)
#     c = Salutation(c)

#     print(c.afficher())

# if __name__ == "__main__":
#     main()
