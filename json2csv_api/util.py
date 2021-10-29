from typing import Any, Dict
import json

def error_response(message: str, **attrs: Any) -> str:
    error_body: Dict[str, Dict[str, Any]] = {'error': {'message': message}}
    error_body['error'].update(attrs)
    return json.dumps(error_body)
