"""
Box Platform access token generator
"""

import os

import yaml
import boxsdk


BOX_JWT_KEYS_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "box_jwt_keys.yml"
)
box_jwt_keys = None
box_client = None


def get_box_jwt_keys():
    """
    Loads Box Platform JWT keys into a global variable.
    """
    global box_jwt_keys
    if not box_jwt_keys:
        with open(BOX_JWT_KEYS_FILE_PATH, "r") as fh:
            box_jwt_keys = yaml.load(fh, Loader=yaml.FullLoader)

    return box_jwt_keys


def get_box_auth():
    """
    Authenticates a Box SDK JWTAuth instance into Box Platform APIs.
    """
    box_jwt_keys = get_box_jwt_keys()
    box_auth = boxsdk.JWTAuth.from_settings_dictionary(box_jwt_keys)
    box_auth.authenticate_instance()

    return box_auth


def get_box_client():
    """
    Sets up a Box Platform API client as a global variable.
    """
    global box_client
    if not box_client:
        box_auth = get_box_auth()
        box_client = boxsdk.Client(box_auth)

    return box_client


if __name__ == "__main__":
    box_auth = get_box_auth()
    print(f"Box Platform access token {box_auth.access_token}")