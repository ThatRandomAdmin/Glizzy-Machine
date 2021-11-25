from methods import *
from tk import *

main()

x = 1
fldr = 'my_folder'

numberOfgb = int(input("Input:        "))

numberOfb = numberOfgb * 1073741824
dupe(numberOfb, fldr)

print(get_size_format(get_directory_size('my_folder')))