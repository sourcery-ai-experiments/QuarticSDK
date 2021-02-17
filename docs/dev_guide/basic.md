# Development Guide
This article explains the various classes alongwith their methods and the available attributes.

## APIClient
---
Class refers to the API client which is used as the interface between the user querying the Quartic AI Platform and the use case.

The available methods are as follows:

### init
This class has the following parameters for initialization:

- **host (mandatory)**: Refers to the host the user connects to for making API calls.
- **username (optional)**: Required for Basic Authentication.
- **password (optional)**: Required for Basic Authentication.
- **oauth_token (optional)**: Required for OAuth2.0 Authentication.
- **verify_ssl (optional)**: Required when the host needs to be verified for SSL.

An example of usage is as follows:
```
client = APIClient(host="http://test.quartic.ai", username="username", password="password")
```

### .version
This method returns the current version of the package.
```
client.version() # Returns 0.0.0 as of the time of writing this document
```

### .assets
This method returns the list of assets that the authenticated user has access to. The list of assets are an object of type `EntityList`. More details on the class is provided below.
```
client_assets = client.assets()
```

### .tags
This method requires the following parameters to be called:

**asset_id (mandatory)**: The asset_id of the asset whose tags are to be returned.
```
tags_of_asset_id_1 = client.tags(1)
```

### .list_models
This method lists the ML models and its parameters and requires the following parameters to be called:
- **is_active (optional)**: This specifies if is_active is true, list_models will list the models which are active in the Quartic AI Platform.
- **ml_node (optional)**: If ml_node (numeric field) is specified, list_models will list all the custom models that are deployed into a specific ml node.

## Entity
---
Entity is the parent term by which all the objects accessible in the SDK are referred to. The available methods are as follows:

#### init
An object of this class is initialiazed with two parameters. These are automatically created and depend on the user's query through the client.

- **body_json (mandatory)**: This is the json object which is used to create the related `Entity` object.
- **api_helper (mandatory)**: This is the APIHelper object which contains all the info about the authentication and is used for making API calls.

### get
The attribute value of the object is returned for the given name.
- **name (mandatory)**: The attribute name whose value is to be returned.

## Asset
---
This refers to the asset entity which contains the details of the asset. Asset contains all the properties of the base entity defined above.

### .get_tags
The method returns all the tags present in the given asset in the form of `EntityList` where each object refers to `Tag`.

### .batches
The method returns all the batches present in the given asset in the form of `EntityList` where each object refers to `Batch`.

### .data
The method returns the tag data iterator for all the tags present in the asset for the set `start_time` and `stop_time`. It can be used to iterate through the data in batches of 200,000 datapoints. More details under the `TagDataIterator` subsection.
The method parameters are:

- **start_time (mandatory)**: (epoch) Refers to the `start_time` for fetching the data of the asset.
- **stop_time (mandatory)**: (epoch) Refers to the `stop_time` for fetching the data of the asset.
- **granularity (optional)**: Refers to the granularity at which data is required. Depending upon the granularity provided. It automatically averages the granularity to either of RAW (granularity of tag edge connector), 5s, 30s, 60s, 300s, 1200s, 3600s, 10800s, 21600s, 43200s or 86400s. If no granularity is provided, it will take the default granularity as the raw granularity.
- **return_type (optional)**: The user can pass either `pd`, which will return the pandas dataframe iterator, or `json` which will return json object on return. This value takes the `pd` value as default.
- **transformations (optional)**: The user is supposed to pass the list of interpolations and aggregations here. Further details on transformations is provided towards the end of this documentation.

## Tag
---
This refers to the tag entity which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

### .data
The method returns the tagdata iterator for the selected tag for the set `start_time` and `stop_time`, which can be used to iterate through the data in batches of 200,000 datapoints. More details under the `TagDataIterator` subsection. The method parameters are:
- **start_time (mandatory)**: (epoch) Refers to the `start_time` for fetching the data of the asset.
- **stop_time (mandatory)**: (epoch) Refers to the `stop_time` for fetching the data of the asset.
- **granularity (optional)**: Refers to the granularity at which data is required. Depending upon the granularity provided. It automatically averages the granularity to either of RAW (granularity of tag edge connector), 5s, 30s, 60s, 300s, 1200s, 3600s, 10800s, 21600s, 43200s, 86400s. If no granularity is provided, it will take the default granularity as the raw granularity.
- **return_type (optional)**: The user can pass either `pd`, which will return the pandas dataframe iterator, or `json` which will return json object on return. This value takes the `pd` value as default.
- **transformations (optional)**: The user is supposed to pass the list of interpolations and aggregations here. Further details on transformations is provided towards the end of this documentation.

