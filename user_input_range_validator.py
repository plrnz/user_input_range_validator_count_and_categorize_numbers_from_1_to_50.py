# Pseudocodes
# 1. Set up the loop and input
# 2. Check if te input is valid
# 3. Counting each range
# 4. Display the results

# Counters for each range
result_1_10 = 0
result_11_20 = 0
result_21_30 = 0
result_31_40 = 0 
result_41_50 = 0

while True:
    number_range = input("PLease enter a number ranging from 1 to 50: ")

    if number_range.isdigit():
        number_range = int(number_range)
    else:
        continue

    if 1 <= number_range <= 50:

        if 1 <= number_range <= 10:
            result_1_10 += 1
        
        elif 11 <= number_range <= 20:
            result_11_20 += 1

        elif 21 <= number_range <= 30:
            result_21_30 += 1

        elif 31 <= number_range <= 40:
            result_31_40 += 1

        elif 41 <= number_range <= 50:
            result_41_50 += 1
    else:
        break

print("1 - 10 =", result_1_10)
print("11 - 20 =", result_11_20)
print("21 - 30 =", result_21_30)
print("31 - 40 =", result_31_40) 
print("41 - 50 =", result_41_50)