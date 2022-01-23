import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

from plugins.filter_languages import filterLanguages

def filterPerLenguage(df, lang):
    df["index"] = df["year"]
    df = df[ df["name"] == lang ].groupby(["index"]).sum()
    df = df [ df["quarter"] == 10 ]
    df["year"] /= 4
    df['year'] = df['year'].astype('int')
    df = df.drop(["quarter"], axis=1)
    return df

def linearModel(data):
    model = smf.ols(formula = "count ~ year", data = data).fit()
    return model

def prediction(data, model):
    model_prediction = model.predict(pd.DataFrame(data['year']))
    # print(model_prediction)
    return model_prediction