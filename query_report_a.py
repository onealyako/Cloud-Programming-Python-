import boto3
from boto3.dynamodb.conditions import Key, Attr

# Generate report (REPORT A)
def query_reports(country_table_name,pop_data_name,econ_table_name):
    
    # Prompt user to select country for Report A
    country_selection = input("Enter Country Name for Report A: ")

    dynamodb = boto3.resource('dynamodb')

    # Store country table name into table variable
    table = dynamodb.Table(country_table_name)
    response = table.scan(
        FilterExpression=Attr('Country Name').eq(country_selection)
    )

    # The below is for country data table.
    items = response['Items']
    mydict = items
    act_dict=(mydict[0]) #Store the items in list into a dict

     # Store UN table name into table variable
    table = dynamodb.Table('UN_country_codes')
    response_un = table.scan(
        FilterExpression=Attr('name').eq(country_selection)
    )
    un_items = response_un['Items']
    myUN = un_items
    un_dict = (myUN[0])
    

    print("\nReport A - Country Level Report")
    print("--------------------------------------------------------")
    print("\n\t\t\tName of Country: "+act_dict['Country Name'])
    print("\t\t\tOfficial Name: "+un_dict['officialname'])
    print("\n\t\tArea: "+act_dict['Area'])
    print("\t\tOfficial/National Languages: "+act_dict['Languages'])
    print("\t\tCapital City: "+act_dict['Capital'])
    query_reports_pop(pop_data_name,country_selection,econ_table_name)

def query_reports_pop(pop_data_name,country_selection,econ_table_name):
    dynamodb = boto3.resource('dynamodb')

    # Store country table name into table variable
    table = dynamodb.Table(pop_data_name)
    response = table.scan(
        FilterExpression=Attr('Country').eq(country_selection)
    )

    items = response['Items']
    mydict = items
    act_dict=(mydict[0]) #Store the items in list into a dict

    # Create Population Table
    print("\nPopulation\n--------------------------------------------------------")
    print("Year |\tPopulation | Rank | Population Density | Rank |\n--------------------------------------------------------\n1970 | "+"\t"+act_dict['1970'])
    print("1971 | "+"\t"+act_dict['1971'])
    print("1972 | "+"\t"+act_dict['1972'])
    print("1973 | "+"\t"+act_dict['1973'])
    print("1974 | "+"\t"+act_dict['1974'])
    print("1975 | "+"\t"+act_dict['1975'])
    print("1976 | "+"\t"+act_dict['1976'])
    print("1977 | "+"\t"+act_dict['1977'])
    print("1978 | "+"\t"+act_dict['1978'])
    print("1979 | "+"\t"+act_dict['1979'])
    print("1980 | "+"\t"+act_dict['1980'])
    print("1981 | "+"\t"+act_dict['1981'])
    print("1982 | "+"\t"+act_dict['1982'])
    print("1983 | "+"\t"+act_dict['1983'])
    print("1984 | "+"\t"+act_dict['1984'])
    print("1985 | "+"\t"+act_dict['1985'])
    print("1986 | "+"\t"+act_dict['1986'])
    print("1987 | "+"\t"+act_dict['1987'])
    print("1988 | "+"\t"+act_dict['1988'])
    print("1989 | "+"\t"+act_dict['1989'])
    print("1990 | "+"\t"+act_dict['1990'])
    print("1991 | "+"\t"+act_dict['1991'])
    print("1992 | "+"\t"+act_dict['1992'])
    print("1993 | "+"\t"+act_dict['1993'])
    print("1994 | "+"\t"+act_dict['1994'])
    print("1995 | "+"\t"+act_dict['1995'])
    print("1996 | "+"\t"+act_dict['1996'])
    print("1997 | "+"\t"+act_dict['1997'])
    print("1998 | "+"\t"+act_dict['1998'])
    print("1999 | "+"\t"+act_dict['1999'])
    print("2000 | "+"\t"+act_dict['2000'])
    print("2001 | "+"\t"+act_dict['2001'])
    print("2002 | "+"\t"+act_dict['2002'])
    print("2003 | "+"\t"+act_dict['2003'])
    print("2004 | "+"\t"+act_dict['2004'])
    print("2005 | "+"\t"+act_dict['2005'])
    print("2006 | "+"\t"+act_dict['2006'])
    print("2007 | "+"\t"+act_dict['2007'])
    print("2008 | "+"\t"+act_dict['2008'])
    print("2009 | "+"\t"+act_dict['2009'])
    print("2010 | "+"\t"+act_dict['2010'])
    print("2011 | "+"\t"+act_dict['2011'])
    print("2012 | "+"\t"+act_dict['2012'])
    print("2013 | "+"\t"+act_dict['2013'])
    print("2014 | "+"\t"+act_dict['2014'])
    print("2015 | "+"\t"+act_dict['2015'])
    print("2016 | "+"\t"+act_dict['2016'])
    print("2017 | "+"\t"+act_dict['2017'])
    print("2018 | "+"\t"+act_dict['2018'])
    print("2019 | "+"\t"+act_dict['2019'])
    print("\n--------------------------------------------------------")
    #print("2020 | "+"\t"+act_dict['2020'])
    #print("2021 | "+"\t"+act_dict['2021'])
    #print("2022 | "+"\t"+act_dict['2022'])
    query_econ_reports(country_selection,econ_table_name)

