# Basics of Bokeh for Visualization_Tuesdays
# python 3.7

#first we need to initiate the bokeh
from bokeh.plotting import figure, output_file, show

# figure handles the stylitic features of the plot
# output_file handles the type of file we output, generally it is html
# output_notebook allows us to do it in Jupyter Notebooks
# show means bokeh will now render it

output_file('first_graph.html')

x = [1,3,5,7]
y = [2,4,6,8]

#initate the graph
p = figure()

# Stylistic features on the graph
p.circle(x,y, size = 10, color = 'red', legend ='circle')
p.line(x,y, color = 'blue', legend ='line')
p.triangle(y,x, color = 'gold', size = 10, legend = 'triangle')

#Interactive Bits
#click_policy will allow us to interact with the legend to hide
# or show various data points we got
p.legend.click_policy = 'hide'

show(p)
