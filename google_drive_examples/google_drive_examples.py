from .examples._list_files_and_folders import main as list_files_and_folders
from .examples._upload_file_to_drive import main as upload_file_to_drive
from .examples._upload_csv_file_as_sheet import main as upload_csv_file_as_sheet
from .examples._download_files_from_drive import main as download_files_from_drive
from .examples._create_folder_in_drive import main as create_folder_in_drive
from .examples._copy_files_in_drive import main as copy_files_in_drive
from .examples._download_gmail_attachments import main as download_gmail_attachments
from .examples._move_files_across import main as move_files_across
from .examples._upload_and_replace_files import main as upload_and_replace_files
from .examples._file_rivision_history_and_restoration import main as file_rivision_history_and_restoration
from .examples._import_excel_files_as_sheets import main as import_excel_files_as_sheets


__all__ = [
    'list_files_and_folders',
    'upload_file_to_drive',
    'upload_csv_file_as_sheet',
    'download_files_from_drive',
    'create_folder_in_drive',
    'documentation'
]

# Documentation :
_sep_ = "\n---------\n\n"
documentation = f"\nGoogle Drive - Examples\n{'='*23}\n\n" \
        + list_files_and_folders.__doc__\
        + _sep_\
        + upload_file_to_drive.__doc__\
        + _sep_\
        + upload_csv_file_as_sheet.__doc__\
        + _sep_\
        + download_files_from_drive.__doc__\
        + _sep_\
        + create_folder_in_drive.__doc__\
        + _sep_\
        
