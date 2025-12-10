# commands/math_tools.py 
def calculate(text):
    expr = text.replace("calculate", "").strip()
    try:
        result = eval(expr)
        return f"The answer is {result}, sir."
    except:
        return "I could not compute that expression, sir."
