# Tudo do Momento Presentes - Loja Virtual de Dropshipping

Bem-vindo ao projeto **Tudo do Momento Presentes**! Esta é uma loja virtual completa de dropshipping, desenvolvida com React (frontend) e Flask (backend), incluindo um agente de IA para pesquisa de mercado e automação de relatórios.

## 📋 Visão Geral

Este projeto é uma solução de e-commerce pronta para ser implantada em plataformas modernas como **Antigravity**, **Vercel**, **Netlify**, **Heroku**, **Railway** ou **Render**. Ele foi estruturado de forma simples e intuitiva para que você possa colocá-lo em funcionamento sem conhecimentos técnicos profundos.

### ✨ Principais Funcionalidades

*   **Loja Virtual Completa**: Catálogo de produtos, busca, filtros por categoria
*   **Painel Administrativo**: Dashboard com estatísticas, gráficos de vendas e controle de estoque
*   **Formulário de Contato**: Integrado com envio de e-mails automáticos
*   **Agente de IA**: Pesquisa automática de mercado para atualizar o catálogo de produtos
*   **Automação de Relatórios**: Geração de planilhas Excel e relatórios em texto
*   **Páginas Legais**: Política de Privacidade, Termos de Uso e Trocas/Devoluções (em conformidade com LGPD)
*   **Design Responsivo**: Interface moderna que funciona em desktop, tablet e celular

## 🚀 Início Rápido

### Opção 1: Importar no Antigravity (Recomendado)

