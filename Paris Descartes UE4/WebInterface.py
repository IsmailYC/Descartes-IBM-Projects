# WebInterface.py

from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.io import output_file, show
from bokeh.events import ButtonClick
from bokeh.layouts import widgetbox, layout, row, column
from bokeh.models.widgets import Select, Panel, Tabs, Button, Div
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def patientSelectHandler(attr, old, new):
    patientInfo.text="""<br><h1>"""+patientSelect.value+"""</h1><br>
    <h2 style='display:inline'>Location: </h2><p style='display:inline; font-size:16px'>"""+dataFrameNameIndexed.loc[patientSelect.value,sheetColumns[3]]+"""</p>""";
    
dataFrame = pd.read_excel('Data/Lung3.metadata.xls', sheet_name='Lung3.metadata')
sheetColumns= dataFrame.columns;
dataFrameNameIndexed= dataFrame.set_index(sheetColumns[0]);
sampleSerie= dataFrame[sheetColumns[0]];
sampleList= sampleSerie.tolist();

patientSelect = Select(title="Patient:", value=sampleList[0], options=sampleList);
patientSelect.on_change("value", patientSelectHandler);
patientInfo = Div(text="""<br><h1>"""+patientSelect.value+"""</h1><br>
<h2 style='display:inline'>Location: </h2><p style='display:inline; font-size:16px'>"""+dataFrameNameIndexed.loc[patientSelect.value,sheetColumns[3]]+"""</p>
<h2 style='display:inline'>Location: </h2><p style='display:inline; font-size:16px'>"""+dataFrameNameIndexed.loc[patientSelect.value,sheetColumns[3]]+"""</p>""");
patientLayout = layout([[patientSelect,patientInfo]]);
patientTab= Panel(child=patientLayout, title="Patients");

categorySelect = Select(title="Category:", value="Table", options=["Table","Category"]);
generalLayout = layout([categorySelect]);
generalTab= Panel(child=generalLayout, title="General");
webInterfaceLayout=Tabs(tabs=[patientTab,generalTab]);

curdoc().add_root(webInterfaceLayout);
