# O'Neal Yako
# Assignment 2
# CIS*4010*CLOUD COMPUTING

--How to Run Program--

**In Mac terminal, I used below and it ran without any errors**: 
     python3 -m userInteraction.py

** TO EXIT PROGRAM: User must input '8'

Quick Program Guide/General Comments: 
--------------------------------------
	       Once you have the program running, you will be shown a user option menu. 
                
	      * * * You MUST create a table using the sample naming convention below:
	   	'oyako_country_data' OR 'oyako_population_data' OR 'oyako_economic_data'

	       I would recommend creating a country data table, population data table, and
	       economic data table as soon as you start the program. Remember what you name
	       them all. 

		Even though I added option to create UN country codes table, I would 
		ignore that as I relied on Deborah's table. 

	       The main thing to remember is when naming the table, make sure the keyword 
	       'country' OR 'population' OR 'economic' is included. This is so that the 
                program can parse and find the right table type when loading data. 

	       * * * You MUST Ensure all CSV files are in the same directory as my program
		     for the load CSV option (#3 from my user menu) to work. 


Python Files Included: 
----------------
userInteraction.py
createATable.py
deleteATable.py
load_country_table.py
load_econ_data.py
load_pop_data.py
query_report_a.py
query_report_b.py

--Understanding User Menu Options--
-------------------------------------
	* * * When you start the program, you are prompted with a user menu to interact with DynamoDb table. * * *

	--SAMPLE of program running startup:
		To continue, choose an option below:
			1. Create Table
			2. Delete Table
			3. Load Records from CSV
			4. Add Item to Existing Table
			5. Delete Item From Table
			6. Display Data From Table
			7. Build Data Reports
			8. Exit Program
		Option Selected: 

To select option, simply input number from user menu.
	Create Table - Option '1' 
        --------------------------	
		Once selected, you will be further asked to specify the table you would like to create.
		
		--SAMPLE of program running:
			Select an option below for table creation:
				1. Create UN Country Codes Table
				2. Create Economic Data Table
				3. Create Country Data Table
				4. Create Population Data Table

		NOTE: I would recommend to not select option '1' (Create UN Country Codes Table), since that already exists.

		IF you select 2, 3, 4, you will be prompted to specify [country/economic/population] table name.
		REMEMBER: you MUST have the correct keyword for each corresponding table. So if you click 
		          'Create Country Data Table', you can name the table whatever you want...just make 
			  sure you have the word 'country' somewhere in the table name. This will be needed
			  for working with your tables later on throughout the program.
	
	Delete Table - Option '2' 
        --------------------------
		Once selected, you will be asked to specify the table you would like to delete. Enter correct table name.

	Load Records from CSV - Option '3' 
        ----------------------------------
		Once selected, you will be asked to specify the table you would like to bulk-load for. Enter correct name.
		* * * MAKE SURE all CSV files are in the location as where  my entire program is running. The CSV files will
		      be automatically run in the background depending on the type of table (ie. Country table will not load 		    		  			'shortlist_gdppc.csv'.

		After specifying table name you will bulk load for, program will ask you to enter directory path. You MUST
		enter your directory path without any file name. Below is a sample of what will work (and what will NOT work).
		Do NOT forget the '/' before entering. 

		* * * MAKE SURE the path you give contains all my python files and all CSV files * * *
		
		See CORRECT directory path entry sample below... 

		* CORRECT directory path entry: '/Users/onealyako/Documents/CloudComputing/Assignment2/'

		** WRONG directory path entry: '/Users/onealyako/Documents/CloudComputing/Assignment2'
		** WRONG directory path entry: '/Users/onealyako/Documents/CloudComputing/Assignment2/filename.py'
		** WRONG directory path entry: '/Users/onealyako/Documents/CloudComputing/Assignment2/shortlist_languages.csv'
		** WRONG directory path entry: 'CloudComputing/Assignment2/'
		** WRONG directory path entry: 'CloudComputing/Assignment2'

		After correct path is properly inputted, you should notice the DynamoDB table properly populate on AWS. An error
		is displayed otherwise (usually saying table does not exist, or file path entry is wrong). * Again *, make sure you 
		move all the CSV files into the same location as my entire program. 

	Add Item to Existing Table - Option '4' 
        ----------------------------------------
		Once selected, you will be asked to specify the table you would like to add item for. Enter correct table name.
		You will then be prompted to enter  specific attribute  values depending on table selected. Follow along with program.

	Delete Item from Table - Option '5' 
        ----------------------------------------
		Once selected, you will be asked to specify the table you would like to delete item for. Enter correct table name.
		You will then be prompted to enter  specific attribute you would like to delete depending on table you enter.
		
		--SAMPLE of program running (with my user input): 
			Enter name of table you would like to delete item from: oyako_population_data
				Fill in population data items to delete... 
			Country Name: Canada

		*** Program will then output the below message to your screen if delete is successful... ***
		SUCCESSFULLY DELETED: Canada,
	
	Display Data From Table - Option '6' 
        -------------------------------------
		This option will display all your items from the specific table you enter (once prompted, after choosing option 6). 

	Build Data Reports - Option '7' 
        --------------------------------
		This option will further prompt you to select the type of report. 
		Select option '1' for Report A - Country Level Report
				OR
		Select option '2' for Report B - Global Report 

		* IF * you select option 1, you will have to enter the country table name, economic table name, population table name all 
		at once. This option will not work unless you have data already in each of those tables. 

		--SAMPLE of program running (with my user input):

		Enter country table name: oyako_country_data
		Enter population table name: oyako_population_data
		Enter economic table name: oyako_economic_data
		Enter Country Name for Report A: Barbados

		If all the tables you input exist in DynamoDb, and the country exists in each one of those tables inputted, you will get
		a Report A generated. Unfortunately, my ranking does not work at all.

		* IF * you select option 2, you will be prompted enter population table name and you will be prompted to enter a year. 
		This Global Report does not fully work unfortunately in terms of what it can output. 

	Exit Program - Option '8' 	
	--------------------------
		This will exit the program. Any other inputs other than the provided (1,2,3,4,5,6,7,8) will generate message to user 
		notifying them of incorrect input.
		
		