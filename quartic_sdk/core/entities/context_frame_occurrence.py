
"""
The given file contains the class to refer to the Context Frame Occurrence entity
"""
import random
import quartic_sdk.utilities.constants as Constants
from quartic_sdk.core.entities.base import Base


class ContextFrameOccurrence(Base):
    """
    The given class refers to the context frame occurrence entity which is created
    based upon the context frame occurrence object returned from the API
    """

    def __init__(self, body_json, api_helper):
        """
        Since, occurrences don't have any id, we provide it a random integer as id
        """
        super().__init__(body_json, api_helper)
        self.id = random.randint(1, 100000000)

    def __repr__(self):
        """
        Override the method to return the asset name with id
        """
        return f"<{Constants.CONTEXT_FRAME_OCCURRENCE_ENTITY}: {self.id}>"
