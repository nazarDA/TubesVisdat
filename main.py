import pandas as pd
import numpy as np
from os.path import dirname, join

from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

from scripts.line import lineline
from scripts.line2 import line_death
from scripts.dot import dotdot
from scripts.vbar import verticalbar

df = pd.read_csv(join(dirname(__file__), 'data', 'copid.csv'), 
	                                          index_col=0)
mask = (df['date'] >= '2021-01-01') & (df['date'] <= '2021-12-31')
df_use = df.loc[mask]
df_use = df_use.reset_index(drop=True)
df_use['date'] = pd.to_datetime(df_use['date'])

tab1 = lineline(df_use)
tab2 = line_death(df_use)
tab3 = dotdot(df_use)
tab4 = verticalbar(df_use)

tabs = Tabs(tabs = [tab1, tab2, tab3, tab4])

curdoc().add_root(tabs)
