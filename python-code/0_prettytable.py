import os
import numpy as np
from prettytable import PrettyTable

# https://blog.csdn.net/weixin_44231148/article/details/120355664

ntable = PrettyTable()
ntable._title = "Parameter Table"  # set table title.
ntable.field_names = ["valueA", "valueB", "valueC"]  # add table column names.
ntable.add_row([1, 2, 3])  # add row value in table.
amat = np.random.randint(0, 5, (3,3))  # generate 3x3 matrix data.
ntable.add_rows(amat)  # add matrix data in table.

ntable_str = ntable.get_string()  # convert table as string format for output in screen.
ntable_json = ntable.get_json_string()  # 
print(ntable_str)  # show table.
print(ntable_json)