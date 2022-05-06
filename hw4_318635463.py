
# Skeleton file for HW4 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_ID.py).
import math

##############
# Question 1 #
##############
# 1b
def change_v2(amount, coins):
    lst = []

    def change(checked, balance, result):
        if balance == 0:
            lst.append(result)
            return
        if checked < 0:
            return
        if balance >= coins[checked]:
            change(checked, balance - coins[checked], result + [coins[checked]])
        change(checked -1, balance, result)
    change(len(coins)-1, amount, [])
    return lst

# 1c_ii
def winnable_mem(board):
    d = {}
    return winnable_mem_rec(board, d)

def winnable_mem_rec(board, d):

    if sum(board)==0:
        d[tuple(board)] = True
        return True

    if tuple(board) in d:
        return d[tuple(board)]

    m = len(board)
    
    for i in range(m): 
        for j in range(board[i]): 
            munched_board = board[0:i] + [min(board[k], j) for k in range(i,m)]
            if not winnable_mem_rec(munched_board, d): 
                d[tuple(board)] = True
                return True
            
    d[tuple(board)] = False
    return False

##############
# Question 2 #
##############
# 2a
def legal_path(A, vertices):
    for i in range (len(vertices)-1):
        if A[vertices[i]][vertices[i+1]] != 1:
            return False
        
    return True
        

# 2c
def path_v2(A, s, t, k):
    if k == 0:
        return s == t
    
    if k == 1 :
        if A[s][t] == 1:
            return True
        else:
            return False
            
    for i in range(len(A)):
        mid = k // 2
        if path_v2(A, s, i, mid) and path_v2(A, i, t, k - mid):
            return True
    return False


# 2d # Fix this code without deleting any existing code #
def path_v3(A, s, t):
    if s == t:
        return True

    for i in range(s,len(A)):
        if A[s][i] == 1:
            if path_v3(A, i, t):
                return True
    return False


path_v3_a = None  # Replace with an example of an input if the claim is true
path_v3_b = ([[0,1,1],[1,0,0],[0,1,0]],0,2)
path_v3_c = None  # Replace with an example of an input if the claim is true
path_v3_d = ([[0,1,1,0,0],[1,0,1,0,0],[0,0,0,1,0],[1,0,0,0,0],[0,0,0,0,0]],0,4)


##############
# Question 3 #
##############
# 3a
def can_create_once(s, L):
    if s == 0 and L == []:
        return True
    if s != 0 and L == []:
        return False
    result = False
    res1 = can_create_once(s-L[0],L[1:])
    res2 = can_create_once(s+L[0],L[1:])
    
    if res1 or res2 == True:
        result = True
    
    return result

        

# 3b   
def can_create_twice(s, L):
    if s == 0 and L == []:
        return True
    if s != 0 and L == []:
        return False
    result = False
    res1 = can_create_twice(s-L[0],L[1:])
    res2 = can_create_twice(s+L[0],L[1:])
    res3 = can_create_twice(s+2*L[0], L[1:])
    res4 = can_create_twice(s-2*L[0], L[1:])
    res5 = can_create_twice(s, L[1:])
    
    if res1 or res2 or res3 or res4 or res5 == True:
        result = True
    
    return result  
        

# 3c
def valid_braces_placement(s, L):
    global res
    res = []
    return valid(s, L)

def valid(s, L):
    global res
    remain = ''

    if isinstance(L[0], int):
        for i in range (len(L)):
            L[i] = str(L[i])
    else:
        remain = L[0]
        L = L[1:]

        
    if '*' in L:
        index = L.index('*')
        for i in range(0,index, 2):
            for j in range(i,index, 2):
                temp = [remain + '(' + ''.join(L[:i + 1]) + ')' + ''.join(L[i + 1 : min(j + 2, index)])+ (''.join(L[j + 2:index])) + '*'] + L[index + 1:]
                result = valid(s, temp)
                res.append(result)
        return bool(sum(res))

    else:
        temp = []
        for i in range(0, len(L), 2):
            temp.append(eval(remain + '(' + ''.join(L[:i + 1]) + ')' + ''.join(L[i + 1:])))
        return s in temp
                            
    
