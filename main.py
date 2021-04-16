# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# part 1 of the exercise
#names of the scorers
scorer_1 = "Ruud Gullit"
scorer_2 = "Marco van Basten"
#minutes of the goals
goal_0 = 32
goal_1 = 54
scorers = (scorer_1 + " " + str(goal_0) + ', ' + scorer_2 + " " + str(goal_1))
print (scorers)
report = (scorer_1 + " scored in the " + str(goal_0) + "nd minute" "\n"+ 
scorer_2 + " scored in the " + str(goal_1) + "th minute")
print (report)

#part 2 of the exercise
player = "Oleksandr Zavarov"
first_name = player [:9]
last_name = player [-7:]
#lenght of the lastname
last_name_len = len(last_name)
print (last_name_len)
#Shortname of player_1
name_short = (player [:1] + '.' + ' ' + last_name)
print (name_short)

# Ik weet dat ik onderstaande niet helemaal goed heb,
# maar ik heb vanmiddag om 12.34 een vraag gesteld en geen antwoord gekregen
# ga hem nu toch inleveren, anders kan ik (het hele weekend) niet verder
# het lukt me niet om de laatste spatie met de 'inequality operator' op te lossen
# Ik had hier graag advies in gehad.

#chant
chant = (last_name_len * (first_name + "!"+" "))
print (chant)

#  good_chant
good_chant = chant
print (good_chant)









