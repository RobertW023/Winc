# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Assignment Strings Part 1
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten' 

goal_0 = 32
goal_1 = 54

scorers =(scorer_1)+' '+str(goal_0)+', '+(scorer_2)+' '+str(goal_1)
print (scorers)

report =(f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute')
print(report)

# Assigment Strings Part 2

player = 'Frank Rijkaard'
first_name = (player[0:5])
print (first_name)

first_name_len = (len(first_name))
print (first_name_len)

last_name = (player[6:])
last_name_len =(len(last_name))
print(last_name_len)

name_short = ((first_name[0]) + '.' + ' ' + (last_name))
print(name_short)

x = (first_name_len - 1)
chant = (x * (first_name + '! ') + (first_name + '!'))
print(chant)

good_chant = chant[-1]!=''
print (good_chant)


