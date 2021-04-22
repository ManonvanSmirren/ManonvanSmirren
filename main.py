# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# part 1 of the exercise
#names of the scorers
scorer_1 = "Ruud Gullit"
scorer_2 = "Marco van Basten"
#minutes of the goals
goal_1 = 32
goal_2 = 54
scorers = (scorer_1 + " " + str(goal_1) + ', ' + scorer_2 + " " + str(goal_2))
print (scorers)

report = f"{scorer_1} scored in the {goal_1}nd minute \n{scorer_2} scored in the {goal_2}th minute"
print (report)

#part 2 of the exercise
player = "Oleksandr Zavarov"

len_first_name = (player.find(' '))
# print (len_first_name) only for checking

first_name = player [:len_first_name]
print (first_name)

len_last_name = len(player[(player.find(' ') +1):])
# print (len_last_name)only for checking

last_name = player [-len_last_name:]
print (last_name)

#Shortname of player_1
name_short = (player [:1] + '.' + ' ' + last_name)
print (name_short)

#chant
chant = (len_last_name * (first_name + "!"+" ")[:-1])
print (chant)

# check laatste position chant, mag geen spatie zijn
good_chant = chant[-1]
print (good_chant != " ")









