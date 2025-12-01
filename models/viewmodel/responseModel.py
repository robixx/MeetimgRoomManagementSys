
from pydantic import BaseModel
from typing import Generic, TypeVar, List, Optional
from pydantic.generics import GenericModel


T=TypeVar("T")

class  ResponseModel(GenericModel,Generic[T]):
    status:int
    message:str
    data:Optional[List[T]]=[]