import json

class JSONReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.users = []

    # Læs JSON filen
    def load_file(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            self.data = json.load(file)
            self.users = self.data.get("users", [])

    # Udskriv hele JSON filen pænt
    def print_full_json(self):
        print("=== Hele JSON filen ===")
        print(json.dumps(self.data, indent=4)) #Indentering er til at holde formattet

    # Udskriv kun navne og IDs (fælles værdier)
    def print_user_list(self):
        print("\n=== Liste af brugere ===")
        for user in self.users:
            print(f"- {user['name']} (ID: {user['id']})")

    # Sammenlign data mellem brugere
    def compare_users(self):
        print("\n=== Sammenligning af brugerdata ===")
        for user in self.users:
            print(f"\nBruger: {user.get('name')}")
            print(f"Email: {user.get('email')}")

            address = user.get("address")
            if address:
                print(f"Adresse: {address.get('street')}, {address.get('city')}")
            else:
                print("Adresse: Ikke angivet")


# --- Brug af klassen ---
if __name__ == "__main__":
    reader = JSONReader("local_data.json")
    reader.load_file()
    reader.print_full_json()
    reader.print_user_list()
    reader.compare_users()
