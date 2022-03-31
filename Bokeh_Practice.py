import bokeh as bk
from bokeh.plotting import figure, output_file, show

x = [1,2,3,4,5]
y = [4,6,2,4,3]

output_file('index.html')

#add our plot
p = figure(
   title='Simple Example',
   x_axis_label='X Axis',
   y_axis_label='Y Axis'
)

#render glphh
p.line(x, y, legend ='Test', line_width=2)

# Show results
show(p)

