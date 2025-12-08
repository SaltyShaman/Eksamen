class TupleDemo:
    def run(self):
        print("\n=== TUPLE ===")
        print("En tuple bruges når data IKKE må ændres (immutable) og rækkefølgen stadig betyder noget.")

        coords = (40.7128, -74.0060)
        print("Tuple:", coords)

        print("Tupler er hurtigere end lister og gode til faste værdier, fx koordinater, datoer, konstanter.")
        
        try:
            coords[0] = 0
        except TypeError:
            print("Du kan ikke ændre en tuple – dette giver fejl.")
