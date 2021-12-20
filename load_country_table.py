import boto3
import csv
import pandas as pd

# This will automatically select  all country data CSV files. 
def data_selecter(existing_table):
    dynamodb = boto3.resource('dynamodb', 'ca-central-1')

    print("\t Ensure these CSV files exist:\n\t• shortlist_languages.csv\n\t• shortlist_capitals.csv\n\t• shortlist_area.csv")
    print("\t * * * You MUST enter directory path where your CSV is stored. Use below path as sample on what you ONLY can enter.\n\t\t/Users/onealyako/Documents/Cloud/A2/\n\t* * * Do NOT include any .csv file (or any file in general) in your path. * * *\n\n")
    user_path = input("Enter your directory path (NO file names, just the path): ")
    filePath = user_path
    table_db = dynamodb.Table(existing_table)
    languages = {}
    capital = {}
    table = []

    with open(filePath+'shortlist_languages.csv') as languages_file:
        for line in languages_file:
            fields = line.strip().split(',')
            languages[fields[0]] = ','.join(fields[2:])

    with open(filePath+'shortlist_capitals.csv') as capitals_file:
        for line in capitals_file:
            fields = line.strip().split(',')
            capital[fields[0]] = ','.join(fields[2:])

    with open(filePath+'shortlist_area.csv') as countries_file:
        for line in countries_file:
            fields = line.strip().split(',')
            table.append(
                {
                    'Country Name': fields[1],
                    'Languages': languages[fields[0]],
                    'ISO3': fields[0],
                    'Area': fields[2],
                    'Capital': capital[fields[0]]

                }
            )
            with table_db.batch_writer(overwrite_by_pkeys=['Country Name']) as batch:
                batch.put_item(
                    Item={
                        'Country Name': fields[1],
                        'Languages': languages[fields[0]],
                        'ISO3': fields[0],
                        'Area': fields[2],
                        'Capital': capital[fields[0]]
                    }
                )