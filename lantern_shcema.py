from pydantic import BaseModel


class LanternState(BaseModel):
    is_on: bool = False
    color: str = 'red'

    @classmethod
    def allowed_colors(cls):
        return ['red', 'green', 'blue']


state = LanternState()
