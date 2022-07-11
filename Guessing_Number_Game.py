# Guessing number
import random
import sys

# Run the game and next write your name


def draw_number():
    print("Let's draw the secret number! Pick number from 1 to 10")
    global drawed_number
    drawed_number = str(random.randint(1, 10))
    
def get_player_name_input():  
    global player_name 
    player_name = input("Player pick your name: ")
    

def checking_for_more_game():
    print("Wanna play more? Pick 'y' for yes or 'n' for no ")
    check_more_game = input()
    if check_more_game == 'y':
        while True:
            draw_number()
            guesing_number()
            checking_number_is_digit()
            compare_number_and_draw()
            checking_for_more_game()
            
    elif check_more_game == 'n':
        print(f"Thanks for game {player_name}")
        sys.exit()
            
    else:
        while check_more_game != 'y' and check_more_game != 'n':
            print("Wrong answer. Pick 'y' or 'n'! ")
            check_more_game = input()
            if check_more_game == 'y':
                while True:
                    draw_number()
                    guesing_number()
                    checking_number_is_digit()
                    compare_number_and_draw()
                    checking_for_more_game()
                    
            elif check_more_game == 'n':
                print(f"Thanks for game {player_name}")
                break

            
            else:
                while check_more_game != 'y' and check_more_game != 'n':
                    print("Wrong answer. Pick 'y' or 'n'!" )
                    check_more_game = input()   
            break
        
def guesing_number():
    global guess_number
    guess_number = input()

def checking_number_is_digit():
    if guess_number.isdigit() == False:
        print(f"{player_name} you must pick a digit from 1 to 10. Try again")


def compare_number_and_draw():
        attempt = 1
        if guess_number == drawed_number:
            print(f"Congratulations {player_name}! You needed {attempt} attempts to guess the secret number!")
        else:
            while guess_number != drawed_number:
                print(f"Try one more time! ({player_name}, you can also pick 'exit' if you wanna leave game.)")
                attempt += 1
                guesing_number()
                if guess_number == 'exit':
                    print(f"Thanks for game {player_name}")
                    sys.exit()
                if guess_number == drawed_number:
                    print(f"Congratulations {player_name}! You needed {attempt} attempts to guess the secret number!")
                    break
    
def main():
    get_player_name_input()
    print(f"Welcome in guessing game {player_name}!")
    draw_number()
    guesing_number()
    checking_number_is_digit()
    compare_number_and_draw()
    checking_for_more_game()

main()



