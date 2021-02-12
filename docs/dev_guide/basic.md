# Development Guide

We explain all the different classes defined in the document here

## APIClient

The class refers to the API Client which is used as the interface between the user querying
the Quartic.ai platform, and him using the SDK for his use cases

### Available methods

#### init

The class has the following parameters for initialization:

* **host(required)**: Refers to the host, to which the user will connect to, for making the API calls
* **username(not required)**: Is required when the user is looking for authenticating based upon BasicAuthentication
* **password(not required)**: Is required when the user is looking for authenticating based upon BasicAuthentication
* **oauth_token(not required)**: Is required when the user is looking to authenticate based upon OAuth2.0
* **verify_ssl(not required)**: When the host needs to be verified for SSL

An example of usage is as follows
```
client = APIClient(host="http://test.quartic.ai", username="username", password="password")
```

#### .version

The method returns the current version of the package
```
client.version() # Returns 0.0.0 based upon the time of writing the documentation
```

#### .assets

The method returns the list of all the assets that the given authenticated user has access to. The list of assets are an object of type `EntityList`. More details on the class is available below in the document.
```
client_assets = client.assets()
```

#### .tags

The method requires the following parameters to be called:

* **asset_id(required)**: The asset_id whose tags are to be returned
```
tags_of_asset_id_1 = client.tags(1)
```

****************

## Entity

Entity is the parent term, through which we refer to all the objects accessible in the SDK

#### init

We initialize an object of this class with the following two parameters. These are automatically created based upon the user querying through the client.

* **body_json(required)**: This is the json object which is used to create the related `Entity` object
* **api_helper(required)**: This is the APIHelper object which contains all the info about the authentication, and hence, used for making the API calls

#### get

We return the attribute value of the object for the given name:

* **name(required)**: The attribute name whose value is to be returned

****************

## Asset

This refers to the asset entity, which contains the details of the asset. Asset contains all the properties of the base Entity defined above.

### Class attributes

* **id**: Refers to the id of the asset entity
* **name**: Refers to the name of the asset entity
* **edge_connectors**: Refers to the list of edge connector ids
* **last_overhaul_date**: Refers to the last_overhaul_date
* **processunit_workcell**: Refers to the id of the process_unit or work_cell
* **site**: Refers to the id of the site, the asset belongs to

### Present methods

#### .get_tags

The method returns all the tags present in the given asset in the form of `EntityList` where each object refers to `Tag`

#### .batches

The method returns all the batches present in the given asset in the form of `EntityList` where each object refers to `Batch`

#### .data

The method returns the tagdata iterator for all the tags present in the asset for the set `start_time` and `stop_time`, which can be used to iterate through the data in batches of 2L datapoints. More details under the `TagDataIterator` subsection.
The method params are:

* **start_time(required)**: (epoch) Refers to the `start_time` for fetching the data of the asset
* **stop_time(required)**: (epoch) Refers to the `stop_time` for fetching the data of the asset
* **granularity(not required)**: Refers to the granularity at which data is required. Depending upon the granularity provided. It automatically averages the granularity to either of RAW(granularity of tag edge connector), 5s, 30s, 60s, 300s, 1200s, 3600s, 10800s, 21600s, 43200s, 86400s. If no granularity is provided, it will take the default granularity as the raw granularity

***************

## Tag

This refers to the tag entity, which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

### Class attributes

* **id**: The id of the Tag
* **name**: The name of the Tag
* **tag_type**: The type of the tag:- 1.Raw, 2.Soft, 3.Aggregation, 4.Bitwise, 5.Writeback
* **tag_data_type**: The tag data types:- 0.Double, 1.String, 2.Boolean, 3.Int, 4.Long, 5.Float
* **short_name**: The short name of the Tag
* **tag_value_type**: The tag value types:- 0.Discrete, 1.Telemetry
* **tag_process_type**: The tag process types:- 1.Process Variable, 2.Condition Variable, 3.Process Alarm, 4.Process Event, 5.Anomaly Score, 6.Predicted Variable, 7.Others, 8.Workflow, 9.Influencing Score
* **category**: Intelligence Categories:- 1.Energy, 2.Throughput, 3.Reliability, 4.Quality, 5.Safety, 6.Environment
* **uom**: The units of measurement
* **asset**: The asset id
* **created_by**: Name of the person who created this
* **value_table**: The dictionary which matches the tag streamed value to its name, and is present as json object