1.  Acesse o **Antigravity** (https://antigravity.dev)
2.  Crie um novo projeto
3.  Escolha a opção de importar um projeto existente
4.  Faça upload do arquivo ZIP deste projeto
5.  O Antigravity reconhecerá automaticamente a estrutura do projeto e configurará tudo para você
6.  Clique em "Deploy" e seu site estará no ar!

### Opção 2: Executar Localmente (Para Desenvolvimento)

#### Pré-requisitos

*   Python 3.8+
*   Node.js 14+ e pnpm
*   Git (opcional)

#### Passos

1.  **Extrair o projeto**
    ```bash
    unzip tudo_do_momento_antigravity.zip
    cd tudo_do_momento_antigravity
    ```

2.  **Instalar dependências do frontend**
    ```bash
    cd frontend
    pnpm install
    cd ..
    ```

3.  **Instalar dependências do backend**
    ```bash
    cd backend
    pip install -r requirements.txt
    cd ..
    ```

4.  **Inicializar o banco de dados**
    ```bash
    cd backend
    python3 src/init_db.py
    cd ..
    ```

5.  **Compilar o frontend**
    ```bash
    cd frontend
    pnpm run build
    cd ..
    ```

6.  **Copiar arquivos compilados para o backend**
    ```bash
    cp -r frontend/dist/* backend/src/static/
    ```

7.  **Iniciar o backend**
    ```bash
    cd backend
    python3 src/main.py
    ```

8.  **Abrir no navegador**
    ```
    http://localhost:5000
    ```

## 📁 Estrutura do Projeto

```
tudo_do_momento_antigravity/
├── frontend/                    # Frontend React
│   ├── src/
│   │   ├── components/         # Componentes React
│   │   ├── pages/              # Páginas da aplicação
│   │   ├── App.jsx             # Componente principal
│   │   └── main.jsx            # Ponto de entrada
│   ├── package.json
│   ├── vite.config.js
│   └── dist/                   # Arquivos compilados (gerado após build)
│
├── backend/                     # Backend Flask
│   ├── src/
│   │   ├── models/             # Modelos de banco de dados
│   │   ├── routes/             # Rotas da API
│   │   ├── static/             # Arquivos estáticos (frontend compilado)
│   │   ├── database/           # Banco de dados SQLite
│   │   ├── main.py             # Aplicação Flask
│   │   ├── init_db.py          # Script de inicialização do BD
│   │   ├── ai_market_research.py    # Agente de IA
│   │   └── automation.py       # Scripts de automação
│   ├── requirements.txt        # Dependências Python
│   └── venv/                   # Ambiente virtual (criado após instalação)
│
├── project.json                # Configuração mestre do projeto
├── README.md                   # Este arquivo
└── SETUP_GUIDE.md              # Guia detalhado de configuração
```

## 🔧 Configuração de Variáveis de Ambiente

Para que o projeto funcione completamente (especialmente a pesquisa de mercado com IA), você precisa configurar as seguintes variáveis de ambiente:

### Variáveis Obrigatórias

*   **`OPENAI_API_KEY`**: Sua chave de API da OpenAI (obtenha em https://platform.openai.com/api-keys)

### Variáveis Opcionais (Para E-mails)

*   **`MAIL_SERVER`**: Servidor SMTP (ex: smtp.gmail.com)
*   **`MAIL_PORT`**: Porta SMTP (ex: 587)
*   **`MAIL_USE_TLS`**: Usar TLS (true/false)
*   **`MAIL_USERNAME`**: Seu e-mail
*   **`MAIL_PASSWORD`**: Sua senha de app (para Gmail)
*   **`ADMIN_EMAIL`**: E-mail do administrador

#### Como Configurar no Antigravity

1.  Acesse as configurações do seu projeto no Antigravity
2.  Procure pela seção "Variáveis de Ambiente" ou "Environment Variables"
3.  Adicione as variáveis listadas acima
4.  Salve e redeploy o projeto

#### Como Configurar Localmente

Crie um arquivo `.env` na raiz do diretório `backend`:

```env
OPENAI_API_KEY=sua_chave_aqui
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=seu_email@gmail.com
MAIL_PASSWORD=sua_senha_de_app
ADMIN_EMAIL=contato@tudodomomentopresentes.com.br
```

## 📊 Funcionalidades Principais

### Frontend (React)

*   **Página Inicial**: Apresentação da loja com categorias de produtos
*   **Catálogo de Produtos**: Listagem completa com filtros e busca
*   **Formulário de Contato**: Para clientes entrarem em contato
*   **Painel Administrativo**: Dashboard com estatísticas, gráficos e ações de gestão
*   **Páginas Legais**: Política de Privacidade, Termos de Uso, Trocas/Devoluções

### Backend (Flask)

*   **API REST Completa**: Endpoints para produtos, vendas, visitas, contatos
*   **Banco de Dados SQLite**: Armazenamento de produtos, vendas, mensagens de contato
*   **Agente de IA**: Pesquisa automática de mercado usando OpenAI
*   **Automação**: Geração de relatórios, planilhas Excel e envio de e-mails
*   **Estatísticas**: Rastreamento de visitas, vendas, lucros e produtos mais vendidos

## 🤖 Agente de IA de Pesquisa de Mercado

O projeto inclui um agente de IA que:

1.  Realiza pesquisas semanais de mercado em sites de dropshipping
2.  Identifica produtos em alta em categorias específicas
3.  Atualiza automaticamente o catálogo de produtos
4.  Sugere preços com margens de lucro otimizadas

Para executar manualmente:

```bash
cd backend
python3 src/ai_market_research.py
```

## 📈 Automação de Relatórios

O projeto inclui scripts para gerar relatórios automáticos:

```bash
# Automação semanal
cd backend
python3 src/automation.py weekly

# Automação mensal
cd backend
python3 src/automation.py monthly
```

Esses scripts geram:

*   Planilhas Excel com detalhes de vendas
*   Relatórios em texto com resumos financeiros
*   Alertas de estoque baixo
*   E-mails com os relatórios (se configurado)

## 🌐 Endpoints da API

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/api/products` | GET | Listar todos os produtos |
| `/api/products/<id>` | GET | Obter detalhes de um produto |
| `/api/visits` | POST | Registrar uma visita |
| `/api/contact` | POST | Enviar mensagem de contato |
| `/api/admin/stats` | GET | Obter estatísticas do dashboard |
| `/api/admin/sales-data` | GET | Obter dados de vendas por período |
| `/api/admin/top-products` | GET | Obter produtos mais vendidos |
| `/api/admin/generate-report` | POST | Gerar relatório |
| `/api/admin/send-report` | POST | Enviar relatório por e-mail |
| `/api/admin/run-market-research` | POST | Executar pesquisa de mercado com IA |

## 🚨 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'flask'"

**Solução**: Certifique-se de que você instalou as dependências do backend:
```bash
cd backend
pip install -r requirements.txt
```

### Erro: "OPENAI_API_KEY not found"

**Solução**: Configure a variável de ambiente `OPENAI_API_KEY` com sua chave de API da OpenAI.

### O frontend não está sendo servido

**Solução**: Certifique-se de que compilou o frontend e copiou os arquivos para `backend/src/static/`:
```bash
cd frontend
pnpm run build
cp -r dist/* ../backend/src/static/
```

### Banco de dados não foi criado

**Solução**: Execute o script de inicialização do banco de dados:
```bash
cd backend
python3 src/init_db.py
```

## 📞 Suporte

Se tiver dúvidas ou problemas, consulte o arquivo `SETUP_GUIDE.md` para instruções mais detalhadas, ou entre em contato através do formulário de contato da loja.

## 📄 Licença

Este projeto está licenciado sob a MIT License.

---

**Desenvolvido por:** Manus AI  
**Data:** 18 de Outubro de 2025  
**Versão:** 1.0.0
