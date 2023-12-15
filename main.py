from csv_generator import *
from operator import attrgetter

# generator = Generator(100)

# generator.generate("big_test")

post = Post()
file_input = input("Enter your CSV file name: ")

test_l = post.csv_to_post(file_input)

print("Imported successfully.")

show_sort = int(input("Do you want to view or sort your file? 1 or 2: "))

if show_sort == 1:
    for item in test_l:
        print(item)
elif show_sort == 2:
    sort_by = int(input("Do you want to sort by Title(1), Likes(2), Comment(3), Reposts(4), Profile visits(5), Topic(6): "))
    if sort_by == 1:
        sorted_test = sorted(test_l, key=attrgetter('post_title'), reverse=True)
    elif sort_by == 2:
        sorted_test = sorted(test_l, key=attrgetter('likes'), reverse=True)
    elif sort_by == 3:
        sorted_test = sorted(test_l, key=attrgetter('comments'), reverse=True)
    elif sort_by == 4:
        sorted_test = sorted(test_l, key=attrgetter('repost'), reverse=True)
    elif sort_by == 5:
        sorted_test = sorted(test_l, key=attrgetter('profile_visits'), reverse=True)
    elif sort_by == 6:
        sorted_test = sorted(test_l, key=attrgetter('topic'), reverse=True)
    for sorted in sorted_test:
        print(sorted)
