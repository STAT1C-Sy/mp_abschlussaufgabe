from functools import reduce 

def generate_gameboard(rows: int, columns: int) -> list:
    '''generiert das Spielfeld'''
    return [
        [ "" for j in range(columns) ] for i in range(rows)
    ]

def add_token(board: list, column: int, identifier: str) -> list:
    '''fügt einen Spielstein zur gegebenen Spalte hinzu'''
    cols = get_column(board, column)
    board[cols.count("") - 1][column] = identifier
    return board

def gameboard_to_string(board: list) -> str:
    '''erzeugt einen String aus einem gegebenen Board'''
    format_row = lambda row: "".join("{:^4}".format(e if e != '' else "''") for e in row) + '\n'
    formatted_board = map(format_row, board)
    return "".join(formatted_board)

def check_valid_move(board: list, column: int) -> bool:
    '''checkt, ob in einer Spalte noch freie Plätze sind'''
    return get_column(board, column).count("") >= 1

def get_column(board: list, column: int) -> list:
    ''' gibt eine Spalte zurück '''
    return [ row[column] for row in board ]

def get_identifier_at_position(board: list, row: int, column: int) -> str:
    ''' Gibt den identifier an einer Position auf dem Board zurück, gibt einen leeren String zurück, wenn die Position nicht valide ist '''
    if row < 0 or column < 0 or row > (len(board) - 1) or column > (len(board[0]) - 1):
        return ''
    if board[row][column] == '':
        return ' '
    return board[row][column]


def get_diag_left_right(board: list, row: int, column: int) -> list:
    '''gibt die diagonale unten links nach oben rechts (ausgegangen vom angegebenen Punkt)'''
    #up wird ab 0 durchgeführt, damit der Punkt von dem ausgegangen wird auch enthalten ist
    down = [ get_identifier_at_position(board, row + i, column - i) for i in range(1, len(board))]
    down.reverse()
    up = [ get_identifier_at_position(board, row - i, column + i) for i in range(0, len(board) )]
    return down + up

def get_diag_right_left(board: list, row: int, column: int) -> list:
    '''gibt die diagonale unten rechts nach oben links (ausgegangen vom angegebenen Punkt)'''
    down = [ get_identifier_at_position(board, row + i, column + i) for i in range(1, len(board) )]
    down.reverse()
    up = [ get_identifier_at_position(board, row - i, column - i) for i in range(0, len(board) )]
    return up + down

def get_all_identifier_positions(board: list, identifier: str) -> list:
    ''' ruft die Position aller Spielsteine einer Art auf dem Board ab'''
    enumerated_board = [ enumerate(row) for row in board ]
    position_board = [
        [ (i , element[0]) for element in enumerated_board[i] if element[1] == identifier ] for i in range(len(enumerated_board))
    ]
    return position_board

def check_won(board: list, identifier: str) -> bool:
    '''Überprüft ob der Spieler mit dem angegebenen Symbol gewonnen hat'''
    concat_rows = lambda result, row: result + row
    ident_positions = reduce(concat_rows, get_all_identifier_positions(board, identifier), [])
    return any([ check_identifier_won(board, coords[0], coords[1], identifier) for coords in ident_positions ])

def check_identifier_won(board: list, row: int, column: int, identifier: str) -> bool:
    '''überprüft ob ein identifer teil einer Kombination ist durch die der Spieler gewonnen hat '''
    diag_lr = "".join(get_diag_left_right(board, row, column))
    diag_rl = "".join(get_diag_right_left(board, row, column))
    col = "".join([ e if e != '' else ' ' for e in get_column(board, column)])
    r = "".join([ e if e != '' else ' ' for e in board[row]])

    find_list = [diag_lr.find(identifier*4), diag_rl.find(identifier*4), col.find(identifier*4), r.find(identifier*4)]

    return any([ e != -1 for e in find_list ])

def print_round_start(turn: int, board: list, identifier: str):
    '''Funktion, um alle Informationen bei Rundenstart auszugeben'''
    print("".join("\n" for i in range(5)))
    #Ausgeben der Trennlinie
    separator = "".join("-" for i in range(10))
    print(separator + " Zug Nr. {:^3}".format(turn + 1) + separator + "\n")
    #Ausgeben des Spielfelds
    print(gameboard_to_string(board))
    #Ausgabe Koordinaten unter dem Board
    print("".join("{:^4}".format(i) for i in range(len(board[0])))) 
    print("Spieler (" + identifier +  ") " + str(1 + (turn % 2)) + " ist an der Reihe")

def basic_user_input():
    '''Funktion, um den User-Input einzulesen und zu validieren'''
    try:
        user_input = input("Spalte: ")
        selected_column = cast_and_validate_input(user_input)
    except ValueError:
        print("Bitte gib einen validen Wert an")
        return basic_user_inupt()
    return selected_column

def cast_and_validate_input(user_input):
    casted_input = int(user_input)
    if casted_input < 0 or casted_input > 7:
        raise ValueError
    return casted_input

def get_identifier(turn: int) -> str:
    return 'x' if turn % 2 == 0 else 'o'

def game_round(turn: int, board: list, selected_column):
    '''Simuliert eine Runde des Spiels und gibt das aktuelle Board zurück'''
    identifier = get_identifier(turn)
    #Wenn der angegebene Zug valide war wird das Board zurück gegeben, ansonsten ruft die Funktion sich mit den gleichen Werten selbst auf
    board = add_token(board, selected_column, identifier)
    return board
    
def game_loop(get_user_input):
    '''Gameloop Funktion, als Iterator damit der Verlauf des Spiels im nachhinein ausgegeben werden kann'''
    board = generate_gameboard(8, 8)
    turn = 0

    while True:
        identifier = get_identifier(turn)
        print_round_start(turn, board, identifier)
        selected_column = get_user_input()
        if check_valid_move(board, selected_column):
            board = game_round(turn, board, selected_column)
            turn += 1
            yield board

        if check_won(board, identifier):
            print_round_start(turn - 1, board, identifier)
            print("Spieler (" + identifier +  ") " + str(1 + ((turn-1) % 2)) + " hat Gewonnen!!!!!!")
            raise StopIteration

def start():
    game = game_loop(basic_user_input)

    while True:
        try:
            next(game)
        except:
            break

if __name__ == "__main__":
    start()