# python_challenge
Created a new repository for this project called python-challenge. 
Cloned the new repository to the computer.
Inside the local Git repository, created a folder for each Python assignment and named them PyBank and PyPoll.
In each folder that was created, added the following content:
A new file called main.py to run for each analysis.
A Resources folder that contains the CSV files 
# python_challenge - Pybank
An analysis folder that contains the output text file that has the results from the analysis.
To get the full path of the directory used the os.chdir(os.path.realpath(_file_))
Set variables for counter, Total_sum, Greatest_increase, Greatest_decrease, Greatest_increase_date, Greatest_decrease_date, Previous_profit as zero. Changes as an array
Pull out header row with next(csvreader) and assign value to previous_profit and Total_sum
For loop in csv reader to read through rows. Counter updates the month count. Total_sum is the total profit or loss. Append profit and loss Changes to the array.  Update greatest_decrease amd Greatest_increase. Since there are negative numbers establish if else statements less than zero, for Greatest_decrease and Greatest_increase.
Average of changes with for loop for Change to iterate through rows
Print the total number of months included in dataset, net total amount of Profit/losses over the entire period, Changes in "profit/losses" and average using F-string, variables go inside {}
Open a text file for writing the results and Write csv file using .writelines()
# python_challenge - Pypoll
Similar logic as above for full path of directory
For loop in csv reader to iterate through rows. 
Establish initial variables, Count the total number of votes and candidate name
Loop through the rows and find the vote count for each candidate with if/else statement of 
candidate_votes dictionary with candidate name as key and votes as the value. 
Print headers, Total number of votes, Complete list of candidates using round brackets
Open text file for writing results,.writelines()
Printpercent votes, list of candidates, percentage and number of votes to the file using F-string
Calculate the winner of the election with if statement 
Using the terminal, first cd into folder, enter git add (name of the folder), enter git commit-m "update", enter git push
Debugging was focused on additional code os.chdir, and git commit command on terminal.


