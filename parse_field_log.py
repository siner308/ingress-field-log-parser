import csv

with open('sample.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    result = 0
    for row in csv_reader:
        text = row[2]
        if str(text).startswith('created a Control Field'):
            mu_token = text.split(' ')[-2].split('+')
            if len(mu_token) == 2:
                mu = mu_token[-1]
                result += int(mu)
        continue
    print(result)
