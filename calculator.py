from fastmcp import FastMCP
from typing import Union
import math

mcp = FastMCP("calculator")

@mcp.tool()
def calculate(a: float, b: float, operation: str = "add") -> float:
    """Basit hesaplama yapar
    
    Args:
        a: İlk sayı
        b: İkinci sayı
        operation: İşlem türü (add, subtract, multiply, divide, power)
    """
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else None,
        "power": lambda x, y: x ** y
    }
    
    if operation not in operations:
        raise ValueError(f"Desteklenmeyen işlem: {operation}")
    
    result = operations[operation](a, b)
    if result is None:
        raise ValueError("Sıfıra bölme hatası!")
    
    return result


@mcp.tool()
def advanced_math(number: float, function: str) -> float:
    """Gelişmiş matematik fonksiyonları
    
    Args:
        number: İşlem yapılacak sayı
        function: Fonksiyon adı (sqrt, log, sin, cos, tan, abs)
    """
    functions = {
        "sqrt": math.sqrt,
        "log": math.log,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "abs": abs
    }
    
    if function not in functions:
        raise ValueError(f"Desteklenmeyen fonksiyon: {function}")
    
    return functions[function](number)

if __name__ == "__main__":
    mcp.run()