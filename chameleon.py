import random
import os


class Chameleon:
    def __init__(self, game_on):
        self.game_on = game_on
        self.game_id = random.randint(10000, 99999)
        self.code = self.get_code()
        self.topic = self.get_topic_cards()

    def get_code(self):
        code_cards = os.listdir("images_codes")
        return f"images_codes/{random.choice(code_cards)}"

    def get_topic_cards(self):
        topic_cards = os.listdir("images_topics")
        with open("excluded_topics.csv") as topic_file:
            excluded_topic_list = [row.strip("\n") for row in topic_file]
        for excluded_topic in excluded_topic_list:
            try:
                topic_cards.remove(excluded_topic)
            except ValueError:
                self.game_on = False
                print("Check excluded_topics.csv for empty lines.")
                break
        if self.game_on:
            try:
                topic = random.choice(topic_cards)
                with open("excluded_topics.csv", "a", newline="") as topic_file:
                    topic_file.write(f"{topic}\n")
            except IndexError:
                self.game_on = False
                self.refresh_topic_cards()
            else:
                return f"images_topics/{topic}"

    def refresh_topic_cards(self):
        print("No More Topics to choose from.")
        refresh_topic_cards = input("Do you want to refresh Topic Cards? ").lower()
        if refresh_topic_cards == "y" or refresh_topic_cards == "yes":
            with open("excluded_topics.csv", "w") as topic_file:
                topic_file.write("")
        else:
            print("End of Game")


