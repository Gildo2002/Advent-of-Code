from csv import reader

list_vals = []
area = 0
ribbon = 0


def Clear_vals(value):
    value = str.replace(value, "[", "")
    value = str.replace(value, "]", "")
    value = str.replace(value, "'", "")
    return str.split(str(value), "x")


def calc_area(l, w, h):
    extra = min(l * w, h * w, h * l)
    return (2 * l * w + 2 * w * h + 2 * h * l) + extra


def calc_ribbon(l, w, h):
    extra = min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h)
    return (l * w * h) + extra


with open("Input/Day02.csv", "r", newline="") as read_obj:
    csv_reader = reader(read_obj)
    for vals in csv_reader:
        list_vals.append(Clear_vals(str(vals)))


for val in list_vals:
    l, w, h = map(int, val)
    area += calc_area(l, w, h)
    ribbon = ribbon + calc_ribbon(l, w, h)

print("Gift Papel: ", area)
print("Feet of Reboon: ", ribbon)
