import gradio as gr

'''
在 Gradio 的官方實例 ToyCalculator 中，實現了一個簡易的計算器
基於此，你暫時還不需要瞭解到 Gradio 中這些高級抽象的 class, 但是你需要為這個計算器添加一些額外的功能

'''


def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise gr.Error("Cannot divide by zero!")
        return num1 / num2
    elif operation == "modulus":
        # &&&
        pass
    elif operation == "exp":
        # &&&
        pass
    elif operation == "less":
        if num1 < num2:
            return 1
        else:
            return 0
    elif operation == "leq":
        pass

demo = gr.Interface(
    calculator,
    [
        "number", 
        # gr.Radio(["add", "subtract", "multiply", "divide"),       # 原始語句
        gr.Radio(["add", "subtract", "multiply", "divide", "modulus", "exp", "less", "leq", ]),     # 添加功能后的語句
        "number"
    ],
    "number",
    examples=[
        [5, "add", 3],
        [4, "divide", 2],
        [-4, "multiply", 2.5],
        [0, "subtract", 1.2],
    ],
    title="Toy Calculator",
    description="Here's a sample toy calculator. Allows you to calculate things like $2+2=4$",
)
demo.launch()