class QuickSort():
    def __init__(self):
        pass

    def __str__(self):
        return "QuickSort"

    @staticmethod
    def run_algorithm(table, l = 0, r = None):
        if (r is None): 
            r = len(table) - 1

        i = l
        j = r

        pivot = table[int((l + r) / 2)]

        while i <= j:
            while table[i] < pivot: 
                i += 1

            while table[j] > pivot: 
                j -= 1

            if i <= j:
                table[i], table[j] = table[j], table[i]
                i += 1 
                j -= 1

        if l < j: 
            QuickSort.run_algorithm(table, l, j) 
        if r > i: 
            QuickSort.run_algorithm(table, i, r)

        return table
