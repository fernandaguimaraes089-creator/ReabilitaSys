# ReabilitaSys - Sistema Web de Gerenciamento de Clínica de Reabilitação

## 📋 Descrição

ReabilitaSys é um sistema web profissional, seguro e escalável para gerenciamento completo de clínicas de reabilitação para dependência química e saúde mental. O sistema controla todo o fluxo operacional, desde o cadastro do paciente até a alta, incluindo prontuário eletrônico, controle de leitos, medicamentos, visitas, relatórios e auditoria.

## 🎯 Objetivo

Fornecer uma solução ERP/HIMS (Hospital Information Management System) completa seguindo melhores práticas de arquitetura, SOLID, Clean Architecture, Clean Code e Design Patterns, com forte foco em segurança e conformidade com LGPD.

## 🏗️ Arquitetura Técnica

### Backend
- **Python 3.13** + **Django 5** + **Django REST Framework**
- **PostgreSQL** - Banco de dados relacional
- **JWT Authentication** - Autenticação segura
- **Celery** - Tasks assíncronas
- **Redis** - Cache e fila de mensagens
- **Docker & Docker Compose** - Containerização
- **Pytest** - Testes automatizados
- **Swagger/OpenAPI** - Documentação interativa

### Frontend
- **React 18** + **TypeScript**
- **Vite** - Build tool moderno
- **Material-UI (MUI)** - Component library
- **React Router v6** - Roteamento
- **React Query** - State management de dados
- **Axios** - HTTP client
- **React Hook Form** + **Zod** - Validação de formulários
- **Chart.js** - Gráficos e visualizações

### Infraestrutura
- **Docker** - Containerização
- **Docker Compose** - Orquestração local
- **Nginx** - Reverse proxy e servidor web
- **PostgreSQL** - Persistência de dados
- **Redis** - Cache distribuído

## 📦 Estrutura do Projeto

```
ReabilitaSys/
├── backend/                    # Aplicação Django
│   ├── config/                # Configurações
│   ├── apps/                  # Aplicações Django
│   │   ├── users/            # Gestão de usuários
│   │   ├── patients/         # Gestão de pacientes
│   │   ├── beds/             # Controle de leitos
│   │   ├── admissions/       # Gestão de internações
│   │   ├── medications/      # Controle de medicamentos
│   │   ├── occurrences/      # Ocorrências
│   │   ├── visits/           # Gestão de visitas
│   │   ├── documents/        # Gestão de documentos
│   │   ├── audit/            # Auditoria
│   │   └── dashboard/        # Dashboard
│   ├── core/                 # Núcleo (utils, mixins, etc)
│   ├── tests/                # Testes
│   ├── requirements.txt      # Dependências
│   ├── manage.py
│   └── Dockerfile
├── frontend/                  # Aplicação React
│   ├── src/
│   │   ├── components/       # Componentes reutilizáveis
│   │   ├── pages/           # Páginas
│   │   ├── hooks/           # Custom hooks
│   │   ├── services/        # API services
│   │   ├── utils/           # Utilitários
│   │   ├── types/           # TypeScript types
│   │   ├── stores/          # State management
│   │   ├── styles/          # Estilos globais
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── public/
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml        # Orquestração de containers
├── nginx/
│   └── nginx.conf           # Configuração Nginx
├── .env.example             # Variáveis de ambiente
└── docs/                    # Documentação adicional
```

## 🚀 Quick Start

### Pré-requisitos
- Docker & Docker Compose (v20+)
- Git

### Instalação e Execução

1. **Clone o repositório**
```bash
git clone https://github.com/fernandaguimaraes089-creator/ReabilitaSys.git
cd ReabilitaSys
```

2. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite .env conforme necessário
```

3. **Inicie os containers**
```bash
docker-compose up -d
```

4. **Execute as migrations**
```bash
docker-compose exec backend python manage.py migrate
```

5. **Crie um superusuário**
```bash
docker-compose exec backend python manage.py createsuperuser
```

6. **Acesse a aplicação**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api/
- Swagger: http://localhost:8000/api/docs/
- Admin Django: http://localhost:8000/admin/

## 📚 Funcionalidades Principais

### 🔐 Segurança
- [x] Autenticação JWT com Refresh Token
- [x] Controle de sessão com expiração automática
- [x] Bloqueio após tentativas inválidas
- [x] Recuperação de senha por e-mail
- [x] Hash BCrypt para senhas
- [x] Proteção CSRF, XSS e SQL Injection
- [x] Rate Limiting
- [x] Conformidade LGPD

### 👥 Gestão de Usuários
- [x] 5 Perfis: Administrador, Coordenação, Recepção, Enfermagem, Financeiro
- [x] Controle de permissões granular
- [x] Auditoria completa de ações

### 🏥 Gestão de Pacientes
- [x] Cadastro completo com foto, CPF, RG, dados pessoais
- [x] Histórico responsáveis e convênios
- [x] Diagnóstico, CID, alergias, comorbidades
- [x] Upload de documentos
- [x] Medicações contínuas

### 🛏️ Controle de Leitos
- [x] Mapa visual de blocos, quartos e leitos
- [x] Status: Disponível, Ocupado, Reservado, Manutenção
- [x] Histórico de movimentações

### 📝 Prontuário Eletrônico
- [x] Evolução multiprofissional (Enfermagem, Psicologia, Psiquiatria, Assistência Social, Terapia Ocupacional)
- [x] Histórico imutável (nunca permitir exclusão)
- [x] Registro de alterações

### 💊 Controle de Medicamentos
- [x] Gestão de estoque, lote, validade
- [x] Dispensação e administração
- [x] Alertas de vencimento

### 📋 Ocorrências
- [x] Registros de: Fuga, Queda, Acidente, Alteração Comportamental, Atendimento Médico, Contenção, etc.

### 👁️ Gestão de Visitas
- [x] Cadastro de visitantes
- [x] Controle de entrada/saída
- [x] Foto, documento e assinatura digital

### 📊 Dashboard
- [x] KPIs em tempo real: Pacientes internados, Entradas/Altas do dia, Taxa de ocupação
- [x] Gráficos mensais
- [x] Alertas prioritários
- [x] Indicadores operacionais

### 📈 Relatórios
- [x] Internados, Altas, Transferências, Medicamentos, Ocorrências, Visitas, Financeiro
- [x] Exportação: PDF, Excel, CSV

### 🔍 Auditoria
- [x] Log de todas as ações: Usuário, IP, Data, Hora, Navegador, Ação, Tela, Descrição
- [x] Logs imutáveis (nunca permitir exclusão)

## 🧪 Testes

### Executar testes do backend
```bash
docker-compose exec backend pytest --cov=apps --cov-report=html
```

### Executar testes do frontend
```bash
docker-compose exec frontend npm test -- --coverage
```

### Cobertura mínima: 80%

## 📖 Documentação Detalhada

Veja os diretórios de documentação para mais detalhes:
- `docs/ARCHITECTURE.md` - Arquitetura e decisões técnicas
- `docs/DATABASE.md` - Modelo de dados
- `docs/API.md` - Documentação da API
- `docs/SECURITY.md` - Estratégias de segurança
- `docs/DEPLOYMENT.md` - Guia de implantação

## 🔄 CI/CD

Configurar:
- GitHub Actions para testes automatizados
- Lint e code quality checks
- Build de imagens Docker
- Deploy automático

## 📝 Padrões de Desenvolvimento

### Backend
- **Clean Architecture** - Separação de concerns
- **SOLID Principles** - Código maintível
- **Design Patterns** - Strategy, Factory, Observer, etc
- **Type Hints** - Tipagem em Python
- **Docstrings** - Documentação de código

### Frontend
- **React Best Practices** - Hooks, Functional Components
- **TypeScript** - Type safety
- **Component Composition** - Reutilização
- **Clean Code** - Nomes claros, funções pequenas
- **Performance** - Memoization, Code Splitting

## 🤝 Contribuições

Para contribuir:
1. Crie uma branch: `git checkout -b feature/sua-feature`
2. Commit suas mudanças: `git commit -m 'Add feature'`
3. Push para a branch: `git push origin feature/sua-feature`
4. Abra um Pull Request

## 📄 Licença

Este projeto está sob licença MIT.

## 👤 Autor

Desenvolvido por **Fernanda Guimarães** - Desenvolvedor Full Stack

## 📞 Suporte

Para suporte, abra uma issue no repositório GitHub.

---

**Versão**: 1.0.0  
**Status**: Em desenvolvimento 🚧  
**Última atualização**: 2026-07-22
