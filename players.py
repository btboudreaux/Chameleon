import csv
import random


class Players:
    def __init__(self):
        self.game_on = True
        self.players_list = self.create_players()

    def create_players(self):
        with open("player_data.csv") as csv_player_file:
            player_data = csv.reader(csv_player_file)
            next(player_data)
            try:
                player_list = [{"Name": row[0], "Email": row[1]} for row in player_data]
                random.shuffle(player_list)
                return player_list
            except IndexError:
                print("Check player_data.csv for empty lines.")
                self.game_on = False

