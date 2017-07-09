#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def findIfExist(item, lst):
    if item in lst:
        return True;
    return False;
   
def getLenthOfArray(array):
    return len(array)

def checkNumExistInLst(lst):
    lenLst = len(lst)
    for num in range(1,lenLst+1):
        if( findIfExist(num,lst) == False ):
            return False;
    return True;

def checkRowValid(lst):
    for ele in lst:
        if( checkNumExistInLst(ele) == False ):
            return False;
    return True;

def buildCol(lst):
    buildArray = []
    lenOfLst = getLenthOfArray(lst);
    for colIndex in range(0,lenOfLst):
        rowArray = [];
        for rowIndex in range(0,lenOfLst):
            #print("[" + str(rowIndex) + "]" + "[" + str(colIndex) + "]" + str(lst[rowIndex][colIndex]))
            #print(lst[rowIndex][colIndex])
            rowArray.append(lst[rowIndex][colIndex]);
            #print(rowArray)
        #print("########")
        buildArray.append(rowArray);
    return buildArray;

def checkColValid(lst):
    colLst = buildCol(lst);
    return checkRowValid(colLst)

def check_sudoku(testLst):
    colValid = checkColValid(testLst);
    rowValid = checkRowValid(testLst);
    return (colValid and rowValid)
    print("##########")
    #return True;
    

#print (check_sudoku(incorrect))
#>>> False

#print (check_sudoku(correct))
#>>> True

print (check_sudoku(incorrect2))
#>>> False

#print (check_sudoku(incorrect3))
#>>> False

#print (check_sudoku(incorrect4))
#>>> False

#print (check_sudoku(incorrect5))
#>>> False


