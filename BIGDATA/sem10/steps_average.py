
import pandas as pd

def avr_steps(file):
    df = pd.read_csv(file, sep=";")
    grouper = df.groupby(['tag'])
    df = grouper['n_steps'].mean().to_frame(name = 'mean_steps')
    return df.to_dict()
