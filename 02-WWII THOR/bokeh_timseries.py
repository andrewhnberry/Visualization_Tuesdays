# This time we will look into how to handle timeseries data

#Import pandas so we can interact with the csv file "thor_wwii.csv"
import pandas as pd

#first we need to initiate the bokeh
from bokeh.plotting import figure, output_file, show

from bokeh.models import ColumnDataSource


from bokeh.palettes import Spectral5

output_file('timeseries_graph.html')


df = pd.read_csv('thor_wwii.csv')


df['MSNDATE'] = pd.to_datetime(df['MSNDATE'], format ='%m/%d/%Y')


grouped = df.groupby(pd.Grouper(key='MSNDATE', freq='M'))['TOTAL_TONS', 'TONS_IC', 'TONS_FRAG'].sum()
grouped = grouped/1000

source = ColumnDataSource(grouped)

# we need to pass through this x_axis_type as date time so they know its a date
p = figure(x_axis_type = 'datetime')

p.line(x="MSNDATE", y= 'TOTAL_TONS', line_width = 2, source =source, legend = 'ALL MUNITIONS')
p.line(x='MSNDATE', y='TONS_FRAG', line_width=2, source=source, color=Spectral5[1], legend='FRAGMENTATION')
p.line(x='MSNDATE', y='TONS_IC', line_width=2, source=source, color=Spectral5[2], legend='INCENDIARY')

p.yaxis.axis_label = 'KILOTONS OF MUNITIONS DROPPED'

show(p)
