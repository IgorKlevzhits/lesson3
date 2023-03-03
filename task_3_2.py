letters_cost_one_point = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"]
letters_cost_two_points = ["D", "G"]
letters_cost_three_points = ["B", "C", "M", "P"]
letters_cost_four_points = ["F", "H", "V", "W", "Y"]
letters_cost_five_points = ["K"]
letters_cost_eight_points = ["J", "X"]
letters_cost_ten_points = ["Q", "Z"]

player_word = input("Введите ваше слово латинскими буквами: ").upper()
cost_player_word = 0

for letter in letters_cost_one_point:
    for str in player_word:
        if letter == str:
            cost_player_word += 1

for letter in letters_cost_two_points:
    for str in player_word:
        if letter == str:
            cost_player_word += 2

for letter in letters_cost_three_points:
    for str in player_word:
        if letter == str:
            cost_player_word += 3

for letter in letters_cost_four_points:
    for str in player_word:
        if letter == str:
            cost_player_word += 4

for letter in letters_cost_five_points:
    for str in player_word:
        if letter == str:
            cost_player_word += 5

for letter in letters_cost_eight_points:
    for str in player_word:
        if letter == str:
            cost_player_word += 8

for letter in letters_cost_ten_points:
    for str in player_word:
        if letter == str:
            cost_player_word += 10

print(cost_player_word)
