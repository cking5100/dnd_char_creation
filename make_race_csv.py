import csv



race_names = input("add list of races: ").split()

print(race_names)


for name in race_names:
    file_name = name + "_names.csv"
    with open(file_name, 'w', newline='') as csv_file:
        continue




