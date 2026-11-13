import numpy as np
import gradio as gr
def p_f(s):
    x=np.linspace(-10,10,400)
    y=eval(s,{"x":x,"np":np})
    return gr.Plot({"x":x,"y":y},x="x",y="y")
gr.Interface(p_f,gr.Textbox(),gr.Plot()).launch()