def query_econ_reports(country_selection,econ_table_name):
    dynamodb = boto3.resource('dynamodb')

    # Store country table name into table variable
    table = dynamodb.Table(econ_table_name)
    response = table.scan(
        FilterExpression=Attr('Country').eq(country_selection)
    )

    items = response['Items']
    mydict = items
    act_dict=(mydict[0]) #Store the items in list into a dict
    print("\nEconomics\nCurrency: "+"\n"+"--------------------------------------------------------")
    print("Year |\tGDPPC | Rank |\n--------------------------------------------------------\n1970 | "+"\t"+act_dict['1970'])
    print("1971 | "+"\t"+act_dict['1971'])
    print("1972 | "+"\t"+act_dict['1972'])
    print("1973 | "+"\t"+act_dict['1973'])
    print("1974 | "+"\t"+act_dict['1974'])
    print("1975 | "+"\t"+act_dict['1975'])
    print("1976 | "+"\t"+act_dict['1976'])
    print("1977 | "+"\t"+act_dict['1977'])
    print("1978 | "+"\t"+act_dict['1978'])
    print("1979 | "+"\t"+act_dict['1979'])
    print("1980 | "+"\t"+act_dict['1980'])
    print("1981 | "+"\t"+act_dict['1981'])
    print("1982 | "+"\t"+act_dict['1982'])
    print("1983 | "+"\t"+act_dict['1983'])
    print("1984 | "+"\t"+act_dict['1984'])
    print("1985 | "+"\t"+act_dict['1985'])
    print("1986 | "+"\t"+act_dict['1986'])
    print("1987 | "+"\t"+act_dict['1987'])
    print("1988 | "+"\t"+act_dict['1988'])
    print("1989 | "+"\t"+act_dict['1989'])
    print("1990 | "+"\t"+act_dict['1990'])
    print("1991 | "+"\t"+act_dict['1991'])
    print("1992 | "+"\t"+act_dict['1992'])
    print("1993 | "+"\t"+act_dict['1993'])
    print("1994 | "+"\t"+act_dict['1994'])
    print("1995 | "+"\t"+act_dict['1995'])
    print("1996 | "+"\t"+act_dict['1996'])
    print("1997 | "+"\t"+act_dict['1997'])
    print("1998 | "+"\t"+act_dict['1998'])
    print("1999 | "+"\t"+act_dict['1999'])
    print("2000 | "+"\t"+act_dict['2000'])
    print("2001 | "+"\t"+act_dict['2001'])
    print("2002 | "+"\t"+act_dict['2002'])
    print("2003 | "+"\t"+act_dict['2003'])
    print("2004 | "+"\t"+act_dict['2004'])
    print("2005 | "+"\t"+act_dict['2005'])
    print("2006 | "+"\t"+act_dict['2006'])
    print("2007 | "+"\t"+act_dict['2007'])
    print("2008 | "+"\t"+act_dict['2008'])
    print("2009 | "+"\t"+act_dict['2009'])
    print("2010 | "+"\t"+act_dict['2010'])
    print("2011 | "+"\t"+act_dict['2011'])
    print("2012 | "+"\t"+act_dict['2012'])
    print("2013 | "+"\t"+act_dict['2013'])
    print("2014 | "+"\t"+act_dict['2014'])
    print("2015 | "+"\t"+act_dict['2015'])
    print("2016 | "+"\t"+act_dict['2016'])
    print("2017 | "+"\t"+act_dict['2017'])
    print("2018 | "+"\t"+act_dict['2018'])
    print("2019 | "+"\t"+act_dict['2019'])
    print("\n--------------------------------------------------------")

