# Guia Completo de Configuração - Tudo do Momento Presentes

Este guia fornece instruções passo a passo para configurar e implantar o projeto "Tudo do Momento Presentes" no Antigravity ou em outras plataformas de desenvolvimento modernas.

## 1. Preparação Inicial

### 1.1. O que você precisa

*   Uma conta no Antigravity (https://antigravity.dev)
*   Uma chave de API da OpenAI (https://platform.openai.com/api-keys)
*   O arquivo ZIP do projeto

### 1.2. Obter a Chave de API da OpenAI

1.  Acesse https://platform.openai.com/api-keys
2.  Faça login com sua conta OpenAI (crie uma se não tiver)
3.  Clique em "Create new secret key"
4.  Copie a chave gerada (você não conseguirá vê-la novamente)
5.  Guarde essa chave em um local seguro

## 2. Importação no Antigravity

### 2.1. Criar um Novo Projeto

1.  Acesse o dashboard do Antigravity
2.  Clique em "New Project" ou "Criar Novo Projeto"
3.  Escolha a opção "Import from ZIP" ou "Importar de ZIP"
4.  Faça upload do arquivo `tudo_do_momento_antigravity.zip`

### 2.2. Configuração Automática

O Antigravity reconhecerá automaticamente:

*   **Frontend React**: Na pasta `frontend/`
*   **Backend Flask**: Na pasta `backend/`
*   **Arquivo de Configuração**: `project.json`

Você verá uma tela mostrando a estrutura detectada. Clique em "Continue" ou "Continuar".

### 2.3. Configurar Variáveis de Ambiente

1.  Na tela de configuração, procure pela seção "Environment Variables" ou "Variáveis de Ambiente"
2.  Adicione as seguintes variáveis:

| Variável | Valor | Obrigatória |
|----------|-------|------------|
| `OPENAI_API_KEY` | Sua chave de API da OpenAI | ✅ Sim |
| `MAIL_SERVER` | smtp.gmail.com (ou seu servidor SMTP) | ❌ Não |
| `MAIL_PORT` | 587 | ❌ Não |
| `MAIL_USE_TLS` | True | ❌ Não |
| `MAIL_USERNAME` | Seu e-mail | ❌ Não |
| `MAIL_PASSWORD` | Sua senha de app do Gmail | ❌ Não |
| `ADMIN_EMAIL` | contato@tudodomomentopresentes.com.br | ❌ Não |

**Nota sobre Gmail**: Se estiver usando Gmail, você precisa gerar uma [senha de app](https://support.google.com/accounts/answer/185833?hl=pt-BR) em vez de usar sua senha regular. Siga o link para instruções.

### 2.4. Configurar Portas

O Antigravity pode pedir para configurar as portas dos serviços:

*   **Frontend**: Porta 3000 (padrão)
*   **Backend**: Porta 5000 (padrão)

Deixe as portas padrão a menos que o Antigravity sugira algo diferente.

### 2.5. Inicialização do Banco de Dados

O Antigravity deve executar automaticamente o comando de inicialização do banco de dados:

```bash
python3 backend/src/init_db.py
```

Se isso não acontecer automaticamente, você pode executar manualmente após o deploy.

## 3. Build e Deploy

### 3.1. Build do Frontend

O Antigravity executará automaticamente:

```bash
cd frontend
pnpm install
pnpm run build
```

Isso gerará os arquivos compilados em `frontend/dist/`.

### 3.2. Build do Backend

O Antigravity executará automaticamente:

```bash
cd backend
pip install -r requirements.txt
```

### 3.3. Deploy

1.  Clique em "Deploy" ou "Implantar"
2.  Aguarde o processo de build e deploy (pode levar alguns minutos)
3.  Quando concluído, você receberá uma URL pública para acessar sua loja

## 4. Verificação Pós-Deploy

### 4.1. Testar o Frontend

1.  Acesse a URL fornecida pelo Antigravity
2.  Você deve ver a página inicial da loja "Tudo do Momento Presentes"
3.  Verifique se:
   - A navegação funciona (Início, Produtos, Contato, etc.)
   - Os produtos estão sendo exibidos
   - O painel administrativo é acessível

### 4.2. Testar a API

1.  Abra o console do navegador (F12 ou Ctrl+Shift+I)
2.  Acesse a aba "Network"
3.  Navegue pela loja e verifique se as requisições para `/api/` retornam status 200

### 4.3. Testar o Formulário de Contato

1.  Acesse a página de contato
2.  Preencha o formulário com dados de teste
3.  Clique em "Enviar Mensagem"
4.  Você deve receber uma mensagem de sucesso

## 5. Configuração da Pesquisa de Mercado com IA

### 5.1. Executar Manualmente

Para popular o banco de dados com produtos iniciais:

1.  No dashboard do Antigravity, procure pela opção "Run Command" ou "Executar Comando"
2.  Execute:
    ```bash
    python3 backend/src/ai_market_research.py
    ```
3.  Aguarde a conclusão (pode levar alguns minutos)
4.  Recarregue a página de produtos para ver os novos itens

### 5.2. Agendar Execução Automática

O Antigravity pode suportar agendamento de tarefas (cron jobs). Se disponível:

1.  Procure pela seção "Scheduled Tasks" ou "Tarefas Agendadas"
2.  Crie uma nova tarefa com:
   - **Comando**: `python3 backend/src/ai_market_research.py`
   - **Frequência**: Semanal (ex: toda segunda-feira à 1h da manhã)

## 6. Configuração de Automação de Relatórios

### 6.1. Executar Manualmente

Para gerar relatórios:

```bash
# Relatório semanal
python3 backend/src/automation.py weekly

# Relatório mensal
python3 backend/src/automation.py monthly
```

### 6.2. Agendar Execução Automática

Se o Antigravity suportar agendamento:

1.  Crie uma tarefa semanal:
   - **Comando**: `python3 backend/src/automation.py weekly`
   - **Frequência**: Toda semana (ex: domingo à 2h da manhã)

2.  Crie uma tarefa mensal:
   - **Comando**: `python3 backend/src/automation.py monthly`
   - **Frequência**: Mensalmente (ex: primeiro dia do mês à 3h da manhã)

## 7. Gerenciamento do Painel Administrativo

### 7.1. Acessar o Painel

1.  Acesse a URL da sua loja
2.  Clique em "Admin" ou acesse `/admin`
3.  Você verá o dashboard com:
   - Estatísticas de vendas, receita, lucro e visitas
   - Gráficos de vendas por período
   - Produtos mais vendidos
   - Botões de ação (Executar Pesquisa de Mercado, Gerar Relatório, etc.)

### 7.2. Executar Pesquisa de Mercado via Painel

1.  No painel administrativo, clique em "Executar Pesquisa de Mercado"
2.  A pesquisa será iniciada em segundo plano
3.  Aguarde alguns minutos e recarregue a página de produtos

### 7.3. Gerar e Enviar Relatórios

1.  No painel administrativo, clique em "Gerar Relatório"
2.  Um relatório será gerado e exibido
3.  Clique em "Enviar Relatório por E-mail" para enviá-lo (se configurado)

## 8. Monitoramento e Manutenção

### 8.1. Verificar Logs

O Antigravity fornece acesso aos logs de aplicação. Verifique regularmente para:

*   Erros de API
*   Problemas com o banco de dados
*   Erros de e-mail

### 8.2. Backup do Banco de Dados

O banco de dados SQLite está armazenado em `backend/src/database/app.db`. Faça backup regularmente:

1.  Acesse os arquivos do projeto no Antigravity
2.  Faça download de `backend/src/database/app.db`
3.  Armazene em um local seguro

### 8.3. Atualizar Produtos

Para atualizar o catálogo de produtos:

1.  Execute a pesquisa de mercado com IA (via painel ou comando)
2.  Os produtos serão atualizados automaticamente

## 9. Troubleshooting

### Problema: "OPENAI_API_KEY not found"

**Solução**: Verifique se você configurou a variável de ambiente `OPENAI_API_KEY` no Antigravity com sua chave de API da OpenAI.

### Problema: Produtos não estão sendo exibidos

**Solução**: Execute a pesquisa de mercado com IA para popular o banco de dados com produtos iniciais.

### Problema: Formulário de contato não funciona

**Solução**: Verifique se as variáveis de e-mail estão configuradas corretamente (ou deixe em branco para desabilitar o envio de e-mails).

### Problema: Painel administrativo mostra "Nenhum dado disponível"

**Solução**: Isso é normal no início. Conforme você recebe visitas e vendas, os dados serão preenchidos.

### Problema: Erro ao compilar o frontend

**Solução**: Certifique-se de que todas as dependências foram instaladas. Tente executar manualmente:
```bash
cd frontend
pnpm install
pnpm run build
```

## 10. Próximos Passos

Após a implantação bem-sucedida:

1.  **Personalizar Informações**: Atualize as informações da loja (endereço, telefone, e-mail)
2.  **Configurar Domínio Personalizado**: Se desejar usar seu próprio domínio
3.  **Configurar SSL/HTTPS**: Garanta a segurança do site
4.  **Adicionar Produtos Manualmente**: Você pode adicionar produtos via API ou banco de dados
5.  **Configurar Pagamentos**: Integre um gateway de pagamento (Stripe, PayPal, etc.)

---

**Desenvolvido por:** Manus AI  
**Data:** 18 de Outubro de 2025
