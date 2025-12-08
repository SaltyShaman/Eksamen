class SetDemo:
    def run(self):
        print("\n=== SET ===")
        print("Et set bruges når du vil undgå duplikater og ikke går op i rækkefølgen.")
        print("Det vil sige brug et set af ID i stedet for navne")
        
        unique_numbers = {1, 2, 3, 3, 2, 1}
        print("Set (duplikater fjernet):", unique_numbers)

        print("Tilføj element:")
        unique_numbers.add(5)
        print(unique_numbers)

        print("Brug SET når du har: unikke værdier, fx brugernavne, tags, unikke IDs.")
        print("Fx en blodprøve analyse med forskellige måleværdier")
