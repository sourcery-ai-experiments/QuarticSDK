
import pandas as pd
from unittest import mock
from aloe import step, world

from quartic_sdk import APIClient
from quartic_sdk.core.entities import Tag, Asset
from quartic_sdk.core.entity_helpers.entity_list import EntityList
from quartic_sdk.core.iterators.tag_data_iterator import TagDataIterator
from quartic_sdk.utilities.test_helpers import (
    APIHelperCallAPI,
    ASSET_LIST_GET,
    TAG_LIST_GET,
    ASSET_DATA_POST
    )
import quartic_sdk.utilities.constants as Constants


@step("we have successfully set up client to test asset data flow")
def step_impl(context):
    """
    For the first step we setup the APIClient
    """
    world.client = APIClient("test_host", username="username", password="password")


@step("we call the required methods to get the asset details")
def step_impl(context):
    """
    Now we call the different internal methods and save their values
    internally in the world parameter
    """

    with mock.patch('requests.get') as requests_get:
        requests_get.return_value = APIHelperCallAPI(ASSET_LIST_GET)

        world.client_assets = world.client.assets()

    world.first_asset = world.client_assets.first()

    with mock.patch('requests.post') as requests_post:
        requests_post.return_value = APIHelperCallAPI(ASSET_DATA_POST)

        # return type default is pandas dataframe
        world.first_asset_data_pd = world.first_asset.data(start_time=1, stop_time=2)

        world.first_asset_data_json = world.first_asset.data(
            start_time=1, stop_time=2, return_type=Constants.RETURN_JSON)

    test_transformation1 = [{
        "transformation_type": "interpolation",
        "column": "1",
        "method": "linear"
    }]

    with mock.patch('requests.post') as requests_post:
        requests_post.return_value = APIHelperCallAPI(ASSET_DATA_POST)

        # return type default is pandas dataframe
        world.first_asset_data_with_correct_transformation_pd = world.first_asset.data(start_time=1, stop_time=2,
                transformations=test_transformation1)

        world.first_asset_data_with_correct_transformation_pd = world.first_asset.data(start_time=1,
            stop_time=2, transformations=test_transformation1, return_type=Constants.RETURN_JSON)

    test_transformation2 = [{
        "transformation_type": "interpolation",
        "method": "linear"
    }]

    test_transformation3 = [{
        "transformation_type": "interpolation",
        "column": "1",
        "method": "linear"
    }, {
        "transformation_type": "aggregation",
        "aggregation_column": "1"
    }]

    with pytest.raises(Exception):
        world.tag_data_with_incorrect_transformation = world.first_asset.data(start_time=1, stop_time=2,
            transformations=test_transformation2)

    with pytest.raises(Exception):
        world.tag_data_with_incorrect_transformation = world.first_asset.data(
            start_time=1, stop_time=2, transformations=test_transformation3)

@step("the return of tag data works correctly for json and pandas df")
def step_impl(context):
    """
    In this step we assert to ensure that the methods call the correct functions
    to ensure the correct variable types and the respective data created
    """
    assert isinstance(world.client_assets, EntityList)
    assert world.client_assets.first().id == 1

    assert isinstance(world.first_asset, Asset)
    assert world.first_asset.id == 1

    assert isinstance(world.first_asset_data_pd, TagDataIterator)

    with mock.patch('requests.post') as requests_post:
        requests_post.return_value = APIHelperCallAPI(ASSET_DATA_POST)
        assert isinstance(world.first_asset_data_pd[0], pd.DataFrame)

    with mock.patch('requests.post') as requests_post:
        requests_post.return_value = APIHelperCallAPI(ASSET_DATA_POST)
        assert isinstance(world.first_asset_data_json[0], dict)

    assert isinstance(world.first_asset_data_with_correct_transformation_pd, TagDataIterator)

    with mock.patch('requests.post') as requests_post:
        requests_post.return_value = APIHelperCallAPI(ASSET_DATA_POST)
        assert isinstance(world.first_asset_data_with_correct_transformation_pd[0], pd.DataFrame)

    assert isinstance(world.first_asset_data_with_correct_transformation_json, TagDataIterator)

    with mock.patch('requests.post') as requests_post:
        requests_post.return_value = APIHelperCallAPI(ASSET_DATA_POST)
        assert isinstance(world.first_asset_data_with_correct_transformation_json[0], dict)
