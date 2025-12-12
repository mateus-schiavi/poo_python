import gradio as gr

def converter_temperatura(temperatura, escala):
    if escala == "Celsius":
        return (temperatura * 9/5) + 32
    elif escala == "Kelvin":
        return (temperatura + 273.15)
    elif escala == "Rankine":
        return (temperatura + 273.15) * 9/5
    else:
        return (temperatura - 32) * 5/9
    
iface = gr.Interface(
    fn=converter_temperatura,
    inputs=[
        gr.Number(label="Temperatura", precision=2),
        gr.Radio(
            choices=["Celsius", "Fahrenheit", "Kelvin", "Rankine"],
            label="Converter de"
        )
    ],
    outputs=gr.Number(label="Resultado"),
    title="Conversor de Temperatura",
    description="Converte temperaturas entre Celsius e Fahrenheit"
)

iface.launch()