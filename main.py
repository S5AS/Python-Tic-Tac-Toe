theboard =  {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' ', }

board_keys = []

for key in theboard:
    board_keys.append(key)

#prints the board
def draw(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print("-+-+-")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("-+-+-")
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#decides turn, keeps count of turns, asks the user things, and checks the game conidtion.
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        draw(theboard)
        print("It's your turn," + turn + ". Move to which place?")

        move = input()

        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")

        if count >= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] != ' ': #across the top
                draw(theboard)
                print("\nGame Over!\n")
                print(" **** " + turn + "won. ****")
                break
            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ': #across the middle
                draw(theboard)
                print("\nGame Over!\n")
                print(" **** " + turn + "won. ****")
                break
            elif theboard['1'] == theboard['2'] == theboard['3'] != ' ': #across the bottom
                draw(theboard)
                print("\nGame Over!\n")
                print(" **** " + turn + "won. ****")
                break
            elif theboard['1'] == theboard['4'] == theboard['7'] != ' ': #straight up on the left
                draw(theboard)
                print("\nGame Over!\n")
                print(" **** " + turn + "won. ****")
                break
            elif theboard['2'] == theboard['5'] == theboard['8'] != ' ': #straight up on the middle
                draw(theboard)
                print("\nGame Over!\n")
                print(" **** " + turn + "won. ****")
                break
            elif theboard['3'] == theboard['6'] == theboard['9'] != ' ': #straight up on the right
                draw(theboard)
                print("\nGame Over!\n")
                print(" **** " + turn + "won. ****")
                break
            elif theboard['7'] == theboard['5'] == theboard['3'] != ' ': #diagnoal starting on the left
                draw(theboard)
                print("\nGame Over!\n")
                print(" **** " + turn + "won. ****")
                break
            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ': #diagnoal starting on the right
                draw(theboard)
                print("\nGame Over!\n")
                print(" **** " + turn + "won. ****")
                break

        if count == 8:
            print("\nGame Over!\n")
            print("Its a tie. Shocker.")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

    #play again section

    restart = input("Do you want to play again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theboard[key] = " "

        game()

#calls the methods
if __name__ == "__main__":
    game()

