import os
import numpy as np
import csv
from prettytable import PrettyTable, from_csv



### generate csv
# csv_data = np.random.randn(5, 5)
# filename = "csv_data1.csv"
# with open(filename, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     for row in csv_data:
#         writer.writerow(row)

# filename = "csv_data.csv"
# np.savetxt(filename, csv_data, delimiter=',')


# https://blog.csdn.net/weixin_44231148/article/details/120355664

ntable = PrettyTable()
# ntable._title = "Parameter Table"  # set table title.
# ntable.field_names = ["valueA", "valueB", "valueC"]  # add table column names.
# ntable.add_row([1, 2, 3])  # add row value in table.
# amat = np.random.randint(0, 5, (3,3))  # generate 3x3 matrix data.
# ntable.add_rows(amat)  # add matrix data in table.


### offcial reademe demo
# ntable.title = "Information"

### add by line
ntable.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
ntable.add_row(["Adelaide", 1295, 1158259, 600.5])
ntable.add_row(["Brisbane", 5905, 1857594, 1146.4])
ntable.add_row(["Darwin", 112, 120900, 1714.7])
ntable.add_row(["Hobart", 1357, 205556, 619.5])
ntable.add_row(["Sydney", 2058, 4336374, 1214.8])
ntable.add_row(["Melbourne", 1566, 3806092, 646.9])
ntable.add_row(["Perth", 5386, 1554769, 869.4])

### add by list rows
# ntable.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# ntable.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
# )

### add column by column
# ntable.add_column("City name",
# ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# ntable.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# ntable.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
# 1554769])
# ntable.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
# 869.4])

### import data from a CSV file
# with open("csv_data1.csv") as f:
#     ntable = from_csv(f)

### import data from a database cursor
# import sqlite3
# from prettytable import from_db_cursor

# connection = sqlite3.connect("mydb.db")
# cursor = connection.cursor()
# cursor.execute("SELECT field1, field2, field3 FROM my_table")
# ntable = from_db_cursor(cursor)


### getting data out
# print(ntable)
# ntable.del_row(1)  # delete row
# ntable.del_column("City name")  # delete column
# ntable.clear_rows()
# ntable.clear()


### Displaying your table in ASCII form
# print(ntable)
# print(ntable.get_string())
# table_str = ntable.get_string()
# table_str = ntable.get_formatted_string("json")  # <text|html|json|csv|latex>
# print(table_str)

### controlling which data gets displayed
# print(ntable.get_string(fields=["City name", "Population"]))
# print(ntable.get_string(start=1, end=4))

### changing the alignment of columns
## All columns at once
# ntable.align = "l"  # <l|r|c>
# print(ntable)

## one column at a time
# ntable.align["City name"] = "l"
# ntable.align["Area"] = "c"
# ntable.align["Population"] = "r"
# ntable.align["Annual Rainfall"] = "c"
# print(ntable)


### sorting your table by a field
# print(ntable.get_string(sortby="Population"))
# print(ntable.get_string(sortby="Population", reversesort=True))

# ntable.sortby = "Population"
# ntable.reversesort = True
# print(ntable)

# ntable.sortby = None
# print(ntable)


### Adding sections to a table
ntable = PrettyTable()
ntable.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
ntable.add_row(["Adelaide", 1295, 1158259, 600.5])
ntable.add_row(["Brisbane", 5905, 1857594, 1146.4])
ntable.add_row(["Darwin", 112, 120900, 1714.7])
ntable.add_row(["Hobart", 1357, 205556, 619.5], divider=True)
ntable.add_row(["Melbourne", 1566, 3806092, 646.9])
ntable.add_row(["Perth", 5386, 1554769, 869.4])
ntable.add_row(["Sydney", 2058, 4336374, 1214.8])
print(ntable)


# ntable_str = ntable.get_string()  # convert table as string format for output in screen.
# ntable_json = ntable.get_json_string()  # 
# print(ntable_str)  # show table.
# print(ntable_json)