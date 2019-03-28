import os

def rename_files():
    # 1st get file names from a folder
    file_list = os.listdir(r"D:\Python learning\Udacity\prank\prank")
    saved = os.getcwd()
    current_folder = os.chdir(r"D:\Python learning\Udacity\prank\prank")
    
    
    #  2nd get the file names
    for file_rename in file_list:
        table = str.maketrans(dict.fromkeys('0123456789'))
        # is removing character from string (OR)removies number in string
        os.rename(file_rename,file_rename.translate(table))
    os.chdir(saved)
    
    
        
    
rename_files()
