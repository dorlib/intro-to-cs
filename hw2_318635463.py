# Skeleton file for HW2 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw2_ID.py).
import random # loads python's random module in order to use random.random() in question 2

##############
# QUESTION 1 #
##############
#  Q1a
def divisors(n):
    allNumbers = [num for num in range(1,n)]
    dividers = [num for num in allNumbers if n/num == n//num]
    return dividers


#  Q1b
def perfect_numbers(n):
    perfectNums = []
    i = 0
    j = 1
    
    while i < n:
        allNumbers = [num for num in range(1,j)]
        dividers = [num for num in allNumbers if j/num == j//num]
        
        sum = 0

        for k in range(len(dividers)):
            sum += dividers[k]

        if sum == j:
            perfectNums.append(j)
            i += 1

        j += 1

    return perfectNums

#  Q1c
def abundant_density(n):
    abdundantNums = []
    i = 0
    j = 1
    
    while i < n:
        allNumbers = [num for num in range(1,j)]
        dividers = [num for num in allNumbers if j/num == j//num]
        
        sum = 0

        for k in range(len(dividers)):
            sum += dividers[k]

        if sum > j:
            abdundantNums.append(j)

        i += 1 
        j += 1

    density = len(abdundantNums)/n
    return density

#  Q1e
def semi_perfect_4(n):
    allNumbers = [num for num in range(1,n)]
    dividers = [num for num in allNumbers if n/num == n//num]
    bool = False
    
    for i in dividers:
        for j in dividers:
            for k in dividers:
                for l in dividers:
                    if (i!=j) & (i!=k) & (i!=l) & (j!=k) & (j!=l) & (k!=l):
                        if (i + j + k + l) == n:
                            bool = True
                            return bool 

    return bool

##############
# QUESTION 2 #
##############
# Q2a
def coin():
    f = random.random()
    bool = False

    if f >= 0.5:
        return True
    if f < 0.5:
        return False 


# Q2b
def roll_dice(d):
    import random
    f = random.random()
    
    for i in range(d):
        if (f > i/d) and ( f < (i+1)/d):
            return i+1
        

# Q2c
def roulette(bet_size, parity):
    f = roll_dice(37) - 1

    if f == 0:
        return 0

    evenOrOdd = "even"
    
    if f%2 != 0:
        evenOrOdd = "odd"

    if parity == evenOrOdd:
        return bet_size * 2

    if parity != evenOrOdd:
        return 0 
        

# Q2d
def roulette_repeat(bet_size, n):
    profit = 0
    par = "even"
    
    for i in range(n):
        c = coin()
        if c == True:
            par = "even"
        if c == False:
            par = "odd"

        res = roulette(bet_size, par)
        profit = profit - bet_size + res

    return profit

        
        
# Q2e
def shuffle_list(lst):
    length = len(lst)
    shuffled = [None]*length
    indexsUsed = []
    i = 0

    while i < len(lst):
        s = roll_dice(length)-1
        if s not in indexsUsed:
            shuffled[s] = lst[i]
            indexsUsed.append(s)
            i += 1 
        
    return shuffled


##############
# QUESTION 3 #
##############
# Q3a
def inc(binary):
    lst = [0] 
    for i in binary:
        if i == "1":
            lst.append(1)
        else:
            lst.append(0)

    length = len(lst)
    add = [0]*(length - 1) + [1]
    result = [None]*length
    
    
    for i in range(length):
        result[length-1-i] = add[length-1-i] + lst[length-1-i]
        if result[length-1-i] == 2 or result[length-1-i] == 3:
            result[length-1-i] -= 2 
            add[length-2-i] = 1

    if result[0] == 0:
        result.pop(result[0])

    res = ""
    
    for i in range(len(result)):
        res += str(result[i])

    return res   


# Q3b
def add(bin1, bin2):
    lst1 = [0]
    for i in bin1:
        if i == "1":
            lst1.append(1)
        else:
            lst1.append(0)

    lst2 = [0]
    for i in bin2:
        if i == "1":
            lst2.append(1)
        else:
            lst2.append(0)

    length = 0 
    len1 = len(lst1)
    len2 = len(lst2)
    diff = abs(len1-len2)

    if len1 > len2:
        lst2 = [0]*diff + lst2
        length = len1
    else:
        lst1 = [0]*diff + lst1
        length = len2

    result = [None]*length
    
    for i in range(length):
        result[length-1-i] = lst1[length-1-i] + lst2[length-1-i]
        if result[length-1-i] == 2 or result[length-1-i] == 3:
            result[length-1-i] -= 2 
            lst2[length-2-i] += 1
            
    if result[0] == 0:
        result.pop(result[0])

    res = ""
    
    for i in range(len(result)):
        res += str(result[i])

    return res


# Q3c
def pow_two(binary, power):
    b = binary + "0"*power
    return b


# Q3d
def div_two(binary, power):
    b = ""

    for i in range(len(binary) - power):
        b += binary[i]

    if b == "":
        b = "0"

    return b


# Q3e
def leq(bin1, bin2):
    if len(bin2) > len(bin1):
       return True
    elif len(bin1) > len(bin2):
        return False

    # if we got here, so len(bin1) == len(bin2)

    for i in range(len(bin1)):
        if (bin1[i] == "1" and bin2[i] == "1") or (bin1[i] == "0" and bin2 == "0"):
            continue
        elif bin1[i] == "0" and bin2[i] == "1":
            return True
        elif bin1[i] == "1" and bin2[i] == "0":
            return False
        
    #if we got here so len(bin1) == len(bin2)
    return True


# Q3f
def to_decimal(binary):
    sum = 0

    for i in range(len(binary)):
        if binary[i] == "1":
            sum += 2**(len(binary)-1- i)
            
    return sum 


##############
# QUESTION 4 #
##############
# Q4a
def lychrel_loops(n):
    bool = False
    num = str(n)
    counter = 0

    while bool == False:
        opposite_num = ""

        for i in range(len(num)):
            opposite_num += num[len(num) -1 - i]

        num = int(num) + int(opposite_num)
        num = str(num)

        new_opposite = ""

        for i in range(len(num)):
            new_opposite += num[len(num) -1 - i]

        counter += 1

        if new_opposite == num:
            bool = True

    return counter

# Q4b
def is_lychrel_suspect(n, t):
    bool = False
    suspect = False
    num = str(n)
    counter = 0

    while bool == False:
        opposite_num = ""

        for i in range(len(num)):
            opposite_num += num[len(num) -1 - i]

        num = int(num) + int(opposite_num)
        num = str(num)

        new_opposite = ""

        for i in range(len(num)):
            new_opposite += num[len(num) -1 - i]

        counter += 1

        if new_opposite == num:
            bool = True
            
        if counter > t:
            suspect = True
            return suspect

    return suspect



# Q4c
def lychrel_sort(numbers, t):
    not_suspect_numbers = []
    suspect_numbers = []

    for i in range(1,t+1):
        for num in numbers:
            b = is_lychrel_suspect(num, i)
            if b == False:
                if num not in not_suspect_numbers:
                    not_suspect_numbers.append(num)

    for num in numbers:
        if num not in not_suspect_numbers:
            suspect_numbers.append(num)
      
    return not_suspect_numbers + suspect_numbers

##############
# QUESTION 5 #
##############
# Q5a
def calculate_grades_v1(grades):
    total_list = []
    
    for i in range(len(grades)):
        hw_sum = 0
        hw_avg = 0
        total = 0
        
        for j in range(3):
            hw_sum += grades[i][1][j]
            
        hw_avg = hw_sum / 3

        if hw_avg > grades[i][0]:
            total = (hw_avg * 0.1) + (grades[i][0] * 0.9)
            total_list.append(total)

        if hw_avg <= grades[i][0]:
            total = grades[i][0]
            total_list.append(total)

    return total_list          
              

# Q5b
def calculate_grades_v2(grades, w, f):
    total_list = []
    
    for i in range(len(grades)):
        hw_sum = 0
        hw_avg = 0
        test_after_factor = 0 
        total = 0
        
        for j in range(3):
            hw_sum += grades[i][1][j]
            
        hw_avg = hw_sum / 3

        test_after_factor = f(grades[i][0])
        
        total = (hw_avg * (1-w)) + (test_after_factor * w)
        total_list.append(total)


    return total_list     

# Q5c_i
def calculate_grades_v3(grades, w):
    total_list = []
    
    for i in range(len(grades)):
        hw_sum = 0
        hw_avg = 0
        total = 0
        best_2_hws = []

        if grades[i][1][0] > grades[i][1][1]:
            if grades[i][1][1] > grades[i][1][2]:
                best_2_hws.extend([grades[i][1][0],grades[i][1][1]])
            else:
                best_2_hws.extend([grades[i][1][0],grades[i][1][2]])
        else:
            if grades[i][1][2] > grades[i][1][1]:
                best_2_hws.extend([grades[i][1][1],grades[i][1][2]])
            else:
                best_2_hws.extend([grades[i][1][1],grades[i][1][0]])
                
        for j in range(2):
            hw_sum += best_2_hws[j]
            
        hw_avg = hw_sum / 2

        total = (hw_avg * (1-w)) + (grades[i][0] * w)
        total_list.append(total)

    return total_list          


# Q5c_ii
def calculate_w(grades, target_average):
    total_list = []
    total_hw = 0
    
    for i in range(len(grades)):
        test_sum = 0 
        total = 0
        best_2_hws = []

        if grades[i][1][0] > grades[i][1][1]:
            if grades[i][1][1] > grades[i][1][2]:
                best_2_hws.extend([grades[i][1][0],grades[i][1][1]])
            else:
                best_2_hws.extend([grades[i][1][0],grades[i][1][2]])
        else:
            if grades[i][1][2] > grades[i][1][1]:
                best_2_hws.extend([grades[i][1][1],grades[i][1][2]])
            else:
                best_2_hws.extend([grades[i][1][1],grades[i][1][0]])
                
            hw_sum = best_2_hws[0] + best_2_hws[1]
            hw_avg = hw_sum / 2
            total_hw += (hw_avg)

    test_total = 0
    for i in range(len(grades)):
        test_total += grades[i][0]

    w = ((target_average*len(grades)-total_hw)/(test_total-total_hw))

    total_list = calculate_grades_v3(grades, w)
    total_final_grades = 0 
    for i in range(len(total_list)):
        total_final_grades += total_list[i]
    class_avg = total_final_grades/len(total_list)
        
    if abs(class_avg - target_average) < 0.000001:
        if w > 1 or w < 0 :
            return None
        return w
        
    #if we got here so there is no suitable W 
    return None


    
##########
# Tester #
##########

def test():
    if divisors(6) != [1, 2, 3] or divisors(7) != [1]:
        print("Error in Q1a")

    if perfect_numbers(2) != [6, 28]:
        print("Error in Q1b")

    if abundant_density(20) != 0.15:
        print("Error in Q1c")

    if not semi_perfect_4(20) or semi_perfect_4(28):
        print("Error in Q1e")

    for i in range(10):
        if coin() not in {True, False}:
            print("Error in Q2a")
            break

    for i in range(10):
        if roll_dice(6) not in {1, 2, 3, 4, 5, 6}:
            print("Error in Q2b")
            break

    for i in range(10):
        if (roulette(100, "even") not in {0, 200}) or (roulette(100, "odd") not in {0, 200}):
            print("Error in Q2c")
            break

    shuffled_list = shuffle_list([1, 2, 3, 4])
    for i in range(1, 5):
        if i not in shuffled_list:
            print("Error in Q2e")
            break

    if inc("0") != "1" or \
            inc("1") != "10" or \
            inc("101") != "110" or \
            inc("111") != "1000" or \
            inc(inc("111")) != "1001":
        print("Error in Q3a")

    if add("0", "1") != "1" or \
            add("1", "1") != "10" or \
            add("110", "11") != "1001" or \
            add("111", "111") != "1110":
        print("Error in Q3b")

    if pow_two("10", 2) != "1000" or \
            pow_two("111", 3) != "111000" or \
            pow_two("101", 1) != "1010":
        print("Error in Q3c")

    if div_two("10", 1) != "1" or \
            div_two("101", 1) != "10" or \
            div_two("1010", 2) != "10" or \
            div_two("101010", 3) != "101":
        print("Error in Q3d")

    if not leq("1010", "1010") or \
            leq("1010", "0") or \
            leq("1011", "1010"):
        print("Error in Q3e")

    if lychrel_loops(28) != 2 or lychrel_loops(110) != 1:
        print("Error in Q4a")

    if (not is_lychrel_suspect(28, 1)) or is_lychrel_suspect(28, 2) or is_lychrel_suspect(28, 3):
        print("Error in Q4b")

    if lychrel_sort([165, 164, 28, 110, 196], 8) != [110, 28, 165, 164, 196]:
        print("Error in Q4c")

    if lychrel_sort([165, 164, 28, 110, 196, 128], 8) != [110, 128, 28, 165, 164, 196]:
        print("Error in Q4c")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    if calculate_grades_v1(grades) != [95, 90.4]:
        print("Error in Q5a")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    w = 0.7
    f = lambda x: min(100, x + 3)
    if calculate_grades_v2(grades, w, f) != [95.6, 93.3]:
        print("Error in Q5b")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    w = 0.7
    if calculate_grades_v3(grades, w) != [94.25, 91.8]:
        print("Error in Q5c_i")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    target_average = 93.025  # This is the average of [94.25, 91.8]
    if abs(calculate_w(grades, target_average) - 0.7) > 0.000001:
        print("Error in Q5c_ii")


