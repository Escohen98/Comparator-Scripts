sf_file = "Salesforce.txt"
ss_file = "Smartsheet.txt"
fileHandler = open(sf_file, "r")

sf = []

#Loading in the Salesforce opportunity #s
for line in fileHandler:
    sf.append(line)

fileHandler.close
fileHandler = open(ss_file, "r")

ss = []
#Loading in the Smartsheet opportunity #s
for line in fileHandler:
    ss.append(line)
print(ss)  
#Checks if a id exists in salesforce
#Returns the row value
# def sf_contains(id):
  # if id in sf:
    # return True
  # return False

# def ss_contains(id):
  # if id in ss:
    # return True
  # return False
    
shared = []

#Checks if Salesforce list has items in Smartsheet list
#Removes mutual items from both and adds to a shared list
for opp in ss:
    if (sf.count(opp) > 0):
        shared.append(opp)
        sf.remove(opp)
    else: 
        only_ss.append(opp)
    ss.remove(opp)

#Prints to file         
output_file = "output.txt"
fileHandler = open(output_file, "w")

fileHandler.write("Opportunities in SF & SS (" + str(len(shared)) + ")\n")
for opp in shared:
    fileHandler.write(opp)

fileHandler.write("\nOpportunities only in SF(" + str(len(sf)) + ")\n")
for opp in sf:
    fileHandler.write(opp)
    
fileHandler.write("\nOpportunities only in SS (" + str(len(ss)) + ")\n")
for opp in ss:
    fileHandler.write(opp)

fileHandler.close()
print("Done.")



        
        