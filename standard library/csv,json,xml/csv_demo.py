import csv
# print(csv.__file__)

with open("users.csv",'r') as f:
    r = csv.reader(f)
    
    # next(r) # skipping the first row
    
    with open('new_names.csv', 'w', newline="" ) as newfile:
        csv_writer = csv.writer(newfile, delimiter='-')
     
        for row in r:
            csv_writer.writerow(row)


