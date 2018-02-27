wrangler                 = 'pandas'


filepath                 = './data'

#Filepath used by downloading_funcs.py
downloads_folder         = './data'

#List of tuples in the form (callable, dict)
schedule                 = []

#Chunking indexes
chunk                    = []
chunkstype               = None
pandas_to_data           = None

#Threads timeout? arg of multiprocessing.join
timeouts                 = None #None or int

#Verbose execution?
loud                     = False