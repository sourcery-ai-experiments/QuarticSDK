
# Authentication types
OAUTH = 1
BASIC = 2

# API method types
METHOD_TYPES = ["GET", "POST", "PUT", "PATCH", "DELETE"]
API_GET = "GET"
API_POST = "POST"
API_PATCH = "PATCH"
API_PUT = "PUT"
API_DELETE = "DELETE"

# API calls
GET_ASSETS = "/asset/"
GET_CONTEXT_FRAME_DEFINITIONS = "/api/v1/context_frame_definitions/"
GET_TAGS = "/tags/"
POST_TAG_DATA = "/tag_data/"
GET_CONTEXT_FRAME_OCCURRENCES = "/api/v1/context_frame_occurrences/"
GET_BATCHES = "/api/v1/batches/"

# Entity types
ASSET_ENTITY = "Asset"
BATCH_ENTITY = "Batch"
CONTEXT_FRAME_ENTITY = "ContextFrame"
CONTEXT_FRAME_OCCURRENCE_ENTITY = "ContextFrameOccurrence"
TAG_ENTITY = "Tag"

# Data return type constants
RETURN_JSON = "json"
RETURN_PANDAS = "pd"

AVAILABLE_GRANULARITIES = [0,5,30,60,300,1200,3600,10800,21600,43200,86400]
