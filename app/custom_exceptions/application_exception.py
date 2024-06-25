from starlette.exceptions import HTTPException
from typing import Any,Optional,Dict

class Main(HTTPException):
    def __init__(
            self,
            status_code: int,
            detail: Any,
            headers: dict = {}):
        super().__init__(status_code, detail, headers)

class BadRequest(Main):
	def __init__(self,
		extra_info: dict = {},
		headers: Optional[Dict[str,str]] = None):
		super().__init__(status_code=400, detail=extra_info)
            
try:
      raise BadRequest(extra_info={"error": "Bad Request"})
except BadRequest as e:
	print(e.detail)
	print(e.status_code)
	print(e.headers)