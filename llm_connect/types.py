from typing import Literal, TypeAlias, TypeVar
from pydantic import BaseModel

JsonOutput = TypeVar("JsonOutput", bound=BaseModel)
