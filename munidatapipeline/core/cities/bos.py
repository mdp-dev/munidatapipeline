def down_shape_specs(message): 
    """
    Specifies errors for city built in functions
    """
    import downloading_funcs as dlf 
    if not message['target_extension']:
        raise FileNotFoundError ('missing target extension')
    if message['gis_method'] == 'geopandas':
        try:
            import geopandas as gpd
        except ImportError as e:
            raise ValueError('String')
        if message['take_first'] == True:
            raise ValueError ('Argument may not be memory safe') 
            
def down_bos_cc(connection, load, message):
    """
    downloads the boston city council districts shape file 
    
    passes message dict to down_extract_zip function from downloading functions. 
    
    reads shape filepath and sends shape.
    -----------
    parameters :
        message: {url : , target_exenstion : , local_filename : } 
        
            url : a string passed to dlf.down_extract_zip, containing the url. if left empty, automatically passes
            
            default function dataset. 
            
            target_extension : desired filetype that needs to be extracted that is contained in the zip folder 
            
            (i.e. 'shp') 
            
            local_filename : A string. The desired filename you would like the file to be written to your directory as. 
            
    """
    down_shape_specs(message)
    import geopandas as gpd 
    import downloading_funcs as dlf 
    if 'url' not in message:
        message['url'] = 'http://bostonopendata-boston.opendata.arcgis.com/datasets/7dc47e49e35b41f3be9e2e0bdd4940f1_4.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)

def down_bos_zd(connection, load, message):
    """
    downloads the boston zoning districts shape file 
    
    passes message dict to down_extract_zip function from downloading functions. 
    
    reads shape filepath and sends shape.
    -----------
    parameters :
        message: {url : , target_exenstion : , local_filename : } 
        
            url : a string passed to dlf.down_extract_zip, containing the url. if left empty, automatically passes
            
            default function dataset. 
            
            target_extension : desired filetype that needs to be extracted that is contained in the zip folder 
            
            (i.e. 'shp') 
            
            local_filename : A string. The desired filename you would like the file to be written to your directory as. 
            
    """
    
    down_shape_specs(message)
    import geopandas as gpd 
    import downloading_funcs as dlf 
    if 'url' not in message:
        message['url'] = 'http://bostonopendata-boston.opendata.arcgis.com/datasets/eebd3daed05a45678894db30d9bf0cfb_0.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)    

def down_bos_wards(connection, load, message):
    """
    downloads the boston wards shape file 
    
    passes message dict to down_extract_zip function from downloading functions. 
    
    reads shape filepath and sends shape.
    -----------
    parameters :
        message: {url : , target_exenstion : , local_filename : } 
        
            url : a string passed to dlf.down_extract_zip, containing the url. if left empty, automatically passes
            
            default function dataset. 
            
            target_extension : desired filetype that needs to be extracted that is contained in the zip folder 
            
            (i.e. 'shp') 
            
            local_filename : A string. The desired filename you would like the file to be written to your directory as. 
            
    """
    down_shape_specs(message)
    import geopandas as gpd 
    import downloading_funcs as dlf 
    if 'url' not in message:
        message['url'] = 'http://bostonopendata-boston.opendata.arcgis.com/datasets/398ee443f4ac49e9a0b7facf80afc20f_8.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)
    
def down_bos_ss(connection, load, message): 
    """
    downloads the boston street segment shape file 
    
    passes message dict to down_extract_zip function from downloading functions. 
    
    reads shape filepath and sends shape.
    -----------
    parameters :
        message: {url : , target_exenstion : , local_filename : } 
        
            url : a string passed to dlf.down_extract_zip, containing the url. if left empty, automatically passes
            
            default function dataset. 
            
            target_extension : desired filetype that needs to be extracted that is contained in the zip folder 
            
            (i.e. 'shp') 
            
            local_filename : A string. The desired filename you would like the file to be written to your directory as. 
            
    """
    down_shape_specs(message)
    import geopandas as gpd 
    import downloading_funcs as dlf 
    if 'url' not in message:
        message['url'] = 'http://bostonopendata-boston.opendata.arcgis.com/datasets/cfd1740c2e4b49389f47a9ce2dd236cc_8.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)
    
def down_bos_nbrhd(connection, load, message): #neighborhoods
    """
    downloads the boston neighborhood shape file 
    
    passes message dict to down_extract_zip function from downloading functions. 
    
    reads shape filepath and sends shape.
    -----------
    parameters :
        message: {url : , target_exenstion : , local_filename : } 
        
            url : a string passed to dlf.down_extract_zip, containing the url. if left empty, automatically passes
            
            default function dataset. 
            
            target_extension : desired filetype that needs to be extracted that is contained in the zip folder 
            
            (i.e. 'shp') 
            
            local_filename : A string. The desired filename you would like the file to be written to your directory as. 
            
    """    
    
    down_shape_specs(message)
    import geopandas as gpd 
    import downloading_funcs as dlf 
    if 'url' not in message:
        message['url'] = 'http://bostonopendata-boston.opendata.arcgis.com/datasets/3525b0ee6e6b427f9aab5d0a1d0a1a28_0.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)

def down_bos_pwd(connection, load, message): 
    """
    downloads the boston public workds district file 
    
    passes message dict to down_extract_zip function from downloading functions. 
    
    reads shape filepath and sends shape.
    -----------
    parameters :
        message: {url : , target_exenstion : , local_filename : } 
        
            url : a string passed to dlf.down_extract_zip, containing the url. if left empty, automatically passes
            
            default function dataset. 
            
            target_extension : desired filetype that needs to be extracted that is contained in the zip folder 
            
            (i.e. 'shp') 
            
            local_filename : A string. The desired filename you would like the file to be written to your directory as. 
            
    """        
    down_shape_specs(message)
    import geopandas as gpd 
    import downloading_funcs as dlf 
    if 'url' not in message:
        message['url'] = 'http://bostonopendata-boston.opendata.arcgis.com/datasets/4b0f71af07664337975119c526f5a3a8_2.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)