# Megalink — CMS Django

CMS interno para gerenciamento de páginas, links, mídia e leads da Megalink Telecom.

## Stack

- **Python** 3.11 / **Django** 5.2
- **Tailwind CSS** (via CDN) + **Font Awesome 6**
- **SQLite** (dev) / PostgreSQL (produção)
- **Quill.js** para campos rich text

## Apps

| App | Responsabilidade |
|-----|-----------------|
| `builder` | CMS de páginas — componentes, revisões, templates, SEO, analytics |
| `dashboard` | Painel administrativo interno |
| `core` | Config do site, menus, rodapé |
| `leads` | Captura e webhook de leads |
| `media_library` | Biblioteca de mídia (upload/browse) |
| `shortener` | Encurtador de URLs com tracking de cliques |

## Instalação

```bash
git clone <repo>
cd site-novo/django_app

# Ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Dependências
pip install -r requirements.txt

# Variáveis de ambiente
cp .env.example .env
# Edite .env com SECRET_KEY e demais configs

# Banco de dados
python manage.py migrate

# Superusuário
python manage.py createsuperuser

# Servidor de desenvolvimento
python manage.py runserver
```

## Variáveis de ambiente

Copie `.env.example` para `.env` e preencha:

```env
SECRET_KEY=...        # obrigatório — gere com python -c "import secrets; print(secrets.token_urlsafe(50))"
DEBUG=True            # False em produção
ALLOWED_HOSTS=...     # domínios separados por vírgula
LEAD_WEBHOOK_URL=...  # opcional
```

## URLs principais

| Rota | Descrição |
|------|-----------|
| `/painel/` | Dashboard administrativo |
| `/painel/paginas/` | Gerenciador de páginas |
| `/painel/paginas/<id>/visual` | Editor visual split-panel |
| `/painel/links/` | Encurtador de URLs |
| `/painel/media/` | Biblioteca de mídia |
| `/painel/analytics/` | Analytics de páginas |
| `/admin/` | Django admin |
| `/sitemap.xml` | Sitemap automático |

## Editor Visual

O editor visual (`/painel/paginas/<id>/visual`) oferece:

- Painel esquerdo com lista de componentes e campos editáveis
- Preview em iframe atualizado em tempo real
- Toggle de viewport: Desktop / Tablet (768px) / Mobile (390px)
- Autosave com debounce (800ms)
- Salvar com revisão via botão ou `Ctrl+S`
- Drag & drop para reordenar componentes

## Testes

```bash
python manage.py test builder --verbosity=2
```

## Deploy (checklist)

- [ ] `DEBUG=False` no `.env`
- [ ] `SECRET_KEY` segura (mínimo 50 chars)
- [ ] `ALLOWED_HOSTS` com os domínios corretos
- [ ] `python manage.py collectstatic`
- [ ] Configurar servidor web (nginx + gunicorn)
- [ ] Banco PostgreSQL em produção
