import pandas as pd

def mean_step(file):
    tags_dict = {}
    df = pd.read_csv(file, sep=";")
    df_tags = df.groupby('tags').mean()["n_steps"]
    df = df.dropna()
    df_tags = df_tags.dropna()
    for tag in df["tags"]:
        if tag not in tags_dict:
            tags_dict[tag] = df_tags[tag]
    return tags_dict
