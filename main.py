import customtkinter as ctk
import os
import shutil
import windnd  # Biblioteca para Drag & Drop no Windows
from tkinter import messagebox

class OrganizadorPastas(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Organizador de fotos - Arrastar e Soltar")
        self.geometry("600x550")
        self.arquivos_selecionados = []

        # Título
        self.label = ctk.CTkLabel(self, text="Organizador de Fotos", font=("Roboto", 24, "bold"))
        self.label.pack(pady=(20, 10))

        # Nome do Lote
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Ex: Lote 01 - Corolla", width=450, height=45)
        self.entry_nome.pack(pady=15)

        # Caixa de Visualização
        self.caixa_drop = ctk.CTkTextbox(self, width=500, height=200, border_width=2, border_color="#1f538d")
        self.caixa_drop.pack(pady=10)
        self.caixa_drop.insert("0.0", "ARRASTE AS FOTOS DO WINDOWS PARA QUALQUER LUGAR DA JANELA...")
        self.caixa_drop.configure(state="disabled")

        # Botões
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=20)

        self.btn_limpar = ctk.CTkButton(self.btn_frame, text="Limpar", fg_color="#A12D2D", command=self.limpar)
        self.btn_limpar.pack(side="left", padx=10)

        self.btn_ok = ctk.CTkButton(self.btn_frame, text="Organizar Pastas", fg_color="#2DA14F", command=self.processar)
        self.btn_ok.pack(side="left", padx=10)

        # Registrar o Drag & Drop (Versão simplificada sem nomes de argumentos problemáticos)
        windnd.hook_dropfiles(self, self.ao_soltar)

    def ao_soltar(self, files):
        # Converte bytes para string e limpa caminhos
        novos = []
        extensoes_validas = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')
        
        for f in files:
            caminho = f.decode('ansi')
            if caminho.lower().endswith(extensoes_validas):
                novos.append(caminho)

        if novos:
            self.arquivos_selecionados.extend(novos)
            self.caixa_drop.configure(state="normal")
            self.caixa_drop.delete("0.0", "end")
            for f in self.arquivos_selecionados:
                self.caixa_drop.insert("end", f"✔ {os.path.basename(f)}\n")
            self.caixa_drop.configure(state="disabled")
        else:
            messagebox.showwarning("Aviso", "Arraste apenas arquivos de imagem!")

    def limpar(self):
        self.arquivos_selecionados = []
        self.caixa_drop.configure(state="normal")
        self.caixa_drop.delete("0.0", "end")
        self.caixa_drop.insert("0.0", "ARRASTE AS FOTOS PARA CÁ...")
        self.caixa_drop.configure(state="disabled")

    import sys # Adicione isso no topo do arquivo

    def processar(self):
        nome = self.entry_nome.get().strip()
        if not nome or not self.arquivos_selecionados:
            messagebox.showwarning("Erro", "Preencha o nome do lote e arraste as fotos!")
            return

        # ESTA LINHA É A CHAVE: Pega a pasta onde o .exe está de verdade
        caminho_do_exe = os.path.dirname(sys.executable)
        
        # Criamos a pasta LOTES_PRONTOS lá
        pasta_lotes = os.path.join(caminho_do_exe, "LOTES_PRONTOS", nome)
        
        try:
            os.makedirs(pasta_lotes, exist_ok=True)
            for i, caminho_origem in enumerate(self.arquivos_selecionados, 1):
                ext = os.path.splitext(caminho_origem)[1]
                novo_nome = f"{nome}_{i}{ext}"
                destino = os.path.join(pasta_lotes, novo_nome)
                shutil.copy2(caminho_origem, destino)

            messagebox.showinfo("Sucesso!", f"Lote organizado!\nSalvo em: {pasta_lotes}")
            self.limpar()
            self.entry_nome.delete(0, 'end')
        except Exception as e:
            messagebox.showerror("Erro", f"Erro: {e}")

if __name__ == "__main__":
    app = OrganizadorPastas()
    app.mainloop()