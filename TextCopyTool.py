import tkinter as tk
from tkinter import simpledialog, messagebox

def create_window(width=200, height=80):
    window_name = simpledialog.askstring("Новое окно", "Введите название окна:")
    if window_name:
        text = simpledialog.askstring("Новое окно", "Введите текст для окна:", show='')

        if text:
            window = tk.Toplevel(root)
            window.title(window_name)
            window.geometry(f"{width}x{height}")
            window.attributes("-topmost", True)

            text_label = tk.Label(window, text=text[:50] + "..." if len(text) > 50 else text)
            text_label.pack(padx=10, pady=10)

            def copy_text():
                root.clipboard_clear()
                root.clipboard_append(text)
                root.update()

            copy_button = tk.Button(window, text="Копировать текст", command=copy_text)
            copy_button.pack(pady=10)

            windows_list.insert(tk.END, f"{len(windows) + 1}. {window_name}")
            windows.append((window_name, text, window, text_label, copy_button))

def update_window_list():
    windows_list.delete(0, tk.END)
    for i, (window_name, text, _, _, _) in enumerate(windows, start=1):
        windows_list.insert(tk.END, f"{i}. {window_name}")

def show_selected_window(event):
    selected_index = windows_list.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        window_name, text, _, _, _ = windows[selected_index - 1]
        messagebox.showinfo(window_name, text)

def delete_window(index):
    window_name, _, window, text_label, copy_button = windows.pop(index)
    window.destroy()
    text_label.destroy()
    copy_button.destroy()
    update_window_list()

def delete_selected_window(event):
    selected_index = windows_list.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        delete_window(selected_index - 1)

def main():
    global root, windows, windows_list

    root = tk.Tk()
    root.title("TextCopyTool")

    windows = []

    windows_list = tk.Listbox(root, selectmode=tk.SINGLE)
    windows_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    windows_list.bind("<ButtonRelease-1>", show_selected_window)

    add_button = tk.Button(root, text="Добавить новое окно", command=create_window)
    add_button.pack(side=tk.TOP, padx=10, pady=10)

    delete_button = tk.Button(root, text="Удалить выбранное окно", command=delete_selected_window)
    delete_button.pack(side=tk.TOP, padx=10, pady=10)

    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()

if __name__ == "__main__":
    main()
