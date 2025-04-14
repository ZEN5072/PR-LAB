from pydantic import BaseModel

class TaskBase(BaseModel):  # рофлянки для fastapi
    title: str
    completed: bool = False # по умолчанию таск не завершен 
                            # (бог сказал, халоп скопировал)

class TaskCreate(TaskBase): # рофлянки для fastapi
    pass

class TaskUpdate(TaskBase): # рофлянки для fastapi
    pass

class Task(TaskBase): # модель тасков
    id: int

    class Config:
        orm_mode = True
