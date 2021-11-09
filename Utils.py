from random import randint

class Utils():
    def __init__(self):
        pass

    def _clear_words(file_content, number_of_elements):
        illegal_chars = [",", ".", "?", "!", ";", ":", "-", "–", "—", "/", "(", ")", "…", 
                        "»", "«", "*", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        table = []

        for word in file_content:
            for char in word:
                if (char in illegal_chars):
                    word = word.replace(char, "")
            
            if (word != ""):
                table.append(word)

            if (len(table) == number_of_elements):
                break

        return table

    @staticmethod
    def generate_table_of_randint(number_of_elements):
        table = [randint(0, number_of_elements) for i in range(number_of_elements)]

        return table

    @staticmethod
    def generate_table_from_file(file_name, number_of_elements):
        with open(file_name, encoding='utf8') as file:
            file_content = file.read().lower().split()

        table = Utils._clear_words(file_content, number_of_elements)

        return table

    @staticmethod
    def print_table(table):
        print("TABLE:")
        print("-------------------------")

        for element in table:
            print(element, end=" | ")

        print("\n-------------------------")
        print("NUMBER OF ELEMENTS: ", len(table), "\n") 
