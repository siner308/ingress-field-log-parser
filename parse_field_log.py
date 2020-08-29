import csv

with open('sample.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    results = dict()
    results['total'] = 0

    for row in csv_reader:
        text = row[2]
        if str(text).startswith('created a Control Field'):
            mu_token = text.split(' ')[-2].split('+')
            if len(mu_token) == 2:
                mu = int(mu_token[-1])
                agent_name = row[1].split('<')[1].split('>')[0]
                try:
                    results[agent_name] += mu
                except:
                    results[agent_name] = mu
                results['total'] += mu
        continue
    print(results)
