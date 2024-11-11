def partition(A, p, r):
 .
 .
 .
 return …
def quicksort(A, p = …, r = …):
 .
 .
 .

import time
def main():
 #asking and validating input from user
 .
 .
 .
 try:
 .
 .
 .
 except .......:
 .
 .
 .
 #constructing the list of numbers, using list comprehension
 numbers = ........
 t1 = time.time()
 t = time.process_time()

 print("Sorting in progress ...")
 quicksort(numbers)

 cpu_time = .................
 duration = .................


 #writing the sorted numbers to the output file
 .............

 ifile.close()
 ofile.close()
 print("CPU time of the quicksort: ", cpu_time)
 print("Clock time of the quicksort: ", duration)
if __name__ == '__main__':
 main()