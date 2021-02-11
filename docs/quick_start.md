# Quick start
To fetch data points of one or more tags, train a model, and save it on the Quartic AI Platform, follow the steps below:

## Step 1
---
Start by initializing the `APIClient` with the authentication details. Currently, Quartic SDK supports two kinds of authentication. These are BasicAuthentication, where the user is supposed to pass the username
and password; and OAuth2.0, where the user passes the client token.
For this example, we will be using BasicAuthentication. Also, we will assume the Quartic host to be `https://test.quartic.ai`, and the username and password being `username` and `password`.

```
from quartic_sdk import APIClient

client = APIClient("https://test.quartic.ai", username="username", password="password")
```

## Step 2
---
Fetch primitive objects. These objects don't require extra parameters and can be fetched directly from the `client` object. The list returned will contain the class object `EntityList`, which consists of the methods required for getting instances based upon the given parameters.

```
assets = client.assets()
context_frames = client.context_frame_definitions()
```

## Step 3
---
Fetch a tag of an assets, which will be further used to fetch data points. Pass the start_time and the stop_time of the query in epoch. For example, for a duration of 1 day, from 1 Jan 2021 to 2 Jan 2021, the corresponding time in epoch would be 1609439400000 and 1609525800000
```
asset = assets.first()
asset_tags = asset.get_tags()

asset_data = asset.data(start_time=1609439400000, stop_time=1609525800000)
```

## Step 4
---
Save the tag data in the data frame.
```
import pandas as pd
combined_data_frame = pd.DataFrame(columns=[tag.id for tag in asset_tags])
for data in asset_data:
    combined_data_frame = combined_data_frame.append(data)
```

## Step 5
Proceed to build and deploy the model.