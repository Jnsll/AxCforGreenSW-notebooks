import random
import sys
import time

def task(count):
    result = count + random.randrange(10)
    #print("Task #", count)
    return result


def loop_reference(number_iterations):
    for count in range(1, number_iterations+1):
        task(count)

def loop_perforation(number_iterations, perforation_step):
    try:
        for count in range(1, number_iterations+1, perforation_step):
            task(count)
    except:
      print("Error. Please, check that your input number is a non null integer!")
        #if (count%3):
        #    task(count)


if __name__ == "__main__":
    #print(sys.argv[1])
    #start = time.time()
    if str(sys.argv[1]) == "reference":
        loop_reference(int(sys.argv[2]))
    else:
        loop_perforation(int(sys.argv[2]), int(sys.argv[3]))
    
    #end = time.time()
    #print("Duration (s):", str(end-start))