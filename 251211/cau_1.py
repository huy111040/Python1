import random
# cau a
def generate_list(n):
    list = []
    for _ in range(n):
        random_number = random.randint(1, 100)
        list.append(random_number)
    return list

#cau b
def check_prime(number):
    if number < 2 :
        return False
    i = 2
    for i in range(2, number//2):
        if number % i == 0:
            return False
    return True

#cau c
def prime_numbers(list_numbers):
    prime_list = []
    for number in list_numbers:
        if check_prime(number):
            prime_list.append(number)
    return prime_list

numbers = generate_list(10)
print("Danh sách:", numbers)

primes = prime_numbers(numbers)
print("Các số nguyên tố trong danh sách:", primes)
