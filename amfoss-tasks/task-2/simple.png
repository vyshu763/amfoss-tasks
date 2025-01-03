def evaluate_expression(expression):
    """Evaluates a simple arithmetic expression.

    Args:
        expression: The arithmetic expression as a string.

    Returns:
        The result of the evaluation.
    """
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None

if _name_ == "_main_":
    expression = "2 + 2"  # Replace with your desired expression
    result = evaluate_expression(expression)
    if result is not None:
        print(f"Result of {expression}: {result}")
