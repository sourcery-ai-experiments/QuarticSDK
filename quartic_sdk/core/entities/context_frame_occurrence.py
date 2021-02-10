
from quartic_sdk.utilities.constants import Constants
from quartic_sdk.core.entities.base import Base


class ContextFrameOccurrence(Base):
    """
    The given class refers to the context frame occurrence entity which is created
    based upon the context frame occurrence object returned from the API
    """
    def __str__(self):
        """
        Override the method to return the asset name with id
        """
        return f"{Constants.CONTEXT_FRAME_OCCURRENCE_ENTITY}: {self.id}"
