# Basics of Bokeh for Visualization_Tuesdays
# python 3.7

#Import pandas so we can interact with the csv file "thor_wwii.csv"
import pandas as pd

#first we need to initiate the bokeh
from bokeh.plotting import figure, output_file, show

# ColumnDataSource is the bokeh object that interacts with pandas Dataframes
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

output_file('second_graph.html')

df = pd.read_csv('thor_wwii.csv')

sample = df.sample(100) #returns a random sample of 50 rows of the DF
source = ColumnDataSource(sample)


p = figure()

#stylistic Works
p.circle(x='TOTAL_TONS', y = 'AC_ATTACKING',
            source = source,
            size =10,
            color = 'green')

p.title.text = 'Attacking Aircraft and Munitions Dropped'
p.xaxis.axis_label = 'Total Tons of Munitions Dropped'
p.yaxis.axis_label = '# of Attacking Aircrafts'

hover = HoverTool()
hover.tooltips = [
                ('Attack Date', '@MSNDATE'),
                ('Attacking Aircraft', '@AC_ATTACKING'),
                ('Tons of Munitions', '@TOTAL_TONS'),
                ('Type of Aircraft','@AIRCRAFT_NAME')
                ]


p.add_tools(hover)

show(p)