### Present Methods

#### .data

The method returns the tagdata iterator for the selected tag for the set `start_time` and `stop_time`, which can be used to iterate through the data in batches of 2L datapoints. More details under the `TagDataIterator` subsection.
The method params are:

* **start_time(required)**: (epoch) Refers to the `start_time` for fetching the data of the asset
* **stop_time(required)**: (epoch) Refers to the `stop_time` for fetching the data of the asset
* **granularity(not required)**: Refers to the granularity at which data is required. Depending upon the granularity provided. It automatically averages the granularity to either of RAW(granularity of tag edge connector), 5s, 30s, 60s, 300s, 1200s, 3600s, 10800s, 21600s, 43200s, 86400s. If no granularity is provided, it will take the default granularity as the raw granularity

***************

## Batch

This refers to the batch entity, which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

### Class attributes

* **id**: Id of the batch
* **batch_name**: The name of the batch. Most refers to the start timestamp of the batch
* **start**: Start time of the batch
* **stop**: Stop time of the batch
* **asset**: Asset ID to which this batch belongs to
* **is_questionable**: Whether the batch is questionable
* **notes**: List of notes, the user might have added to the batch

***************

## ContextFrame

This refers to the context frame entity, which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

### Class attributes

* **id**: Id of the ContextFrame
* **name**: Name of the context frame
* **description**: Description of the context frame
* **pu_or_wc**: The ID of the process unit or work cell this belongs to

#### occurrences

The method returns all the occurrences of the given ContextFrame in the form of `EntityList` where each object refers to `ContextFrameOccurrence`

**************

## ContextFrameOccurrence

This refers to the context frame occurrence entity, which contains the details of the tag. Tag contains all the properties of the base Entity defined above.

***************

## EntityList

The class contains the list of entities, where each entity can be of the type `Asset`, `Tag`, `ContextFrame`, `ContextFrameOccurrence` and `Batch`

#### init

The class requires the following parameters for initialization:

* **class_type(required)**: Refers to the type of objects it will contain. These can be `Asset`, `Tag`, `ContextFrame`, `ContextFrameOccurrence` or `Batch`
* **entities_list(not required)**: Refers to the list of entities, which will be contained in the list. The types should match the `class_type` as provided. In case, this is not present, it will default to an empty list

#### .get

The method returns the first item in the list whose attribute `name` has the value `value`. It requires the following params:

* **name(required)**: Refers to the name of the attribute
* **value(required)**: Refers to the value of this attribute

The usage is as below:
```
asset_with_id_1 = client_assets.get("id", 1)
```

#### .all

The method returns all the entities present in the list.
```
all_assets = client_assets.all()
```

#### .first

The method returns the first element of the EntityList
```
first_asset = client_assets.first()
```

#### .last

The method returns the last element of the EntityList
```
last_asset = client_assets.last()
```

#### .add

The method adds the given object into the list. If the object already exists or it is of a different class_type. It throws an exception
```
client_assets.add(new_asset_entity)
```

#### .exclude

The method filters the given EntityList to return an updated list which doesn't contain the entity which has the `name` attribute value as `value`
```
updated_entity_list = client_assets.exclude("id", 1)
```

****************

## TagDataIterator

When the user queries for data for any set of tags in any given duration, we return an instance of `TagDataIterator`, which the user can use to iterate between the given time range. When the user calls the `.data` method of tags/assets, it divides the complete interval between `start_time` and `stop_time` into different time_ranges
such that each time range contains upto 2L data points for all the tags. The user can loop through this interval to get all the data points.

****************
