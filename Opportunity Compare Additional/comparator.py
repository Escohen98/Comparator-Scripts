#Advanced Comparator (Located in Additional)
sf_file = "Salesforce.txt"
ss_file = "Smartsheet.txt"
fileHandler = open(sf_file, "r")

sf = []
sf_name = []
sf_num = []
sf_date = []

#Loading in the Salesforce opportunity #s
for line in fileHandler:
    txt = str(line)
    sf.append(line)
    sf_name.append(line.split("\t")[0])
    sf_num.append(line.split("\t")[1])
    sf_date.append(line.split("\t")[2])

fileHandler.close
fileHandler = open(ss_file, "r")

ss = []
ss_name = []
ss_num = []
ss_date = []
#Loading in the Smartsheet opportunity #s
for line in fileHandler:
    ss.append(line)
    ss_name.append(line.split("\t")[0])
    ss_num.append(line.split("\t")[1])
    ss_date.append(line.split("\t")[2])
    
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
shared_num = []
shared_name = []
shared_date = []

#Checks if Salesforce list has items in Smartsheet list
#Removes mutual items from both and adds to a shared list
for x in range(0, len(ss_num)):
    #Checks if the opp nums match and if not checks if the name and date (quarter and year) match
    if (sf_num.count(ss_num[x]) > 0 or (sf_name.count(ss_name[x]) and sf_date.count(ss_date[x]))):
        num = ss_num[x]
        date = ss_date[x]
        name = ss_name[x]
        
        if(num == ""):
            num = sf_num[x]
        if(date == ""):
            date = sf_date[x]
        if(name == ""):
            name = sf_name[x]
        
        shared.append(name + " " + num + " " + date)
        shared_num.append(num)
        shared_name.append(name)
        shared_date.append(date)
#Prints to file         
output_file = "output.txt"
fileHandler = open(output_file, "w")

while(True):
    value = input("What column do you want: ")
    if (value == "num"):
       for opp in shared_num:
            fileHandler.write(opp+"\n")
       break
    elif (value == "date"):
        for opp in shared_date:
            fileHandler.write(opp)
        break
    elif (value == "name"):
        for opp in shared_name:
            fileHandler.write(opp+"\n")
        break
    elif (value == "all"):
        fileHandler.write("Opportunities in SF & SS (" + str(len(shared)) + ")\n")
        for opp in shared:
            fileHandler.write(opp)
        break;
    elif (value == "count"):
        print(len(shared))
        break
    elif (value == "help"):
        print("options:")
        print("date\nname\nnum\nall")
    else:
        print("Invalid option.")

fileHandler.close()
print("Done.")



        
        