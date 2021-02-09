
asset_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "last_overhaul_date": {
            "type": "string"
        },
        "edge_connectors": {
            "type": "array",
            "items": {"type": "integer"}
        }
    },
    "required": {"id", "name", "last_overhaul_date", "edge_connectors"}
}

tag_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "tag_type": {
            "type": "integer",
            "minimum": 1,
            "exclusiveMaximum": 6
        },
        "tag_data_type": {
            "type": "integer",
            "minimum": 0,
            "exclusiveMaximum": 6
        },
        "short_name": {"type": "string"},
        "tag_value_type": {
            "type": "integer",
            "minimum": 0,
            "exclusiveMaximum": 2
        },
        "edge_connector": {"type": "integer"},
        "tag_process_type": {
            "type": "integer",
            "minimum": 1,
            "exclusiveMaximum": 10
        },
        "asset": {"type": "string"}
    },
    "required": {"id", "name", "short_name", "tag_type", "tag_data_type", "edge_connector", "asset"}
}

batch_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "batch_name": {"type": "integer"},
        "start": {"type": "integer"},
        "stop": {"type": "integer"},
        "asset": {"type": "integer"},
        "is_questionable": {"type": "boolean"},
        "notes": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": {"id", "batch_name", "start", "stop", "asset", "is_questionable"}
}

edge_connector_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "edge_device": {"type": "integer"},
        "connector_protocol": {
            "type": "integer",
            "minimum": 200,
            "exclusiveMaximum": 208
        },
        "name": {"type": "string"},
        "stream_status": {
            "type": "integer",
            "minimum": 0,
            "exclusiveMaximum": 6
        }
    }
}
