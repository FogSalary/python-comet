import numpy as np
from prettytable import PrettyTable


### Displaying your table in JSON
table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5], divider=True)
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])
table.add_row(["Sydney", 2058, 4336374, 1214.8])

# print(table.get_json_string())

### Displaying your table in HTML form
## Styling HTML tables
# print(table.get_html_string())

# table.format = True
# print(table.get_html_string())

## Settings HTML attributes
# print(table.get_html_string(attributes={"id":"my_table", "class":"red_table"}))

## Settings HTML escaping
# print(table.get_html_string(escape_header=False, escape_data=False))

## copying a table
ntable = table[0:2]
print(ntable)