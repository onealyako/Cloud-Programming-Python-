import csv

from createATable import *
from deleteATable import *
from load_country_table import *
from load_pop_data import *
from load_econ_data import *
from query_report_a import *
from query_report_b import *
from pprint import pprint
from boto3.dynamodb.conditions import Key, Attr
import boto3 

# Prompt user to select type of table they want to create.
def create_table_options():
    print("Select an option below for table creation:\n")
    print("\t1. Create UN Country Codes Table\n\t2. Create Economic Data Table\n\t"
          "3. Create Country Data Table\n\t4. Create Population Data Table\n")

    create_table_userSelect = input("Option Selected: ")


    if (create_table_userSelect == '1'):
        name_of_table = input("Enter table name for UN Country Table: ")
        userNaming_UN(name_of_table)

    elif (create_table_userSelect == '2'):
            name_of_table = input("Enter economic data table name: ")
            economic_creation(name_of_table)

    elif (create_table_userSelect == '3'):
            name_of_table = input("Enter country data table name: ")
            country_data_creation(name_of_table)

    elif (create_table_userSelect == '4'):
            name_of_table = input("Enter population data table name: ")
            pop_data_creation(name_of_table)
    else:
        print("\t\n*** INVALID OPTION ***")

# This will delete the table from dynamodb.
def del_table():
    table_to_delete = input("Enter table name you want to delete: ")
    delete_a_table(table_to_delete)

# Adds Item to Table
def add_item_table():
    try:
        print("\t*** NOTE: In order to add an item to a table, ensure the tables you search for contain\n\t\t\t\teither 'economic', OR, 'country', OR ,'population' in its name.")
        existing_table = input("Enter name of table you would like to create new item for: ")

        dynamodb_client = boto3.client('dynamodb')

        try:

            response = dynamodb_client.describe_table(TableName=existing_table)

            # Economic Data Table
            if ("economic" in existing_table):
                print("\tFill in Economic Data Item Information Below...")
                country_name = input("Country Name: ")
                year = int(input("Year: "))
                GDPCC = int(input("GDPCC: "))
                currency = input("Currency: ")

                dynamodb = boto3.resource('dynamodb')
                table = dynamodb.Table(existing_table)

                table.put_item(
                    Item={
                        'Country': country_name,
                        'Year': year,
                        'GDPCC': GDPCC,
                        'Currency': currency,
                    }
                )
                print("SUCCESSFULLY ADDED: " + country_name + ", " + str(year)+", "+str(GDPCC)+", "+currency)

            # Country data table
            elif ("country" in existing_table):
                print("\tFill in Country Data Item Information Below...")
                iso3 = input("ISO3: ")
                country_name = input("Country Name: ")
                area = int(input("Area: "))
                languages = input("Languages: ")
                capital = input("Capital: ")
                off_coun_name = input("Official Country Name: ")

                dynamodb = boto3.resource('dynamodb')
                table = dynamodb.Table(existing_table)

                table.put_item(
                    Item={
                        'ISO3': iso3,
                        'Country Name': country_name,
                        'Area': area,
                        'Languages': languages,
                        'Capital': capital,
                        'Official Country Name': off_coun_name,
                    }
                )
                print("SUCCESSFULLY ADDED: " + iso3 + ", " + capital + ", " + str(area) + ", " + languages+", "+ country_name+", "+off_coun_name)

            # Population Data
            elif ("population" in existing_table):

                print("\tFill in Population Data Item Information Below...")

                iso3 = input("ISO3: ")
                country_name = input("Country: ")
                pop = int(input("Population: "))
                year = int(input("Year: "))

                dynamodb = boto3.resource('dynamodb')
                table = dynamodb.Table(existing_table)

                table.put_item(
                    Item={
                        'ISO3': iso3,
                        'Country': country_name,
                        'Population': pop,
                        'Year': year,

                    }
                )
                print("SUCCESSFULLY ADDED: " + iso3 + ", " + country_name + ", " + str(pop) + ", " + str(year))
            # Else, print error message.
            else:
                print("\t*** FAILED to add item to table. Ensure the table you created contains\neither 'economic', OR, 'country', OR ,'population' in the search below.")
        except dynamodb_client.exceptions.ResourceNotFoundException:
                # do something here as you require
                    print("Table "+existing_table+" does not exist.")

    except Exception:
        print("FAILED to add item to table.")

# Function to Delete item from table
def del_item_table():
    try:
        print("\t*** NOTE: In order to delete an item to a table, ensure the tables you search for contain\n\t\t\t\teither 'economic', OR, 'country', OR ,'population' in the search below.")
        existing_table = input("Enter name of table you would like to delete item from: ")

        dynamodb_client = boto3.client('dynamodb')

        try:
            response = dynamodb_client.describe_table(TableName=existing_table)

            # Economic Data Table
            if ("economic" in existing_table):
                print("\tFill in Economic Data items to delete... ")
                country_name = input("Country Name: ")
                #year = int(input("Year: "))


                dynamodb = boto3.resource('dynamodb')
                table = dynamodb.Table(existing_table)

                table.delete_item(
                    Key={
                        'Country': country_name,
                        #'Year': year,

                    }
                )
                print("SUCCESSFULLY DELETED: "+country_name)

            elif ("country" in existing_table):
                print("\tFill in Country Data items to delete... ")
                country_name = input("Country Name: ")

                dynamodb = boto3.resource('dynamodb')
                table = dynamodb.Table(existing_table)

                table.delete_item(
                    Key={
                        'Country Name': country_name,
                    }
                )
                print("SUCCESSFULLY DELETED: " + country_name)

            elif ("population" in existing_table):
                print("\tFill in population data items to delete... ")
                country_name = input("Country Name: ")
                #year = int(input("Year: "))

                dynamodb = boto3.resource('dynamodb')
                table = dynamodb.Table(existing_table)

                table.delete_item(
                    Key={
                        'Country': country_name,
                        #'Year': year,

                    }
                )
                print("SUCCESSFULLY DELETED: " + country_name + ", ")

            else:
                print("\t*** FAILED to delete item from table. Ensure the table you created contains\neither 'economic', OR, 'country', OR ,'population' in the search below.")

        except:
            print("Table "+existing_table+" does not exist.")

    except:
        print("Failed to delete item from table.")

