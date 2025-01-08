"""[Drive Upload]
Author :
    Name : Ankit Kumar
    Email : ankit.kumar05@telusinternational.com
Contributers : ...
"""

from typing import List

def main(
    service,
):
    """
    \r## Create Folders in Drive
    
    In this example we will create folders for the given name .
    We will create folders with following names :-
        'India', 'Russia', 'America' and 'France'

    Args:
        service (object): a drive object. must be a drive v3 service object.
    
    Returns:
        None
    """

    # Main :

    folder_names : List[str] =  ['India', 'Russia', 'America', 'France']

    for name in folder_names:
        file_metadata: dict = {
            'name': name
        ,   'mimeType': "application/vnd.google-apps.folder" # < must be a supported mimetype .
        ,   'parents': []
        }

        service.files().create(
            body=file_metadata
        ).execute()


__extended_docs__ = """
#### Pre-requisites for running this example :
    
    None

""" + """
#### Code Description :

    - we have a list of folder names
    - we will do an iteration over all these names and call the drive api
        - during each call , we pass a metadata, which directs drive api, how to
            create a folder .

""" + """
#### References :

[List of all Google Covention supported Drive mimetypes](https://developers.google.com/drive/api/guides/mime-types)

"""

main.__doc__ += __extended_docs__
