from __future__ import division
import sys
import os
import multiprocessing
from multiprocessing import Pipe
import prefab
import options as opts
import download

try:
    from core import *
except Exception as e:
    
    pass

class muni_data_pipe:
    """TODO: Docstring"""

    
    def __init__(self, wrangler='pandas', load='pandas', gis='geopandas', **kwargs):
                
        self.data     = None
        self.opts     = opts
        self.load     = load
        self.prefab   = prefab
        self.download = download
        
        
        #Default to Pandas if Dask won't wrangle
        if wrangler is 'pandas':
            import pandas as wg
        if wrangler is 'dask':
            try: 
                import dask as wg
            except ImportError:
                try:
                    import pandas as wg
                except ImportError:
                    raise ImportError(
            'Unable to import dask or pandas! (This should never happen.)'
                                     )
        self.wg = wg
        
        if self.load in ['SQLite']:
            sql_conn  = sqlite3.connect(self.opts.db_pth)
            curs     = sql_conn.cursor()
            curs.execute(self.opts.create_tables)
            
            
        if self.load == 'pandas':
            self.data = self.wg.DataFrame()
    
    def scheduler(self, chunk = None, sched = None):
        """TODO: Docstring"""
        
        if not sched:
            sched = self.opts.schedule
        
        if not chunk:
            chunk = self.opts.chunk
        
        
        sched_copy = [i for i in sched]
        sched_copy.reverse()
        
        while len(sched_copy) > 0:
            parent_conn, child_conn = Pipe()
            
            scheduled_func, message = sched_copy.pop()
            
            #The user must define chunk somewhere
            if 'chunk' in message:
                pass
            elif chunk:
                message['chunk'] = chunk
            else:
                raise ValueError(
            "The scheduler needs to know which chunk of data to use."
             )

            #Spawn the process and pass the connection, data and message to it
            if message:
                if 'load' in message:
                    if message['load'] == False:
                        p = multiprocessing.Process(target=scheduled_func, 
                                        args=(child_conn, None, message), 
                                        name = scheduled_func.__name__)
                        p.start()
                else:
                    p = multiprocessing.Process(target=scheduled_func, 
                                        args=(child_conn, self.data, message), 
                                        name = scheduled_func.__name__)
                    p.start()
            else:
                p = multiprocessing.Process(target=scheduled_func, 
                                        args=(child_conn, None, None), 
                                        name = scheduled_func.__name__)
                p.start()
                
             
                
            
            
            
            if self.opts.loud:
                print(
                    'Beginning next function: {}, {} remaining'.format(
                        p.name, len(sched_copy)))
            
            recv = parent_conn.recv()    
            p.join(timeout = self.opts.timeouts)
            
            if "BREAK" in recv:
                print("\n \nERROR IN CHILD PROCESS:\n")               
                print(recv["BREAK"])
                print(recv['TB'])
                raise recv["BREAK"]
                
                
            
            #Decide how to store result with Pandas
            if self.load == 'pandas':
                if "pandas_to_data" in message:
                    if message['pandas_to_data'] in [
                        'append', 'concat', 'overwrite', 'none',]:
                        pass
                    
                elif self.opts.pandas_to_data in [
                    'append', 'concat', 'overwrite', 'none',]:
                    
                    message['pandas_to_data'] = self.opts.pandas_to_data
                else:
                    raise ValueError(
        "To store data with pandas you must define "             
        "the pandas_to_data option or pass it to your UDF "
        "\nSupports: 'none', 'append', 'concat', 'merge' and 'overwrite'"
                                    )
                
                if message['pandas_to_data'] == 'none':
                    pass
                if message['pandas_to_data'] == 'append':
                    if "pandas_to_data_args" in message:
                        pandas_to_data_args = message['pandas_to_data_args']
                        self.data.append(recv,
                                         **pandas_to_data_args)
                    else:
                        self.data.append(recv)
                if message['pandas_to_data'] == 'concat':
                    if "pandas_to_data_args" in message:
                        pandas_to_data_args = message['pandas_to_data_args']
                        self.data.concat(recv,
                                         **pandas_to_data_args)
                    else:
                        self.data.concat(recv)
                if message['pandas_to_data'] == 'merge':
                    if "pandas_to_data_args" in message:
                        pandas_to_data_args = message['pandas_to_data_args']
                        self.data.append(recv,
                                         **pandas_to_data_args)
                    else:
                        raise ValueError(
                        "You must define pandas_to_data_args "
                            "with the merge option"
                        )
                if message['pandas_to_data'] == 'overwrite':
                    self.data = recv
            
           
            
            #Not yet implemented
            if self.load == 'postgreSQL':
                raise ValueError("postgreSQL is not currently supported")
            
            #Not yet implemented
            if self.load == 'SQLite':
                raise ValueError("SQLite is not currently supported")

            
            
            #Join the process and move on
            
            
            if self.opts.loud:
                print(
                    'Scheduled function completed, {} remaining.'.format(
                        len(sched_copy)))
    
    #TODO: build this out if needed
    def _stack_local_data(self, filepath, filetype=None):
        
        if not os.path.exists(filepath):
            raise FileNotFoundError(
            "File {} does not exist.".format(filepath)
            )
        
        if self.wg.__name__ == 'pandas':
            pass
        
        if self.wg.__name__ == 'dask':
            pass
    
    
    def chunker(self, chunks=None, chunk_args=None):
        """Method for telling the scheduler which data to use
        up the data."""
        
        
        
        #Ensure chunks is assigned and valid
        if not chunks:
            if type(self.opts.chunk).__name__ in ['list', 'tuple']:
                chunks = [i for i in self.opts.chunk]
            elif type(self.opts.chunk).__name__ == 'str':
                chunks = self.opts.chunk
        if type(chunks).__name__ not in ['list', 'tuple', 'str']: 
            raise ValueError(
                "chunks must be list, tuple or str, not {}".format(
                type(chunks).__name__))

        while len(chunks)>0:

            if self.opts.loud == True:
                print("\nMoving to next chunk: "
                      "\n{} chunks remaining\n".format(len(chunks)))
                
            self.scheduler(chunk=chunks.pop())
            
        