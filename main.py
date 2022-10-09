print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names_joined = (name1 + name2)
names_combined = names_joined.lower()
score_1 = names_combined.count('t') 
score_2 = names_combined.count('r') 
score_3 = names_combined.count('u') 
score_4 = names_combined.count('e')
score_5 = names_combined.count('l')
score_6 = names_combined.count('o')
score_7 = names_combined.count('v')
score_8 = names_combined.count('e')
love_score_1 = score_1 + score_2 + score_3 + score_4
love_score_2 = score_5 + score_6 + score_7 + score_8

love_total = str(love_score_1)+str(love_score_2)
love_number = int(love_total)

if love_number < 10 or love_number > 90:
    print(f"Your score is {love_number}, you are destined for forever.")
elif love_number >= 40 and love_number <= 50:
    print(f"Your score is {love_number}, you are alright together.")
else:
    print(f"Your score is {love_number}, maybe pick someone else.")

print ('''
                _.-==-._            _.-==-._
               ,-'` `.`:::`-.      ,-'` `.`:::`-.
             ,'        `.::::`.  ,'        `.::::`.
            /             `:::::'             `::::\
           |               `.`:'               `.:::|
           |                `:'                 .:::|
           \                                    .:::/  ,///  ,///
   ,dP'     \     .                            ,:::/ ,///  ,///
  <@@@@@@@@@@@@@@@@)                          ,.:/@@@@@@@@@@@@@@
   `?b,        `\ ::                        ,.:/'    `\\\  `\\\
                 `::.                     ,.:/'        `\\\  `\\\
                  `::.                   ,./'
                    ::\                 ,/'
                    `' `\             ,/'
                         `\         ,/'             
                           \      ,:/
                            `\   '/'      
                              \ '/
                               \/
''')