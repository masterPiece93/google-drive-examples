"""[Drive Upload]
Author :
    Name : Ankit Kumar
    Email : ankit.kumar05@telusinternational.com
Contributers : ...
"""

import os
from pathlib import PosixPath
from typing import Dict
from enum import Enum
from functools import wraps
from googleapiclient.http import MediaFileUpload
from . import __data_path__, __csv_file__
from .errors import ArgumentError, _Type
from ..meta import ExampleData


class FileMimeTypes(Enum):
    """
    Standard File MimeTypes
    """
    csv = 'text/csv'
    txt = 'text/plain'
    json = 'application/json'


class GoogleMimeTypes(Enum):
    """
    Google (specific) Drive MimeTypes
    """
    google_sheets = 'application/vnd.google-apps.spreadsheet'


def _check_all_required_files_exist(func):
    """
    - checks if `sample_data_dir` is provides by user or not .
        - if not provided , it re-aligns the `sample_data_dir` variable
        to point to the internal data directory .
    - checks if all the files required by the example are present .
    """
    
    # utilities
    file_not_found_error_template = '{0} Required | No such file or directory : {1}'
    fetch_arg = lambda name, position, *args, **kwargs, : (kwargs[name], 'kwargs') if len(args) <= 1 else (args[position], 'args')
    fetch_kwarg = lambda kwargs, name: kwargs[name]

    @wraps(func)
    def _wrapper(*args, **kwargs):
        
        sample_data_dir, fetched_from = fetch_arg('sample_data_dir', 1, *args, **kwargs)
        is_unpecified = not sample_data_dir or sample_data_dir.lower() == 'unspecified' 
        if is_unpecified:
            if fetched_from == 'kwargs':
                kwargs['sample_data_dir'] = sample_data_dir = __data_path__
            else:
                args[1] = sample_data_dir = __data_path__

        # TypeCheck
        if not isinstance(sample_data_dir, (str,PosixPath)):
            raise ArgumentError(
                originator_name= func.__name__,
                _type= _Type.VALUE_TYPE_ERROR,
                _message= _Type.VALUE_TYPE_ERROR.value.format(
                    argument=f"{sample_data_dir=}",
                    expected= str,
                    got= type(sample_data_dir),
                    additional_message=''
                )
            )
        
        csv_path = os.path.join(sample_data_dir, ExampleData.CSV_FILE_NAME.value)

        # ValueCheck
        if not os.path.exists(csv_path):
            raise FileNotFoundError(file_not_found_error_template.format(f"{csv_path=}",csv_path))
        
        return func(*args, **kwargs)
    return _wrapper

@_check_all_required_files_exist
def main(
    service,
    sample_data_dir,
    folder_id: str = ''
):
    """
    \r## Uploading csv files in drive
    
    Args:
        service (object): a drive object
        sample_data_dir (str): a path to set of files required for this example to run
            - example_csv_file.csv : a dummy/sample csv file
        folder_id (str): a google drive id of folder in which you want to
            upload sample files . Defaults to empty string .
    
    Returns:
        None
    """
    file_names_to_mimetype_map : Dict[str, str] =  {
            f'example_csv_file.csv'    :   FileMimeTypes.csv.value
    }

    for file_name, file_mimetype in file_names_to_mimetype_map.items():
        file_metadata: dict = {
            'name': file_name
        ,   'parents': [folder_id] if folder_id else []
        }

        # for updating as google sheets
        file_metadata.update({'mimeType': GoogleMimeTypes.google_sheets.value})

        file_path = os.path.join(sample_data_dir, file_name)
        media = MediaFileUpload(
            filename= file_path
        ,   mimetype= file_mimetype
        )

        service.files().create(
                body=file_metadata
            ,   media_body=media  
        ).execute()


# : ====================== :
# : Extended Documentation :
# : ====================== :
__extended_docs__ = """
#### Pre-requisites for running this example :

    You need to create a folder/directory ( for the sample data that'll be used in this example )
    in your local system , in which you need to create folowwing sample files :
        - A csv file with name  : example_csv_file.csv
        - A json file with name : example_json_file.json
        - A text file with name : example_text_file.txt
    The conent in these files can be anything you like .

""" + """
#### Code Description :

    Following is the psuedocode/steps of the program code :

        - we have a list of file names ( accordingly as per their name where they are saved )
    
        - we have a folder_id ( which you can get from drive ui/app in your webbrowser )
            - folder_id is not a required parameter
            - if folder_id is present , 
                - files are uploaded in that folder
            - else
                - files are uploaded at rool/drive level

        - we will do an iteration over all these names and call the drive api
            - during each call , we pass a metadata, which directs drive api, how to
            create a folder .

            - during each call, we create a media object

            - pass the metadata and media to the `create` api .

""" + """
#### References :

[List of all supported file mimetypes](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types)

[List of all Google Covention supported Drive mimetypes](https://developers.google.com/drive/api/guides/mime-types)

"""

main.__doc__ += __extended_docs__
