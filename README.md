# -MuseScore-sheet-music-mobile-app-local-file-workaround
A fix for those having trouble opening MuseScore files in the mobile app "Musescore: Sheet Music" since the release of MuseScore 4

as of now 2022 Jan 3, the mobile app "MuseScore: sheet music" can't import local mscz files saved in the MuseScore 4 desktop software.  This script is a wrapper for MuseScore's built in command line tools to export files and include style sheets.  This script requres the installation of MuseScore 3 and MuseScore 4 to call those command line tools.

Create a folder to which the converted files will be saved. I created a folder on my desktop called “Mobile MuseScore Sheet Music”.

Next, you’ll need to create a default style sheet file. Open MuseScore 3. If you don’t have a new untitled score open automatically, create a new score, add an instrument, and click finish. It may not be necessary, but you can click on “Format” then “Reset Text Style Overrides”, “Reset Beams”, and “Reset Shapes and Positions”. Click on “Format” again and “Save Style”. Name the file “Style-Defaults.mss” and save it to the folder you created in the previous step.

At the beginning of the Python script, there are four lines that will need to be changed to match your folder paths and file names. The first two variables (mscore3 and mscore4) are the paths to your MuseScore 3 and 4 executables. The next variable (sourceFolder) is the path to the folder containing the mscz files that you will convert from Musescore 4 format. The last variable (destFolder) is the path to the destination folder that you created which contains the Style-Defaults.mss file.

Run the script and move the newly created mscz files to a folder on your tablet or phone.  Then open the Musescore mobile app, tap the "My Library" icon, tap "Songbook", and import your files.
