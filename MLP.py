
from os.path import join, dirname, abspath
import xlrd
import numpy as np
import csv

fname = join(dirname(dirname(abspath(__file__))), 'Perceptrons', 'testingInputs.xlsx')
xl_workbook = xlrd.open_workbook(fname)

sheet_names = xl_workbook.sheet_names()
xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])

initialWeights = xl_sheet.row(1)
print(initialWeights)

# w13 = 0.5
# w14 = -0.45
# thresh3 = 1
#
# w23 = -0.45
# w24 = 0.5
# thresh4 = -1
#
# w35 = -0.3
# w45 = 0.3
# thresh5 = 0.1


w13 = float(input("Enter Weight 1 for Perceptron 3"))
w23 = float(input("Enter Weight 2 for Perceptron 3"))
thresh3 = 1

w14 = float(input("Enter Weight 1 for Perceptron 4"))
w24 = float(input("Enter Weight 2 for Perceptron 4"))
thresh4 = -1

w35 = float(input("Enter Weight 1 for Perceptron 5"))
w45 = float(input("Enter Weight 2 for Perceptron 5"))
thresh5 = 0.1

alpha = 0.3

class Perceptrons():
    weight1 = 0
    weight2 = 0
    thresh = 0
    output = 0

    def __init__(self, weight1, weight2, thresh):
        self.weight1 = weight1
        self.weight2 = weight2
        self.thresh = thresh

    def calculateOutput(self, input1, input2):
        summation = (input1 * self.weight1) + (input2 * self.weight2) - self.thresh
        output = self.sigmoid(summation)
        return output

        # sigmoid function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))


per1 = Perceptrons(w13, w23, thresh3)
per2 = Perceptrons(w14, w24, thresh4)
per3 = Perceptrons(w35, w45, thresh5)

# input dataset
input = np.array([[0, 0, 0],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 0]])



errors = 1
epoch = 1

while errors > 0.001:
    errors = 0
    epoch += 1
    # print("Epoch is:", epoch)
    # ================================================
    for i in range(4):
        x1 = input[i, 0]
        x2 = input[i, 1]

        per1output = per1.calculateOutput(x1, x2)
        per2output = per2.calculateOutput(x1, x2)

        per3output = per3.calculateOutput(per1output, per2output)

        # print("Output 1:", per1output)
        # print("Output 2:", per2output)
        # print("Output 3:", per3output)

        # ---------------------------------------------------------

        yd5 = input[i, 2]
        error = yd5 - per3output
        # print("Here is the error:", error)

        delta3 = per3output * (1 - per3output) * error

        # WEIGHT ADJUSTMENT FOR PERCEPTRON 3
        p3w1adjustment = alpha * per1output * delta3
        p3w2adjustment = alpha * per2output * delta3

        delta1 = per1output * (1 - per1output) * delta3 * per3.weight1
        delta2 = per2output * (1 - per2output) * delta3 * per3.weight2

        # print("Here is the new weightadjustment for perceptron3:", delta3)

        # WEIGHT ADJUSTMENT FOR PERCEPTRON 1 & 2
        p1w1adjustment = alpha * x1 * delta1
        p1w2adjustment = alpha * x2 * delta1

        p2w1adjustment = alpha * x1 * delta2
        p2w2adjustment = alpha * x2 * delta2

    #     WEIGHT UPDATES FINALLY!!!!
        per1.weight1 = per1.weight1 + p1w1adjustment
        per1.weight2 = per1.weight2 + p1w2adjustment

        per2.weight1 = per2.weight1 + p2w1adjustment
        per2.weight2 = per2.weight2 + p2w2adjustment

        per3.weight1 = per3.weight1 + p3w1adjustment
        per3.weight2 = per3.weight2 + p3w2adjustment

        errors += error * error


        # print("Sum of squared Error is:", errors)
#
# with open('h2pe1.csv', 'a') as file:
#     file.write(str())

    if epoch % 10000 == 0:
        print("Epoch:", epoch)
        print("Per3 weight1", per3.weight1)
        print("Per3 weight2", per3.weight2)
        print("Sum of squared Error is:", errors)

print("Epoch:", epoch)
print("Per3 weight1", per3.weight1)
print("Per3 weight2", per3.weight2)
print("Sum of squared Error is:", errors)

# ==================================================