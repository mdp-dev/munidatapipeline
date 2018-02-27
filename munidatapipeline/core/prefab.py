import sys
import os
import traceback
from shapely.geometry import Point
import core.download as dlf
import pandas as pd
import geopandas as gpd


def err_to_parent(UDF):

    def handling(connection, load, message):
        try:
            UDF(connection, load, message)
        except Exception as e:
            
            connection.send({"BREAK": e,
                            "TB": traceback.format_exc()})
    handling.__name__ = UDF.__name__
    return handling

@err_to_parent
def simple_groupby(connection, load, message):
    """
    Return the result of a Pandas groupby method for
    the load dataframe.
    
    Inputs: 
    
    load (must be DataFrame or GeoDataFrame)
    message['col_name'], the series to group by
    message['groupby_method'], may be count, mean, sum, or median
    
    Output: sends the result of the method back up the pipe
    
    """
    
    if 'groupby_method' in message:
        groupby_method = message['groupby_method']
    else:
        raise ValueError('groupby_method must be sum, count, mean, or median')
    
    if 'col_name' not in message:
        raise ValueError("message['col_name'] not defined")
    
    if type(load).__name__ not in ['DataFrame', 'GeoDataFrame']:
        raise TypeError('load must be DataFrame or GeoDataFrame, not {}'.format(
            type(load).__name__))
                        
    
    valid_methods = ['sum', 'count', 'mean', 'median']
    if groupby_method not in(valid_methods):
        raise ValueError(
            'groupby must be sum, count, mean, or median , not {}'.format(
                groupby_method))
    if groupby_method == 'sum':
           grouped = load.groupby(message['col_name']).sum()
    if groupby_method == 'count':
           grouped = load.groupby(message['col_name']).count()
    if groupby_method == 'mean':
           grouped = load.groupby(message['col_name']).mean()
    if groupby_method == 'median':
           grouped = load.groupby(message['col_name']).median()
    
    connection.send(grouped)

@err_to_parent    
def points_from_latlong(connection, load, message):
    """
    Render a lat and long column to shapely points.
    
    Inputs: connection, load (a DataFrame or GeoDataFrame), message (see below)
    
        Message:
            message['lat'], the key/column name for lattitude listlike
            message['long'], the key/column name for the longitude listlike
            message['out_column'], name of new points column to be created

    Output: sends the load back up the pipe with a new points column
    
    """
    
    
    
    long = message['long']
    lat  = message['lat']
    
    load[message['out_column']] = [Point(x, y) for x, y in zip(
        load[long], load[lat]
    )]
    
    connection.send(load)

@err_to_parent    
def col_to_datetime (connection, load=None, message=None): 
    #turn list of columns into a date time object
    
    if type(load).__name__ == 'DataFrame':

        if not isinstance(message['col_to_datetime'], list):                 
                raise TypeError("message['col_to_datetime'] must be a list")
        if message['col_to_datetime'] == []:
                raise ValueError(
                    'List of columns to be converted to datetime object is empty')

        for i in message['col_to_datetime']:
            load[i] = pd.to_datetime(i)
        connection.send(load)

@err_to_parent
def data_down(connection, load, message):
    #A simple way to use the scheduler for downloading data

    if 'urls' not in message:
        raise ValueError("Required value 'message['urls']' missing!")
    
    for i in message['urls']:
        dlf.simple_download(i)
    
    print("Sending filepath!")
    connection.send("Finished Downloading")
        
        

        
@err_to_parent        
def pd_simple_merge(connection, load, message):
    """
    Perform a merge on two dataframes with the pandas merge.
    
    The left DataFrame is always the load argument while the
    right DataFrame is always constructed from a file.
    
    Requires: Pandas
    Inputs: connection, load (the left side, 
    a DataFrame), and message(see below)
    
        Message:
            message['path'], filepath for the right side of the join
            
            message['merge_args'], dict of required args for joining 
            the DataFrames
            
            message['DataFrame_right_args'], dict of 
            required args for constructing the DataFrame 
            from the path using the pd.DataFrame command
            
    
    Output: send the merged load back up the pipe
    
    """
    
    if type(load).__name__ != 'DataFrame':
        raise ValueError("load must be a Pandas DataFrame not {}".format(
            type(load).__name__))
    
    left  = load
    right = pd.DataFrame(message['path'], **message['DataFrame_right_args'])
    
    merged = pd.merge(left, right, **message['merge_args'])
    
