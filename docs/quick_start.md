# Quick start

We are going to fetch data points for a few tags, train a model, and save it on the Quartic.ai platform

## Step 1

We start by initializing the `APIClient` with the authentication details. As of now, QuarticSDK supports
two kinds of authentication. These are BasicAuthentication, where the user is supposed to pass the username
and password; and OAuth2.0, where the user passes the client token.
For this example, we will be using BasicAuthentication. Also, we will assume our quartic.ai host
to be `https://test.quartic.ai`, with the username and password being `username` and `password`

```
from quartic_sdk import APIClient

client = APIClient("https://test.quartic.ai", username="username", password="password")
```

## Step 2

Fetching the primitive objects. These are the objects that don't require any extra parameters and
can be directly fetched from the `client` object. The returned list is of an object of the class
`EntityList`, which in turn contains all the required methods for getting instances based upon
the given parameters

```
assets = client.assets()
context_frames = client.context_frame_definitions()
```

## Step 3

Fetch the tags for one of the assets, to be further used to fetch data points. We are supposed to pass
the start_time and the stop_time of the query in epoch. In this case, we consider the duration of 1 day
from 1 Jan 2021 to 2 Jan 2021. The corresponding time in epoch format is 1609439400000 and 1609525800000
```
asset = assets.first()
asset_tags = asset.get_tags()

asset_data = asset.data(start_time=1609439400000, stop_time=1609525800000)
```

## Step 4

Save the data for the tags in the data frame
```
import pandas as pd
combined_data_frame = pd.DataFrame(columns=[tag.id for tag in asset_tags])
for data in asset_data:
    combined_data_frame = combined_data_frame.append(data)
```

## Step 5

We can go ahead and do the required model building here, and deploy the model then
...
