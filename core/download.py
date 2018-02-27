def simple_download(url, local_filename= None):
    """
    Input: 
    url: url to download
    local_filename: optional, by default will use the downloads folder
    from options. (Can be set with  
    Checks if a file exists at a filepath, and if not, requests the file.
    Note: If the directory does not exist, it will try to make one using os.mkdir
    so targeting a subdirectory is not supported (yet)
    Returns: the relative path to the file.
    """
    
    import core.options as opts
    
    import os
    import requests
    import time
    
    if not isinstance(url, str):
        raise TypeError("url must be str, not {}".format(
            type(url).__name__
        ))
    
    if not os.path.exists(opts.downloads_folder):
        os.mkdir(opts.downloads_folder)
    if not local_filename:
        local_filename = str(opts.downloads_folder + url.split('/')[-1]) #TODO: Improve
    if not os.path.exists(local_filename):
        r = requests.get(url)

        if r.status_code != 200: #Check connection
            raise ConnectionError(
                "Connection Failed")

        with open(local_filename, 'wb') as f:
            f.write(r.content)
    return local_filename
        

    

def down_extract_zip(url, target_ext, local_filename=None, take_first=True):
    """Downloads and unzips a shape file and returns
    the filepath of the file(s) as a string or list of strings
    
    Usage: flname = down_extract_zip(url_of_zipfile, 'shp', )
    flname is now the path of the shpfile.
    
    Inputs: 
    URL, a URL string
    target_ext, a string such as 'shp' or 'json'
    local_filename, the name of the file where the data 
    will be written
    take_first, default True, if False return a list of matching files
    in the unzipped shape file, if True return just the filepath
    as a string
    
    """
    
    import core.options as opts
    
    import zipfile
    import requests
    import time
    
    if not isinstance(url, str):
        raise TypeError("url must be str, not {}".format(
            type(url).__name__
        ))
    
    if not isinstance(target_ext, str):
        raise TypeError("target_ext must be str, not {}".format(
            type(target_ext).__name__
        ))
        
    if not isinstance(take_first, bool):
        raise TypeError("take_first must be bool, not {}".format(
            type(take_first).__name__
        ))
        
    if not local_filename: 
        local_filename = str(opts.downloads_folder + url.split('/')[-1])
    zip_fld = local_filename[:-4]
    if not os.path.exists(zip_fld):
        r = requests.get(url)

        if r.status_code != 200: #Check connection
            raise ConnectionError(
                "Connection Failed")

        with open(local_filename, 'wb') as f:
            f.write(r.content)
        os.makedirs(zip_fld)
        
        with zipfile.ZipFile(local_filename, "r") as zip_pl:
            zip_pl.extractall(zip_fld)

    fld_arr = os.listdir(zip_fld) #get array of unzipped files
    flname = None
    
    if take_first:
        #Find the first match
        
        for unzippedfile in fld_arr[::-1]:  #Hacky, replace later?
            if str(unzippedfile[-3:]) == target_ext:
                flname = zip_fld + '/' + unzippedfile
        
        if not flname: 
            raise FileNotFoundError('File with extension "{}" not found!'.format(target_ext))
        
        return flname
    
    if not take_first:
        #Return a list of filepaths
        
        matches = [path for path in fld_arr if path[-3:] == target_ext] 
        
        if len(matches) < 1:
            raise FileNotFoundError(
                'File with extension "{}" not found!'.format(
                    target_ext))
        
        if len(matches) >= 1:
            return matches