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


def down_la_census_council(connection, load, message):#city council districts joined with census tracts 2010
    """
    downloads the la city council and census polygons shape file  
    
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
        message['url'] = 'http://geohub.lacity.org/datasets/3d41239eaa564ca699b17dbefd5d2981_0.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape) 
    
def down_la_pd(connection, load, message):#police districts 
    """
    downloads the la police districts shape file  
    
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
        message['url'] = 'http://geohub.lacity.org/datasets/031d488e158144d0b3aecaa9c888b7b3_0.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape) 
    
def down_la_congress(connection, load, message):#congressional districts  
    """
    downloads the la congressional districts shape file  
    
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
        message['url'] = 'http://geohub.lacity.org/datasets/ab63122b097641d28d70ef434ebdf852_10'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)     

def down_la_precincts(connection, load, message): 
    """
    downloads the la precincts districts shape file  
    
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
        message['url'] = 'http://geohub.lacity.org/datasets/c1447c80d12b4d499c273999314a6aee_1.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape)   
    
    
def down_la_zoning(connection, load, message):  
    """
    downloads the la zoning districts shape file  
    
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
        message['url'] = 'http://geohub.lacity.org/datasets/49ad06a6b8c945debbbea865b1832ee2_0.zip'

    shape = dlf.down_extract_zip(message['url'], message['target_extension'], local_filename = message['local_filename'],)
    shape = gpd.read_file(shape)

    connection.send(shape) 