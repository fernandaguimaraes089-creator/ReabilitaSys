# Arquitetura do ReabilitaSys

## Visão Geral

O ReabilitaSys segue uma arquitetura moderna de três camadas:

```
┌─────────────────────────────────────────┐
│         Frontend (React)                 │
│  TypeScript, Vite, Material-UI, Axios   │
└────────────┬────────────────────────────┘
             │ HTTPS/REST
             ↓
┌─────────────────────────────────────────┐
│       Nginx (Reverse Proxy)             │
│     Load Balancing, Caching             │
└────────────┬────────────────────────────┘
             │
    ┌────────┴────────┐
    ↓                 ↓
┌──────────────┐  ┌──────────────┐
│ Django REST  │  │   Static     │
│   Framework  │  │   Files      │
│   Backend    │  │   & Media    │
└──────┬───────┘  └──────────────┘
       │
   ┌───┴─────────────┬──────────────┐
   ↓                 ↓              ↓
┌────────┐    ┌──────────┐    ┌─────────┐
│PostgreSQL│  │  Redis   │    │ Celery  │
│ Database │  │  Cache   │    │ Tasks   │
└────────┘    └──────────┘    └─────────┘
```

## Backend - Clean Architecture

### Estrutura em Camadas

```
backend/
├── config/                    # Configurações Django
│   ├── settings.py           # Settings principais
│   ├── urls.py               # URLs root
│   ├── wsgi.py               # WSGI
│   └── celery.py             # Celery config
│
├── apps/                      # Aplicações Django
│   ├── users/                # Domínio de Usuários
│   │   ├── models.py         # Entidades
│   │   ├── serializers.py    # DTOs
│   │   ├── views.py          # Controllers/Handlers
│   │   ├── permissions.py    # Permissões
│   │   ├── services.py       # Casos de uso
│   │   ├── repositories.py   # Acesso a dados
│   │   ├── urls.py           # Rotas
│   │   └── tests/            # Testes
│   │
│   ├── patients/             # Domínio de Pacientes
│   ├── beds/                 # Domínio de Leitos
│   ├── admissions/           # Domínio de Internações
│   ├── medications/          # Domínio de Medicamentos
│   ├── occurrences/          # Domínio de Ocorrências
│   ├── visits/               # Domínio de Visitas
│   ├── documents/            # Domínio de Documentos
│   ├── audit/                # Domínio de Auditoria
│   └── dashboard/            # Dashboard
│
├── core/                      # Camada de infraestrutura
│   ├── models.py             # Base models (timestamps, UUID)
│   ├── exceptions.py         # Exceções customizadas
│   ├── permissions.py        # Permissões base
│   ├── pagination.py         # Paginação
│   ├── filters.py            # Filtros
│   ├── mixins.py             # Mixins reutilizáveis
│   ├── validators.py         # Validadores customizados
│   ├── utils.py              # Funções utilitárias
│   ├── decorators.py         # Decoradores
│   └── tasks.py              # Tasks Celery base
│
├── tests/                     # Testes globais
│   ├── fixtures.py           # Fixtures compartilhadas
│   ├── factories.py          # Factory Boy factories
│   └── conftest.py           # Pytest configuration
│
├── requirements.txt           # Dependências Python
├── manage.py
└── Dockerfile
```

### Padrões de Design

#### 1. Repository Pattern
```python
class UserRepository:
    """Abstração para acesso a dados de usuários"""
    
    def get_by_id(self, user_id):
        return User.objects.get(id=user_id)
    
    def create(self, data):
        return User.objects.create(**data)
```

#### 2. Service Layer Pattern
```python
class UserService:
    """Casos de uso de usuários"""
    
    def __init__(self, repository=None):
        self.repository = repository or UserRepository()
    
    def create_user(self, data):
        # Lógica de negócio
        pass
```

#### 3. Factory Pattern (viewsets)
```python
class UserViewSet(viewsets.ModelViewSet):
    """View factory para operações CRUD"""
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
```

#### 4. Observer Pattern (Signals)
```python
@receiver(post_save, sender=User)
def create_audit_log(sender, instance, created, **kwargs):
    """Dispara log de auditoria ao salvar"""
    AuditLog.objects.create(
        user=instance,
        action='CREATE' if created else 'UPDATE'
    )
```

### SOLID Principles

#### S - Single Responsibility
- `UserService` responsável apenas por lógica de usuários
- `AuditService` responsável apenas por auditoria
- Cada classe tem uma única razão para mudar

#### O - Open/Closed
- Classes abertas para extensão via herança
- Fechadas para modificação

#### L - Liskov Substitution
- `BasePermission` pode ser substituída por qualquer subclasse
- `BaseModel` fornece contrato comum

#### I - Interface Segregation
- `ReadPermission` vs `WritePermission` separadas
- Permissões específicas por recurso

#### D - Dependency Injection
- Services recebem repositórios como dependência
- ViewSets recebem serializers
- Testes podem injetar mocks

## Frontend - Component-Based Architecture

