# CLAUDE.md — Megalink CMS

Instruções para todos os agentes que trabalham neste projeto.

---

## Identificação obrigatória

**Toda resposta deve começar identificando o agente que está respondendo**, usando o formato:

> 🧱 **Backend Agent** respondendo

Os agentes disponíveis são:
| Emoji | Agente | Quando usar |
|-------|--------|-------------|
| 🧱 | Backend Agent | Python, views, models, migrations, APIs |
| 🎨 | Frontend Agent | HTML, templates, CSS, JavaScript |
| 🔍 | QA Agent | Testes, bugs, validação |
| 🚀 | DevOps Agent | Deploy, .env, servidor, segurança |
| 📝 | Content Agent | Seeds, schemas de componentes, conteúdo |

Se a tarefa envolver mais de um agente, identifique o principal e mencione o secundário.

---

## Salvar conversa

Use o comando **"salvar conversa"** para registrar um resumo da sessão em `.claude/conversations/YYYY-MM-DD.md`.

**Momentos em que o agente deve sugerir salvar:**
- Após resolver 3 ou mais itens em sequência
- Antes de encerrar uma sessão longa
- Após um deploy ou commit importante
- Quando o usuário disser "é isso por hoje" ou similar

---

## Regra fundamental

**Todo trabalho acontece dentro de `django_app/`.** Não toque em arquivos fora dessa pasta a menos que o usuário peça explicitamente.

---

## Contexto do projeto

Site institucional + CMS da **Megalink Telecom** — provedor de internet em Parnaíba/PI.
Migrado de PHP estático para Django em março de 2026.

**Stack:**
- Python 3.11 / Django 5.2
- SQLite (dev) → PostgreSQL (produção)
- Tailwind CSS via CDN + Font Awesome 6
- Quill.js para rich text

**Apps:**

| App | Função |
|-----|--------|
| `builder` | CMS: páginas, componentes, revisões, templates, analytics |
| `dashboard` | Painel administrativo interno (`/painel/`) |
| `core` | SiteConfig singleton, menus, rodapé |
| `leads` | Captura de leads + webhook |
| `media_library` | Upload e biblioteca de mídia |
| `shortener` | Encurtador de URLs com tracking |

**Acesso ao painel:** `/painel/` — requer login

---

## Estrutura de arquivos do time

```
.claude/
├── agents/           ← definições dos agentes
│   ├── backend.md
│   ├── frontend.md
│   ├── qa.md
│   ├── devops.md
│   └── content.md
├── tasks/            ← tarefas em andamento
└── conversations/    ← histórico de sessões salvas
```

---

## Bugs conhecidos (backlog)

- [ ] Botão "Aplicativo" no menu não está funcionando
- [ ] Links "Contratar plano" apontam para WhatsApp suporte (0068) — devem ir para vendas (0067)
- [ ] Rodapé: "Nossa Loja" redireciona para `megalinktelecom.com.br/lojas` (link externo legado)

---

## Números de WhatsApp

- **Vendas** (contratar plano): `558922210067`
- **Suporte** (autoatendimento): `558922210068`

---

## Comandos úteis

```bash
# Servidor de desenvolvimento
python manage.py runserver

# Testes
python manage.py test --verbosity=2

# Verificação de segurança
python manage.py check --deploy

# Publicar páginas agendadas (cron)
python manage.py publish_scheduled

# Seed de componentes
python manage.py seed_components

# Seed de páginas de exemplo
python manage.py seed_pages
```

---

## Variáveis de ambiente (.env)

```env
SECRET_KEY=           # obrigatório
DEBUG=True            # False em produção
ALLOWED_HOSTS=127.0.0.1,localhost
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
LEAD_WEBHOOK_URL=     # opcional
```
