# this file will contain the class which will contain our main function
# from reading the input to displaying the information into a tabular format

import tableReuse as tr             # importing tableReuse file as tr


class makingTable:
    # class named makingTable for creating table

    def __init__(self, colTotal, rowTotal, colList, rowList, maxLength):
        # using init function in order to initilise the data members
        self.colTotal = colTotal        # integer variable for storing number of columns
        self.rowTotal = rowTotal        # integer variable for storing number of rows
        self.colList = colList          # list for storing the column names
        self.rowList = rowList          # list for storing the information for the row
        self.maxLength = maxLength      # list for storing maximum length of the member in the table

    def inputColRow(self):
        # this function is for inputting total number of rows and column required
        tr.lineTime(sec=0.5)                            # using lineTime function, sec = 0.5

        self.colTotal = tr.inputInfo(value='colTotal')  # using inputInfo function, value = 'colTotal'

        tr.logException(msg=f'{self.colTotal} is the total number of columns')  # using logException function

        tr.lineTime(sec=0.5)                            # using lineTime function, sec = 0.5

        self.rowTotal = tr.inputInfo(value='rowTotal')  # using inputInfo function, value = 'infoTotal'

        tr.logException(msg=f'{self.rowTotal} is the total number of rows')     # using logException function

    def writeColInfo(self):
        # this function will input the column names and append the inputted information into colList

        tr.lineTime(sec=0.5)                            # using lineTime function, sec = 0.5

        for i in range(self.colTotal):
            y = tr.inputInfoLoop(value='colInfo', num=i+1, num2=None, l=None)      # using inputInfo function
            self.colList.append(y)                          # appending the column name in colList
            tr.lineTime(sec=0.5)                            # using lineTime function, sec = 0.5

    def writeRowInfo(self):
        # this function will input the row names and append the inputted information into rowList

        tr.lineTime(sec=0.5)                            # using lineTime function, sec = 0.5

        for i in range(self.rowTotal):
            for j in range(self.colTotal):
                y = tr.inputInfoLoop(value='rowInfo', num=j+1, num2=i+1, l=self.colList)  # using inputInfo function
                self.rowList.append(y)                                      # appending the row inforamtion into rowList
                tr.lineTime(sec=0.5)                            # using lineTime function, sec = 0.5

    def findMaxLength(self):
        # this function will find out the maximum length of the string in the colList and rowList and append it in maxLength
        c = 0                         # assigning the value zero to variable c

        for i in range(self.colTotal):
            temp = len(self.colList[i])
            for j in range(c, len(self.rowList), self.colTotal):
                if(len(self.rowList[j]) > temp):
                    temp = len(self.rowList[j])
            self.maxLength.append(temp)
            c += 1
        # appending the maximum length of the element for each column and it's description in maxLength

    def printColumn(self):
        # this function is for printing down the column names in the screen in tabular format

        tr.lineTime(sec=0.5)                            # using lineTime function, sec = 0.5

        dashes = 0
        c = 0
        # assigning the value zero to variable c and dashes

        for i in self.colList:
            dashes += len('| ' + i + ' ' * (self.maxLength[c] - len(i)) + ' |')  # adding the length for each column name with | in dashes
            print('| ' + i + ' ' * (self.maxLength[c] - len(i)) + ' |', end='')  # printing out the column names
            c += 1                                                              # incrementing the value of c by 1
        print(end='\n')

        print('=' * dashes)     # printing down '=' equal to the total length of column line

    def printRow(self):
        # this function is for printing down the row names in the screen in tabular format

        c = 0

        for i in self.rowList:
            print('| ' + i + ' ' * (self.maxLength[c] - len(i)) + ' |', end='')  # printing out the row names
            c += 1                                                              # incrementing the value of c by 1

            if(c == self.colTotal):
                c = 0
                print(end='\n')             # for jumping into another line

# the end of the program
# Programmed By Slothfulwave@612
