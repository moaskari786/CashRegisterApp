# CashRegisterApp
Welcome to Mohammad's Cash Register
In order to run the program you will need to save all these files in your current working directory
-rewardsmember.csv
-grocery.csv
-rmgrocery.csv
-reciept.csv
-register.py

In order to get your reciept we need to make sure pandas is installed in the working directory
Instruction on How to Install pandas
-Make sure Python is installed
-Open terminal
-change you're cd to whherever register.py and other files are saved
-then type pip install pandas

then it's pretty simple
all you need to do is run the file register.py through the terminal
Then the prgram will ask you if you are a rewardsmember and if you are not do you want to sign up
according your answer the program will do different things
if you answer yes the program will ask to enter your phone number, but it will not check if you are not a member, if write an invalid phone number the program will just keep running
once entered a valid phone number the program will ask you to scan items
RULES for scanning items
-You can only write the names of the product which you can find in grocery.csv and rmgrocery.csv
-There can be no mistakes because the scanner is case sensitive

Once Done Scanning items the user must enter the phrase "Done" 
this register does not accept payment so it just assumes that you've paid once you've written Done
Then the register will print your receipt 

IF you answer no the program will ask you to scan items
RULES for scanning items
-You can only write the names of the product which you can find in grocery.csv and rmgrocery.csv
-There can be no mistakes because the scanner is case sensitive

Once Done Scanning items the user must enter the phrase "Done" 
this register does not accept payment so it just assumes that you've paid once you've written Done
Then the register will print your receipt 

if your answer was signup the program will prompt you to enter a phone number which will be stored in the system
then it'll ask you to scan your items
RULES for scanning items
-You can only write the names of the product which you can find in grocery.csv and rmgrocery.csv
-There can be no mistakes because the scanner is case sensitive
Once Done Scanning items the user must enter the phrase "Done" 
this register does not accept payment so it just assumes that you've paid once you've written Done
Then the register will print your receipt 
