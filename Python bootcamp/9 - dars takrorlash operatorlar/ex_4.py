def reverse_digits(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num

def reverse_numbers():
    numbers = input("Istalgan son ").split()
    numbers = [int(num) for num in numbers]
    reversed_numbers = [reverse_digits(num) for num in numbers]
    print("Natija:", " ".join(map(str, reversed_numbers)))


reverse_numbers()
