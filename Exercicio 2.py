import tkinter as tk

def is_fibonacci(number):
    """Verifica se um número pertence à sequência de Fibonacci"""
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number

def calculate_fibonacci_sequence(number):
    """Calcula a sequência de Fibonacci até um determinado número"""
    a, b = 0, 1
    fibonacci_sequence = [a]
    while b <= number:
        fibonacci_sequence.append(b)
        a, b = b, a + b
    return fibonacci_sequence

def check_fibonacci():
    """Verifica se o número pertence à sequência de Fibonacci e exibe uma mensagem"""
    number = int(entry.get())
    fibonacci_sequence = calculate_fibonacci_sequence(number)
    if number in fibonacci_sequence:
        result_label.config(text=f"O número {number} pertence à sequência de Fibonacci.")
        result_label.after(2000, lambda: result_label.config(text=""))
    else:
        result_label.config(text=f"O número {number} não pertence à sequência de Fibonacci.")
        result_label.after(2000, lambda: result_label.config(text=""))

# Criar a janela principal
root = tk.Tk()
root.title("Verificador da Sequência de Fibonacci")

# Criar os widgets
number_label = tk.Label(root, text="Digite um número:")
entry = tk.Entry(root)
check_button = tk.Button(root, text="Verificar", command=check_fibonacci)
result_label = tk.Label(root, text="")

# Posicionar os widgets na janela
number_label.pack()
entry.pack()
check_button.pack()
result_label.pack()

# Iniciar o loop principal da janela
root.mainloop()
