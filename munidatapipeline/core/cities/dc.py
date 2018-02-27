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

def down_dc_ward(connection, load, message):
    """
    downloads the dc ward shape file 
    
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
        message['url'] = 'https://opendata.arcgis.com/datasets/0ef47379cbae44e88267c01eaec2ff6e_31.zip' 

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)
    
    
def down_dc_anc(connection, load, message): 
    """
    downloads the dc anc shape file 
    
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
        message['url'] = 'https://opendata.arcgis.com/datasets/fcfbf29074e549d8aff9b9c708179291_1.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)
    
def down_dc_census (connection, load, message):   
    """
    downloads the dc census shape file 
    
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
        message['url'] = 'https://opendata.arcgis.com/datasets/6969dd63c5cb4d6aa32f15effb8311f3_8.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)
    
