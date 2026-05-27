BOOKING_SCHEMA = {
    "type": "object",
    "properties": {
        "bookingid": {
            "type": "integer"
        },
        "booking": {
            "type": "object",
            "properties": {
                "firstname": {"type": "string"},
                "lastname": {"type": "string"},
                "totalprice": {"type": "integer"},
                "depositpaid": {"type": "boolean"},
                "bookingdates": {
                    "type": "object",
                    "properties": {
                        "checkin": {"type": "string"},
                        "checkout": {"type": "string"}
                    },
                    "required": ["checkin", "checkout"],
                    "additionalProperties": False
                },
                "additionalneeds": {"type": "string"}
            },
            "required": [
                "firstname",
                "lastname",
                "totalprice",
                "depositpaid",
                "bookingdates"
            ],
            "additionalProperties": False
        }
    },
    "required": ["bookingid", "booking"],
    "additionalProperties": False
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
