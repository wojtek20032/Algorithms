def display(bracket):
    print("------------")
    print('  '+bracket[0] + ' | ' + bracket[1] + ' | ' + bracket[2])
    print('  '+bracket[3] + ' | ' + bracket[4] + ' | ' + bracket[5])
    print('  '+bracket[6] + ' | ' + bracket[7] + ' | ' + bracket[8])
    print("------------")


def makae_a_choice():
    choice = 'Error'
    choice_range = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while choice.isdigit() == False or int(choice) not in choice_range:
        choice = input("Enter a number between 1 - 9 to place your mark")
        if choice.isdigit() == False:
            print("Enter a number pls!")
        if int(choice) not in choice_range:
            print("Please enter a value in choosing range")

    return int(choice)


def update_bracket(choice, bracket, taken_places, player_signature):
    if choice in taken_places:
        print("This place is already taken")
        return False
    bracket[choice - 1] = player_signature
    taken_places[choice - 1] = 1
    return True


def validate_bracket(bracket, taken_bracket):
    if 0 in taken_bracket:
        pass
    else:
        print("No more spaces NO WINNER!!")
        return True

    if bracket[0] == bracket[1] and bracket[1] == bracket[2] and bracket[0] == bracket[2] and bracket[0] != ' ':
        winner = bracket[0]
        print(f'We have a winner, {winner} WON! ')
        display(bracket)
        return True
    if bracket[0] == bracket[3] and bracket[3] == bracket[6] and bracket[0] == bracket[6] and bracket[0] != ' ':
        winner = bracket[0]
        print(f'We have a winner, {winner} WON! ')
        display(bracket)
        return True
    if bracket[1] == bracket[4] and bracket[4] == bracket[7] and bracket[1] == bracket[7] and bracket[1] != ' ':
        winner = bracket[1]
        print(f'We have a winner, {winner} WON! ')
        display(bracket)
        return True
    if bracket[2] == bracket[5] and bracket[5] == bracket[8] and bracket[2] == bracket[8] and bracket[2] != ' ':
        winner = bracket[2]
        print(f'We have a winner, {winner} WON! ')
        display(bracket)
        return True
    if bracket[3] == bracket[4] and bracket[3] == bracket[5] and bracket[3] == bracket[5] and bracket[3] != ' ':
        winner = bracket[3]
        print(f'We have a winner, {winner} WON! ')
        display(bracket)
        return True
    if bracket[6] == bracket[7] and bracket[6] == bracket[8] and bracket[7] == bracket[8] and bracket[6] != ' ':
        winner = bracket[6]
        print(f'We have a winner, {winner} WON! ')
        display(bracket)
        return True
    if bracket[0] == bracket[4] and bracket[0] == bracket[8] and bracket[4] == bracket[8] and bracket[0] != ' ':
        winner = bracket[0]
        print(f'We have a winner, {winner} WON! ')
        display(bracket)
        return True
    if bracket[2] == bracket[4] and bracket[2] == bracket[6] and bracket[4] == bracket[6] and bracket[2] != ' ':
        winner = bracket[2]
        print(f'We have a winner, {winner} WON! ')
        display(bracket)
        return True
    print("WE ARE STILL PLAYING")
    return False


def restart_game(bracket, taken_bracket):
    for i in range(0, 9):
        bracket[i] = ' '
        taken_bracket[i] = 0


print("Hi welcome to tic tack to game")
bracket = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
taken_bracket = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player1_choice = "NONE"
while player1_choice != 'X' and player1_choice != 'O':
    player1_choice = input("Player1 choose X or O")
    if player1_choice != 'X' and player1_choice != 'O':
        print("Choose X or O !")

if player1_choice == 'X':
    player2_choice = 'O'
else:
    player2_choice = 'X'

keep_playing = True

while keep_playing == True:
    if validate_bracket(bracket, taken_bracket):
        keep_playing = False
        continue
    while True:
        still = input("Do you wanna keep playing 0 is NO 1 is Yes")
        if still == '1':
            break
        elif still == '0':
            keep_playing = False
            break
        else:
            pass
    if keep_playing == False:
        print("GAME OVER")
        break
    print("Player 1 move")
    choice1 = makae_a_choice()
    update_bracket(choice1, bracket, taken_bracket, player1_choice)
    if validate_bracket(bracket, taken_bracket):
        keep_playing = False
        continue
    display(bracket)
    print("Player 2 move")
    choice2 = makae_a_choice()
    update_bracket(choice2, bracket, taken_bracket, player2_choice)
    if validate_bracket(bracket, taken_bracket):
        keep_playing = False
        continue
    display(bracket)
