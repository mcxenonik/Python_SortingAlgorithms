from SelectionSort import SelectionSort
from QuickSort import QuickSort
from Utils import Utils

if __name__ == "__main__":
    file_name = "pan-tadeusz.txt"
    # number_of_elements_list = [n for n in range(1000, 20000, 1000)]
    number_of_elements_list = [1000]

    Utils.start_measurements(SelectionSort, file_name, number_of_elements_list)

    Utils.start_measurements(QuickSort, file_name, number_of_elements_list)

