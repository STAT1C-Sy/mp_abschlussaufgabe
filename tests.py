from vier_gewinnt import *

def test_generate_gameboard():
    assert(generate_gameboard(3, 3) == [
           ['', '', ''], ['', '', ''], ['', '', '']])
    assert(generate_gameboard(5, 5) == [['', '', '', '', ''], ['', '', '', '', ''], [
           '', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']])

    print("Tests für generate_gameboard erfolgreich")


def test_get_identifier():
    assert(get_identifier(1) == 'o')
    assert(get_identifier(0) == 'x')
    assert(get_identifier(10) == 'x')
    assert(get_identifier(21) == 'o')
    assert(not get_identifier(19) == 'x')
    assert(not get_identifiers(7) == 'o')

    print("Tests für get_identifier erfolgreich")


def test_add_token():
    assert(add_token([["", "", ""], ["x", "", "o"], ["x", "o", "x"]], 2, "x") == [
           ["", "", "x"], ["x", "", "o"], ["x", "o", "x"]])
    assert(add_token([["", "", ""], ["", "", ""], ["", "", ""]], 1, "x") == [
           ["", "", ""], ["", "", ""], ["", "x", ""]])

    print("Tests für add_token erfolgreich")


def test_check_valid_move():
    assert(not check_valid_move(
        [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]], 2))
    assert(check_valid_move(
        [["1", "2", ""], ["4", "5", "6"], ["7", "8", "9"]], 2))
    assert(not check_valid_move(
        [["x", "", ""], ["o", "", ""], ["x", "o", "x"]], 0))
    assert(check_valid_move(
        [["x", "", ""], ["o", "", ""], ["x", "o", "x"]], 2))

    print("Tests für check_valid_move erfolgreich")


def test_get_column():
    assert(get_column([["1", "2", "3"], ["4", "5", "6"],
           ["7", "8", "9"]], 2) == ["3", "6", "9"])
    assert(get_column([["x", "x", "o", "x", "o"], ["x", "o", "o", "o", "o"], ["x", "x", "o", "x", "x"], [
           "o", "x", "o", "x", "o"], ["x", "x", "x", "x", "x"]], 3) == ["x", "o", "x", "x", "x"])
    assert(get_column([["", "o", ""], ["", "x", "o"],
           ["o", "x", "x"]], 2) == ["", "o", "x"])

    print("Tests für get_column erfolgreich")


def test_get_identifier_at_position():
    assert(get_identifier_at_position(
        [["x", "", ""], ["o", "", ""], ["x", "o", "x"]], 0, 0) == "x")
    assert(get_identifier_at_position(
        [["x", "", ""], ["o", "", "o"], ["x", "o", "x"]], 1, 2) == "o")
    assert(get_identifier_at_position(
        [["x", "", ""], ["o", "", ""], ["x", "o", "x"]], -2, 3) == "")
    assert(get_identifier_at_position(
        [["x", "", ""], ["o", "", ""], ["x", "o", "x"]], 10, 0) == "")
    assert(get_identifier_at_position(
        [["x", "", ""], ["o", "", ""], ["x", "o", "x"]], 1, 2) == " ")

    print("Tests für get_identifier_at_position erfolgreich")


def test_get_all_identifier_positions():
    assert(get_all_identifier_positions([["x", "", "o", ""], ["o", "", "", ""], ["x", "", "x", ""], [
           "x", "o", "o", "x"]], "x") == [[(0, 0)], [], [(2, 0), (2, 2)], [(3, 0), (3, 3)]])
    assert(get_all_identifier_positions([["x", "", "o", ""], ["o", "", "", ""], ["x", "", "x", ""], [
           "x", "o", "o", "x"]], "o") == [[(0, 2)], [(1, 0)], [], [(3, 1), (3, 2)]])

    print("Tests für get_all_identifier_positions erfolgreich")


def test_gameboard_to_string():
    assert(gameboard_to_string([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]) == " 1   2   3  \n 4   5   6  \n 7   8   9  \n")
    print("Tests für gameboard_to_string erfolgreich")


def test_check_identifier_won():
    assert(check_identifier_won([["x", "", "", ""], ["x", "", "", ""], [
           "x", "", "", ""], ["x", "", "", ""]], 0, 0, "x"))
    assert(check_identifier_won([["x", "x", "x", "x"], ["", "", "", ""], [
           "", "", "", ""], ["", "", "", ""]], 0, 3, "x"))
    assert(check_identifier_won([["o", "", "", ""], ["", "o", "", ""], [
           "", "", "o", ""], ["", "", "", "o"]], 1, 1, "o"))
    assert(check_identifier_won([["", "", "", "o"], ["", "", "o", ""], [
           "", "o", "", ""], ["o", "", "", ""]], 3, 0, "o"))
    assert(not check_identifier_won([["x", "", "o", ""], ["o", "", "", ""], [
           "x", "", "x", ""], ["x", "o", "o", "x"]], 3, 0, "x"))

    print("Tests für check_identifier_won erfolgreich")


def test_get_diag_left_right():
    assert(get_diag_left_right([["1", "2", "3", "4"], ["5", "6", "7", "8"], [
           "9", "10", "11", "12"], ["13", "14", "15", "16"]], 0, 3) == ['13', '10', '7', '4', '', '', ''])
    assert(get_diag_left_right([["1", "2", "3", "4"], ["5", "6", "7", "8"], [
           "9", "10", "11", "12"], ["13", "14", "15", "16"]], 1, 1) == ['', '', '9', '6', '3', '', ''])
    assert(get_diag_left_right([["1", "2", "3", "4"], ["5", "6", "7", "8"], [
           "9", "10", "11", "12"], ["13", "14", "15", "16"]], 0, 1) == ['', '', '5', '2', '', '', ''])

    print("Tests für get_diag_left_right erfolgreich")


def test_get_diag_right_left():
    assert(get_diag_right_left([["1", "2", "3", "4"], ["5", "6", "7", "8"], [
           "9", "10", "11", "12"], ["13", "14", "15", "16"]], 0, 0) == ['1', '', '', '', '6', '11', '16'])
    assert(get_diag_right_left([["1", "2", "3", "4"], ["5", "6", "7", "8"], [
           "9", "10", "11", "12"], ["13", "14", "15", "16"]], 1, 0) == ['5', '', '', '', '10', '15', ''])
    assert(get_diag_right_left([["1", "2", "3", "4"], ["5", "6", "7", "8"], [
           "9", "10", "11", "12"], ["13", "14", "15", "16"]], 2, 0) == ['9', '', '', '', '14', '', ''])

    print("Tests für get_diag_right_left erfolgreich")


def test_check_won():
    assert(check_won([["x", "", "", ""], ["x", "", "", ""],
           ["x", "", "", ""], ["x", "", "", ""]], "x"))
    assert(check_won([["x", "x", "x", "x"], ["", "", "", ""],
           ["", "", "", ""], ["", "", "", ""]], "x"))
    assert(check_won([["o", "", "", ""], ["", "o", "", ""],
           ["", "", "o", ""], ["", "", "", "o"]], "o"))
    assert(check_won([["", "", "", "o"], ["", "", "o", ""],
           ["", "o", "", ""], ["o", "", "", ""]], "o"))
    assert(not check_won([["x", "", "o", ""], ["o", "", "", ""], [
           "x", "", "x", ""], ["x", "o", "o", "x"]], "x"))

    print("Tests für check_won erfolgreich")


def test_cast_and_validate_input():
    assert(cast_and_validate_input(3) == 3)
    assert(cast_and_validate_input(1) == 1)
    assert(cast_and_validate_input(0) == 0)
    assert(not cast_and_validate_input(8) == 8)
    assert(not cast_and_validate_input(-3))

    print("Tests für cast_and_validate_input erfolgreich")


def test_game_round():
    assert(game_round(6, [["x", "", ""], ["o", "", ""], ["x", "o", "o"]], 1) == [
           ["x", "", ""], ["o", "x", ""], ["x", "o", "o"]])
    assert(game_round(7, [["x", "", ""], ["o", "x", ""], ["x", "o", "o"]], 2) == [
           ["x", "", ""], ["o", "x", "o"], ["x", "o", "o"]])
    assert(game_round(1, [["", "", ""], ["", "", ""], ["", "", ""]], 0) == [
           ["", "", ""], ["", "", ""], ["o", "", ""]])
    assert(not game_round(1, [["", "", ""], ["", "", ""], ["", "", ""]], 0) == [
           ["", "", ""], ["", "", ""], ["x", "", ""]])
    assert(not game_round(7, [["x", "", ""], ["o", "x", ""], ["x", "o", "o"]], 2) == [
           ["x", "", ""], ["o", "x", "x"], ["x", "o", "o"]])

    print("Tests für game_round erfolgreich")


def run_all_tests():

    test_get_all_identifier_positions()
    test_check_identifier_won()
    test_check_won()
    test_get_identifier_at_position()
    test_game_round()
    test_add_token()
    test_get_column()
    test_get_diag_left_right()
    test_get_diag_right_left()
    test_gameboard_to_string()

    print("Alle Tests wurden erfolgreich ausgeführt!")


run_all_tests()

