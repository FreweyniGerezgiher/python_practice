while True:    
    n = int(input("check this number: "))
    def prime_checker(number = n):
        x = 0
        for i in range(1, number + 1):
            if number % i == 0:
                x += 1
        if x >= 3:
            print(f"{number} is even")
        else:
            print(f"{number} is prime")
    prime_checker()

