# Home

Quartic SDK is an external SDK provided by Quartic.ai to allow users to use assets, tags, etc. outside the Quartic AI Platform.
It lets third party developers, who have authorization to access Quartic.ai entities, build custom applications using the SDK.

## Installation
---

Install using `pip`

```
pip install quartic-sdk
```
...or follow the following steps to install it from the source:
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
