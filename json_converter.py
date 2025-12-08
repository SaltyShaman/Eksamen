import json

#I Python er det tætteste format til json en dict
class JSONConverter:
    def __init__(self, filename):
        self.filename = filename

        # JSON string hentet fra local_data.json (kan også hardcodes)
        self.json_string = self._load_json_string()

        # Dict der kommer fra json_string
        self.data_from_string = None

    # Henter selve filens indhold som en string
    def _load_json_string(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return file.read()

    # Konverter JSON string til Python dict
    def convert_string_to_dict(self):
        self.data_from_string = json.loads(self.json_string)
        print("=== JSON string til Python dict ===")
        print("Type:", type(self.data_from_string))

        # Eksempel: Print første brugers navn
        first_name = self.data_from_string["users"][0]["name"]
        print("Første bruger:", first_name)

    # Konverter Python dict til JSON string
    def convert_dict_to_json(self):
        python_dict = {
            "fruits": ["apple", "banana"],
            "price": 12.5
        }

        json_output = json.dumps(python_dict, indent=4)

        print("\n=== Python dict til JSON string ===")
        print(json_output)

    # Læs JSON fra fil til Python dict
    def read_local_file(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            local_dict = json.load(f)

        print("\n=== Læsning af local_data.json som dict ===")
        print("Første bruger:", local_dict["users"][0]["name"])
        print("Anden bruger:", local_dict["users"][1]["name"])


# --- Brug af klassen ---
if __name__ == "__main__":
    converter = JSONConverter("local_data.json")

    converter.convert_string_to_dict()
    converter.convert_dict_to_json()
    converter.read_local_file()