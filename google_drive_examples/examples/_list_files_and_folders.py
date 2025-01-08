"""[Drive Upload]
Author :
    Name : Ankit Kumar
    Email : ankit.kumar05@telusinternational.com
Contributers : ...
"""

import pandas as pd

def main(
    service,
    folder_id: str = "" # with default value , it will search at root level of drive
):
    """
    \r## Listing Files in Drive

    Lists all the files and folders inside the provided folder_id
    if folder_id not specified , it gives all the files/folder at root

    Args:

        service (object): a drive object. must be a drive v3 service object.
        folder_id (str): a google drive id of folder in which you want to
            upload sample files . Defaults to empty string .
    
    Returns:
        None : Only Prints the list of files in table format .
    """
    
    query = f"parents = '{folder_id}'" if folder_id else ''
    
    files = []
    while True:

        response = service.files().list(q=query).execute()
        response_files = response.get('files', [])
        files.extend(response_files)
        nextPageToken = response.get('nextPageToken')

        if not nextPageToken:
            break
        
        print(nextPageToken)
        
    # -- displaying :
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.min_rows', 500)
    pd.set_option('display.max_colwidth', 150)
    pd.set_option('display.width', 200)
    pd.set_option('expand_frame_repr', True)
    df = pd.DataFrame(files)
    print(df)

__extended_docs__ = """
#### Pre-requisites for running this example :
    
    None

""" + """
#### Code Description :

    In Google Drive coventions, the folders are also treated as a file 
    with filetype as -> `folder`.

    Following is the psuedocode/steps of the program code :
        ...

""" + """
#### References :
[Searching for files in Drive](https://developers.google.com/drive/api/guides/search-files)
"""

main.__doc__ += __extended_docs__
