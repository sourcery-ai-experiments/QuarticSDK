# Home

Quartic SDK is an external SDK provided by Quartic.ai to allow users to use assets, tags, etc. outside the Quartic AI Platform. Here are some use cases for Quartic SDK:

- Creating a seperate UI
- Using in Jupyter Shell while training models

## Requirements
---
Quartic SDK is built on Python 3.5+. Currently, the package has the following requirements:

- [requests==2.25.1](https://pypi.org/project/requests/)
- [mkdocs==1.1.2](https://pypi.org/project/mkdocs/)
- [PyYAML==5.4.2](https://pypi.org/project/PyYAML/)
- [pandas==1.2.2](https://pypi.org/project/pandas/)

Other dependencies are downloaded automatically, after the requirements are installed.

## Installation
---

Install using `pip`

```
pip install quartic-sdk
```
...or follow the following steps to install it from the repo:
```
git clone https://github.com/Quarticai/QuarticSDK/
python setup.py install
```

## Examples
---
Here are a couple of examples on how the SDK can be used:

#### Case 1: Getting the assets, tags, batches from the server


```
# Assuming that the Quartic.ai server is at `https://test.quartic.ai/`, with the login
# and the username and password is `username` and `password.`

from quartic_sdk import APIClient

client = APIClient("https://test.quartic.ai/", username="username", password="password")
user_assets = client.assets() # Get the list of all assets that the user has access to

asset = user_assets.get(name="Test Asset") # Get a specific asset with the name "Test Asset"
asset_tags = asset.get_tags() # Gets the list of all tags
asset_data = asset.data(start_time=1000000, stop_time=2000000) # Get the data of the asset for the given interval between start_time and stop_time. This returns an iterator, which can be iterated to get all the data points present.
```

#### Case 2: Saving a model on the server

....

## QuickStart

Quickly move to our [Quick start guide](/quick_start) to get started

## Support

....

## License

....
