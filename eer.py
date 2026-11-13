import numpy as np
import pandas as pd
import gradio as gr
def p_f(s):
    x=np.linspace(-10,10,400)
    y=eval(s,{"x":x,"np":np})
    return gr.LinePlot({"x":x,"y":y},x="x",y="y")
gr.Interface(p_f,gr.Textbox(),gr.LinePlot()).launch()
