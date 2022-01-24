import pandas as pd
from multiprocessing import Process, Queue, current_process, freeze_support
from multiprocessing import Process, Queue, current_process, freeze_support

def avr_steps(file):
    df = pd.read_csv(file, sep=";")
    grouper = df.groupby(['tag'])
    df = grouper['n_steps'].mean().to_frame(name = 'mean_steps')
    return df.to_dict()

def worker(input_, output):
    for file in iter(input_.get, 'STOP'):
        result = avr_steps(file)
        output.put(result)
