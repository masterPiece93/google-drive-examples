"""[Drive Upload]
Author :
    Name : Ankit Kumar
    Email : ankit.kumar05@telusinternational.com
Contributers : ...
"""

import os
import io
from pathlib import Path
from typing import Dict
from enum import Enum
from functools import wraps
from googleapiclient.http import MediaIoBaseDownload


class FileMimeTypes(Enum):
    csv = 'text/csv'
    txt = 'text/plain'
    json = 'application/json'


__prohobited_file_extendions__ = ('.xlsx',)

def _check_all_required_files_exist(func):
    """
    checks if all the files required by the example are present .
    """

    @wraps(func)
    def _wrapper(*args, **kwargs):
        
        if len(args) <= 1:
            download_files_map = kwargs['download_files_map']
        else:
            download_files_map = args[1]

        for key in download_files_map:
            _, file_extension = os.path.splitext(key)
            if file_extension in __prohobited_file_extendions__:
                raise KeyError(f'download_files_map must not contain keys with extension : {__prohobited_file_extendions__}')
        
        return func(*args, **kwargs)
    return _wrapper

@_check_all_required_files_exist
def main(
    service,
    download_files_map: Dict[str, str]
):
    """
    \r## Downloading Files From Drive

    In this example, we will download some files from drive based
        on file id's.
    The downloaded files will be visible in downloads folder inside
    a folder named - `google_drive_test`. The name of the files
    will be the key name you provided in `download_files_map` .

    Args:
        service (object): a drive object. must be a drive v3 service object.
        download_files_map (Dict[str, str]): a map of filename.extension with corresponding drive id .
            for example :
                {
                    # 'my_downloaded_file.xlsx':'1PZrvx_0e09ecglzSPf92JbZzxyNTOrV6aQAp1hA2dLs'
                    'my_random_filename.png': '9631b31e-c19e-4cbb-b6f1-af90e903a1e3'
                }

                Note : .xlsx files are not downloadable . Please find the list of 
                prohibitted files attached .
    Returns:
        None : Only Prints the list of files in table format .
    """

    # Main :

    files_map : Dict[str, str] = download_files_map 

    for file_name, file_id in files_map.items():

        request = service.files().get_media(fileId=file_id)

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)
        
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(file_name, ' | ','Download Progress : {}'.format(status.progress() * 100))
        fh.seek(0) # < resetting the buffer , for each new file ( in order to reuse buffer ).

        # paths
        system_home = os.path.expanduser('~') # < path @ Home folder
        my_downloads_folder_path = os.path.join(system_home, "Downloads") # < path @ System Downloads folder
        google_drive_test_folder_path =  os.path.join(my_downloads_folder_path, 'google_drive_test') # path @ google_drive_test folder
        
        # create the folder for containing downloaded files :
        Path(google_drive_test_folder_path).mkdir(parents=True, exist_ok=True)
        
        # saving downloaded files
        with open(os.path.join(google_drive_test_folder_path, file_name), 'wb') as file:
            file.write(fh.read()) # < writing the buffered data obj onto file object
            file.close()


__extended_docs__ = f"""
#### Pre-requisites for running this example :
    None

""" + """
#### Notes :
1. List of Prohibitted Files ( that can't be downloaded ): {__prohobited_file_extendions__}

""" + """
#### Code Description :

    - we have a list of file id's .

    - Q: how to get the file-id of a file in google drive in browser .
    - A: -for a file in drive , click on `share` & `get sharable link`
            in that link , last/second-last part is the file-id

    - we will do an iteration over all these names 

        - during each call , we create a media request object based on file-id

    - a buffer object is created .

    - based on this media request object & buffer, a downloader object is created .
        The downloader , downloads this data into the buffer .

    - once all the data/chunks are recieved , the buffer data is then written to
        a file .
    
""" + """
#### References :

[List of all supported file mimetypes](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types)

[List of all Google Covention supported Drive mimetypes](https://developers.google.com/drive/api/guides/mime-types)

"""

main.__doc__ += __extended_docs__
