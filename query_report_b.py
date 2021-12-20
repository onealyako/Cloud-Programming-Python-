import boto3
from boto3.dynamodb.conditions import Key, Attr
from tabulate import tabulate

# Global Report B 
def query_reports_pop_b(pop_table_name,country_table_name):

    # Prompt user to enter year for Global Report B
    year_selection = input("Enter Year for Report B: ")
    dynamodb = boto3.resource('dynamodb')
    dynamodb_two = boto3.resource('dynamodb')

    # Store population table information below...
    table = dynamodb.Table(pop_table_name)
    response = table.scan(AttributesToGet=["Country",year_selection]) 
    items = response['Items']
    mydict=items

    # Store country table information below...
    table_two = dynamodb_two.Table(country_table_name)
    response_country = table_two.scan(AttributesToGet=["Country Name","Area"]) 
    items_country = response_country['Items']
    codict = items_country
  
    print("\nReport B - Global  Report")
    print("\n\t\tGlobal Report\n")
    
    # Below outputs table ranked by population 
    print("Year: "+year_selection+"\n")
    print("Table of Countries Ranked by Population")
    print("--------------------------------------------------------")
    print("Country Name | Population | Rank |\n--------------------------------------------------------")
    for val in mydict:
       data_co=[val['Country']]
       data_yr=[val[year_selection]]
       data_final=[[data_co,data_yr]]
       print(tabulate(data_final))
    print("--------------------------------------------------------")
    
    # Below outputs Ranked By Area 
    print("\nTable of Countries Ranked by Area")
    print("--------------------------------------------------------")
    print("Country Name | Area (sq km) | Rank |\n--------------------------------------------------------")
    for val in codict:
        data_con=[val['Country Name']]
        data_area=[val['Area']]
        data_final_co=[[data_con,data_area]]
        print(tabulate(data_final_co))