#Loads CSV files
# Will prompt the user more to narrow down what they want.
def load_csv_file():
    print("\t\t* * * You will specify the table you want to bulk load. **NOTE**: your table name must contain\n\t\teither 'country' OR 'population' OR 'economic' for system to find the type of your table. Make sure if table is created, either of \n\t\tthose workds are contained.")
    existing_table = input("\nEnter name of table you would like to bulk load item for: ")

    dynamodb_client = boto3.client('dynamodb','ca-central-1')

    try:

        dynamodb_client.describe_table(TableName=existing_table)
        if ("country" in existing_table):
            data_selecter(existing_table)

        elif("population" in existing_table):
            data_selecter_pop(existing_table)

        elif("economic" in existing_table):
            data_selector_econ(existing_table)

    except:
        print("Table does not exist.")

def scan_table(table_name):
    dynamodb=boto3.resource('dynamodb',region_name='ca-central-1')
    table = dynamodb.Table(table_name) 
    response = table.scan()
    items = response['Items']
    #print(items)
    for i,j in enumerate(items):
        print(f"Item: {i} --> {j}\n")   

# Prompt user menu to select an option.
def userInteraction():

    # Welcome user to program
    print("\t** Welcome to DynamoDB Interactive Services **")

    while 1:
        print("\nTo continue, choose an option below:\n")
        print("\t1. Create Table\n\t2. Delete Table\n\t3. Load Records from CSV\n\t4. Add Item to Existing Table\n\t5. Delete Item From Table\n\t6. Display Data From Table\n\t7. Build Data Reports\n\t8. Exit Program")

        userInput = input("Option Selected: ")

        # Prompt user for create table option selection
        if (userInput == '1'):
            create_table_options()

        # Prompt user to enter table name they would like to delete
        elif (userInput == '2'):
            del_table()

        # Prompt user with table name they would like to load CSV files for
        elif (userInput == '3'):
            load_csv_file()

        # Prompt user with table name they would like to add items for
        elif (userInput == '4'):
            add_item_table()

        # Prompts user to specify which item they want to delete using key value
        elif (userInput == '5'):
            del_item_table()
        
        # Display all items in a table
        elif (userInput == '6'):
            data_to_display = input("\tEnter table name for data you want displayed: ")
            scan_table(data_to_display)
        
        # Prompts user to select whether they want Report A or Report B
        elif(userInput == '7'):
            print("Select type of report:\n\t1. Report A - Country Level Report\n\t2. Report B - Global Report")
            report_select = input("Enter Report Choice #: ")
            if (report_select == '1'):
                print("\t* * *You will have to enter the country, population, and economic table names in order\n\tto be able to generate a report containing all information. Please ensure the names of each table contain\n\tthe keyword country, population, economic--respectively, in order for program to function.")
                try:
                    dynamodb_client = boto3.client('dynamodb','ca-central-1')
                    # Get country table name
                    country_table_name = input("\t\t\nEnter country table name: ")
                    dynamodb_client.describe_table(TableName=country_table_name)
                    # Get Population table name
                    pop_table_name = input("Enter population table name: ")
                    dynamodb_client.describe_table(TableName=pop_table_name)
                    #query_reports(country_table_name,pop_table_name)
                    # Get economics table name
                    econ_table_name = input("Enter economic table name: ")
                    dynamodb_client.describe_table(TableName=econ_table_name)
                    query_reports(country_table_name,pop_table_name,econ_table_name) 
                    
                except:
                    print("\t* * *Table does not exist. Make sure the table you create has country, population, or economic in the naming.")
            else: 
                print("Report B")
                print("\t* * *You will have to enter the country, population, and economic table names in order\n\tto be able to generate a report containing all information. Please ensure the names of each table contain\n\tthe keyword country, population, economic--respectively, in order for program to function.")
                try:
                    dynamodb_client = boto3.client('dynamodb','ca-central-1')
                    # Get population table name
                    pop_table_name = input("\t\t\nEnter population table name: ")
                    dynamodb_client.describe_table(TableName=pop_table_name)
                    
                    # Get country table name
                    country_table_name = input("\t\t\nEnter country table name: ")
                    dynamodb_client.describe_table(TableName=country_table_name)
                    query_reports_pop_b(pop_table_name,country_table_name)
                   
                    
                except:
                    print("\t* * *Table does not exist. Make sure the table you create has country, population, or economic in the naming.")


        elif (userInput == '8'):
            print("\t\t* * * Exiting Program...GOODBYE! * * *")
            exit()

        # Error check for invalid input. Display message.
        else:
            print("\t** Your input is INVALID. Try again -- select from options to continue.")

userInteraction()