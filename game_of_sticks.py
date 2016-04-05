# game of sticks
import random


def turn(player):
    # tell the player its their turn
    print("Player {}, it's your turn!".format(player))

    # limit to 1-3 sticks
    while True:
        pick_up = int(input("You can pick up 1, 2, or 3 sticks. \nHow many do you want?: "))
        try:
            if pick_up > 3:
                print("That's too many, don't be greedy!")
                continue

            else:
                return pick_up
        except ValueError:
            continue
        except TypeError:
            print("That's not even a number. Are you feeling ok?")
            continue
    # pass to next player



def stick_count(sticks, player):
    # remove sticks collected by each player
    sticks = sticks - player
    return sticks

def show_board(sticks):
    print("There are {} on the board".format(sticks))

def is_end(sticks, player):
    if player > sticks:
        print("There aren't that many sticks left, what are you trying to pull?")
    elif player == sticks:
        print("You lose!")
        return True
    else:
        return False

def main():
    # get number of sticks for game
    sticks = random.choice(range(1, 100))
    again = True
    while again:
        show_board(sticks)
        player1 = turn("Player1")

        player2 = turn("Player2")



if __name__ is '__main__':
    main()
