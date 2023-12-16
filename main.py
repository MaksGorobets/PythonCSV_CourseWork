from csv_generator import *
from post import Sorter

# generator = Generator(20)

# generator.generate("test")

post = Post()
generator = Generator(0)
sorter = Sorter()

file_input = input("Enter your CSV file name: ")

test_l = generator.csv_to_post(file_input)

print("Imported successfully.")

show_sort = int(input("Do you want to view(1) sort(2) or get statistics for your file(3)?"))

if show_sort == 1:
    sorter.print_list(test_l)
elif show_sort == 2:
    sorter.sort(test_l)
elif show_sort == 3:
    sorter.show_popular(test_l)