##############
# Question 4 #
##############
# 4a
def grid_escape1(B):
    global n
    n = len(B)
    left = 0
    right = 0

    return grid_escape1_rec(B, left, right)

def grid_escape1_rec(B, left, right):
    global n
    
    if left == n-1 and right == n-1 :
        return True
    if left > n-1 or right > n-1:
        return False

    num = B[left][right]
    
    res1 = grid_escape1_rec(B,left + num, right)
    res2 = grid_escape1_rec(B,left, right + num)

    return res1 or res2
 

# 4b
def grid_escape2(B):
    global n
    n = len(B)
    left = 0
    right = 0
    mem = {}

    return grid_escape2_rec(B, left, right, mem)

def grid_escape2_rec(B, left, right, mem):
    global n

    if (left,right) in mem:
        return mem[(left,right)]
    if left == n-1 and right == n-1:
        return True
    if left > n-1 or right > n-1 or left < 0 or right < 0:
        return False
    
    res1 = grid_escape2_rec(B,left, right + B[left][right], mem)
    res2 = grid_escape2_rec(B,left + B[left][right], right, mem)
    
    mem[(left,right)] = res1 or res2
    
    if res1 == False and res2 == False:
        res3 = grid_escape2_rec(B,left, right - B[left][right], mem)
        res4 = grid_escape2_rec(B,left - B[left][right], right, mem)
        mem[(left,right)] = res3 or res4
        return res3 or res4     
    
    return res1 or res2

##########
# Tester #
##########
def test():
    # 1b
    if len(change_v2(5, [1, 2, 3])) != 5:
        print("error in change_v2")

    # 1c
    if winnable_mem([5, 5, 3]) or not winnable_mem([5, 5, 5]):
        print("error in winnable_mem")

    # 2a
    A = [[0, 1, 1, 0, 0], [1, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    if not legal_path(A.copy(), [0, 1, 2, 3]) or \
            not legal_path(A.copy(), [0, 1, 2, 3, 0, 1]) or \
            legal_path(A.copy(), [1, 2, 3, 4]):
        print("error in legal_path")

    # 2d
    if path_v3_a != None and not path_v3(path_v3_a[0], path_v3_a[1], path_v3_a[2]):
        print("error in path_v3 or with path_v3_a")

    if path_v3_b != None and not path_v3(path_v3_b[0], path_v3_b[1], path_v3_b[2]):
        print("error in path_v3 or with path_v3_b")

    if path_v3_c != None and path_v3(path_v3_c[0], path_v3_c[1], path_v3_c[2]):
        print("error in path_v3 or with path_v3_c")

    if path_v3_d != None and path_v3(path_v3_d[0], path_v3_d[1], path_v3_d[2]):
        print("error in path_v3 or with path_v3_d")

    # 3a
    if not can_create_once(6, [5, 2, 3]) or not can_create_once(-10, [5, 2, 3]) \
            or can_create_once(9, [5, 2, 3]) or can_create_once(7, [5, 2, 3]):
        print("error in can_create_once")
    # 3b
    if not can_create_twice(6, [5, 2, 3]) or not can_create_twice(9, [5, 2, 3]) \
        or not can_create_twice(7, [5, 2, 3]) or can_create_once(19, [5, 2, 3]):
        print("error in can_create_twice")
    # 3c
    L = [6, '-', 4, '*', 2, '+', 3]
    if not valid_braces_placement(10, L.copy()) or \
            not valid_braces_placement(1, L.copy()) or \
            valid_braces_placement(5, L.copy()):
        print("error in valid_braces_placement")

    B1 = [[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]
    B2 = [[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]
    B3 = [[2, 1, 2, 1], [1, 2, 1, 1], [2, 2, 2, 2], [4, 4, 4, 4]]

    # 4a
    if not grid_escape1(B1.copy()):
        print("error in grid_escape1 - B1")
    if grid_escape1(B2.copy()):
        print("error in grid_escape1 - B2")
    if grid_escape1(B3.copy()):
        print("error in grid_escape1 - B3")

    # 4b
    if not grid_escape2(B1.copy()):
        print("error in grid_escape2 - B1")
    if not grid_escape2(B2.copy()):
        print("error in grid_escape2 - B2")
    if grid_escape2(B3.copy()):
        print("error in grid_escape2 - B3")
