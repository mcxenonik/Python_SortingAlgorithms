class SelectionSort():
    def __init__(self):
        pass

    def __str__(self):
        return "SelectionSort"
    
    def _find_minimum(table, element_index):
        minimum_index = element_index

        for i in range(element_index + 1, len(table)):
            if (table[i] < table[minimum_index]):
                minimum_index = i
        
        return minimum_index

    def _swap_elements(table, element_index, minimum_index):
        table[element_index], table[minimum_index] = table[minimum_index], table[element_index]

        return table

    @staticmethod
    def run_algorithm(table):
        for element_index in range(len(table) - 1):
            
            minimum_index = SelectionSort._find_minimum(table, element_index)
            
            if (element_index != minimum_index):
                table = SelectionSort._swap_elements(table, element_index, minimum_index)

        return table