```
frontend/src/
├── components/              # Componentes reutilizáveis
│   ├── common/             # Componentes genéricos
│   │   ├── Header.tsx
│   │   ├── Sidebar.tsx
│   │   ├── Footer.tsx
│   │   ├── Loading.tsx
│   │   └── ErrorBoundary.tsx
│   │
│   ├── auth/               # Componentes de autenticação
│   │   ├── LoginForm.tsx
│   │   ├── PrivateRoute.tsx
│   │   └── ProtectedLayout.tsx
│   │
│   ├── patients/           # Componentes de pacientes
│   │   ├── PatientForm.tsx
│   │   ├── PatientTable.tsx
│   │   └── PatientDetail.tsx
│   │
│   ├── beds/               # Componentes de leitos
│   │   ├── BedMap.tsx
│   │   └── BedStatus.tsx
│   │
│   └── dashboard/          # Componentes de dashboard
│       ├── KPICard.tsx
│       ├── Chart.tsx
│       └── AlertsPanel.tsx
│
├── pages/                  # Páginas (rotas)
│   ├── Login.tsx
│   ├── Dashboard.tsx
│   ├── Patients/
│   │   ├── PatientsList.tsx
│   │   ├── PatientDetail.tsx
│   │   └── PatientForm.tsx
│   ├── Beds/
│   ├── Admissions/
│   ├── Medications/
│   ├── Occurrences/
│   ├── Visits/
│   └── Reports/
│
├── hooks/                  # Custom React Hooks
│   ├── useAuth.ts          # Autenticação
│   ├── useApi.ts           # Chamadas API
│   ├── useForm.ts          # Gestão de forms
│   ├── useLocalStorage.ts  # Local storage
│   └── usePagination.ts    # Paginação
│
├── services/               # API Services
│   ├── api.ts              # Instância Axios
│   ├── authService.ts      # Serviço de auth
│   ├── patientService.ts   # Serviço de pacientes
│   ├── userService.ts      # Serviço de usuários
│   └── ...
│
├── stores/                 # State Management (Context API / Zustand)
│   ├── authStore.ts        # Estado de autenticação
│   ├── patientStore.ts     # Estado de pacientes
│   └── uiStore.ts          # Estado da UI
│
├── types/                  # Tipos TypeScript
│   ├── index.ts            # Tipos globais
│   ├── api.ts              # Tipos de API
│   ├── auth.ts             # Tipos de autenticação
│   └── entities.ts         # Tipos de entidades
│
├── utils/                  # Funções utilitárias
│   ├── formatting.ts       # Formatação de dados
│   ├── validation.ts       # Validação de dados
│   ├── date.ts             # Utilitários de data
│   └── constants.ts        # Constantes
│
├── styles/                 # Estilos globais
│   ├── theme.ts            # Theme Material-UI
│   ├── globals.css         # CSS global
│   └── colors.ts           # Paleta de cores
│
├── App.tsx                 # Root component
├── main.tsx                # Entry point
└── index.html
```

### Padrões Frontend

#### Custom Hooks
```typescript
const useAuth = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  // lógica de autenticação
  return { user, loading, login, logout };
};
```

#### Context API para State
```typescript
const AuthContext = React.createContext({
  user: null,
  login: () => {},
  logout: () => {},
});
```

#### Higher-Order Component para proteção
```typescript
const withAuth = (Component) => {
  return (props) => {
    const { user } = useAuth();
    return user ? <Component {...props} /> : <Navigate to="/login" />;
  };
};
```

## Banco de Dados

### Modelo Relacional

```
Usuários ─┬─→ Perfis
          ├─→ Permissões
          └─→ Logs de Auditoria

Pacientes ─┬─→ Responsáveis
           ├─→ Internações
           ├─→ Medicamentos
           ├─→ Alergias
           ├─→ Comorbidades
           ├─→ Documentos
           └─→ Evoluções

Internações ─┬─→ Pacientes
             ├─→ Quarto
             ├─→ Leito
             ├─→ Usuário Recepcionista
             ├─→ Altas
             ├─→ Medicações
             └─→ Ocorrências

Leitos ─┬─→ Quarto
        ├─→ Movimentações
        └─→ Status

Medicamentos ─┬─→ Lotes
              ├─→ Administrações
              └─→ Alertas

Visitas ─┬─→ Paciente
         ├─→ Visitante
         ├─→ Entrada/Saída
         └─→ Documentos

Ocorrências ─┬─→ Paciente
             ├─→ Internação
             ├─→ Usuário
             └─→ Tipo
```

### Base Models

Todas as entidades herdam de:

```python
class BaseModel(models.Model):
    id = UUIDField(primary_key=True, default=uuid4)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    created_by = ForeignKey(User, on_delete=PROTECT)
    updated_by = ForeignKey(User, on_delete=PROTECT)
    is_deleted = BooleanField(default=False)  # Soft delete
    
    objects = SoftDeleteManager()  # Manager customizado
```

## Segurança

### Autenticação
- JWT com acesso/refresh tokens
- Sessions com timeout
- Logout com invalidação de token

### Autorização
- Permissões por perfil
- RBAC (Role-Based Access Control)
- Object-level permissions

### Proteção
- HTTPS obrigatório
- CSRF protection via tokens
- XSS protection via sanitization
- SQL Injection prevention via ORM
- Rate limiting por IP e usuário

## Padrões de Comunicação

### REST API
- Recursos bem definidos
- Métodos HTTP corretos
- Status codes apropriados
- Versionamento de API (/api/v1/)

### WebSockets (opcional)
- Notificações em tempo real
- Dashboard updates
- Chat entre staff

## Deployment

### Docker
- Multi-stage builds
- Lightweight images
- Production-ready configs

### Escalabilidade
- Stateless backend
- Redis para cache distribuído
- Celery para tasks assíncronas
- Load balancing com Nginx

---

**Próximas etapas**: Implementação das models, views e serializers de cada domínio.
