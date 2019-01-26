import psycopg2
from graphqlclient import GraphQLClient

#postgres database credentials
connection = psycopg2.connect(database="XXXXXXXXX", user="XXXXXXXXX",
                            password="XXXXXXXXXXXXXXXXXX",
                            host="XXXXXXXXX.XXXX", port="XXXX")

#GraphQL API for CRUD operations
client = GraphQLClient('https://XXXXXXXXX.herokuapp.com/v1alpha1/graphql')

#Wolfram Alpha app id
app_id = "XXXXXXXXXXXXXXX"
