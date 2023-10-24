filename_in = 'text_3_var_24'
filename_out = 'res3.txt'
limit = 74.0
result = []

def is_limited(num):
    return float(num) ** (1 / 2) < limit

with open(filename_in) as f_in:
    lines = f_in.readlines()

for line in lines:
    nums = line.strip().split(',')
    row = []
    for i in range(len(nums)):
        num = nums[i]
        if(num == 'NA'):
            num = str((int(nums[i + 1]) + int(nums[i - 1])) / 2)
        if(not is_limited(num)):
                row.append(num)
    result.append(row)

with open(filename_out, 'w') as f_out:
     for row in result:
         for i in range(len(row) - 1):
             f_out.write(row[i] + ',')
         f_out.write(row[len(row) - 1] + '\n')


