"""
We test the generic methods in the entities through Asset entity and Tag entity
"""
import pytest
import quartic_sdk.utilities.constants as Constants
from quartic_sdk.core.entity_helpers.entity_factory import EntityFactory
from quartic_sdk.utilities.test_helpers import ASSET_LIST_GET, TAG_LIST_GET, SINGLE_ASSET_GET, TAG_LIST_MULTI_GET


test_asset_entity = EntityFactory(
    Constants.ASSET_ENTITY, ASSET_LIST_GET[0], None)
test_tag_entity = EntityFactory(Constants.TAG_ENTITY, TAG_LIST_GET[0], None)
test_same_tag_entity = EntityFactory(
    Constants.TAG_ENTITY, TAG_LIST_MULTI_GET[0], None)
test_diff_tag_entity = EntityFactory(
    Constants.TAG_ENTITY, TAG_LIST_MULTI_GET[0], None)


def test_entity_equality():
    """
    We test that the equality works correctly for the entities
    """
    assert test_tag_entity == test_same_tag_entity
    with pytest.raises(AssertionError):
        assert test_asset_entity != test_tag_entity
    with pytest.raises(AssertionError):
        assert test_tag_entity != test_diff_tag_entity
