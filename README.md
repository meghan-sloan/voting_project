# Voting Project

### Preliminary data analysis
The first step is to look at the data to see how it is structured and if any cleaning is necessary.  
I recommend using pandas.  
In the voting_EDA.ipynb jupyter notebook you can use the code to look at the data.

### Cleaning
From the EDA, it is obvious that cleaning is needed.
There are only 4 lines in the precinct_polling_list.csv that need cleaning, so this can be done manually.
***However, there are optional functions in the merge_tables.py file for certain cleaning circumstances 
if manual cleaning is unreasonable.***
Additionally, for large datasets, the code could be run and sorted by "NOT AVAILABLE" and new functions written for specific errors.

### Merging
This is an explanation of the merging_data.py file.  
In order to merge the documents based on precinct ID, the IDs must be in the same format.  
In the merging_data.py script, the ID in the precinct_polling_list.csv is changed from the state abbreviation-precinct number
to state number-precinct number.    
  
EXAMPLE:  
NEWY-072 &rarr; 036-072  
  
A dictionary is created with the precinct ID as the key and the address, city, state/ZIP as values sub-dictionaries.
This dictionary is used to map the addresses in the addresses.csv to the correct polling place.  
If data pertaining to a precinct ID from the addresses.csv is absent in the precinct_polling_list.csv, 
"NOT AVAILABLE" is filled into the corresponding cell.  
Note: Address 274 CABOT MAIL CTR (Line 12) has a Precinct ID as 025-076, but this ID is not found in the precinct_polling csv.  Based on the zip code, I think it is safe to assume that this is a typo, and should be corrected to 025-070, but it is currently "NOT AVAILABLE"
There are other addresses with precinct IDs that do not appear in the precinct_polling_list, but I am not sure if these are typos or just not provided.  

### Instructions on using the merging_data.py file
1. Name the files addresses.csv and precinct_polling_list.csv 
2. Make sure the merging_data.py file is in the same directory as the 
3. From the command line type python merging_data.py.  This will save a merged file to the current directory.

### VIP formatting
I used Google drive to format the combined.csv into the polling_location.txt, precinct.txt and precinct_polling_location.txt.
I sorted by address and elimintated "NOT AVAILABLE" rows
Created a new sheet with only the desired rows
Copied the necessary data

### Future Work
In the interest of time, I am submitting the combined csv file as well as the VIP formatted file as is.  
I will continue to explore this problem.  I would like to:
* See if I can find missing information using the Google Civic API
* Build an app that can be hosted on AWS so that users can just upload files and a merged file will be created and can be downloaded.



