TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "select_data_source",
            "description": "Select sales or admin data source and extract identifier",
            "parameters": {
                "type": "object",
                "properties": {
                    "source": {
                        "type": "string",
                        "enum": ["sales", "admin"]
                    },
                    "id": {
                        "type": "integer",
                        "description": "Customer ID or Admin ID"
                    },
                    "name": {
                        "type": "string",
                        "description": "Customer name"
                    },
                    "username":{
                        "type": "string",
                        "description": "Admin username"
                    }
                },
                "required": ["source"]
            }
        }
    }
]
