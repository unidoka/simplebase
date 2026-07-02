# Backend template

[English version](#english) | [Русская версия](#russian)

<a name="english"></a>
## English Version

### Project Concept
This architecture is designed for a microservice ecosystem where business logic is separated from infrastructure orchestration. The primary goal is to provide a unified environment for developing, testing, and deploying multiple services written in different languages (Go, Python, Node.js, etc.) using a single entry point.

### Directory Structure
*   **services/**: The core directory containing all microservices.
    *   **auth/, profile/, etc.**: Each subdirectory is a standalone microservice.
    *   **Dockerfile**: Every service contains its own Dockerfile, ensuring environment isolation.
    *   **__legacy/**: Used for deprecated code or older versions during migration.
*   **shared/** (Optional): Directory for common code, helper functions, or configuration templates shared across multiple services.
*   **.gitignore**: Global ignore rules for the entire services workspace.

### Key Features
1.  **Polyglot Support**: You can host services written in Go, Python, or any other language within the `services/` directory.
2.  **Infrastructure-First**: All services are launched and orchestrated via the [-infra](https://github.com/niyazgim/infra-template) repository using Docker Compose.
3.  **Local Development**: In `dev` mode, services can be run individually or collectively, with the frontend typically launched separately.
4.  **Shared Resources**: Support for common logic through shared directories that can be mounted or built into service containers.

### Integration with Infra
The [-infra](https://github.com/niyazgim/infra-template) repository interacts with this structure by defining build contexts. For example, in `docker-compose.yml`:
```yaml
services:
  auth:
    build:
      context: ../microservices-repo-name/services/microservice-name
      dockerfile: Dockerfile
```

<a name="russian"></a>
## Русская версия

### Концепция проекта
Данная архитектура разработана для экосистемы микросервисов, где бизнес-логика отделена от оркестрации инфраструктуры. Основная цель — предоставить единую среду для разработки, тестирования и развертывания нескольких сервисов на разных языках (Go, Python, Node.js и др.), используя единую точку входа.

### Структура директорий
*   **services/**: Основная директория, содержащая все микросервисы.
    *   **auth/, profile/ и др.**: Каждый подкаталог является независимым микросервисом.
    *   **Dockerfile**: Каждый сервис содержит собственный Dockerfile, что обеспечивает изоляцию среды окружения.
    *   **__legacy/**: Используется для устаревшего кода или старых версий сервисов в процессе миграции.
*   **shared/** (Опционально): Директория для общего кода, вспомогательных функций или шаблонов конфигурации, используемых несколькими сервисами.
*   **.gitignore**: Глобальные правила игнорирования для всего рабочего пространства сервисов.

### Ключевые особенности
1.  **Полиглотная архитектура**: Внутри директории `services/` можно размещать сервисы на Go, Python или любых других языках.
2.  **Infrastructure-First**: Все сервисы запускаются и управляются через репозиторий [-infra](https://github.com/niyazgim/infra-template) с помощью Docker Compose.
3.  **Локальная разработка**: В режиме `dev` сервисы могут запускаться как по отдельности, так и совместно, при этом фронтенд обычно запускается отдельно.
4.  **Общие ресурсы**: Поддержка общей логики через shared-директории, которые могут монтироваться или копироваться в контейнеры сервисов при сборке.

### Интеграция с Infra
Репозиторий [-infra](https://github.com/niyazgim/infra-template) взаимодействует с этой структурой через определение контекстов сборки. Пример в `docker-compose.yml`:

```yaml
services:
  auth:
    build:
      context: ../название-репо-с-микросервисами/services/название-микросервиса
      dockerfile: Dockerfile
```

