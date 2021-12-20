import boto3

def delete_a_table(table_to_delete):

    try:
        dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')

        table = dynamodb.Table(table_to_delete)

        table.delete()
        print("\t* * * "+table_to_delete+" has been successfully deleted. * * *")
    except:
        print("FAILED to delete table. Ensure correct table name has been entered.")


if __name__ == '__main__':
    delete_a_table()
    print("Table has been deleted.")
