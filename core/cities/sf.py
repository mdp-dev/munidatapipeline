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

def down_sf_zipcodes(connection, load, message):
    """
    downloads the sf zipcodes shape file  
    
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
        message['url'] = 'https://data.sfgov.org/api/geospatial/u5j3-svi6?method=export&format=Shapefile'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)      
    
def down_sf_pn(connection, load, message):#planning neighborhoods
    """
    downloads the sf planning neighborhoods shape file  
    
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
        message['url'] = 'https://data.sfgov.org/api/geospatial/iacs-ws63?method=export&format=Shapefile'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)  
    
    
def down_sf_census(connection, load, message):
    """
    downloads the sf census tracts shape file  
    
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
        message['url'] = 'https://data.sfgov.org/api/geospatial/rarb-5ahf?method=export&format=Shapefile'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)   
