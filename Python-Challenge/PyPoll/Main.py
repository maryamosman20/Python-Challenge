import os
import csv 

file_to_save= os.path.join("analysis","election_analysis.txt")

voters = []

list_candidates = []
candidate_votes ={}
the_percent_of_votes_each_candidate_won = []

the_total_number_of_votes_each_candidate_won = []
total_votes=0
the_winner = []
Count_votes = 0
pecent = 0
paypoll = os.path.join("Resources", "election_data.csv")

winning_percentage = 0
county_name=[]
county_names={}
winning_candidate =""
winning_count= 0
with open(paypoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

   
   #csvheader = next(csv_reader)
   #print(csvheader)



    # read the header row
    csv_header = next(csvreader)
 
    for row in csvreader:
        candidate_name= row[2]
        county_name =row[1]
    # Count of votes
        Count_votes += 1
        if candidate_name not in list_candidates:
            list_candidates.append(candidate_name)
            candidate_votes[candidate_name]= 0
     #Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"total votes: {Count_votes}"
    )
    print(election_results)
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = votes /Count_votes *100
        candidate_results = (f"{candidate_name}: {vote_percentage}% ({votes}) \n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if(votes >winning_count) and (vote_percentage>winning_percentage):
            winning_count =votes
            winning_candidate=candidate_name
            winning_percentage=vote_percentage

    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Count: {winning_count}\n"
        f"Winning percentage: {winning_percentage}\n"
        f"-----------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)







