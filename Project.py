import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Entry Widget
        self.entry = tk.Entry(master, width=30, borderwidth=5, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button colors
        btn_bg = '#f0f0f0'  # light gray
        btn_fg = '#000000'  # black
        btn_active_bg = '#e0e0e0'  # lighter gray

        # Button configuration
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('<-', 5, 3)
        ]

        # Create buttons
        for (text, row, col) in buttons:
            btn = tk.Button(master, text=text, width=5, height=2, font=('Arial', 14),
                            bg=btn_bg, fg=btn_fg, activebackground=btn_active_bg,
                            command=lambda t=text: self.button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, value):
        current = self.entry.get()

        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == '<-':
            self.entry.delete(len(current) - 1)
        else:
            self.entry.insert(tk.END, value)

def main():
    root = tk.Tk()
    root.config(bg='#ffffff')  # white background
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
 