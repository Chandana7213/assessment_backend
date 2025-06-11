from pydantic import BaseModel

class CategoryRequest(BaseModel):
    name: str
    
    
class QuestionRequest(BaseModel):
    question: str
    answer: str
    marks: int
    category: int