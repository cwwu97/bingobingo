import datetime
from google.cloud import bigtable, storage
from google.cloud.bigtable import column_family
from google.cloud.bigtable import row_filters
from google.cloud.bigtable.row_set import RowSet

def implicit():
    

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    # storage_client = storage.Client()
    storage_client = storage.Client.from_service_account_json('bingodis-7466969cd012.json')

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())

def get_bigtable():

    client = bigtable.Client(project='bingodis', admin=True)
    instance = client.instance('bingodis-bigtable')
    table = instance.table('bingo')

    return client, instance, table