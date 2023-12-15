from faker import *
from random import *
from post_title_generator import *

fake = Faker()
post_t = PostTitle()

class Post:
    def __init__(self, post_title=None, likes=None, comments=None, reposts=None, profile_visits=None, topic=None):
        self.post_title = post_title or post_t.get_random()
        self.likes = likes or random.randint(50, 3000)
        self.comments = comments or random.randint(1, self.likes // 2)
        self.reposts = reposts or random.randint(0, self.comments)
        self.profile_visits = profile_visits or random.randint(self.likes, 10000)
        self.topic = topic or self.post_title.split()[-1]

    def __str__(self):
            return f"Post Title: {self.post_title}, Likes: {self.likes}, Comments: {self.comments}, Reposts: {self.reposts}, Profile Visits: {self.profile_visits}, Topic: {self.topic}"
    
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
            new_post = Post(item[0], int(item[1]), int(item[2]), int(item[3]), int(item[4]), item[5])
            object_list.append(new_post)


        return object_list


class Generator:
    def __init__(self, rows):
        self.rows = rows

    def generate(self, filename):
        with open(f"{filename}.csv", "a") as f:
            f.write("Post title, Likes, Comments, Reposts, Profile visits, Topic" + "\n")
            for _ in range(self.rows):
                post = Post()
                f.write(str(post) + "\n")
