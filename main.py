from Generator.csv_generator import *
from sorter import Sorter
from csv_reader import CSV_Reader
from colors import Bcolors

# generator = Generator(20)

# generator.generate("test")

post = Post()
csv_reader = CSV_Reader()
sorter = Sorter()

while not csv_reader.file:
    csv_reader.import_file()
    opened_file = csv_reader.opened_file
else:
    while True:
        show_sort = int(input(f"{Bcolors.WHITE}Do you want to view(1), sort(2), get statistics for your file(3), or pick other file(4)?"))

        if show_sort == 1:
            sorter.print_list(opened_file)
        elif show_sort == 2:
            sorter.sort(opened_file)
        elif show_sort == 3:
            sorter.show_popular(opened_file)
        elif show_sort == 4:
            csv_reader.file = None
            csv_reader.import_file()
            while not csv_reader.file:
                csv_reader.import_file()
            else:
                opened_file = csv_reader.opened_file