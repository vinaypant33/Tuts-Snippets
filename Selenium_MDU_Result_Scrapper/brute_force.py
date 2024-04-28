import itertools 
import os




file_name  = 1

def brute_force(file_path ,  password_length):

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    total_combinations = len(digits) ** password_length
    file_size_megabytes = (total_combinations * password_length) / 1000000
    with open(file_path, 'w') as file:
        if file_size_megabytes > 100:
            file_name  = file_name + 1
            file_path = str(file_name)
            for combination in itertools.product(digits, repeat=password_length):
                file.write(''.join(map(str, combination)) + '\n')
    return total_combinations, file_size_megabytes
    



password_length = 7



total_combinations, file_size_megabytes = brute_force("1.txt", password_length)
print(f"Total combinations: {total_combinations}")
print(f"File size: {file_size_megabytes} + MB")


