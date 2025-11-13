import multiprocessing

def child_process():
    print("Child executing same program with same code.")

def main():
    process = multiprocessing.Process(target=child_process)
    process.start()
    process.join()
    print("Parent executing same program with same code.")

if __name__ == "__main__":
    main()


    #  output:
#      kushlinux    \Desktop\practicals   0ms   10:15 AM   
#  ⚡kushkumarkashyap7280 ❯❯ /usr/bin/python3 "/home/kushkumarkashyap7280/Desktop/practicals/practical1(a).py"
# Child executing same program with same code.
# Parent executing same program with same code.
