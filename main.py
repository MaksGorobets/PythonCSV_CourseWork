from csv_generator import *
from post import Sorter
from file_manager import FileManager
from colors import Bcolors

# generator = Generator(20)

# generator.generate("test")

post = Post()
file_manager = FileManager()
sorter = Sorter()
colors = Bcolors()

file_manager.import_file()

while not file_manager.file:
    file_manager.import_file()
    opened_file = file_manager.opened_file
else:
    while True:
        show_sort = int(input(f"{colors.WHITE}Do you want to view(1), sort(2), get statistics for your file(3), or pick other file(4)?"))

        if show_sort == 1:
            sorter.print_list(opened_file)
        elif show_sort == 2:
            sorter.sort(opened_file)
        elif show_sort == 3:
            sorter.show_popular(opened_file)
        elif show_sort == 4:
            file_manager.file = None
            file_manager.import_file()
            while not file_manager.file:
                file_manager.import_file()
            else:
                opened_file = file_manager.opened_file