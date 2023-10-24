filename_in = 'text_1_var_24'
filename_out = 'res1.txt'
d = dict()

with open(filename_in) as f_in:
    lines = f_in.readlines()

for line in lines:
    words = line.strip() \
    .replace(',', ' ') \
    .replace('!', ' ') \
    .replace('?', ' ') \
    .replace('.', ' ') \
    .strip().split(' ')
    for word in words:
        if(word in d):
            d[word] += 1
        else:
            d[word] = 1

sorted_d = dict(sorted(d.items(), reverse=True, key= lambda x : x[1]))

with open(filename_out, 'w') as f_out:
    for pair in sorted_d.items():
         f_out.write(pair[0] + ' : ' + str(pair[1]) + '\n')


        