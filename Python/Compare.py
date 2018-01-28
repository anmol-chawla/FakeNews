import csv


def check(domain):
    with open('sources.csv', 'r') as csv_data:
        fields = csv.reader(csv_data)
        for row in fields:
            if domain == row[0]:
                return row[1]
    return 1
