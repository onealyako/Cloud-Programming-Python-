import boto3
import csv
import pandas as pd

# This will automatically select correct economic data CSV files
def data_selector_econ(existing_table):
    dynamodb = boto3.resource('dynamodb', 'ca-central-1')

    print("\t Ensure these CSV files exist:\n\t• shortlist_gdppc.csv\n\t• shortlist_curpop.csv\n")
    print("\t * * * You MUST enter directory path where your CSV is stored. Use below path as sample on what you ONLY can enter.\n\t\t/Users/onealyako/Documents/Cloud/A2/\n\t* * * Do NOT include any .csv file (or any file in general) in your path. * * *\n\n")
    user_path = input("Enter your directory path (NO file names, just the path): ")
    filePath = user_path
    table_db = dynamodb.Table(existing_table)

    cur_pop = {}
    table = []

    with open(filePath+'shortlist_curpop.csv') as curpop_file:
        for line in curpop_file:
            fields = line.strip().split(',')
            cur_pop[fields[0]] = ','.join(fields[1:])

    with open(filePath+'shortlist_gdppc.csv') as countries_file:
        for line in countries_file:
            fields = line.strip().split(',')
            table.append(
                {
                    'Country': fields[0],
                    '1970': fields[1],
                    '1971': fields[2],
                    '1972': fields[3],
                    '1973': fields[4],
                    '1974': fields[5],
                    '1975': fields[6],
                    '1976': fields[7],
                    '1977': fields[8],
                    '1978': fields[9],
                    '1979': fields[10],
                    '1980': fields[11],
                    '1981': fields[12],
                    '1982': fields[13],
                    '1983': fields[14],
                    '1984': fields[15],
                    '1985': fields[16],
                    '1986': fields[17],
                    '1987': fields[18],
                    '1988': fields[19],
                    '1989': fields[20],
                    '1990': fields[21],
                    '1991': fields[22],
                    '1992': fields[23],
                    '1993': fields[24],
                    '1994': fields[25],
                    '1995': fields[26],
                    '1996': fields[27],
                    '1997': fields[28],
                    '1998': fields[29],
                    '1999': fields[30],
                    '2000': fields[31],
                    '2001': fields[32],
                    '2002': fields[33],
                    '2003': fields[34],
                    '2004': fields[35],
                    '2005': fields[36],
                    '2006': fields[37],
                    '2007': fields[38],
                    '2008': fields[39],
                    '2009': fields[40],
                    '2010': fields[41],
                    '2011': fields[42],
                    '2012': fields[43],
                    '2013': fields[44],
                    '2014': fields[45],
                    '2015': fields[46],
                    '2016': fields[47],
                    '2017': fields[48],
                    '2018': fields[49],
                    '2019': fields[50],
                    'Currency': cur_pop[fields[0]],

                }
            )
            with table_db.batch_writer(overwrite_by_pkeys=['Country']) as batch:
                batch.put_item(
                    Item={
                        'Country': fields[0],
                        '1970': fields[1],
                        '1971': fields[2],
                        '1972': fields[3],
                        '1973': fields[4],
                        '1974': fields[5],
                        '1975': fields[6],
                        '1976': fields[7],
                        '1977': fields[8],
                        '1978': fields[9],
                        '1979': fields[10],
                        '1980': fields[11],
                        '1981': fields[12],
                        '1982': fields[13],
                        '1983': fields[14],
                        '1984': fields[15],
                        '1985': fields[16],
                        '1986': fields[17],
                        '1987': fields[18],
                        '1988': fields[19],
                        '1989': fields[20],
                        '1990': fields[21],
                        '1991': fields[22],
                        '1992': fields[23],
                        '1993': fields[24],
                        '1994': fields[25],
                        '1995': fields[26],
                        '1996': fields[27],
                        '1997': fields[28],
                        '1998': fields[29],
                        '1999': fields[30],
                        '2000': fields[31],
                        '2001': fields[32],
                        '2002': fields[33],
                        '2003': fields[34],
                        '2004': fields[35],
                        '2005': fields[36],
                        '2006': fields[37],
                        '2007': fields[38],
                        '2008': fields[39],
                        '2009': fields[40],
                        '2010': fields[41],
                        '2011': fields[42],
                        '2012': fields[43],
                        '2013': fields[44],
                        '2014': fields[45],
                        '2015': fields[46],
                        '2016': fields[47],
                        '2017': fields[48],
                        '2018': fields[49],
                        '2019': fields[50],
                        'Currency': cur_pop[fields[0]],
                        }
                )