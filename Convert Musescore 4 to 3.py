
# Path to your MuseScore 3 executable
mscore3 = 'C:/Program Files/MuseScore 3/bin/musescore3.exe'

# Path to your MuseScore 4 executable
mscore4 = 'C:/Program Files/MuseScore 4/bin/musescore4.exe'

# Path to the folder where your mszc file(s) are currently located
# This line must end with /'
sourceFolder ='C:/Users/ThisGuy/Desktop/Sheet Music/'

# Path to the folder where the converted files will be created
# This line must end with /'
destFolder = 'C:/Users/ThisGuy/Desktop/Mobile MuseScore Sheet Music/'



import os, subprocess

# Count the number of mscz files in the source folder to convert
count1 = 0
count2 = 0
for file in os.listdir(sourceFolder):
    if file.endswith("mscz"): count1 += 1
print (str(count1) + " files to convert.\n")

# Convert the MuseScore 4 files to MuseScore 3 files
for file in os.listdir(sourceFolder):
    
    if file.endswith("mscz"):
    
        count2 += 1
        print("Converting file " + str(count2) + " of " + str(count1))
        
        # Convert from MuseScore 4 mscz to mxl
        command1 = '"' + mscore4 + '" -o "' + destFolder + file[:-4] + 'mxl" "' + sourceFolder + file + '"'
        #print(command1)
        try:
            subprocess.run(command1)
        except:
            print("Unable to convert " + file + " to " + file[:-4] + "mxl")
            continue
        
        # Convert from mxl to MuseScore 3 mscz with default style sheet
        command2 = '"' + mscore3 + '" -S "' + destFolder + 'Style-Defaults.mss" -o "' + destFolder + file + '" "' + destFolder + file[:-4] + 'mxl"'
        #print(command2)
        try:
            subprocess.run(command2)
        except:
            print("Unable to convert " + file[:-4] + "mxl to " + file)


print("Done!")
os.system("pause")