## Batch
---
This refers to the batch entity which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

## ContextFrame
---
This refers to the context frame entity which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

### occurrences
The method returns all the occurrences of the given ContextFrame in the form of `EntityList` where each object refers to `ContextFrameOccurrence`.

## ContextFrameOccurrence
---
This refers to the context frame occurrence entity which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

## Model
---
This refers to Model entity, which contains the details of Model, Model contains all the properties of the base Entity defined above.

### .model_instance
This methode returns the Model object (created and deployed by extending model base- ModelABC).

## EntityList
---
This class contains the list of entities, where each entity can be of the type `Asset`, `Tag`, `ContextFrame`,`ContextFrameOccurrence`, and `Batch`.

### init
The class requires the following parameters for initialization:

- **class_type (mandatory)**: Refers to the type of objects it will contain. These can be `Asset`, `Tag`, `ContextFrame`, `ContextFrameOccurrence`, or `Batch`.
- **entities_list (optional)**: Refers to the list of entities, which will be contained in the list. The types should match the `class_type` as provided. In case this is not present, it will default to an empty list.

### .get
The method returns the first item in the list whose attribute `name` has the value `value`. It requires the following parameters:
- **name (mandatory)**: Refers to the name of the attribute.
- **value (mandatory)**: Refers to the value of this attribute.

The usage is as below:
```
asset_with_id_1 = client_assets.get("id", 1)
```

### .all
The method returns all the entities present in the list.
```
all_assets = client_assets.all()
```

### .first
This method returns the first element of the Integer variable to list the ML models deployed to a particular node. The default value is *None*, which returns all the accessible ML models for the user.
```
first_asset = client_assets.first()
```

### .last
This method returns the last element of the EntityList.
```
last_asset = client_assets.last()
```

### .add
This method adds the given object into the list. If the object already exists or it belongs to a different class_type, it throws an exception.
```
client_assets.add(new_asset_entity)
```
### .exclude
This method filters the given EntityList to return an updated list that doesn't contain the entity which has the `name` attribute value as `value`.
```
updated_entity_list = client_assets.exclude("id", 1)
```

### .data
This method is present only for the `Tag` type EntityList, and it returns the data present in the given tags. It returns a TagDataIterator instance, and has the following parameters:

- **start_time (mandatory)**: (epoch) Refers to the `start_time` for fetching the data of the asset.
- **stop_time (mandatory)**: (epoch) Refers to the `stop_time` for fetching the data of the asset.
- **granularity (optional)**: Refers to the granularity at which data is required. Depending upon the granularity provided. It automatically averages the granularity to either of RAW (granularity of tag edge connector), 5s, 30s, 60s, 300s, 1200s, 3600s, 10800s, 21600s, 43200s or 86400s. If no granularity is provided, it will take the default granularity as the raw granularity.
- **return_type (optional)**: The user can pass either `pd`, which will return the pandas dataframe iterator, or `json` which will return json object on return. This value takes the `pd` value as default.
- **transformations (optional)**: The user is supposed to pass the list of interpolations and aggregations here. Further details on transformations is provided towards the end of this documentation.

## TagDataIterator
---
Querying data for any set of tags in any given duration returns an instance of `TagDataIterator`, which can be used to iterate between the given time range. When the `.data` of tags/assets is called, the method divides the complete interval between `start_time` and `stop_time` into different time_ranges, with each range containing up to 200,000 data points for all the tags. The user can loop through this interval to get all the data points.

### Transformations:
The tag data iterator is created based upon the multiple transformations that the user might need. The transformations is a list of dictionaries where each dictionary contains the details of interpolation/aggregation to be performed on the data. The different transformations are:

#### Interpolation:

Interpolation contains the following keys to be present:
- **transformation_type (mandatory)**: Refers to the type of transformation. It should always be `interpolation` for this.
- **column (mandatory)**: Refers to the column which is to be interpolated.
- **method (mandatory)**: Refers to the interpolation method; the options are: linear, spline, cubic interpolation, and polynomial.
- **order (mandatory)**: Refers to the order of the interpolation, and is required for all methods except `linear`.
- **limit_direction (optional)**: Refers to the direction in which the interpolation takes place. The default value is `forward`.

#### Aggregation:
Aggregation requires the following keys to be present:
- **transformation_type (mandatory)**: Refers to the type of transformation. It should always be `aggregation` for this.
- **aggregation_column (mandatory)**: Refers to the column being aggregated.
- **aggregation_dict (mandatory)**: This dictionary refers to the methods based upon which the different columns in the dataset will be aggregated.
