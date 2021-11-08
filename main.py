from random import randint

from SelectionSort import SelectionSort

def generate_table(number_of_elements):
    table = [randint(0, number_of_elements) for i in range(number_of_elements)]

    return table

def print_table(table):
    for element in table:
        print(element, end=" | ")

    # print("\n", len(table))

if __name__ == "__main__":
    number_of_elements = 1000
    
    table = generate_table(number_of_elements)

    print_table(table)

    table_sort = SelectionSort().run_algorithm(table)

    print_table(table_sort)
    
