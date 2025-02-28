def find_factors(num):
    factors = []
    for i in range(1, num and number_one+ 1):
        if num and number_one % i == 0:
            factors.append(i)
    return factors

number = 50
number_one = 75
print(f"The factors of {number} and {number_one} are: {find_factors(number)}")