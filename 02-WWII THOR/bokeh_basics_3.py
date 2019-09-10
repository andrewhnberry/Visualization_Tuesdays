# Basics of Bokeh for Visualization_Tuesdays
# python 3.7

#Import pandas so we can interact with the csv file "thor_wwii.csv"
import pandas as pd

#first we need to initiate the bokeh
from bokeh.plotting import figure, output_file, show

# ColumnDataSource is the bokeh object that interacts with pandas Dataframes
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool


from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap

output_file('third_graph.html')

df = pd.read_csv('thor_wwii.csv')

grouped = df.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS', 'TONS_HE', 'TONS_IC', 'TONS_FRAG'].sum()

grouped = grouped / 1000

source = ColumnDataSource(grouped)
countries = source.data['COUNTRY_FLYING_MISSION'].tolist()


p = figure(x_range = countries)

color_map = factor_cmap(field_name='COUNTRY_FLYING_MISSION',
                        palette = Spectral5, factors = countries)

p.vbar(x='COUNTRY_FLYING_MISSION', top = "TOTAL_TONS",
        source = source, width = 0.5, color = color_map)

p.title.text =' Munitions Dropped by Allied Country'
p.xaxis.axis_label =  'Country'
p.yaxis.axis_label =  'Kilotons of Munitions'


hover = HoverTool()
hover.tooltips = [
                ("Totals","@TONS_HE High Explosvie / @TONS_IC Incendiary / @TONS_FRAG Fragmentation")
                ]
hover.mode = 'vline'
p.add_tools(hover)

show(p)
