
Google Drive - Examples
=======================


    ## Listing Files in Drive

    Lists all the files and folders inside the provided folder_id
    if folder_id not specified , it gives all the files/folder at root

    Args:

        service (object): a drive object. must be a drive v3 service object.
        folder_id (str): a google drive id of folder in which you want to
            upload sample files . Defaults to empty string .
    
    Returns:
        None : Only Prints the list of files in table format .
    
#### Pre-requisites for running this example :
    
    None


#### Code Description :

    In Google Drive coventions, the folders are also treated aa a file 
    with filetype as -> `folder`.

    Following is the psuedocode/steps of the program code :
        ...


#### References :
[Searching for files in Drive](https://developers.google.com/drive/api/guides/search-files)

---------


    ## Uploading Files to Drive

    In this example we will upload some files to drive at a
    specific folder.
    We will use Drive Api V3 for this purpose .
    
    Args:
        service (object): a drive object. must be a drive v3 service object.
        sample_data_dir (str): a path to set of files required for this example to run
            - example_csv_file.csv    : a dummy/sample csv file 
            - example_json_file.json  : a dummy/sample json file
            - example_text_file.txt   : a dummy/sample text file
        folder_id (str): a google drive id of folder in which you want to
            upload sample files . Defaults to empty string .
    
    Returns:
        None
    
#### Pre-requisites for running this example :

    You need to create a folder/directory ( for the sample data that'll be used in this example )
    in your local system , in which you need to create folowwing sample files :
        - A csv file with name  : example_csv_file.csv
        - A json file with name : example_json_file.json
        - A text file with name : example_text_file.txt 
    The conent in these files can be anything you like .


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


#### References :

[List of all supported file mimetypes](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types)

[List of all Google Covention supported Drive mimetypes](https://developers.google.com/drive/api/guides/mime-types)


---------


    ## Uploading csv files in drive
    
    Args:
        service (object): a drive object
        sample_data_dir (str): a path to set of files required for this example to run
            - example_csv_file.csv : a dummy/sample csv file
        folder_id (str): a google drive id of folder in which you want to
            upload sample files . Defaults to empty string .
    
    Returns:
        None
    
#### Pre-requisites for running this example :

    You need to create a folder/directory ( for the sample data that'll be used in this example )
    in your local system , in which you need to create folowwing sample files :
        - A csv file with name  : example_csv_file.csv
        - A json file with name : example_json_file.json
        - A text file with name : example_text_file.txt
    The conent in these files can be anything you like .


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


#### References :

[List of all supported file mimetypes](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types)

[List of all Google Covention supported Drive mimetypes](https://developers.google.com/drive/api/guides/mime-types)


---------


    ## Downloading Files From Drive

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
    
#### Pre-requisites for running this example :
    None


#### Notes :
1. List of Prohibitted Files ( that can't be downloaded ): {__prohobited_file_extendions__}


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
    

#### References :

[List of all supported file mimetypes](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types)

[List of all Google Covention supported Drive mimetypes](https://developers.google.com/drive/api/guides/mime-types)


---------


    ## Create Folders in Drive
    
    In this example we will create folders for the given name .
    We will create folders with following names :-
        'India', 'Russia', 'America' and 'France'

    Args:
        service (object): a drive object. must be a drive v3 service object.
    
    Returns:
        None
    
#### Pre-requisites for running this example :
    
    None


#### Code Description :

    - we have a list of folder names
    - we will do an iteration over all these names and call the drive api
        - during each call , we pass a metadata, which directs drive api, how to
            create a folder .


#### References :

[List of all Google Covention supported Drive mimetypes](https://developers.google.com/drive/api/guides/mime-types)


---------


