from vier_gewinnt import generate_gameboard, get_identifier

#generate_gameboard tests
assert(generate_gameboard(3, 3) == [['', '', ''], ['', '', ''], ['', '', '']])
assert(generate_gameboard(5, 5) == [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']])

#get_identifier tests
assert(get_identifier(1) == 'o')
assert(get_identifier(0) == 'x')
assert(get_identifier(10) == 'x')
assert(get_identifier(21) == 'o')
