import ipywidgets as widgets

from ipywidgets import Button, Layout
from IPython.display import display

layout = Layout (width='50%', height='100px')

btn = Button(description = 'non-optimized geo information of restaurant', layout = btn.layout)
display(btn)

btn2 = Button(description = 'optimized geo information of restaurant', layout = btn.layout)

display(btn2)
