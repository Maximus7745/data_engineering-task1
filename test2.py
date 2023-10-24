filename_in = 'text_2_var_24'
filename_out = 'res2.txt'
sums = []

with open(filename_in) as f_in:
    lines = f_in.readlines()

for line in lines:
    nums = line.strip().split(',')
    sum = 0
    for num in nums:
        sum += int(num)
    sums.append(sum)

with open(filename_out , 'w') as f_in:
    for sum in sums:
        f_in.write(str(sum) + '\n')

