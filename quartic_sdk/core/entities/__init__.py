
from quartic_sdk.core.entities.asset import Asset
from quartic_sdk.core.entities.batch import Batch
from quartic_sdk.core.entities.context_frame import ContextFrame
from quartic_sdk.core.entities.context_frame_occurrence import ContextFrameOccurrence
from quartic_sdk.core.entities.tag import Tag
from quartic_sdk.utilities.constants import * as Constants


ENTITY_DICTIONARY = {
    Constants.ASSET_ENTITY: Asset,
    Constants.TAG_ENTITY: Tag,
    Constants.CONTEXT_FRAME_ENTITY: ContextFrame,
    Constants.CONTEXT_FRAME_OCCURRENCE_ENTITY: ContextFrameOccurrence,
    Constants.BATCH_ENTITY: Batch
}
