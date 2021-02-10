# Home

QuarticSDK is an external SDK provided by Quarticdotai to allow our clients to
use the clients outside the platform.
Some use cases for using the SDK are:
* Creating a seperate UI
* Using in jupyter shell while training models

## Requirements

QuarticSDK has been built on Python 3.5+
The package has the following mandatory requirements as of writing this documentation on 10 Feb 2021:

* [requests==2.25.1](https://pypi.org/project/requests/)
* [mkdocs==1.1.2](https://pypi.org/project/mkdocs/)
* [PyYAML==5.4.2](https://pypi.org/project/PyYAML/)
* [pandas==1.2.2](https://pypi.org/project/pandas/)

The remaining optional dependencies get downloaded automatically, after the above packages are installed

## Installation

Install using `pip`

```
pip install quartic-sdk
```
... or follow the following steps to install it from the repo:
```
git clone https://github.com/Quarticai/QuarticSDK/
python setup.py install
```

## Example

A small example on how to use the SDK for two different cases is as shown below:

#### Case 1: Getting the assets, tags, batches from the server

```

# Assuming that the quartic.ai server is at `https://test.quartic.ai/`, with the login
# username and password being `username` and `password`

from quartic_sdk import APIClient

client = APIClient("https://test.quartic.ai/", username="username", password="password")
user_assets = client.assets() # Get the list of all assets that the user has access to

asset = user_assets.get(name="Test Asset") # Get a specific asset with the name "Test Asset"
asset_tags = asset.get_tags() # Gets the list of all tags
asset_data = asset.data(start_time=1000000, stop_time=2000000) # Get the data of the asset for the given interval between start_time and stop_time. This returns an iterator, which can be iterated to get all the data points present

```

#### Case 2: Saving a model on the server

....

## QuickStart

Quickly move to our [Quick start guide](/quick_start) to get started

## Support

....

## License

....
