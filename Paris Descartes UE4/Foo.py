from bokeh.client import push_session
from bokeh.layouts import column, row
from bokeh.models import Toggle
from bokeh.plotting import figure, curdoc
import numpy as np
# Create an arbitrary figure
p1 = figure(name = 'plot1')

# Create sin and cos data
x = np.linspace(0, 4*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create two plots
r1 = p1.circle(x,y1)

# Create the toggle button
toggle = Toggle(label = 'Add Graph',active=False)

mainLayout = column(row(toggle,name='Widgets'),p1,name='mainLayout')
curdoc().add_root(mainLayout)
# Callback which either adds or removes a plot depending on whether the toggle is active
def toggleCallback(attr):
    # Get the layout object added to the documents root
    rootLayout = curdoc().get_model_by_name('mainLayout')
    listOfSubLayouts = rootLayout.children

    # Either add or remove the second graph
    if  toggle.active == False:
        plotToRemove = curdoc().get_model_by_name('plot2')
        listOfSubLayouts.remove(plotToRemove)

    if toggle.active == True:
        if not curdoc().get_model_by_name('plot2'):
            p2 = figure(name='plot2')
            plotToAdd = p2
            p2.line(x,y2)
            # print('Remade plot 2')
        else:
            plotToAdd = curdoc().get_model_by_name('plot2')
        listOfSubLayouts.append(plotToAdd)

# Set the callback for the toggle button
toggle.on_click(toggleCallback)
