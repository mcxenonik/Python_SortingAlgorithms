class BubbleSort():
    def __init__(self):
        pass

    def __str__(self):
        return "BubbleSort"

    @staticmethod
    def run_algorithm(table):
        table_len = len(table)
        for i in range(table_len):
            is_swap = False
            for j in range(0, table_len - i - 1):
                if table[j] > table[j + 1]:
                    table[j], table[j+1] = table[j+1], table[i]
                    is_swap = True
            if not is_swap:
                break

        # return table
        return table
