from chameleon import Chameleon
from emailer import Emailer
from players import Players

players = Players()
chameleon = Chameleon(players.game_on)
emailer = Emailer()


if chameleon.game_on:
    emailer.send_codes(chameleon.game_id, chameleon.topic, chameleon.code, players.players_list)
    print(f"Game ID: {chameleon.game_id}: - {chameleon.topic.split('/')[1]} - Completed")

