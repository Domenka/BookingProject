BOOKING_SCHEMA = {
    "type": "object",
    "properties": {
        "firstname" : {"type": "string"},
        "lastname" : {"type": "string"},
        "totalprice" : {"type": "integer"},
        "depositpaid" : {"type": "boolean"},
        "bookingdates" : {"type": "object",
        "properties": {"checkin" : {"type": "string"},
                       "checkout" : {"type": "string"}}},
        "additionalneeds" : {"type": "string"},

    },  "additionalProperties": False,
        "required": [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates"
    ],
}

BOOKINGIDS_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "bookingid": {
                "type": "integer"
            }
        },
        "required": ["bookingid"],
        "additionalProperties": False
    }
}