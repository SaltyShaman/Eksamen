import json

class UniversalJSONReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.all_values = []  # liste over alle primitive værdier

    # Læs JSON filen
    def load_json(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    # Rekursiv gennemgang af JSON-strukturen
    def _extract_values(self, element):
        if isinstance(element, dict):
            for value in element.values():
                self._extract_values(value)

        elif isinstance(element, list):
            for item in element:
                self._extract_values(item)

        else:  # primitive værdier (str, int, bool, float, None)
            self.all_values.append(element)

    # Giv en liste over ALLE værdier uanset JSON-struktur
    def get_all_values(self):
        if self.data is None:
            self.load_json()

        # Reset listen hvis metoden kaldes flere gange
        self.all_values = []
        self._extract_values(self.data)

        return self.all_values


# --- Brug af klassen ---
if __name__ == "__main__":
    reader = UniversalJSONReader("local_data.json")
    reader.load_json()
    values = reader.get_all_values()

    print("=== Alle værdier i JSON-strukturen ===")
    for v in values:
        print("-", v)
