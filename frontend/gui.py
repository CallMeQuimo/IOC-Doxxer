import tkinter as tk
from tkinter import ttk, messagebox
from backend.functions import validIOC, trimURL, opVT, opIPBD

def centrarGUI(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f'+{x}+{y}')


def launch_gui():
    root = tk.Tk()
    root.title("IOC-Doxxer! [v0.3]")
    root.minsize(350, 150)               # Ajuste manual del ancho para que entre cómodo
    centrarGUI(root)

    ##Checkboxes
    tools_frame = ttk.Frame(root, padding=10)
    tools_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

    vt = tk.BooleanVar(value=True)
    ipbd = tk.BooleanVar(value=True)
    checkPlaceholder = tk.BooleanVar(value=False)

    #Columna izquierda
    ttk.Checkbutton(tools_frame, text="VirusTotal", variable=vt).grid(row=0, column=0, sticky="w", padx=5, pady=2)
    ttk.Checkbutton(tools_frame, text="AbuseIPDB", variable=ipbd).grid(row=1, column=0, sticky="w", padx=5, pady=2)
    ttk.Checkbutton(tools_frame, text="Placeholder", variable=checkPlaceholder).grid(row=2, column=0, sticky="w", padx=5, pady=2)
    #Columna derecha
    ttk.Checkbutton(tools_frame, text="Placeholder", variable=checkPlaceholder).grid(row=0, column=1, sticky="w", padx=5, pady=2)
    ttk.Checkbutton(tools_frame, text="Placeholder", variable=checkPlaceholder).grid(row=1, column=1, sticky="w", padx=5, pady=2)
    ttk.Checkbutton(tools_frame, text="Placeholder", variable=checkPlaceholder).grid(row=2, column=1, sticky="w", padx=5, pady=2)

    ##Entrada + Botón
    input_frame = ttk.Frame(root, padding=(0,10))
    input_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

    #Variable y placeholder
    ioc = tk.StringVar()
    placeholder = "Ingrese IP o URL... (sin ofuscar)"
    ioc.set(placeholder)

    #Entry
    entry = ttk.Entry(input_frame, textvariable=ioc, width=30, foreground="gray")
    entry.grid(row=0, column=0, sticky="ew", padx=(10,5))
    input_frame.columnconfigure(0, weight=1)  #Hace el entry expandible

    def clear_placeholder(event):
        if ioc.get() == placeholder:
            ioc.set("")
            entry.config(foreground="black")

    def restore_placeholder(event):
        if not ioc.get():
            ioc.set(placeholder)
            entry.config(foreground="gray")

    entry.bind("<FocusIn>", clear_placeholder)
    entry.bind("<FocusOut>", restore_placeholder)

    # Botón
    btn = ttk.Button(input_frame, text="Abrir páginas", command=lambda: submitIOC(ioc, vt, ipbd))
    btn.grid(row=0, column=1, padx=(5,10))

    def submitIOC(ioc, vt_var, ipbd_var):
        raw = ioc.get().strip().lower()
        if raw == "" or raw == placeholder.lower():
            messagebox.showerror("Error", "El campo de IOC no puede estar vacío.")
            return
        if not validIOC(raw):
            messagebox.showerror("Error", "IOC ilegible.")
            return

        clean = trimURL(raw)
        if vt_var.get():
            opVT(clean)
        if ipbd_var.get():
            opIPBD(clean)

        messagebox.showinfo("Hecho", f"Se abrieron las pestañas para: {clean}")

    root.mainloop()