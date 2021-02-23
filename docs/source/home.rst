
Installation
---------------

Install using ``pip``:

::

    pip install quartic-sdk

...or follow the following steps to install it from the source:

::

    git clone https://github.com/Quarticai/QuarticSDK/
    python setup.py install

Example
----------

Here's an example on how the Quartic SDK can be used:

Getting the assets, tags, batches from the server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    # Assuming that the Quartic.ai server is at `https://test.quartic.ai`, with the login
    # and the username and password is `username` and `password.`

    from quartic_sdk import APIClient

    client = APIClient("https://test.quartic.ai", username="username", password="password")
    user_assets = client.assets() # Get the list of all assets that the user has access to

    asset = user_assets.get("name","Test Asset") # Get a specific asset with the name "Test Asset"
    asset_tags = asset.get_tags() # Gets the list of all tags
    asset_data = asset.data(start_time=1000000, stop_time=2000000) # Get the data of the asset for the given interval between start_time and stop_time. This returns an iterator, which can be iterated to get all the data points present.
    print(asset_data[0]) # Returns the data present at the 0th index

