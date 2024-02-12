from operator import attrgetter
from colors import Bcolors

class Sorter:

    def __init__(self, post_title=None, impressions=None):
        self.post_title = post_title or "Example"
        self.impressions = impressions or "0"

    def print_out(self):
        return f"{Bcolors.OKCYAN}Post Title: {self.post_title}, {Bcolors.OKGREEN}Impressions: {self.impressions}"

    def print_list(self, post_list):
        for item in post_list:
            print(item.print_out())

    def sort(self, post_list):
        option_list = ["post_title", "likes", "comments", "repost", "profile_visits", "topic"]
        sort_by = int(input("Do you want to sort by Title(1), Likes(2), Comment(3), Reposts(4), Profile visits(5): "))
        atter_sort = option_list[sort_by - 1]
        sorted_test = sorted(post_list, key=attrgetter(atter_sort), reverse=True)
        for test in sorted_test:
            print(test.print_out())

    def show_popular(self, post_list):
        imr_list = []
        for post in post_list:
            impressions = post.likes + post.comments + post.reposts + post.profile_visits
            imr_list.append(Sorter(post.post_title, impressions))
        sorted_imp = sorted(imr_list, key=attrgetter("impressions"), reverse=True)
        for srd in sorted_imp:
            print(srd.print_out())