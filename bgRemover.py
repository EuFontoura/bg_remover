import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
from rembg import remove
from PIL import Image, ImageTk
import io, os, threading, time

def remover_fundo(imagem_path, progress_bar, progress_label):
    try:
        progress_bar['value'] = 0
        progress_label.config(text="Processando...")

        print(f"Removendo fundo da imagem: {imagem_path}")

        with open(imagem_path, 'rb') as input_file:
            input_data = input_file.read()

        # Simulando o progresso do processo (só simulando mesmo porque exibir o progresso real daria um trabalho do cão)
        progress_bar['maximum'] = 100
        for i in range(101):
            progress_bar['value'] = i
            progress_label.config(text=f"Processando... Não feche essa janela {i}%")
            progress_bar.update()
            time.sleep(0.05)

        output_data = remove(input_data)
        
        output_image = Image.open(io.BytesIO(output_data))

        messagebox.showinfo("Processamento Concluído", "Fundo da imagem removido com sucesso! Agora, selecione onde salvar")

        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("All files", "*.*")])

        if output_path:
            output_image.save(output_path)
            messagebox.showinfo("Sucesso", f"Imagem salva em: {output_path}")
        else:
            messagebox.showwarning("Aviso", "A imagem não foi salva!")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao remover o fundo: {str(e)}")

def selecionar_arquivo(progress_bar, progress_label):
    file_path = filedialog.askopenfilename(filetypes=[("Imagem", "*.png;*.jpg;*.jpeg")])
    if file_path:
        messagebox.showinfo("Imagem Carregada", f"Imagem {file_path} carregada com sucesso!")
        threading.Thread(target=remover_fundo, args=(file_path, progress_bar, progress_label)).start()

def on_drop(event, progress_bar, progress_label):
    file_path = event.data.strip('{}') 
    print(f"Arquivo solto: {file_path}")
    
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        messagebox.showinfo("Imagem Carregada", f"Imagem {file_path} carregada com sucesso!")
        threading.Thread(target=remover_fundo, args=(file_path, progress_bar, progress_label)).start()
    else:
        messagebox.showerror("Erro", "Por favor, solte uma imagem válida (.png, .jpg, .jpeg).")

root = TkinterDnD.Tk()

root.title("Removedor de Fundo de Imagem")
root.geometry("500x400")

label = tk.Label(root, text="Arraste uma imagem aqui ou clique para selecionar", pady=20)
label.pack()

progress_bar = tk.ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

progress_label = tk.Label(root, text="Aguardando...")
progress_label.pack()

botao_selecionar = tk.Button(root, text="Selecionar Imagem", command=lambda: selecionar_arquivo(progress_bar, progress_label))
botao_selecionar.pack(pady=10)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', lambda event: on_drop(event, progress_bar, progress_label))

root.mainloop()
