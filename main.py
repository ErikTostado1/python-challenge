

import os
import csv



#Start of the Pybudget Data Segment

budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')


#The main lists to store the data 

Dates=[]

Profits_Losses=[]

with open(budget_csv) as budget:

    # Split the data on commas

    csvreader = csv.reader(budget, delimiter=',')

# Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    for row in csvreader:
        
        # Appending Dates to the 1st Column.
        Dates.append(row[0])

        # Appending Profit/Losses to the 2nd Column.
        Profits_Losses.append(int(row[1]))


    # Count of Total Months
    Total_Months = len(Dates)

    # Summation of Profits & Losses 
    Total_Profits_Losses_Summed = sum(Profits_Losses)



    # The Loop was referenced by the following website.  
                # https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/
                # 1. (The 2nd Row subtracted the first by the ith row)
                # 2. (Loop is necessary to go through every row) 
                # 3. (Subtraction is necessary because there is one less row from total difference in calculation) 
                # 4. (The Changes_Calc_Avg Variable will be used to Calculate average staying in its true Sample Size; An extra Zero would throw off the average value off.)  
                # 5. (The Changes_Calc_Min_Max Variable Will be solely used to calculate the Min/Max as well as the index positions for the dates variable; An extra zero is required for this computation.
                #     That way there could be alignment between the "Dates" variable and the Changes_Calc_Min_Max Variable.)
                           
    Changes_Calc_Avg = [Profits_Losses[i + 1] - Profits_Losses[i] for i in range(len(Profits_Losses)-1)]
    
    Changes_Calc_Min_Max = [Profits_Losses[i + 1] - Profits_Losses[i] for i in range(len(Profits_Losses)-1)]

    #  We emplace a zero value through the insert function to accommodate.
    # The Following Website was used for reference on this matter. 
    # https://blog.finxter.com/how-to-insert-at-the-first-position-of-a-list-in-python/
    Changes_Calc_Min_Max.insert(0, 0) 

    # Getting Greatest Increase/Decrease in Profits.

    Changes_Max = max(Changes_Calc_Min_Max)
    Changes_Min = min(Changes_Calc_Min_Max)


    # Following Website is a reference to the Index Syntax
    # https://www.programiz.com/python-programming/methods/list/index

    # Max/Min Change Index Position used for Getting Specific element in Dates
    Max_Index = Changes_Calc_Min_Max.index(Changes_Max)
    Min_Index = Changes_Calc_Min_Max.index(Changes_Min)
   

    GIP_Date = Dates[Max_Index]
    GDP_Date = Dates[Min_Index]


    # Computing Average & Total Sum
    Total_Change = sum(Changes_Calc_Avg)
    
    Total_Change_Rows_Avg = len(Changes_Calc_Avg)

    # Average Change with Rounding
    Average_Change_Calc = round(Total_Change / int(Total_Change_Rows_Avg), 2)

    # Budget Data Printing Statement


    print("Financial Analysis")

    print("----------------------------")

    print(f"Total Months:  {Total_Months}")

    print(f"Total:  ${Total_Profits_Losses_Summed}")

    print(f"Average Change: ${Average_Change_Calc}")

    print(f"Greatest Increase in Profits:   {GIP_Date}  (${Changes_Max})")

    print(f"Greatest Decrease in Profits:   {GDP_Date}  (${Changes_Min})")
    

    #The following Website was used for directions on how to create Txt Files with Print Statements. 
    # https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file

    
    Budget_Path = os.path.join('.', 'analysis', 'Budget_Data_Output.txt')

    Budget_Data_Output = open(Budget_Path, "a")
    print("Financial Analysis", file=Budget_Data_Output)
    print("----------------------------", file=Budget_Data_Output)
    print(f"Total Months:  {Total_Months}", file=Budget_Data_Output)

    print(f"Total:  ${Total_Profits_Losses_Summed}", file=Budget_Data_Output)

    print(f"Average Change: ${Average_Change_Calc}", file=Budget_Data_Output)

    print(f"Greatest Increase in Profits:   {GIP_Date}  (${Changes_Max})", file=Budget_Data_Output)

    print(f"Greatest Decrease in Profits:   {GDP_Date}  (${Changes_Min})", file=Budget_Data_Output)


    Budget_Data_Output.close()

    #Start of the Pypoll Data Segment

    election_csv = os.path.join('.', 'Resources', 'election_data.csv')

    Ballot_ID=[]

    County=[]

    Candidate=[]

with open(election_csv) as election:

    # Split the data on commas
    csvreader1 = csv.reader(election, delimiter=',')

# Read the header row first (skip this step if there is no header)
    csv_header1 = next(csvreader1)

    for row in csvreader1:

        Ballot_ID.append(row[0])

        County.append(str(row[1]))

        Candidate.append(str(row[2]))

    # Declaring Fundamental thwe variables
    Total_Votes = len(Candidate)

    # Further Instruction to use the count() function was referenced in the following website.
    # https://www.w3schools.com/python/ref_list_count.asp 

    Cannidate_Charles_Votes = Candidate.count("Charles Casper Stockham")
    
    Cannidate_Diana_Votes = Candidate.count("Diana DeGette")
    
    Cannidate_Raymon_Votes = Candidate.count("Raymon Anthony Doane")
    
    Charles_Percentage = round((Cannidate_Charles_Votes / Total_Votes) * 100, 3)

    Diana_Percentage = round((Cannidate_Diana_Votes / Total_Votes) * 100, 3)

    Raymon_Percentage = round((Cannidate_Raymon_Votes / Total_Votes) * 100, 3)

    # The following defined function is created to get the max occurances off a string. 
    # This function is referenced in this website: https://statisticsglobe.com/count-min-max-occurrences-list-python

    def max_occurrences(List):
        return max(set(List),key = List.count)
    
    Cannidate_Winner = max_occurrences(Candidate)
    
    
    print("----------------------------")

    print("Election Results")

    print("----------------------------")

    print(f"Total Votes:  {Total_Votes}")

    print("----------------------------")

    print(f"Charles Casper Stockham: {Charles_Percentage}% ({Cannidate_Charles_Votes})")

    print(f"Diana DeGette: {Diana_Percentage}% ({Cannidate_Diana_Votes})")

    print(f"Raymon Anthony Doane: {Raymon_Percentage}% ({Cannidate_Raymon_Votes})")

    print(f"Winner: {Cannidate_Winner}")

    Election_Path = os.path.join('.', 'analysis', 'Election_Data_Output.txt')

    Election_Data_Output = open(Election_Path, "a")
    
    print("Election Results", file = Election_Data_Output)

    print("----------------------------", file = Election_Data_Output)

    print(f"Total Votes:  {Total_Votes}", file = Election_Data_Output)

    print("----------------------------", file = Election_Data_Output)

    print(f"Charles Casper Stockham: {Charles_Percentage}% ({Cannidate_Charles_Votes})", file = Election_Data_Output)

    print(f"Diana DeGette: {Diana_Percentage}% ({Cannidate_Diana_Votes})", file = Election_Data_Output)

    print(f"Raymon Anthony Doane: {Raymon_Percentage}% ({Cannidate_Raymon_Votes})", file = Election_Data_Output)

    print(f"Winner: {Cannidate_Winner}", file = Election_Data_Output)
    
    Election_Data_Output.close()


