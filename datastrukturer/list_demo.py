class ListDemo:
    def run(self):
        print("\n=== LIST ===")
        print("En liste bruges når rækkefølgen betyder noget, og når data kan ændres (mutable).")

        fruits = ["apple", "banana", "orange"]
        print("Startliste:", fruits)

        print("Tilføj element:")
        fruits.append("pear")
        print("Efter append:", fruits)

        print("Fjerne element:")
        fruits.remove("banana")
        print("Efter remove:", fruits)

        print("Brug LIST når du har: ordnet data, fx brugernavne, scores, rækkefølger, filer.")
