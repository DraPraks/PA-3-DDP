import time


def partition(A, p, r):
    """
 Partition an array A[p..r] into two parts by selecting A[r] as the pivot.

 :param A: List of integers
 :param p: Starting index
 :param r: Ending index
 :return: The index position of the pivot after partitioning
 """
    pivot = A[r]  # Set pivot point
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]  # Swap elements
    A[i + 1], A[r] = A[r], A[i + 1]  # Place pivot in correct position
    return i + 1


def quicksort(A, p, r):
    """
 Recursively sorts the subarray IN PLACE A[p..r] using the QuickSort algorithm.

 :param A: List of integers
 :param p: Starting index
 :param r: Ending index
 """
    if p < r:
        q = partition(A, p, r)  # Partition the array and get pivot index
        quicksort(A, p, q - 1)  # Recursively sort the left subarray
        quicksort(A, q + 1, r)  # Recursively sort the right subarray


def main():
    input_filename = input("Enter the name of the input text file: ") # Assign the file path str to input_filename
    try:
        ifile = open(input_filename, 'r') # If all is good we should open the file and assign it to ifile
    except:
        print("Error: Unable to open the input file.") # If not, print an error message and return None
        return

    output_filename = input("Enter the name of the output text file: ") # Assign the file path str to output_filename
    try:
        ofile = open(output_filename, 'w')
    except:
        print("Error: Unable to open/create the output file.")
        ifile.close()  # Close the input file before exiting
        return

    # Constructing the list of numbers using list comprehension by iterating through each line in the input file
    try:
        numbers = [int(line.strip()) for line in ifile if line.strip()]
    except:
        print("Error: Input file contains non-integer values.")
        ifile.close()
        ofile.close()
        return

    # Measuring CPU and clock time
    t1 = time.time()  # Start clock time
    t = time.process_time()  # Start CPU time

    print("Sorting in progress ...")
    quicksort(numbers, 0, len(numbers) - 1)  # Initial call to quicksort as per pseudocode

    cpu_time = time.process_time() - t  # Calculate CPU time taken
    duration = time.time() - t1  # Calculate clock time taken

    # Writing the sorted numbers to the output file
    for number in numbers:
        ofile.write(str(number) + '\n')  # Write each number on a new line

    ofile.close()
    ifile.close()
    print("CPU time of the quicksort: ", cpu_time, "seconds")
    print("Clock time of the quicksort: ", duration, "seconds")


if __name__ == '__main__':
    main()
