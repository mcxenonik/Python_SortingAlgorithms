from SelectionSort import SelectionSort
from QuickSort import QuickSort
from Utils import Utils

if __name__ == "__main__":
    input_file_name = "pan-tadeusz.txt"
    number_of_elements_list = [n for n in range(10000, 30000, 5000)]

    Utils.start_measurements(QuickSort, input_file_name, number_of_elements_list)

    Utils.start_measurements(SelectionSort, input_file_name, number_of_elements_list)

