===================
Basic Functionality
===================

This article explains the various classes of Quartic SDK along with their methods and
available attributes.

===============
GraphQL Client
===============

GraphQLClient
------------

Class refers to the Graphql client which is used as the interface between
the user querying the Quartic AI Platform and their use case.

This class has the following parameters for initialization:

-  **url (mandatory)**: Refers to the host URL the user connects to for
   making API calls.
-  **username (optional)**: Required for Basic Authentication.
-  **password (optional)**: Required for Basic Authentication.
-  **token (optional)**: Required for OAuth2.0 Authentication.
-  **ssl (optional)**: Required when the host needs to be
   verified for SSL.
- **timeout (optional)**: Required if the user wants to specify timeout for API calls.

Here's an example:

::

    client = GraphqlClient(url='https://stag.quartic.ai', username="username", password="password")

The two methods are Basic Authentication and OAuth2.0:
*****************************************************

Basic Authentication:
~~~~~~~~~~~~~~~~~~~~

The user must pass the username and password along with the hostname in the GraphqlClient
to ensure the successive API calls are authenticated via Basic Authentication.

::

    client = GraphqlClient(host="https://test.quartic.ai", username="username", password="password")

OAuth2.0
~~~~~~~~

The user must pass the OAuth token along with the hostname to ensure that all the
successive API calls are authenticated via OAuth2.0. For detailed information on fetching
tokens, please refer to the Quartic Knowledge Base.

::

    client = GraphqlClient(url="https://test.quartic.ai", token="9865c994212e495690c2db3fc6cbdfea")



The available methods are as follows:
*************************************

.version
~~~~~~~~

This method returns the current version of the package.

::

    client.version() # Returns 2.1.0 as of the time of writing this document

.execute_query
~~~~~~~~

This method executes the GraphQL query.

-  **query\_params (required)**: User needs to pass the string in the format given below:

::

    query='''
        query MyQuery {
          Site {
            id
            name
          }
        }'''

-  **variables\_params (optional)**: User can pass a dictionary of variables which are defined in the query in the format below.

::

    query = '''
        mutation($file: Upload!, $edge_connector: Int!, $date_format: DateTime!) {
            uploadTelemetryCsv(
                file: $file,
                fileName: "123",
                edgeConnector: $edge_connector,
                dateFormat: $date_format
                )
                {
                taskId
                status
            }
        }
    '''

    variables = {
        'file': open('<path/to/file>', 'rb'),
        'edge_connector': 'edgeConnector Id',
        'date_format': 'DatTime format'
    }


::

    client.execute_query(query, variables) # Returns a json response on a success.
