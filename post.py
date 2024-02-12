import random
from faker import *
from Generator.generator_resources import PostTitle
from colors import Bcolors

fake = Faker()

class Post:

    def __init__(self, post_title=None, likes=None, comments=None, reposts=None, profile_visits=None):
        self.post_title = post_title or PostTitle.get_random()
        self.likes = likes or random.randint(50, 3000)
        self.comments = comments or random.randint(1, self.likes // 2)
        self.reposts = reposts or random.randint(0, self.comments)
        self.profile_visits = profile_visits or random.randint(self.likes, 10000)

    def __str__(self):
        return f"{self.post_title}, {self.likes}, {self.comments}, {self.reposts}, {self.profile_visits}"
    
    def print_out(self):
        return f"{Bcolors.OKCYAN}Post Title: {self.post_title}, {Bcolors.OKGREEN}Likes: {self.likes}, {Bcolors.OKBLUE}Comments: {self.comments}, {Bcolors.FAIL}Reposts: {self.reposts}, {Bcolors.WARNING}Profile Visits: {self.profile_visits}"
