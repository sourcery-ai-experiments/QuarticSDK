import base64

from cloudpickle import cloudpickle
from quartic_sdk.model.helpers import ModelUtils

from quartic_sdk.core.entities.base import Base
import quartic_sdk.utilities.constants as Constants
from quartic_sdk.core.iterators.tag_data_iterator import TagDataIterator


class Model(Base):
    """
    The given class refers to the tag entity which is created based upon the
    Model object returned from the API
    """

    def __repr__(self):
        """
        Override the method to return the asset name with id
        """
        return f"<{Constants.MODEL_ENTITY}: {self.model_name}_{self.model_id}>"

    def model_instance(self):
        response = self.api_helper.call_api(Constants.GET_MODEL_ENDPOINT, method_type='GET',
                                            path_params=[self.model_id],
                                            query_params={},
                                            body={})
        response.raise_for_status()
        data = response.json()
        model_string = response.json()['model']
        checksum_received = model_string[:32]
        decoded_model = base64.b64decode(model_string[32:])
        assert ModelUtils.get_checksum(model_string[32:].encode()) == checksum_received
        model = cloudpickle.loads(decoded_model)
        return model
