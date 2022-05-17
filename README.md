# Chameleon
This is a clone of the game Chameleon

Official Chameleon rules   
https://bigpotato.com/blogs/blog/how-to-play-the-chameleon-instructions

Instructions

1) In emailer.py, put in your own credentials. It uses gmail by default. 
2) In player_data.csv, put in Names/Email addresses as needed
3) run main.py
4) Sometimes the game may cause an error b/c there are empty lines in the .csv file. Make sure no empty lines are in the csv file after editing. 

Files:   
main.py - runs the game   

player_data.csv - contains list of names,emails of players   

players.py - responsible for getting player list from csv file player_data.csv and randomly shuffling them.   

excluded_topics.csv - when game runs, it puts the used topic in this file so it doesn't get picked again  
                    - you can manually clear this file out, or it will ask if you want to clear it if all topics are used.   

chameleon.py - Gets random topic and code cards.   
            - Puts used topic card in excluded_topics.csv   
            - Clears out excluded_topic.csv when all are used   

emailer.py - Send out Chameleon/Topic email to first player in shuffled player list   
            - Sends out Code/Topic email to remaining players in player list   