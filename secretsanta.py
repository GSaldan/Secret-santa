import random
# instructions: choose an even number of players and add their names, the computer will then sort and 
# combine the players into pairs

players = []
show_names = []


def name_players():
    # ask for the players names
    how_many = int(input('How many players do you want on the game (even number): '))
    if how_many % 2 == 0:
        while how_many >= 1:
            how_many -= 1
            players.append(input('name: '))

    else:
        print(f'Please add an Even number, {how_many}, is not Even')
        name_players()


def go():
    # create a list of the given names and combine then into pairs 
    while len(players) >= 1:

        create_ = random.choices(players, k=2)

        if create_[0] != create_[1]:
            show_names.append(create_)
            for i in create_:
                players.remove(i)

    print(show_names)


name_players()
go()

