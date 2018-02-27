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

def down_nyc_pd(connection, load, message): #police districts 
    """
    downloads the nyc police districts shape file  
    
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
        message['url'] = 'https://data.cityofnewyork.us/api/geospatial/78dh-3ptz?method=export&format=Shapefile'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)

def down_nyc_sd(connection, load, message): #school districts 
    """
    downloads the nyc school districts shape file  
    
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
        message['url'] = 'https://data.cityofnewyork.us/api/geospatial/r8nu-ymqj?method=export&format=Shapefile'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)
    
def down_nyc_cd(connection, load, message):#community districts 
    """
    downloads the nyc community districts shape file  
    
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
        message['url'] = 'https://data.cityofnewyork.us/api/geospatial/yfnk-k7r4?method=export&format=Shapefile'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)
     
    
def down_nyc_census(connection, load, message):#census tracts
    """
    downloads the nyc census shape file  
    
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
        message['url'] = 'https://data.cityofnewyork.us/api/geospatial/v2h8-6mxf?method=export&format=Shapefile'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)
    
def down_nyc_cc(connection, load, message):#city council districts 
    """
    downloads the nyc city council shape file  
    
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
        message['url'] = 'https://data.cityofnewyork.us/api/geospatial/yusd-j4xi?method=export&format=Shapefile'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)
       
    
def down_nyc_congress(connection, load, message):#congressional districts 
    """
    downloads the nyc congressional districts shape file  
    
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
        message['url'] = 'https://data.cityofnewyork.us/api/geospatial/qd3c-zuu7?method=export&format=Shapefile'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)  
