from csv import reader
list_vals = []

def Clear_vals(value):
    value = str.replace(value,'[','')
    value = str.replace(value,']','')
    value = str.replace(value,"'",'')
    return value

with open('Advent of Code - 2015/Day02.csv','r',newline='') as read_obj:
    csv_reader = reader(read_obj)
    for vals in csv_reader:
        list_vals.append(Clear_vals(str(vals)))

print(list_vals)

for val in (list_vals):
    value = str.split(str(val),'x')
    l,w,h = value
    print(l,h,w)