#Loads contents of a txt file into an array
#Returns array
def load_file(file):
    fileHandler = open(file, "r")
    array = []
    #Loading in the file to an array
    for line in fileHandler:
        array.append(line[0:len(line)-1])
    fileHandler.close()
    #print(array)
    return array

#Exe type can be either x or w
#This is for basic array writing
def write_file(array, file, exe_type):
    fileHandler = open(file, exe_type)
    for line in array:
        fileHandler.write(line + "\n")
    fileHandler.close()

# #array1 = ss
# #array2 = sf
# #Takes two arrays and returns an array of all strings present in both arrays
# #Warning: Will remove matching values from arrays
# def compare_strings(array1, array2):
    # #Checks if Salesforce list has items in Smartsheet list
    # #Removes mutual items from both and adds to a shared list
# for opp in ss:
    # if (sf.count(opp) > 0):
        # shared.append(opp)
        # sf.remove(opp)
    # else: 
        # only_ss.append(opp)
    # ss.remove(opp)

#Replaces spaces with _ then prints to file. 
#Takes an array of strings, file name, and execution type, and the char to concat.
#Returns array
def concat_string(master_array, split_val, concat_val):
    newArray = []
    for line in master_array: 
        array = line.split(split_val)
        string = array[0]
        if len(array) > 1:
            for val in range(1,len(array)-1):
                string += concat_val + array[val]
        newArray.append(string)
    return newArray
    
#Merges the text of one file with another
def merge_strings(array1, array2, concat_val):
    if (len(array1) != len(array2)):
        ValueError: print("Array length mismatch.")
        return 
    array = []
    for x in range(0,len(array1)-1):
        if(array1[x] != "" and array2[x] != ""):
            array.append(array1[x] + concat_val + array2[x])
        else: 
            array.append("")
    return array

#Main Loop
while(True):
    option = input("Select operation: ")
    if(option == "remove space"):
        read_file = "opp_name.txt"
        file_write = "opp_name_output.txt"
        write_file(concat_string(load_file(read_file)," ", "_"),file_write, "w")
    elif(option == "add space"):
        read_file = input("file: ")
        file_write = "compare_output.txt"
        write_file(concat_string(load_file(read_file),"_", " "),file_write, "w")
    elif(option == "merge column"):
        quarters = load_file("quarter.txt")
        years = load_file("year.txt")
        write_file(merge_strings(quarters, years, "-"), "ss_report_period.txt", "w")
    elif(option == "stop"):
        break
    elif(option == "help"):
        print("Options:")
        print("remove space\nmerge column\nadd space")
    else:
        print("That is not an option.")

    print("Done.")
    
print("Exiting...")
        
    