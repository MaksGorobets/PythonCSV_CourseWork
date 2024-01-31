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
