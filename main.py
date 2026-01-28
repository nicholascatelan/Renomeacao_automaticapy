import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import shutil

# Configuração visual
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Organizador de Lotes - Leilão")
        self.geometry("500x350")

        # Interface
        self.label = ctk.CTkLabel(self, text="Organizador de Fotos", font=("Roboto", 24))
        self.label.pack(pady=20)

        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome do Lote (Ex: Lote 001)", width=300)
        self.entry_nome.pack(pady=10)

        self.btn_selecionar = ctk.CTkButton(self, text="Selecionar Fotos e Organizar", command=self.processar)
        self.btn_selecionar.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="Aguardando ação...", font=("Roboto", 12))
        self.status_label.pack(side="bottom", pady=10)

    def processar(self):
        nome_lote = self.entry_nome.get().strip()
        
        if not nome_lote:
            messagebox.showwarning("Aviso", "Por favor, digite o nome do lote primeiro!")
            return

        # Abre seletor de arquivos
        arquivos = filedialog.askopenfilenames(
            title=f"Selecione as fotos para o {nome_lote}",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.webp")]
        )

        if not arquivos:
            return

        try:
            # Define o local de destino (onde o programa está rodando)
            pasta_destino = os.path.join(os.getcwd(), nome_lote)
            
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            for i, caminho_original in enumerate(arquivos, 1):
                extensao = os.path.splitext(caminho_original)[1]
                # Novo nome: Lote 001_1.jpg, Lote 001_2.jpg...
                novo_nome = f"{nome_lote}_{i}{extensao}"
                destino_final = os.path.join(pasta_destino, novo_nome)
                
                # Copia o arquivo (melhor que mover para evitar perdas se algo der erro)
                shutil.copy2(caminho_original, destino_final)

            messagebox.showinfo("Sucesso!", f"Lote criado com sucesso!\n{len(arquivos)} fotos organizadas na pasta '{nome_lote}'.")
            self.entry_nome.delete(0, 'end')
            self.status_label.configure(text=f"Última ação: {nome_lote} finalizado.")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    app = App()
    app.mainloop()