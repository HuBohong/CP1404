# import csv
#
# FILENAME = "countries.csv"
#
#
# def main():
#     with open(FILENAME) as in_file:
#         reader = csv.reader(in_file)
#         next(reader)
#         # new_list = []
#         country_to_data = {}
#         for record in reader:
#             country = record[0].strip()
#             city = record[1].strip()
#             population = int(record[2].strip().replace(',', ''))
#             perse = record[3].strip()[0:-1]
#             country_to_data[record[0]] = [country, city, population, perse]
#             # print(country_to_data)
#
#         x = sorted(country_to_data)
#         print(x)
#
# main()


x = input()
