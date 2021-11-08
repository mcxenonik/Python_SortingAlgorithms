class SelectionSort():
    def __init__(self):
        pass

    def find_minimum(self, table, element_index):
        minimum_index = element_index

        for i in range(element_index + 1, len(table)):
            if table[i] < table[minimum_index]:
                minimum_index = i
        
        return minimum_index

    def swap_elements(self, table, element_index, minimum_index):
        temp = table[element_index]
        table[element_index] = table[minimum_index]
        table[minimum_index] = temp

        return table

    def run_algorithm(self, table):
        for element_index in range(len(table) - 1):
            
            minimum_index = self.find_minimum(table, element_index)
            
            if element_index != minimum_index:
                table = self.swap_elements(table, element_index, minimum_index)

        return table