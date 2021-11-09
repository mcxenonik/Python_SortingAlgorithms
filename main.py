from SelectionSort import SelectionSort
from Utils import Utils

if __name__ == "__main__":
    file_name = "pan-tadeusz.txt"
    number_of_elements = 100

    table = Utils.generate_table_from_file(file_name, number_of_elements)
    Utils.print_table(table)

    table_sorted = SelectionSort.run_algorithm(table)
    Utils.print_table(table_sorted)

