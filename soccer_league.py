import csv

# create a list to hold the entire league

football_league = [[],[],[]]

# Manually create a single collection that contains all information for all 18 players.
# Each player should themselves be represented by their own collection.'''

def get_all_players():

    # open the file and read intp a single dictonary
    with open('soccer_players.csv', newline = '') as csvfile:

        soccer_reader = csv.DictReader(csvfile, delimiter = ',')
        players = list(soccer_reader)

    # assign all the playesr to a team
    create_teams(players)

    # write the letters to the parents
    write_letters(players)

# Create appropriate variables and logic to sort and store players into three
# teams: Sharks, Dragons and Raptors.
# Be sure that your logic results in all teams having the same number of
# experienced players on each.
# The collections will be named sharks, dragons, raptors, and league.'''

def create_teams(players):

    # create a variable to count the number of yes's and the number of no's we
    # have added to each team
    yes_ctr = 0
    no_ctr = 0

    # step 1: with the len of the list / 3  - this will tell us how many
    # players we have to add the 3 teams
    team_count = len(players) / 3

    # step 2: create the 3 teams
    for player in players:
        if player['Soccer Experience'].upper() == "YES":
            football_league[yes_ctr].append(player)
            yes_ctr += 1

        else:
            football_league[no_ctr].append(player)
            no_ctr += 1

        if yes_ctr == team_count / 2:
            yes_ctr = 0

        if no_ctr == team_count / 2:
            no_ctr = 0


# check the average of player height +/- 1

def check_height(player):
    pass


# Create a function named write_letter that takes a player and returns a
# string of the letter to their guardian(s).
# Be sure the string is formatted as a letter and starts with "Dear" and the
# guardian(s) name(s) and with the additional required information:
# player's name, team name, and date & time of first practice.'''

def write_letters(players):

    for player in players:
        if player in football_league[0]:
            player['Team'] = 'Sharks'
            player['Practice Time'] = 'March 17th at 3pm'

        elif player in football_league[1]:
            player['Team'] = 'Dragons'
            player['Practice Time'] = 'March 17th at 1pm'
        else:
            player['Team'] = 'raptors'
            player['Practice Time'] = 'March 18th at 1pm'

        letter_string = """\n\nDear {Guardian Names}\n
          This is to inform you that {Name} will be playing for {Team} and
          the first team practice will begin on the {Practice Time}.\n
          Please ensure {Name} is on time.
                     \n\nKind Regards,
                    \nStuart McIntosh """.format(**player)

        save_letters(letter_string, player)

# Save all 18 letters to disk, giving each letter a filename of the player's
# name, in lowercase and with underscores and ending in .txt.
# For example, kenneth_love.txt.'''

def save_letters(letter, player):

    file_name = player['Name'].replace(' ', '_') + '.txt'
    letter_file = open(file_name, 'w')
    letter_file.write(letter)
    letter_file.close

# Ensure your script doesn't execute when imported; put all of your logic and
# function calls inside of an if __name__ == "__main__": block.

if __name__ == '__main__':
    get_all_players()
