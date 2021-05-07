from vier_gewinnt import game_loop, check_valid_move
import random

def user_or_bot_input(params: dict) -> int:
    '''Funktion, um Input vom User oder vom Bot einzulesen und ggf. validieren'''
    if params["turn"] % 2 == 0:
        try:
            user_input = input("Spalte: ")
            selected_column = cast_and_validate_input(user_input)
        except ValueError:
            print("Bitte gib einen validen Wert an")
            return user_or_bot_input(params)
    else:
        #generiert eine zufällige Zahl und prüft ob diese einen validen Zug darstellt
        selected_column = random.randint(0, 7)
        if not check_valid_move(params["board"], selected_column):
            user_or_bot_input(params)
        
    return selected_column

def cast_and_validate_input(user_input: str):
    '''Wandelt den input zu einem integer und wirft ggf einen error'''
    casted_input = int(user_input)
    if casted_input < 0 or casted_input > 7:
        raise ValueError
    return casted_input

def start():
    game = game_loop(user_or_bot_input)

    while True:
        try:
            next(game)
        except:
            break
start()