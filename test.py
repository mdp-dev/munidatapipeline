#Testing
import munidatapipeline as mdp
from core.prefab import err_to_parent
import pandas as pd


tst = mdp.muni_data_pipe()
tst.opts.load = 'pandas'
tst.opts.pandas_to_data = 'overwrite'
tst.opts.loud = False
tst.opts.chunk = ['a', 'b', 'c']

chunklist = [i for i in tst.opts.chunk]
while chunklist:

    i = {'a': [a for a in range(10)], 'b': [b for b in range(10, 20)],
        'c': ['dog', 'cat', 'spam', 'egg', 'dog', 
              'cat', 'spam', 'egg', 'dog', 'spam']}

    tst.data = pd.DataFrame(i)

    @err_to_parent
    def grouping(connection, load, message):

        load = load.groupby(message['chunk']).sum()
        load.to_csv('./grouped_by_' + message['chunk'] + '.csv')
        connection.send("nada")


    tst.opts.schedule = [[grouping, {'pandas_to_data':'none'}],
                        ]


    current = chunklist.pop()
    tst.scheduler(chunk=current)
    
test_frames = pd.read_csv('grouped_by_c.csv')
assert list(test_frames['b']) == [26, 42, 30, 47]

print('Passing')
