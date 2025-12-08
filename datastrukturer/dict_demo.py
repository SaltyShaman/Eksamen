class DictDemo:
    def run(self):
        print("\n=== DICT ===")
        print("Et dictionary bruges når du vil lagre data som key–value par.")
        
        #Forslag til key: bruge en tabel ID. Fx en SQL tabel.

        user = {
            "name": "Kristoffer",
            "age": 29,
            "role": "developer"
        }

        print("Dictionary:", user)

        print("Hent værdi via nøgle:")
        print("Navn:", user["name"])

        print("Tilføj nøgle:")
        user["email"] = "test@example.com"
        print(user)

        print("Brug DICT til: objekter, JSON-lignende data, opslagsdata, konfigurationer.")
        print("Det vil sige DICT er det naturlige format hvis man henter API data")
