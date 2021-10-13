# short illustration of game logic
def play():
    room = "You are standing in a room full of mirrors, what do you do?\n"

    # The main game loop
    while True:

        # Setup and describe to the user where they are.
        print(room)

        # Take and process user input
        user_input = input()

        # apply logic to game input
        if user_input == 'escape!':
            print('Ah! you escaped!')
            break


if __name__ == "__main__":
    play()
