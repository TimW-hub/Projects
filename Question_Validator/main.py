# The goal:
# To be able to copy a lab question from moodle table and paste directly into input of program to idenfity if it works correctly

# Things I know
# the table typically has an input row and expected results row, sometimes a test name row
# may require copying a specific column eg. inputs and results
# when copied the table data leaves blank lines when starting a new row
# the tested program needs to always match output to the results copied

# Things I want to work out
# If my code (input) will generate results (output) which are equal to the results (input) from moodle lab.
# What the differences are between the two sets of results

# Bonus goals
# Distinguish input, results from irrelevant details so that a single copy paste is all that's necessary

# Take info from user
lab_inputs = input("Please copy the input column of the lab question and paste it in here. You can do this by copying to excel and then selecting an individual column.\nInsert: ")
lab_results = input("Please do the same for the results.\nInsert: ")

# now interpret and store inputs as lists/arrays to call within the user code evaluation

# Take code from user and run it
user_code = eval(input("Paste your code into "))

# how do i take user inputs and read them

        # after reading them store into table/array/list

                # somehow put that into the code given by the user

                #run code


                #output result


                #compare vs expected results