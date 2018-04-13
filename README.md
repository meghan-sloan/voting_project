# Voting Project

### Preliminary data analysis
The first step is to look at the data to see how it is structured and if any cleaning is necessary.  
I recommend using pandas.  
In the voting_EDA.ipynb jupyter notebook you can use the code to look at the data.

### Cleaning
From the EDA, it is obvious that cleaning is needed as some of the data has ended up in the wrong column.
There are only 4 lines in the precinct_polling_list.csv that need cleaning, so this can be done manually.
However, for large datasets, the merging_data.py code could be run and the resulting data sorted by "NOT AVAILABLE".  New functions could be written for specific errors.  An example is the check_if_zip function in the merging_data.py file.

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
Google drive was used to format the combined.csv into the polling_location.txt, precinct.txt and precinct_polling_location.txt.
Rows were sorted by address and elimintated if "NOT AVAILABLE" since only precinct polling data would be needed.
A new sheet with only the desired columns and copied the necessary data from the combined data sheet. This sheet was downloaded as a .csv, the name changed and the extension changed to .txt.
NOTES: 
In the csv files provided, there is only street, city, state, zip, country, and precinct.  I am not sure where to find the information for the VIP files:
| File      | Missing Data           |
| ------------- |:-------------:|
| polling_location.txt      | address_location_name, directions, polling_hours, photo_url | 
| precinct.txt   | name, locality_id, ward, mail_only, ballot_style_image_url     |
| precinct_polling_location | polling_location_id |

### Future Work
In the interest of time, I am submitting the combined csv file as well as the VIP formatted file as is.  
I will continue to explore this problem.  I would like to:
* Write a script to automate the VIP formatting
* See if I can find missing information using the Google Civic API
* Add additional cleaning functions
* Build an app that can be hosted on AWS so that users can just upload files and a merged file will be created and can be downloaded.



