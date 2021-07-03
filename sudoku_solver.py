def get_empty_place(arr,l):
    for i in range(9):
        for j in range(9):
            if(arr[i][j]==0):
                l[0]=i
                l[1]=j
                return True
    return False
def check_row(arr,row,val):
    if val in arr[row]:
        return False
    return True
def check_column(arr,col,num):
    for i in range(9):
        if(arr[i][col] == num):
            return False
    return True
def check_box(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row-row%3][j+col-col%3] == num):
                return False
    return True
def check_suitable(arr,row,col,num):
    return check_row(arr,row,num) and check_column(arr,col,num) and check_box(arr,row,col,num)
def sudoku_solver(arr):
    l=[0,0]
    if(not get_empty_place(arr,l)):
        return True
    row=l[0]
    col=l[1]
    for num in range(1,10):
        if(check_suitable(arr,row,col,num)):
            arr[row][col]=num
            if(sudoku_solver(arr)):
                return True
            arr[row][col] = 0
    return False
question=[]
for i in range(9):
    l = list(map(int,input().split()))
    question.append(l)
if(sudoku_solver(question)):
    for i in range(9):
        print(question[i])
else:
    print("Question is wrong,no solution exists for given question.")
