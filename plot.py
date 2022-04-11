import csv
import collections
from datetime import datetime
import matplotlib.pyplot as plt
file = open('Project_data.csv')
csvreader = csv.reader(file)
header = next(csvreader)
print(header)


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

mon_dic = {"JAN": 1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "DEC": 12, "NOV": 11, "OCT": 10, "SEP": 9, "AUG": 8}
rows = []
wells_dict = collections.defaultdict(list)
pre_api = "#"
cur_api = "^"
time_list, oil_list = [], []
greater_list = set()
for row in csvreader:
	cur_api = row[0]
	if cur_api != pre_api:
		pre_api = cur_api
		first_date = datetime(int(row[1]),mon_dic[row[2]],1)
		wells_dict[row[0]].append([0,row[3]])
		i = 0
		continue
	curr_date = datetime(int(row[1]),mon_dic[row[2]],1)
	diff = diff_month(curr_date, first_date)
	wells_dict[row[0]].append([diff,row[3]])
	i += 1
	if i >= 4:
		greater_list.add(row[0])

import matplotlib.pyplot as plt

def draw_plot(greater_list, wells_dict):
    for well in greater_list:
        t_list, oil_list = [], []
        wells_list = wells_dict[well]
        for t, oil in wells_list:
            t_list.append(t)
            oil_list.append(float(oil))
        print(len(t_list))
        print(len(oil_list))
        plt.plot(t_list, oil_list)
        # plt.title('oil Vs t')
        # plt.xlabel('t')
        # plt.ylabel('oil')
        plt.show()

draw_plot(list(greater_list)[:20], wells_dict)
# print(greater_list)
# print(wells_dict)

# t_dic = {}
# for i in greater_list:
# 	max = -1
# 	for j in wells_dict[i]:
# 		if j[1] > max:




file.close()