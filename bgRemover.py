from rembg import remove
from PIL import Image
import io
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

def remove_background():
    root = Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)

    messagebox.showinfo("Bem-vindo", "✨ Bem-vindo ao Removedor de Fundo!\nVamos começar escolhendo uma imagem.")

    input_path = askopenfilename(title="Selecione a imagem", filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])
    if not input_path:
        messagebox.showwarning("Aviso", "❌ Você não selecionou nenhuma imagem. Tente novamente.")
        return

    messagebox.showinfo("Salvar arquivo", "➡️ Agora escolha onde salvar a imagem sem fundo (lembre-se de nomear o arquivo).")
    output_path = asksaveasfilename(title="Salvar imagem como", defaultextension=".png",
                                    filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg;*.jpeg")])
    if not output_path:
        messagebox.showwarning("Aviso", "❌ Nenhum local de salvamento foi escolhido. Tente novamente.")
        return

    try:
        messagebox.showinfo("Processando", "⏳ Processando sua imagem. Isso pode levar alguns segundos...")

        with open(input_path, 'rb') as img_file:
            input_image = img_file.read()

        result = remove(input_image)

        result_image = Image.open(io.BytesIO(result))
        result_image.save(output_path)

        messagebox.showinfo("Sucesso", f"✅ Fundo removido com sucesso!\nSua imagem está salva em:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"❌ Ocorreu um erro ao processar a imagem:\n{e}")

remove_background()
