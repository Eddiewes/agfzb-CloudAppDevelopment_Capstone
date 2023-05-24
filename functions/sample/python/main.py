"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


def main(param_dict):
    """Main Function

    Args:
        param_dict (Dict): input paramater

    Returns:
        _type_: _description_ TODO
    """

    try:
        client = Cloudant.iam(
            account_name=param_dict["986c4636-5e97-4a25-9156-6f14676e7141-bluemix"],
            api_key=param_dict["xfJCWu55dC5765SP6IR3PXDv5PCTI5V-JiW4PRpgqYqD"],
            connect=True,
        )
        print(f"Databases: {client.all_dbs()}")
    except CloudantException as cloudant_exception:
        print("unable to connect")
        return {"error": cloudant_exception}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"dbs": client.all_dbs()}
