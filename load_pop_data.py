import boto3
import csv
import pandas as pd

# This will automatically select all population data CSV files in background. 
def data_selecter_pop(existing_table):
    dynamodb = boto3.resource('dynamodb', 'ca-central-1')

    print("\t Ensure these CSV files exist:\n\t• shortlist_curpop.csv\n")
    print("\t * * * You MUST enter directory path where your CSV is stored. Use below path as sample on what you ONLY can enter.\n\t\t/Users/onealyako/Documents/Cloud/A2/\n\t* * * Do NOT include any .csv file (or any file in general) in your path. * * *\n\n")
    user_path = input("Enter your directory path (NO file names, just the path): ")
    filePath = user_path
    table_db = dynamodb.Table(existing_table)

    table = []

    with open(filePath+'shortlist_curpop.csv', encoding="utf-8-sig") as countries_file:
        for line in countries_file:
            fields = line.strip().split(',')
            table.append(
                {
                    'Country': fields[0],
                        '1970': fields[2],
                        '1971': fields[3],
                        '1972': fields[4],
                        '1973': fields[5],
                        '1974': fields[6],
                        '1975': fields[7],
                        '1976': fields[8],
                        '1977': fields[9],
                        '1978': fields[10],
                        '1979': fields[11],
                        '1980': fields[12],
                        '1981': fields[13],
                        '1982': fields[14],
                        '1983': fields[15],
                        '1984': fields[16],
                        '1985': fields[17],
                        '1986': fields[18],
                        '1987': fields[19],
                        '1988': fields[20],
                        '1989': fields[21],
                        '1990': fields[22],
                        '1991': fields[23],
                        '1992': fields[24],
                        '1993': fields[25],
                        '1994': fields[26],
                        '1995': fields[27],
                        '1996': fields[28],
                        '1997': fields[29],
                        '1998': fields[30],
                        '1999': fields[31],
                        '2000': fields[32],
                        '2001': fields[33],
                        '2002': fields[34],
                        '2003': fields[35],
                        '2004': fields[36],
                        '2005': fields[37],
                        '2006': fields[38],
                        '2007': fields[39],
                        '2008': fields[40],
                        '2009': fields[41],
                        '2010': fields[42],
                        '2011': fields[43],
                        '2012': fields[44],
                        '2013': fields[45],
                        '2014': fields[46],
                        '2015': fields[47],
                        '2016': fields[48],
                        '2017': fields[49],
                        '2018': fields[50],
                        '2019': fields[51],


                }
            )

            with table_db.batch_writer(overwrite_by_pkeys=['Country']) as batch:
                batch.put_item(
                    Item={
                        'Country': fields[0],
                        '1970': fields[2],
                        '1971': fields[3],
                        '1972': fields[4],
                        '1973': fields[5],
                        '1974': fields[6],
                        '1975': fields[7],
                        '1976': fields[8],
                        '1977': fields[9],
                        '1978': fields[10],
                        '1979': fields[11],
                        '1980': fields[12],
                        '1981': fields[13],
                        '1982': fields[14],
                        '1983': fields[15],
                        '1984': fields[16],
                        '1985': fields[17],
                        '1986': fields[18],
                        '1987': fields[19],
                        '1988': fields[20],
                        '1989': fields[21],
                        '1990': fields[22],
                        '1991': fields[23],
                        '1992': fields[24],
                        '1993': fields[25],
                        '1994': fields[26],
                        '1995': fields[27],
                        '1996': fields[28],
                        '1997': fields[29],
                        '1998': fields[30],
                        '1999': fields[31],
                        '2000': fields[32],
                        '2001': fields[33],
                        '2002': fields[34],
                        '2003': fields[35],
                        '2004': fields[36],
                        '2005': fields[37],
                        '2006': fields[38],
                        '2007': fields[39],
                        '2008': fields[40],
                        '2009': fields[41],
                        '2010': fields[42],
                        '2011': fields[43],
                        '2012': fields[44],
                        '2013': fields[45],
                        '2014': fields[46],
                        '2015': fields[47],
                        '2016': fields[48],
                        '2017': fields[49],
                        '2018': fields[50],
                        '2019': fields[51],


                    }
                )
