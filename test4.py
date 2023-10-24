import csv

filename_in = 'text_4_var_24.csv'
filename_out = 'res4.csv'
data = []
filtered_data = []
years_min = 25 + (24 % 10)

def getAverageSalary():
    sum = 0
    for human in data:
        sum += int(human['salary'][ : len(human['salary']) - 1])
    return sum / len(data)

def setDataFiltered(average):
    for human in data:
        if(int(human['salary'][ : len(human['salary']) - 1]) > average and int(human['age']) > years_min):
            filtered_data.append(human)




with open(filename_in, encoding='utf-8') as f_in:
    lines = csv.reader(f_in, delimiter=',')
    for line in lines:
         human = {
             'id': int(line[0]),
             'name': line[1] + ' ' + line[2],
             'age': line[3],
             'salary': line[4]
        }
         data.append(human)


setDataFiltered(getAverageSalary())
filtered_data = sorted(filtered_data, key= lambda x : x['id'])

with open(filename_out, 'w', encoding='utf-8', newline='') as f_out:
    writer = csv.writer(f_out)
    for human in filtered_data:
        writer.writerow(human.values())

    