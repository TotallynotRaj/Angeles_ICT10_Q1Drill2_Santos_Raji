from pyscript import document


def show_result(message, error=False):
    output = document.querySelector("#output")
    message_class = "result-message error" if error else "result-message"
    output.innerHTML = (
        f'<div class="result-title">Answer</div>'
        f'<p class="{message_class}">{message}</p>'
    )


def get_numbers():
    """Read both inputs and report invalid or missing values."""
    try:
        num1 = float(document.querySelector("#num1").value)
        num2 = float(document.querySelector("#num2").value)
    except (TypeError, ValueError):
        show_result("Please enter two valid numbers.", error=True)
        return None

    return num1, num2



def add(event):
    numbers = get_numbers()
    if numbers is None:
        return
    num1, num2 = numbers

    addition_result = num1 + num2

    show_result(f"Addition: {num1} + {num2} = {addition_result}")



def subtract(event):
    numbers = get_numbers()
    if numbers is None:
        return
    num1, num2 = numbers

    subtraction_result = num1 - num2

    show_result(f"Subtraction: {num1} - {num2} = {subtraction_result}")


def multiply(event):
    numbers = get_numbers()
    if numbers is None:
        return
    num1, num2 = numbers

    multiplication_result = num1 * num2

    show_result(f"Multiplication: {num1} × {num2} = {multiplication_result}")



def divide(event):
    numbers = get_numbers()
    if numbers is None:
        return
    num1, num2 = numbers

    if num2 == 0:
        division_result = "Cannot divide by zero"
    else:
        division_result = num1 / num2

    show_result(f"Division: {num1} ÷ {num2} = {division_result}",
        error=num2 == 0)
