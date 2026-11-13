import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

def p_f(s):
    x = np.linspace(-10, 10, 400)
    y = eval(s, {"x": x, "np": np})

    fig, ax = plt.subplots()
    ax.plot(x, y)
    return fig

gr.Interface(p_f, gr.Textbox(), gr.Plot()).launch()
