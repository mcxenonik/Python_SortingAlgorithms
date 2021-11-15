from MergeSort import MergeSort
from SelectionSort import SelectionSort
from QuickSort import QuickSort
from BubbleSort import BubbleSort
from Utils import Utils

def run(input_file_name, number_of_elements_list):
    Utils.start_measurements(QuickSort, input_file_name, number_of_elements_list)

    Utils.start_measurements(MergeSort, input_file_name, number_of_elements_list)

    Utils.start_measurements(SelectionSort, input_file_name, number_of_elements_list)

    Utils.start_measurements(BubbleSort, input_file_name, number_of_elements_list)

if __name__ == "__main__":
    input_file_name = "pan-tadeusz.txt"
    number_of_elements_list = [n for n in range(1000, 68336, 5000)]            # MAX 68336

    run(input_file_name, number_of_elements_list)
