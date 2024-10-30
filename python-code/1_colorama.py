from colorama import Fore, Back, Style

# https://blog.csdn.net/xcntime/article/details/115016933

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
print(Back.GREEN + 'and in dim text')
print(Style.RESET_ALL)