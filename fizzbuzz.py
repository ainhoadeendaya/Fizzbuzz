def fizz_buzz(max_num):

    for num in range(1,max_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuz")   
        elif num % 3 == 0:
            print("fizz")    
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)
    num += 1

fizz_buzz(54)