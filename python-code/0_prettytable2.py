import numpy as np
from prettytable import PrettyTable, MARKDOWN, DOUBLE_BORDER


### Changing the appearance of your table - the easy way
ntable = PrettyTable()
ntable.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
ntable.add_row(["Adelaide", 1295, 1158259, 600.5])
ntable.add_row(["Brisbane", 5905, 1857594, 1146.4])
ntable.add_row(["Darwin", 112, 120900, 1714.7])
ntable.add_row(["Hobart", 1357, 205556, 619.5], divider=True)
ntable.add_row(["Melbourne", 1566, 3806092, 646.9])
ntable.add_row(["Perth", 5386, 1554769, 869.4])
ntable.add_row(["Sydney", 2058, 4336374, 1214.8])

### Setting a table style
# ntable.set_style(DOUBLE_BORDER)  # <DEFAULT|PLAN_COLUMNS|MSWORD_FRIENDLY|ORGMODE|SINGLE_BORDER|DOUBLE_BORDER>
# print(ntable)

### Changing the appearance of your table - the hard way
# - border: True|False
# - preserve_internal_border: True|False
# - header: True|False
# - hrules: FRAME|HEADER|ALL|NONE
# - HEADER, ALL, NONE: prettytable.FRAME
# - vrules: FRAME|ALL|NONE
# - int_format: print("%<int_format>d" % data)
# - float_format: print("%<float_format>f" % data)
# - custom_format:
# - padding_width: Number of spaces on either side of column data
# - left_padding_width: Number of spaces on left-hand side of column data.
# - right_padding_width: Number of spaces on right-hand side of column data.
# - vertical_char: Single character string used to draw vertical lines. Default: |.
# - horizontal_char: Single character string used to draw horizontal lines. Default: -.
# - _horizontal_align_char: 
# - junction_char: Single character string used to draw line junctions. Default: +.
# - top_junction_char: 
# - bottom_junction_char:
# - right_junction_char: 
# - left_junction_char:
# - top_right_junction_char: 
# - top_left_junction_char: 
# - bottom_right_junction_char: 
# - bottom_left_junction_char: 


ntable.border = False
print(ntable)
ntable.border = True
print(ntable)


# table = PrettyTable()
# table.border = False
# table.header = False
# table.padding_width = 5

# table = PrettyTable(border=False, header=False, padding_width=5)

### changing style options just once
print(ntable)
print(ntable.get_string(border=False))
print(ntable)

### changing the appearance of your table - with colors
from prettytable.colortable import ColorTable, Themes, Theme

ntable = ColorTable(theme = Themes.OCEAN)
ntable.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
ntable.add_row(["Adelaide", 1295, 1158259, 600.5])
ntable.add_row(["Brisbane", 5905, 1857594, 1146.4])
ntable.add_row(["Darwin", 112, 120900, 1714.7])
ntable.add_row(["Hobart", 1357, 205556, 619.5], divider=True)
ntable.add_row(["Melbourne", 1566, 3806092, 646.9])
ntable.add_row(["Perth", 5386, 1554769, 869.4])
ntable.add_row(["Sydney", 2058, 4336374, 1214.8])
print(ntable)

### creating a custom theme
custom_theme = Theme(
        default_color="34",
        vertical_color="20",
        horizontal_color="20",
        junction_color="20",
    )
ntable = ColorTable(theme = custom_theme)
ntable.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
ntable.add_row(["Adelaide", 1295, 1158259, 600.5])
ntable.add_row(["Brisbane", 5905, 1857594, 1146.4])
ntable.add_row(["Darwin", 112, 120900, 1714.7])
ntable.add_row(["Hobart", 1357, 205556, 619.5], divider=True)
ntable.add_row(["Melbourne", 1566, 3806092, 646.9])
ntable.add_row(["Perth", 5386, 1554769, 869.4])
ntable.add_row(["Sydney", 2058, 4336374, 1214.8])
print(ntable)
