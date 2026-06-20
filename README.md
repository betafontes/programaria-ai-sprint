## Projeto Prático desenvolvido durante a **Sprint IA no Trabalho**, da **PrograMaria**.

### 📌 Productivity Agent

O Productivity Agent é um agente de produtividade que integra Inteligência Artificial com o Google Calendar para auxiliar na organização da agenda e no planejamento de tarefas.

A aplicação é capaz de analisar eventos existentes, interpretar tarefas descritas em linguagem natural e sugerir ajustes na agenda para otimizar a rotina do usuário.

### 🚀 Funcionalidades

- Integração com Google Calendar
- Leitura de eventos da agenda
- Criação e atualização de compromissos
- Organização de tarefas utilizando IA
- Classificação de eventos por categorias
- Identificação de eventos importantes
- Automação de planejamento semanal

### 🛠️ Tecnologias utilizadas

- Python
- Google Calendar API
- Anthropic Claude API
- Python Dotenv
- Google OAuth
- JSON

### ⚙️ Configuração

#### Clone o repositório

```bash
git clone https://github.com/betafontes/programaria-ai-sprint
cd productivity-agent
```

#### Crie e ative o ambiente virtual

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

#### Instale as dependências

```bash
pip install -r requirements.txt
```

#### Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
ANTHROPIC_API_KEY=
CALENDAR_ID=
CLAUDE_MODEL=claude-sonnet-4-6
```

#### Configure as credenciais do Google

Adicione o arquivo `credentials.json` na raiz do projeto para autenticação com a Google Calendar API.

#### ▶️ Executando o projeto

```bash
python main.py
```

#### 📚 Aprendizados

Durante o desenvolvimento deste projeto foram explorados conceitos como:

- Inteligência Artificial Generativa
- Engenharia de Prompts
- Integração com APIs
- Automação de Processos
- Desenvolvimento de Agentes de IA

#### 👩‍💻 Desenvolvido por

**Roberta Fontes**

Projeto desenvolvido como parte da **Sprint IA no Trabalho**, promovida pela **PrograMaria**.