@err_to_parent    
def pandas_frame_file(connection, load, message):
    """Simply read a file into a dataframe and send it back up the pipe.
    Input: filepath, filetype, read_args in message.
    Note: If message['use_chunk'] is True, then the function
    takes the filepath from the scheduler's current chunk
    
    Output: Sends a dataframe back up the pipe."""
    
    
    if 'use_chunk' in message:
        if message['use_chunk']:
            filepath = message['chunk']
    elif 'filepath' in message:
         filepath = message['filepath']
    
    try:
        os.path.exists(filepath)
    except Exception as e:
        raise e
    
    #Pick a reader and send back the df
    df = _pd_reader_pick(message)
    connection.send(df)

@err_to_parent
def simple_gpd_sjoin(connection, load, message):
    """
    Perform an sjoin on two dataframes with GeoPandas.
    
    If the load is not of type GeoDataFrame then try to
    construct it into one.
    
    The other GeoDataFrame is always constructed from a file.
    
    Requires: Geopandas
    Inputs: connection, load (the left side, 
    a DataFrame or GeoDataFrame), and message(see below)
    
        Message:
            message['path'], filepath for the right side of the join
            
            message['sjoin_args'], required args for joining 
            the GeoDataFrames
            
            message['GeoDataFrame_right_args'], required args for constructing
            the GeoDataFrame from the path using the gpd.read_file command
            
            message['GeoDataFrame_left_args'], optional args for constructing 
            the GeoDataFrame from the load using the gpd.read_file command
    
    Output: send the sjoined load back up the pipe
    """

    
    for i in ['sjoin_args', 'GeoDataFrame_right_args', 'path']:
        if i not in message:
            raise KeyError("{}".format(i))
    
    if type(load).__name__ != 'GeoDataFrame':
        if 'GeoDataFrame_left_args' in message:
            left = gpd.GeoDataFrame(load, **message['GeoDataFrame_left_args'])
        else:
            raise ValueError('GeoDataFrame_left_args is required if the load'
                            ' is not already a GeoDataFrame')
    else:
        left = load
    


    right = gpd.read_file(message['right_path'],
                **message['GeoDataFrame_right_args'])
    
    
    
    
@err_to_parent    
def pd_simple_merge(connection, load, message):
    """
    Perform a merge on two dataframes with the pandas merge.
    
    The left DataFrame is always the load argument while the
    right DataFrame is always constructed from a file.
    
    Requires: Pandas
    Inputs: connection, load (the left side, 
    a DataFrame), and message(see below)
    
        Message:
            message['path'], filepath for the right side of the join
            
            message['merge_args'], required args for joining 
            the DataFrames
            
            message['DataFrame_right_args'], required args for constructing
            the DataFrame from the path using the gpd.read_file command
            
    
    Output: send the merged load back up the pipe
    
    """
    

    
    if type(load).__name__ != 'DataFrame':
        raise ValueError("load must be a Pandas DataFrame not {}".format(
            type(load).__name__))
    
    left  = load
    right = pd.DataFrame(message['path'], **message['DataFrame_right_args'])
    
    merged = pd.merge(left, right, **message['merge_args'])
    
    connection.send(merged)
    
def _pd_reader_pick(message):
    
    if 'use_chunk' in message:
        if message['use_chunk']:
            filepath = message['chunk']
    elif not 'filepath' or 'use_chunk' in message:
        raise ValueError("Must pass message['filepath'] or message['use_chunk']")
    else:
        filepath = message['filepath']
    
    if not 'filetype' in message:
        raise ValueError("Must pass message['filetype'] \n"
                        "Supported types: 'csv', 'excel', 'pkl'")
    
    
    #Construct dataframes (with args if neccessary)
    if message['filetype'] == "csv":
        if 'read_args' in message:
            df = pd.read_csv(filepath, **message['read_args'])
        else:
            df = pd.read_csv(filepath)
    if message['filetype'] == "pkl":
        if 'read_args' in message:
            df = pd.read_pickle(filepath, **message['read_args'])
        else:
            df = pd.read_pickle(filepath)
    if message['filetype'] == "excel":
        if 'read_args' in message:
            df = pd.read_excel(filepath, **message['read_args'])
        else:
            df = pd.read_excel(filepath)
    return df

def pd_writer(connection, load, message):
    """Exposes the pandas to_file operations.
    Inputs:
    
    load, the dataframe to be written
    message['filetype'], can be 'csv', 'hd5' or 'excel'
    message['pd_args'], args for the pandas file writer
    message['path'], optional, filepath to write to, overrides opts.filepath
        
    Outputs: writes a file to target path
    """
    
    