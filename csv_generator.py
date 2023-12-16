from faker import *
from random import *
from post_title_generator import *
from post import Post

class Generator:
    def __init__(self, rows):
        self.rows = rows

    def generate(self, filename):
        with open(f"{filename}.csv", "a") as f:
            f.write("Post title, Likes, Comments, Reposts, Profile visits" + "\n")
            for _ in range(self.rows):
                post = Post()
                f.write(str(post) + "\n")

    def csv_to_post(self, filename):
        csv_file = open(f"{filename}.csv")

        decoded_list = []

        for row in csv_file:
            decoded_list.append(row.split(","))

        for number in range(len(decoded_list)):
            decoded_list[number][-1] = decoded_list[number][-1].strip()

        decoded_list.pop(0)

        object_list = []

        for item in decoded_list:
            new_post = Post(item[0], int(item[1]), int(item[2]), int(item[3]), int(item[4]))
            object_list.append(new_post)


        return object_list
