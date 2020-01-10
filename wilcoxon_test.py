import xlrd
import pandas as pd
import numpy as np

book = xlrd.open_workbook(r'C:\Users\Vishwa\Downloads\Algo_Python_Test\Algo Test.xlsx')
sheet = book.sheets()[0]
sheet = book.sheet_by_name("Data")
sheet = book.sheet_by_index(0)
r = sheet.row(0)
c = sheet.col_values(0)
data = []
for i in range(sheet.nrows):
	data.append(sheet.row_values(i))

col = len(data[0])
rows = len(data)
row_name = [i[0] for i in data]
key_list = [i[1] for i in data]
non_key_list1 = [i[2] for i in data]
non_key_list2 = [i[3] for i in data]
non_key_list3 = [i[4] for i in data]
non_key_list4 = [i[5] for i in data]
non_key_list5 = [i[6] for i in data]

def sgn(x):
	if x<0:
		return -1
	elif x>0:
		return 1
	else:
		return 0

sgn_list = np.subtract(key_list,non_key_list1)

sgn_list1 = [sgn(x) for x in sgn_list]

abs_list1 = [abs(x) for x in sgn_list]

sgn_list1 = list(filter(lambda x:x!=0,sgn_list1))

abs_list1 = list(filter(lambda x:x!=0,abs_list1))

abs_list1, sgn_list1 = zip(*sorted(zip(abs_list1,sgn_list1)))

sr = pd.Series(abs_list1)

rank1 = sr.rank()
rank1 = list(rank1)

op1 = np.multiply(sgn_list1,rank1)

w1 = sum(op1)



