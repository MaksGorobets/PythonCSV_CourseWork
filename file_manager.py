from post import Post
from colors import Bcolors

class FileManager:

    def __init__(self) -> None:
        self.file = None
        self.opened_file = []

    def import_file(self):
        file_input = input(f"{Bcolors.WHITE}Enter your CSV file name: ")

        try:
            with open(f"{file_input}.csv") as opened_file:
                self.file = opened_file  
                print(f"{Bcolors.OKGREEN}Imported successfully.")
                self.opened_file = self._csv_to_post()
        except FileNotFoundError:
            print(f"{Bcolors.WARNING}File \"{file_input}\" does not exist")

    def _csv_to_post(self):
        csv_file = self.file

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