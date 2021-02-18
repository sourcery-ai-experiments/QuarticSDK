# Authentication types
OAUTH = 1
BASIC = 2

# MODEL Constants
NUM_ROW_PER_PREDICTION = 100
MAX_PREDICTION_PROCESSING_TIME = 10  # In seconds
MAX_MODEL_SIZE = 100 * 1024 * 1024  # 100 MB
MODEL="model"
MODEL_NAME="model_name"
OUTPUT_TAG_NAME="output_tag_name"
FEATURE_TAGS="feature_tags"
TARGET_TAG_ID="target_tag_id"
TEST_DATA="test_data"
ML_NODE_ID="ml_node_id"

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
CMD_MODEL_ENDPOINT = '/cmd/model/'

# Entity types
ASSET_ENTITY = "Asset"
BATCH_ENTITY = "Batch"
CONTEXT_FRAME_ENTITY = "ContextFrame"
CONTEXT_FRAME_OCCURRENCE_ENTITY = "ContextFrameOccurrence"
TAG_ENTITY = "Tag"
MODEL_ENTITY = "Model"

# Data return type constants
RETURN_JSON = "json"
RETURN_PANDAS = "pd"
