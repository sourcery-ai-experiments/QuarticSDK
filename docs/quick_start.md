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
---
Once the client is initialized and data is fetched using the steps above, model can now be trained, tested and deployed to Quartic Platform using below steps.

Model can be created in multiple ways:
##### Creating The Model and training the model within the Wrapper 

```python
import pandas as pd
from quartic_sdk.model import ModelABC
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class ExampleModel(ModelABC):
    def __init__(self):
        self.model = RandomForestRegressor()
        super().__init__("My Sample Model", description='This is a simple model where model within the Quartic Wrapper') 
                         
    def train(self, X, y):
        self.model.fit(X, y)
    
    def predict(self, input_df: pd.DataFrame) -> pd.Series:
        return self.model.predict(input_df)


feature_tags = [1, 3, 5, 7] # selected Feature tags are 1,3,5,7
target_tag = 8  # Target of the current model is the tag 8
df = combined_data_frame[feature_tags]
X_train, X_test, y_train, y_test = train_test_split(df.drop(["price"], axis=1), df[["price"]].values.ravel(), random_state=42)

example_model = ExampleModel()
example_model.train(X_train, y_train)
example_model.predict(X_test)
example_model.save(client, output_tag_name='Prediction Tag Name',
                    feature_tags=feature_tags, target_tag=target_tag,
                    test_df=X_test)
```


##### Create and train the model and Wrap the train model into Quartic Base

```python
import pandas as pd
from quartic_sdk.model import ModelABC
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# Suppose we are training a  LinearRegression model
model = linear_model.LinearRegression() 
feature_tags = [1, 3, 5, 7] # selected Feature tags are 1,3,5,7
target_tag = 8  # Target of the current model is the tag 8
df = combined_data_frame[feature_tags]
X_train, X_test, y_train, y_test = train_test_split(df.drop(["price"], axis=1), df[["price"]].values.ravel(), random_state=42)
model.fit(X_train, y_train)
model.predict(X_test)

class ExampleModel(ModelABC):
    def __init__(self, model):
        self.model = model
        super().__init__("My Sample Model", description='This is a simple model where model is created,' +
                                                        'trained already and Simply wrapped into Quartic Base')
        
    def predict(self, input_df):
        return self.model.predict(input_df)


example_model = ExampleModel(model)
example_model.predict(X_test)
example_model.save(client, output_tag_name='Prediction Tag Name',
                   feature_tags=feature_tags, target_tag=target_tag,
                   test_df=X_test)
    


```

##### Adding custom pre and/or transformations

```python
from quartic_sdk.model import ModelABC
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class ExampleModel(ModelABC):
    def __init__(self):
        self.model = RandomForestRegressor()
        super().__init__("My Sample Model", description='This is a simple model where model within the Quartic Wrapper')

    def train(self, X, y):
        X_transformed = self.pre_transform(X)
        self.model.fit(X_transformed, y)
        
    def pre_transform(self, df):
        df['new_column'] = df['1'] * df['2']
        return df
        
    def predict(self, input_df: pd.DataFrame) -> pd.Series:
        transformed_df = self.pre_transform(input_df)
        return self.model.predict(transformed_df)

example_model = ExampleModel()
X_train, X_test, y_train, y_test = train_test_split(df.drop(["price"], axis=1), df[["price"]].values.ravel(), random_state=42)

example_model = ExampleModel()
example_model.train(X_train, y_train)
example_model.predict(X_test)


```

##### Adding Logs to the Model
```python
class ExampleModel(ModelABC):
    def __init__(self, model, log_level='INFO'):
        self.model = model
        super().__init__("My Sample Model", description='This is a Model logging example', log_level)
        self.log.info("Model is Initialized")
    
    def pre_transform(self, df, column_1, column_2):
        self.log.info("Transforming the Dataframe")
        self.log.debug("Transforming the Dataframe by simple multiplication")
        df['new_column'] = df[column_1] * df[column_2]
        return df    
    def train(self, X,y):
        self.log.info("Started Training steps")
        X = self.pre_transform(X, '1', '2')
        self.model.fit(X, y)
    
    def predict(self, input_df):
        self.log.info("Starting the Prediction step")
        transformed_df = self.pre_transform(input_df, '1', '2')
        return self.model.predict(transformed_df)
```


##### Deploying model -- Once trained and tested, model can be deployed using below:
```python

example_model.save(client, output_tag_name='Prediction Tag Name',
                   feature_tags=feature_tags, target_tag=target_tag,
                   test_df=X_test)
```
**Notes**: 
- save method takes a sample of test data frame to validate the model.
- This test dataframe is expected to have tag ids as the column names. If model is trained with tag names instead, a transformation step needs to be added and used in predict method to convert the tag ids in input dataframe into tag names.
- Any intermediate steps that are used model training outside wrapper, must be included in wrapper for applying similar set of transformations during prediction.  
