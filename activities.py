import arrays
import random
import time
import array_utils
import searches
import turtle
import sorts

def making_arrays():
    array_a = arrays.Array(5)
    array_b = arrays.Array(1,0)
    array_c = arrays.Array(10,"")
    array_d = arrays.Array(20,False)
    print(array_a)
    print(array_b)
    print(array_c)
    print(array_d)

def while_fill(an_array):
    length = len(an_array)
    i = 0
    while(i<length):
        an_array[i] = i
        i = i+1
    return an_array

def while_fill_for(an_array):
    for i in range(len(an_array)):
        an_array[i] = i
    return an_array

def roll_the_die(n_of_sides):
    return random.randint(1,n_of_sides)

def random_array(size, min_value=0, max_value=None):
    array = arrays.Array(size)
    if max_value == None:
        max_value = size
    range_new = range(size)
    for i in range_new:
        array[i] = random.randint(min_value,max_value)
    return array

def linear_search_timer(an_array, target):
    begin = time.perf_counter()
    searches.linear_search(an_array,target)
    end = time.perf_counter()
    elapsed = end - begin
    return elapsed

def linear_timer():
    array = array_utils.range_array(1,10000000)
    print("first:",linear_search_timer(array,1))
    print("middle:",linear_search_timer(array,5000000))
    print("last:",linear_search_timer(array,10000000))

def print_odds(an_array):
    for i in range(len(an_array)):
        if an_array[i] % 2 == 1:
            print(str(an_array[i]) + " ")

def print_odds_rec(an_array, index):
    if index < len(an_array):
        if an_array[index] % 2 == 1:
            print(an_array[index])
            print_odds_rec(an_array, index+1)
        else:
            print_odds_rec(an_array, index+1)

def countdown(number):
    if number < 0:
        return
    elif number == 0:
        print(number)
        return 0
    else:
        print(number)
        return number + countdown(number-1)

def factorial(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    else:
        return N * factorial(N-1)

def circles(radius,depth):
    rad = radius/2
    if depth==0:
        return None
    elif depth==1:
        turtle.circle(radius)
    else:
        dep = depth*depth
        for i in range(dep):
            turtle.penup()
            turtle.circle(radius,90)
            turtle.pendown()
            circles(rad,depth-1)


def count_up(number):
    if number >= 1:
        count_up(number-1)
        print(number)
    else:
        print(0)

def binary_search_timer(an_array, target):
    begin = time.perf_counter()
    searches.binary_search(an_array,target)
    end = time.perf_counter()
    elapsed = end - begin
    return elapsed

def binary_timer():
    array = array_utils.range_array(1,10000000)
    print("first:",binary_search_timer(array,1))
    print("middle:",binary_search_timer(array,5000000))
    print("last:",binary_search_timer(array,10000000))

def runner(function,number):
    print('running \''+function.__name__+'\' ...')
    result = function(number)
    print(result)

def evens(n):
    sum = 0
    n = range(n+1)
    for i in n:
        if i%2==0:
            sum = sum + i
    return sum
#==========================================================#
def insertion_sort_timer(an_array):
    begin = time.perf_counter()
    sorts.insertion_sort(an_array)
    end = time.perf_counter()
    elapsed = end - begin
    return elapsed

def insertion_timer():
    array = array_utils.range_array(1,5000)
    print("sorted:",insertion_sort_timer(array))
    random.seed(1)
    print("random:",insertion_sort_timer(random_array(5000,0,10000)))
    print("reverse:",insertion_sort_timer(array_utils.range_array(5000,0,-1)))
#==========================================================#
def main():
    insertion_timer()

if __name__ == "__main__":
    main()