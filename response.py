from fastapi.responses import JSONResponse


def _format_response(status: str, data=None, message: str = "", status_code: int = 200):
    content = {"status": status, "data": data, "message": message}
    return JSONResponse(content=content, status_code=status_code)


def success(data=None, message: str = "Data fetched successfully", status_code: int = 200):
    return _format_response("success", data, message, status_code)


def created(data=None, message: str = "Resource created successfully", status_code: int = 201):
    return _format_response("success", data, message, status_code)


def deleted(data=None, message: str = "Resource deleted successfully", status_code: int = 200):
    return _format_response("success", data, message, status_code)


def not_found(message: str = "Not found", status_code: int = 404):
    return _format_response("error", None, message, status_code)


def error(message: str = "Internal server error", status_code: int = 500):
    return _format_response("error", None, message, status_code)
