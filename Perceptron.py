# THIS ASSIGNMENT HAS BEEN DONE USING PYTHON 3.


# from __future__ import print_function
from os.path import join, dirname, abspath
import xlrd

# os.chdir("../../Dropbox/WSU/Machine Learning/HW/")
#
# print(os.getcwd())

fname = join(dirname(dirname(abspath(__file__))), 'Perceptrons', 'data.xlsx')
xl_workbook = xlrd.open_workbook(fname)

# List sheet names, and pull a sheet by name

sheet_names = xl_workbook.sheet_names()
# print('Sheet Names', sheet_names)

# print(sheet_names[0])
# print(sheet_names[1])

xl_sheet1 = xl_workbook.sheet_by_name(sheet_names[0])
xl_sheet2 = xl_workbook.sheet_by_name(sheet_names[1])

# Pull the first row by index
#  (rows/columns are also zero-indexed)

x1 = xl_sheet1.row(0)
x2 = xl_sheet1.row(1)
# print(type(x1))

x1.extend(xl_sheet2.row(0))
x2.extend(xl_sheet2.row(1))

# Print 1st row values and types
# from xlrd.sheet import ctype_text
# print('(Column #) type:value')

# for idx, cell_obj in enumerate(x):
#     print(cell_obj.value)

# print(len(x1))

# for each in x1:
#     # print(x1[0].value)
#     print(each.value)

epoch = 0

error = 1

# STEP1: INITIALIZATION
x1w = 1.0
x2w = -2.0
thresh = -2.0
alpha = 0.2

def desiredOutFor(index):
    # so all apples desired out is 1, everything else is 0
    if(index <= 9):
        return 1
    else:
        return 0


def actualOut(sumSigma):
    if (sumSigma <= 0):
        return 0
    else:
        return 1

# def weightTraining():

counter = 1

# STEP4: ITERATION
while counter > 0:
# for i in range(1):
    epoch +=1
    counter = 0

    # print("Epoch", epoch, "!")

    for eachX1, eachX2 in zip(x1, x2):

        # STEP2: ACTIVATION

        # print(eachX1.value, " and ", eachX2.value)
        summation = (eachX1.value * x1w) + (eachX2.value * x2w) - thresh

        actualOutput = actualOut(summation)
        # print("Actual Output for:", eachX1.value, " and ", eachX2.value , " is: ", actualOutput)
        # if actualOutput > 0:
            # print("Number", x1.index(eachX1), "is an apple")
        # else:
            # print("Number", x1.index(eachX1), "is an orange")

        # print("Desired Output for:", x1.index(eachX1), "is: ", desiredOutFor(x1.index(eachX1)))
        desiredOutput = desiredOutFor(x1.index(eachX1))

        error = desiredOutput - actualOutput
        print(error)
        # print("Step value for", x1.index(eachX1), "and", "is:", error)

        # STEP3: WEIGHT TRAINING
        if error != 0:
            counter += 1
            x1w = x1w + (alpha * eachX1.value * error)
            print(x1w,";",x2w)
            x2w = x2w + (alpha * eachX2.value * error)


        # with open('weight2.csv', 'a') as file:
        #     file.write(str(x2w))
# print(x1w,";",x2w)