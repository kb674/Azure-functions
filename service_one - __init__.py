import logging
import requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey

endpoint = "add cosmo db endpoint"
key = "add cosmo db key"

client = CosmosClient(endpoint, key)
database = client.create_database_if_not_exists(id="lettersandnumbers")
container = database.create_container_if_not_exists(id="container1", partition_key=PartitionKey(path="/username"), offer_throughput=400)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letters = requests.get("add url of service two")
    numbers = requests.get("add url of service three")

    username = letters.text+numbers.text
    container.create_item(body={"id": str(3), "username": username})

    return func.HttpResponse(
        username,
        status_code=200
    )
