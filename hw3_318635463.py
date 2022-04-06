import math
import random

# Q2 - C
def oct_to_fraction(octal):
    assert len(octal) == 12
    sum = 0

    for i in range(len(octal)):
        if octal[i] != 0:
            sum += (int(octal[i])*(8**(-(i+1))))

    return sum



# Q2 - D
oct_to_float = lambda octal: 0 if (octal == "0"*16 or octal == "1"+"0"*15) else ((1 if octal[0] == "0" else -1)*(8**((int(octal[1])*64)+(int(octal[2])*8)+(int(octal[3]))-255))*(1+7*(oct_to_fraction(octal[4:]))))

# Q2 - E
def is_greater_equal(oct1, oct2):
    if oct1[0] > oct2[0]:
        return False
    elif oct1[0] < oct2[0]:
        return True

    if oct1[0] == "0":
        for i in range(1,15):
            if oct1[i] > oct2[i]:
                return True
            if oct1[i] < oct2[i]:
                return False
        return True

    if oct1[0] == "1":
        for i in range(1,15):
            if oct1[i] > oct2[i]:
                return False
            if oct1[i] < oct2[i]:
                return True
        return True
        


# Q3 - A
def approx_root(x, eps):
    a = math.floor(1/x) + 1
    nums = []
    total = 0
    res = 1
    
    while x > ((eps**2) + (2*eps*total) + (total**2)):
        res *= (a)
        total += 1/(res)
        if total**2 > x:
            total -= 1/(res)
            res = res / a
            a += 1
        else:
            nums.append(a)
            
    return (nums,total)

# Q3 - B
def game():
    sum = 0
    counter = 0
    while sum < 1:
        sum += random.random()
        counter += 1

    return counter

def approx_e(N):
    total = 0

    for i in range(N):
        total += game()

    return (total/N)
    
	
# Q4 - A
def find(lst, s):
    n = len(lst)
    min = 0
    max = n-1
    while min <= max:
        mid = (min+max)//2
        if s == lst[mid]:
            return mid
        elif s == lst[mid-1]:
            return mid-1
        elif s == lst[mid+1]:
            return mid+1
        elif s < lst[mid]:
            max = mid-2
        else:
            min = mid+2
    return None


# Q4 - B
def sort_from_almost(lst):
    n = len(lst)
    i = 0

    while i < n-1:
        if lst[i] > lst[i+1]:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
            i += 2
        else:
            i += 1
            
    return lst


# Q4 - C
def generate_queries(k = 100, n = 1000):
    L = []
    for i in range(n):
        L.append(random.randint(0, k-1))
    
    def q_g(m):
        size = 0
        for i in range(n): 
            if L[i]>m: size +=1
        return size
    
    def q_l(m):
        size = 0
        for i in range(n): 
            if L[i]<m: size +=1
        return size

    return q_l, q_g

k = 100000
n = 100
q_l, q_g = generate_queries(k, n)


def compute_median(q_l, q_g, k, n):
    max = k-1
    min = 0

    while min <= max:
        mid = (max + min) // 2
        smaller = q_l(mid)
        greater = q_g(mid)
        if smaller == greater:
            return mid
        elif smaller > greater:
            max = mid - 1
        else:
            min = mid + 1

    return None
                
# Q5 - A
def string_to_int(s):
    di = {'a':0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
    sum = 0
    n = len(s)
    
    for i in range(n):
        sum += di[s[n-1-i]]*(5**(i))
        
    return sum


# Q5 - B
def int_to_string(k, n):
    di = {0:'a',1:'b',2:'c',3:'d',4:'e'}
    result = ""
    i = 1
    
    while i <= k:
        result = di[(n//(5**(i-1)) % 5)] + result
        i += 1
                 
    return result


# Q5 - C
def sort_strings1(lst, k):
    result = []
    helper_lst = []
    for i in range(5**k):
        helper_lst.append(-1)

    for char in lst:
        res = string_to_int(char)
        helper_lst[res] = res

    for i in range(0, 5**k):
        if helper_lst[i] != -1:
            result.append(int_to_string(k, i))

    return result

# Q5 - E
def sort_strings2(lst, k):
    result = []

    for i in range(5**k):
        helper = int_to_string(k,i)
        for string in lst:
            if helper == string:
                result.append(string)

    return result
            


##########
# Tester #
##########
def test():
    # Q2 - C
    if oct_to_fraction('621000000000') != 0.783203125 or oct_to_fraction('202200000000') != 0.25439453125:
        print('error in oct_to_fraction')
    # Q2 - D
    if oct_to_float('0400621000000000') != 51.859375:
        print("error in oct_to_float")
    # Q2 - E
    if is_greater_equal('0401010000000000', '0400010000000000') == False or \
       is_greater_equal('0400007777777777', '0400010000000000') == True:
        print("error in is_greater_equal")
    # Q3 - A
    if approx_root(2, 0.1) != ([1, 3], 1 + 1/3):
        print("error in approx_root (1)")
    if approx_root(2, 0.02) != ([1, 3, 5], 1 + 1/3 + 1/15):
        print("error in approx_root (2)")
    if approx_root(2, 0.001) != ([1, 3, 5, 5], 1 + 1/3 + 1/15 + 1/75):
        print("error in approx_root (3)")
    # Q3 - B
    if abs(approx_e(1000000) - math.e) > 0.01:
        print("MOST LIKELY there's an error in approx_e (this is a probabilistic test)")

    # Q4 - A
    almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]
    if find(almost_sorted_lst, 5) != 3:
        print("error in find")
    if find(almost_sorted_lst, 50) != None:
        print("error in find")
    
    # Q4 - B
    if sort_from_almost(almost_sorted_lst) != sorted(almost_sorted_lst):
        print("error in sort_from_almost")
    
    # Q4 - C
    M = compute_median(q_l, q_g, k, n)
    if not ((q_l(M) <= n//2) and (q_g(M) <= n//2)):
        print("error in compute_median")
    
    # Q5
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if string_to_int(s) != i:
            print("error in int_to_string and/or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    if sort_strings1(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")
