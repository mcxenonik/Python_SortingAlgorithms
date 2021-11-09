import matplotlib.pyplot as plt
from random import randint

import time
import gc

class Utils():
    def __init__(self):
        pass

    def _clear_words(words_list, number_of_elements):
        illegal_chars = [",", ".", "?", "!", ";", ":", "-", "–", "—", "/", "(", ")", "…", 
                        "»", "«", "*", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        table = []

        for word in words_list:
            for char in word:
                if (char in illegal_chars):
                    word = word.replace(char, "")
            
            if (word != ""):
                table.append(word)

            if (len(table) == number_of_elements):
                break

        return table

    def _generate_table_of_randint(number_of_elements):
        table = [randint(0, number_of_elements) for i in range(number_of_elements)]

        return table

    def _generate_table_from_file(file_name, number_of_elements):
        with open(file_name, encoding='utf8') as file:
            words_list = file.read().lower().split()

        table = Utils._clear_words(words_list, number_of_elements)

        return table

    def _print_table(table):
        print("TABLE:")
        print("-------------------------")

        for element in table:
            print(element, end=" | ")

        print("\n-------------------------")
        print("NUMBER OF ELEMENTS: ", len(table), "\n")

    def _draw_plot(xpoints, ypoints):
        plt.plot(xpoints, ypoints)
        plt.savefig("Plot.png")
        # plt.show()

    def _measure_time(algorithm, table):
        gc_old = gc.isenabled()
        gc.disable()

        start = time.process_time()
        table_sorted = algorithm.run_algorithm(table)
        stop = time.process_time()

        if (gc_old): 
            gc.enable()

        # Utils._print_table(table_sorted)

        return stop - start

    @staticmethod
    def start_measurements(algorithm, file_name, number_of_elements_list):
        ypoints = []

        for number_of_elements in number_of_elements_list:
            table = Utils._generate_table_from_file(file_name, number_of_elements)
            process_time = Utils._measure_time(algorithm, table)
            ypoints.append(process_time)

            print('PROCESS TIME: ', format(process_time, '.10f'))

        Utils._draw_plot(number_of_elements_list, ypoints)
