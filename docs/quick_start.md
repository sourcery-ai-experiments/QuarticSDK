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
feature_tags = [tag.id for for tag in asset_tags[:5]]
target_tag = asset_tags.last().id
asset_data = asset.data(start_time=1609439400000, stop_time=1609525800000)
```

## Step 4
---
Save the tag data in the data frame.
```
import pandas as pd
combined_data_frame = pd.DataFrame(columns=[tag.id for tag in feature_tags])
for data in asset_data:
    combined_data_frame = combined_data_frame.append(data)
```

## Step 5
---
Once the client is initialized and data is fetched using the steps above, model can now be trained, tested and deployed to Quartic Platform using below:

``` python
from quartic_sdk.model import ModelABC
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


class ExampleModel(ModelABC):
    def __init__(self, model):
        self.model = model
        super().__init__("My Sample Model", description='This is a simple model to give a quick start for user')
        
    def predict(self, input_df):
        return self.model.predict(input_df)

model = linear_model.LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(combined_data_frame[feature_tags], 
                df[[feature_tags[-1]]].values.ravel(), random_state=42)
                
model.fit(X_train, y_train)
model.predict(X_test)
example_model = ExampleModel(model)
example_model.predict(X_test)
 
example_model.save(client, output_tag_name='Prediction Tag Name',
                   feature_tags=feature_tags, target_tag=target_tag,
                   test_df=X_test)
```