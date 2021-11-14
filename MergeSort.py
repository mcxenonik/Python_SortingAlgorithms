class MergeSort():
    def __init__(self):
        pass

    def __str__(self):
        return "MergeSort"

    def _merge(table_a, table_b):
        if table_a[-1] <= table_b[0]:
            return table_a + table_b
        len_a, len_b = len(table_a), len(table_b)
        i, j = 0, 0

        table = []
        k = 0
        while(i < len_a and j < len_b):
            if table_a[i] < table_b[j]:
                table.append(table_a[i])
                i += 1
            else:
                table.append(table_b[j])
                j += 1            
            k += 1

        for m in range(i, len_a):
            table.append(table_a[m])
            k += 1
            
        for m in range(j, len_b):
            table.append(table_b[m])
            k += 1

        return table

    def _sort(table):
        if len(table) <= 1:
            return table
        mid = len(table) // 2
        table_a = table[:mid]
        table_b = table[mid:]  
        table_a = MergeSort._sort(table_a)
        table_b = MergeSort._sort(table_b)
        table = MergeSort._merge(table_a, table_b)
        return table

    @staticmethod
    def run_algorithm(table):
        table = MergeSort._sort(table)
        return table
