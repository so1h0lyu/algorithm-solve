a = int(input())
b = int(input())

b_units = b % 10
b_tens = ((b - b_units) % 100)
b_hundreds = ((b - (b_tens + b_units)) % 1000)

result_1 = a * b_units
result_2 = a * b_tens
result_3 = a * b_hundreds

total = result_1 + result_2 + result_3

print("{}\n{}\n{}\n{}".format(result_1, int(result_2 / 10), int(result_3 / 100), total))