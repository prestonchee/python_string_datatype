# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name
#   - my_last_name
#       -set this equal to your last name
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
#   - current_year
#       -set this equal to 2020

my_first_name = "Preston"
my_last_name = "Chee"
my_year_of_birth = 2000
current_year = 2020


# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
#       - last name
#       - first letter of your first name (use the +index)
#       - second letter of your last name (use the -index)
#       - first two letter of your first name (use the +index)
#       - second two letter of your last name (use the -index)

# print (my_first_name)
# print (my_last_name)
# print ( my_first_name[0])
# print (my_last_name[-3])
# print (my_first_name[0:2])
# print (my_last_name[-4:-2])



#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
#       -first name six times

# print (my_first_name, my_last_name)
# print (my_first_name + "\n" * 6)


# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current yeawhol

# birth_year_statement = '{} {} was born in {}'
# print (birth_year_statement.format(my_first_name, my_last_name, my_year_of_birth))
# random_statement ='{}. {} enjoyed celebrating {}'
# print (random_statement.format(birth_year_statement.format(my_first_name,my_last_name,my_year_of_birth), my_first_name , current_year))



# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
#       - tab last name current year
# escape_example = "{}\'s birth year is {}"
# print (escape_example.format(my_first_name,my_year_of_birth))
# tab_escape = '{}\t{}'
# print (tab_escape.format(my_last_name,current_year))

# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
#       - length of last name
#       - first name and last name all in upper case

print(my_first_name.casefold(), my_last_name.casefold())
print (len(my_last_name))
print(my_first_name.upper(), my_last_name.upper())
