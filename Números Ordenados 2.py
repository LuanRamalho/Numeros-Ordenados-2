import tkinter as tk
from tkinter import messagebox, scrolledtext

class NumberSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Número Sorter")
        self.root.geometry("400x400")
        self.root.configure(bg="#E0FFFF")

        # Lista para armazenar os números
        self.numbers = []

        # Título
        title_label = tk.Label(self.root, text="Adicione Números", font=("Arial", 18), bg="#E0FFFF")
        title_label.pack(pady=10)

        # Entrada para números
        self.entry = tk.Entry(self.root, font=("Arial", 14), width=10, bg="#ffffff", bd=2)
        self.entry.pack(pady=10)

        # Botão para adicionar número
        add_button = tk.Button(self.root, text="Adicionar Número", command=self.add_number, bg="#4CAF50", fg="#ffffff", font=("Arial", 12))
        add_button.pack(pady=5)

        # Botões para ordenar
        sort_asc_button = tk.Button(self.root, text="Ordenar Crescente", command=self.sort_ascending, bg="#2196F3", fg="#ffffff", font=("Arial", 12))
        sort_asc_button.pack(pady=5)

        sort_desc_button = tk.Button(self.root, text="Ordenar Decrescente", command=self.sort_descending, bg="#f44336", fg="#ffffff", font=("Arial", 12))
        sort_desc_button.pack(pady=5)

        # Botão para excluir número
        delete_button = tk.Button(self.root, text="Excluir Selecionado", command=self.delete_selected, bg="#FF5722", fg="#ffffff", font=("Arial", 12))
        delete_button.pack(pady=5)

        # Listbox para mostrar os números
        self.listbox = tk.Listbox(self.root, font=("Arial", 12), width=25, height=10, bg="#ffffff", bd=2)
        self.listbox.pack(pady=10)

    def add_number(self):
        """Adiciona um número à lista e atualiza a Listbox."""
        try:
            number = float(self.entry.get())
            self.numbers.append(number)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

    def update_listbox(self):
        """Atualiza a Listbox com os números atuais."""
        self.listbox.delete(0, tk.END)
        for number in self.numbers:
            self.listbox.insert(tk.END, number)

    def sort_ascending(self):
        """Ordena os números em ordem crescente e atualiza a Listbox."""
        self.numbers.sort()
        self.update_listbox()

    def sort_descending(self):
        """Ordena os números em ordem decrescente e atualiza a Listbox."""
        self.numbers.sort(reverse=True)
        self.update_listbox()

    def delete_selected(self):
        """Exclui o número selecionado da lista."""
        try:
            selected_index = self.listbox.curselection()[0]
            del self.numbers[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showerror("Erro", "Nenhum número foi selecionado para exclusão.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberSorterApp(root)
    root.mainloop()
