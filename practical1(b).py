import os
import multiprocessing

def parent_task():
    print("Parent executing with its own code.")

def child_task():
    print("Child executing with its own code.")

if __name__ == "__main__":
    print("Parent executing same program with different code.")

    # Create a child process
    child_process = multiprocessing.Process(target=child_task)
    child_process.start()
    child_process.join()  # Wait for the child process to finish

    # Execute parent's task
    parent_task()


    #  output:

#  ⚡kushkumarkashyap7280 ❯❯ /usr/bin/python3 "/home/kushkumarkashyap7280/Desktop/practicals/practical1(b).py"
# Parent executing same program with different code.
# Child executing with its own code.
# Parent executing with its own code.