# Development Guide
This article explains and defines the various classes 

## APIClient
---
Class refers to the API client which is used as the interface between the user querying the Quartic AI Platform, and him using the SDK for his use cases

### Available methods

#### init
The class has the following parameters for initialization:

- **host (required)**: Refers to the host the user connects to for making API calls
- **username (not required)**: Required for Basic Authentication
- **password (not required)**: Required for Basic Authentication
- **oauth_token (not required)**: Required for OAuth2.0 Authentication
- **verify_ssl(not required)**: Required when the host needs to be verified for SSL

An example of usage is as follows:
```
client = APIClient(host="http://test.quartic.ai", username="username", password="password")
```

#### .version

The method returns the current version of the package
```
client.version() # Returns 0.0.0 based upon the time of writing the documentation
```

#### .assets
The method returns the list of all the assets that the authenticated user has access to. The list of assets are an object of type `EntityList`. More details on the class is provided below.
```
client_assets = client.assets()
```

#### .tags

The method requires the following parameters to be called:

**asset_id (required)**: The asset_id of the asset whose tags are to be returned
```
tags_of_asset_id_1 = client.tags(1)
```

#### .list_models
Lists the Models and its parameters
The method requires the following parameters to be called:
- **is_active (optional)**: Boolean variable indicating to list the models that are active or inactive currently in quartic platform. Default: None, Indicating to return both active and inactive models
- **ml_node (optional)**: Integer variable to list the models deployed to particular node. Default: None, returns all the accessible models for the user.

## Entity
---
Entity is the parent term through which all the objects accessible in the SDK are referred to. The available methods are as follows:

#### init
An object of this class is initialiazed with two parameters. These are automatically created and depends on the user querying through the client.

- **body_json(required)**: This is the json object which is used to create the related `Entity` object
- **api_helper(required)**: This is the APIHelper object which contains all the info about the authentication and is used for making API calls.

### get
The attribute value of the object is returned for the given name.
- **name(required)**: The attribute name whose value is to be returned

## Asset
---
This refers to the asset entity which contains the details of the asset. Asset contains all the properties of the base Entity defined above.

### .get_tags
The method returns all the tags present in the given asset in the form of `EntityList` where each object refers to `Tag`.

### .batches
The method returns all the batches present in the given asset in the form of `EntityList` where each object refers to `Batch`.

### .data
The method returns the tagdata iterator for all the tags present in the asset for the set `start_time` and `stop_time`, which can be used to iterate through the data in batches of 2L datapoints. More details under the `TagDataIterator` subsection.
The method params are:
- **start_time (required)**: (epoch) Refers to the `start_time` for fetching the data of the asset
- **stop_time (required)**: (epoch) Refers to the `stop_time` for fetching the data of the asset
- **granularity (not required)**: Refers to the granularity at which data is required. Depending upon the granularity provided. It automatically averages the granularity to either of RAW(granularity of tag edge connector), 5s, 30s, 60s, 300s, 1200s, 3600s, 10800s, 21600s, 43200s, 86400s. If no granularity is provided, it will take the default granularity as the raw granularity.

## Tag
---
This refers to the tag entity, which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

### .data
The method returns the tagdata iterator for the selected tag for the set `start_time` and `stop_time`, which can be used to iterate through the data in batches of 2L datapoints. More details under the `TagDataIterator` subsection. The method parameters are:
- **start_time(required)**: (epoch) Refers to the `start_time` for fetching the data of the asset
- **stop_time(required)**: (epoch) Refers to the `stop_time` for fetching the data of the asset
- **granularity(not required)**: Refers to the granularity at which data is required. Depending upon the granularity provided. It automatically averages the granularity to either of RAW(granularity of tag edge connector), 5s, 30s, 60s, 300s, 1200s, 3600s, 10800s, 21600s, 43200s, 86400s. If no granularity is provided, it will take the default granularity as the raw granularity.

## Batch
---
This refers to the batch entity, which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

## ContextFrame
---
This refers to the context frame entity, which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

### occurrences
The method returns all the occurrences of the given ContextFrame in the form of `EntityList` where each object refers to `ContextFrameOccurrence`

## ContextFrameOccurrence
---
This refers to the context frame occurrence entity, which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

## Model
---

This refers to Model entity, which contains the details of Model, Model contains all the properties of the base Entity defined above.

### .model_instance

Returns the Model object(created and deployed by extending model base- ModelABC).

## EntityList
---
The class contains the list of entities, where each entity can be of the type `Asset`, `Tag`, `ContextFrame`, `ContextFrameOccurrence` and `Batch`

### init
The class requires the following parameters for initialization:

- **class_type(required)**: Refers to the type of objects it will contain. These can be `Asset`, `Tag`, `ContextFrame`, `ContextFrameOccurrence` or `Batch`
- **entities_list(not required)**: Refers to the list of entities, which will be contained in the list. The types should match the `class_type` as provided. In case, this is not present, it will default to an empty list

### .get
The method returns the first item in the list whose attribute `name` has the value `value`. It requires the following params:
- **name(required)**: Refers to the name of the attribute
- **value(required)**: Refers to the value of this attribute

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
The method returns the first element of the EntityList
```
first_asset = client_assets.first()
```

### .last
The method returns the last element of the EntityList
```
last_asset = client_assets.last()
```

### .add
The method adds the given object into the list. If the object already exists or it is of a different class_type. It throws an exception
```
client_assets.add(new_asset_entity)
```
### .exclude
The method filters the given EntityList to return an updated list which doesn't contain the entity which has the `name` attribute value as `value`
```
updated_entity_list = client_assets.exclude("id", 1)
```

## TagDataIterator
---
Querying data for any set of tags in any given duration returns an instance of `TagDataIterator`, which can be used to iterate between the given time range. When the `.data` of tags/assets is called, the method divides the complete interval between `start_time` and `stop_time` into different time_ranges, with each range containing up to 200,000 data points for all the tags. The user can loop through this interval to get all the data points.