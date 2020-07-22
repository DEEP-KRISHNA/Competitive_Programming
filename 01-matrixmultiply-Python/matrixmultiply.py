# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    si1 = len(m1[0])
    for i in m1:
        if (si1 != len(i)):
            return None
    si2 = len(m2[0])
    for i in m2:
        if (si2 != len(i)):
            return None
    if (si1 != len(m2)):
        return None
    else:
        fnllst = []
        for k in range(len(m1)):
            lst = []
            for i in range(len(m2[0])):
                summ = 0
                for j in range(len(m1[0])):
                    summ = summ + m1[k][j] * m2[j][i]
                lst.append(summ)
            fnllst.append(lst)
        return fnllst

if __name__ == "__main__":
    fun_matrixmultiply([[1, 3], [2, 4], [2, 5]], [[1, 3, 2, 2], [2, 4, 5, 1]])




