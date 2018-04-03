# this is the reuse python file from where we can take the function and reuse it in other files

import logging             # importing logging module
import time                # importing time module
import os                  # importing os module


def lineTime(sec):
    # this function will print a blank line and stops the time for 'sec' seconds
    print()
    time.sleep(sec)        # stopping the time for 0.5 seconds


def logException(msg):
    # this function will take 'msg' which is string message and write it in logging file
    for files in os.listdir():
        # searching for tableLogFile.log file
        if(files == 'tableLogFile.log'):
            # if file is found then we pass the if clause
            pass
    else:
        # if file is not found then make a new file
        logging.basicConfig(filename='tableLogFile.log', level=logging.INFO, format='%(asctime)s : %(message)s')

    logging.info(msg)        # and writing down the message 'msg' into the log file


def inputInfo(value):
    # this function will look for input based upon the value
    while True:
        # try-except clause
        try:
            if(value == 'colTotal'):
                x = int(input('Enter Total Number of Columns Required :- ').strip())
                # asking for total number of columns required

            elif(value == 'rowTotal'):
                x = int(input('Enter Total Number of Rows Required :- ').strip())
                # asking for total number of rows required

            break

        except ValueError:
            # if ValueError is caught
            lineTime(sec=0.5)    # using lineTime function, sec = 0.5
            print('Invalid Input')
            lineTime(sec=0.5)    # using lineTime function, sec = 0.5

    return(x)


def inputInfoLoop(value, num, num2, l):
    # this function will look for input based upon the value for loop
    while True:
        # try-except clause
        try:
            if(value == 'colInfo'):
                x = input(f'Enter Description in Column {num} :- ').strip()
                # asking for description in particular columns
                logException(msg=f'{x} is the column number {num}')                         # using logException function

            elif(value == 'rowInfo'):
                x = input(f'Enter Description in {l[num-1]} For Row {num2}:- ').strip()
                # asking for description for particular row
                logException(msg=f'{x} is the description for {l[num-1]} for row {num2}')   # using logException function

            break

        except ValueError:
            # if ValueError is caught
            cr.lineTime(sec=0.5)    # using lineTime function, sec = 0.5
            print('Invalid Input')
            cr.lineTime(sec=0.5)    # using lineTime function, sec = 0.5

    return(x)

# the end of the program
# Programmed By Slothfulwave@612
