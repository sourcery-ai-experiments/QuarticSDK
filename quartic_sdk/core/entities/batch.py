
from quartic_sdk.core.entities.base_entity import Base
from quartic_sdk.utilities.constants import * as Constants


class Batch(Base):
    """
    The given class refers to the batch entity which is created based upon the batch
    object returned from the API
    """

    def __str__(self):
        """
        Override the method to return the asset name with id
        """
        return f"{Constants.BATCH_ENTITY}: {self.name}_{self.id}"
