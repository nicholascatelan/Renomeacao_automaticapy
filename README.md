🚀 Organizador de Lotes para Leilão
Um software desktop intuitivo desenvolvido para automatizar o processo braçal de renomeação e organização de fotos para leiloeiros. Com este programa, o que levava minutos de cliques repetitivos agora é feito em segundos através de Drag & Drop (Arrastar e Soltar).

✨ Funcionalidades
Arrastar e Soltar: Selecione centenas de fotos no Windows Explorer e solte-as diretamente na interface.

Renomeação Sequencial: Nomeia automaticamente os arquivos seguindo o padrão Nome_do_Lote_1.jpg, Nome_do_Lote_2.jpg, etc.

Auto-Organização: Cria automaticamente pastas individuais para cada lote, mantendo a estrutura de diretórios limpa.

Interface Moderna: Desenvolvida com CustomTkinter para uma experiência de usuário (UX) nativa e agradável.

Segurança de Dados: O sistema utiliza cópia de arquivos (shutil.copy2) em vez de movimentação, garantindo que as fotos originais nunca sejam perdidas em caso de erro.

 ---
 
🛠️ Tecnologias Utilizadas
Python - Linguagem principal.

CustomTkinter - UI moderna e customizável.

windnd - Manipulação de eventos de Drag & Drop nativos do Windows.

PyInstaller - Empacotamento para executável (.exe).

---

📦 Como Instalar e Rodar
Pré-requisitos
Python 3.10 ou superior instalado.

Passo a passo
Clone este repositório:

Bash
git clone https://github.com/seu-usuario/organizador-lotes-leilao.git
Acesse a pasta do projeto:

Bash
cd organizador-lotes-leilao
Instale as dependências:

Bash
pip install customtkinter windnd
Execute o programa:

Bash
python main.py
🔨 Gerando o Executável (.exe)
Para gerar uma versão que rode em computadores sem Python instalado (como o do usuário final), utilize:

Bash
pyinstaller --noconsole --onefile --collect-all customtkinter --collect-all windnd main.py
📖 Como Usar
Abra o programa e digite o nome do lote no campo de texto (ex: Lote 01 - Mercedes).

Arraste as fotos do veículo/item do seu explorador de arquivos para dentro da janela do programa.

Clique em "Organizar Lote".

---

Uma pasta chamada LOTES_PRONTOS será criada no mesmo local do programa com todas as fotos devidamente nomeadas e organizadas.

💡 Desenvolvido para facilitar o fluxo de trabalho de profissionais de leilão.

