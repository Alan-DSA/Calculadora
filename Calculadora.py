import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        # Criação do Display
        self.display = tk.Entry(master, width=30, justify='right', font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Criação dos botões
        button_list = [
            '7', '8', '9', '/', 'AC',
            '4', '5', '6', '*', 'C',
            '1', '2', '3', '-', '+',
            '0', '.', '='
        ]
        r = 1
        c = 0
        for b in button_list:
            if b == '=':
                tk.Button(master, text=b, width=10, height=2, command=lambda: self.calculate()).grid(row=r, column=c, columnspan=2, rowspan=2, padx=5, pady=5)
            elif b == 'C':
                tk.Button(master, text=b, width=5, height=2, command=lambda: self.clear_entry()).grid(row=r, column=c, padx=5, pady=5)
            elif b == 'AC':
                tk.Button(master, text=b, width=5, height=2, command=lambda: self.clear_all()).grid(row=r, column=c, padx=5, pady=5)
            else:
                tk.Button(master, text=b, width=5, height=2, command=lambda value=b: self.append(value)).grid(row=r, column=c, padx=5, pady=5)
            c += 1
            if c > 4:
                c = 0
                r += 1

    def append(self, value):
        self.display.insert(tk.END, value)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erro")

    def clear_entry(self):
        self.display.delete(len(self.display.get())-1)

    def clear_all(self):
        self.display.delete(0, tk.END)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
