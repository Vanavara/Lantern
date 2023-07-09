# thirdparty
import socket

from fastapi import APIRouter

# project
from shcemas.lantern_shcema import state, LanternState
from utils.errors import ErrorResponseEnum
from utils.helpers import CustomHTTPException

lantern_router = APIRouter(tags=["1. LANTERN"])


@lantern_router.get("/lantern")
async def get_lantern_state():
    """
    Get a lantern current situation
    """
    return state


@lantern_router.put("/lantern/on")
async def turn_on_lantern():
    """
    Turn the lantern on
    """
    state.is_on = True
    return {"message": "Lantern turned on"}


@lantern_router.put("/lantern/off")
async def turn_off_lantern():
    """
    Turn the lantern off
    """
    state.is_on = False
    return {"message": "Lantern turned off"}


@lantern_router.put("/lantern/color")
async def change_lantern_color(color: str):
    """
    Switch the color of the lantern
    """
    if color in LanternState.allowed_colors():
        state.color = color
        return {"message": f"Lantern color changed to {color}"}
    else:
        return {"message": "Invalid color"}


@lantern_router.put("/lantern/control")
async def control_lantern(host: str, port: int):
    """
    Control the lantern with specified host and port
    """
    try:
        # Create TCP-connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        # Sending control protocol
        protocol = "YOUR_CONTROL_PROTOCOL"
        sock.sendall(protocol.encode())

        # Receiving a server answer
        response = sock.recv(1024).decode()

        # Closing of the connection
        sock.close()

        return {"message": "Lantern control initiated", "response": response}

    except:
        raise CustomHTTPException(error_response=ErrorResponseEnum.SOMETHING_WENT_WRONG)
