import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class CodeEditorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Code Editor")
        self.geometry("800x600")

        # Set darker background color
        self.configure(bg="#1e1e1e")

        self.textarea = scrolledtext.ScrolledText(self, wrap=tk.WORD, undo=True, bg="#2e2e2e", fg="white")  # Adjust background and foreground color
        self.textarea.pack(expand=True, fill=tk.BOTH)

        self.folder_panel = tk.Frame(self, bg="#333333", width=200)  # Folder panel
        self.folder_panel.pack(side=tk.LEFT, fill=tk.Y)

        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.textarea.delete(1.0, tk.END)
                self.textarea.insert(tk.END, content)

    def save_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            with open(file_path, 'w') as file:
                content = self.textarea.get(1.0, tk.END)
                file.write(content)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_as_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            with open(file_path, 'w') as file:
                content = self.textarea.get(1.0, tk.END)
                file.write(content)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def exit_app(self):
        if messagebox.askyesno("Exit", "Do you want to exit?"):
            self.destroy()

def main():
    app = CodeEditorApp()
    app.mainloop()

if __name__ == "__main__":
    main()
