stopped = True

while True:
    user_input = input('> ').lower()
    if user_input == 'stop':
        if stopped:
            print("Car already stopped.")
        else:
            stopped = True
            print('Car stopped.')
    elif user_input == 'start':
        if not stopped:
            print("Car already started.")
        else:
            stopped = False
            print('Car started.')
    elif user_input == 'help':
        print('start - start the car\nstop - stop the car\nquit - quit game\n')
    elif user_input == 'quit':
        break
    else:
        print('I don\'t understand.')
