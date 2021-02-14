# Model Creation
This article gives an introduction on how to create, wrap and deploy models into Quartic Platform. 

## ModelABC
ModelABC is a base class for all the user models that can be deployed to QuarticPlatform. 
User needs to extend this class and implement predict method to make the model compatible to deploy in quartic platform.

### Available methods

#### init
The method has following parameters for initialization:
- **name (required)**: A Unique Name for the model
- **description (optional)**: A sentence to describe the Model. Default = `''`
- **log_level (optional)**: str - sets log level for the model. one of `'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'`. Default: `INFO`

_Note: While implementing an instance of ModelABC, user needs to call `super().__init__` with above parameters._

#### .save
This is a private method used to save the model to QuarticPlatform.

**Do not Override this method**
- **client (required)**:    Refers to an instance of APIClient 
- **output_tag_name (required)**: A Unique name for the Prediction results
- **feature_tags (required)**:  A list of tags that are used as features in the model
- **target_tag (required)**:   A Tag with both asset and edge connector assigned which can be used as a parent for the current prediction output
- **test_df (required)**:   Test Dataframe to validate model prediction results
- **ml_node (optional)**:   Ml Node Id if User wants to deploy model to particular node. 

_**Note**_:
1. _By Default Quartic selects the best Ml Node based on cpu and memory utilization at that point to deploy the model if ml_node is not provided(**Recommended**)_
2. _save method takes a sample of test data frame to validate the model.__


#### .predict
The method has following parameters for running the predictions for user model:
- **input_df (required)** - Input Dataframe to prefrom prediction on.

_**Note**_: 
1. _User needs to override this method to transform and run predictions for the model created_
2. _input_df is expected to have tag ids as the column names. If model is trained with tag names instead, a transformation step needs to be added and used in predict method to convert the tag ids in input dataframe into tag names._

#### Example
```python
import pandas as pd
from quartic_sdk.model import ModelABC
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class ExampleModel(ModelABC):
    def __init__(self):
        self.model = RandomForestRegressor()
        super().__init__("My Sample Model", description='This is a simple model to give a quick introduction on creating and deploying models to quartic platform.')
        
    def train(self, X, y):
        self.model.fit(X, y)
        
    def predict(self, input_df):
        predictions = self.model.predict(input_df)
        return pd.Series(predictions)
        
quartic_model = ExampleModel()
quartic_model.train(X_train, y_train) # Training data extracted from data loaded from Quartic Platform
quartic_model.save(client=api_client, output_tag_name="Prediction Result",
                   feature_tags=[1,2,3], # tags that are used in X variable say 1,2,3
                   target_tag = 3, # tag that specifies a relation for prediction say 3
                   test_df = X_train
                   )


```
**Notes**:
- Any intermediate steps that are used model training outside wrapper, must be included in wrapper for applying similar set of transformations during prediction.
