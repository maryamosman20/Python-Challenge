#financial budget data records


import os
import csv

file_to_save= os.path.join("analysis","budget_analysis.txt")


months = []
profit_loss_changes = []
count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0
Average = 0

# csvreader files
pybank = os.path.join("Resources", "budget_data.csv")
with open(pybank, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
   


#skip the header row
    header_row =next(csv_reader, None)
    for row in csv_reader:
        count_months += 1

   # print(count_months)

   #find the total net of profit/loss 
   
        current_month_profit_loss = int(row[1])

        if(count_months== 1):
    #then, previous month's profit and loss be equal to the current month's
            previous_month_profit_loss =current_month_profit_loss


        else:
            # check the change in profit and loss
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            
            #add each month when computing the change in profit/loss
            months.append(row[0])

            profit_loss_changes.append(profit_loss_change)

            previous_month_profit_loss = current_month_profit_loss

    
    # the first  and last winner/loser 
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # the total change 
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)


    # Locate the index value of highest and lowest changes in "Profit/Losses" 
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]


    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {count_months}")
    print(f"Total Profit/Loss: {net_profit_loss}")
    print(f"Average Change: {average_profit_loss}")
    print(f"Greatest Increase In Profits: {highest_change}")
    print(f"Greatest Decrease In Profits: {lowest_change}")

text_file = os.path.join("Analysis", "financial_analysis.txt")

with open(text_file, "w") as output:
    output.write("Financial Analysis \n")
    output.write("---------------------------\n")
    output.write(f"Total Months: {count_months}\n")
    output.write(f"Total Profit/Loss: {net_profit_loss}\n")
    output.write(f"Average Changes: {average_profit_loss}\n")
    output.write(f"Greatest Increase In Profits: {best_month} (${highest_change})\n")
    output.write(f"Greatest Decrease In Profits: {worst_month} (${lowest_change}\n")
    output.write("-----  That's a wrap -----------\n") # editorial license ;-)



    

        


    





 