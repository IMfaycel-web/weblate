# Weblate

Weblate is a web-based continuous localization platform with tight version-control integration. It helps software teams manage translations alongside source code, synchronize localization changes with repositories, review translation quality, and collaborate through a browser-based workflow.

## Overview

Weblate connects translation projects directly to source repositories. Source updates can introduce new translatable strings, while completed translations can be committed back to the configured repository.

It is suitable for:

- Software localization
- Documentation translation
- Mobile application localization
- Website translation
- Continuous localization
- Community translation projects
- Enterprise translation teams
- Open-source projects

## Features

### Translation

- Browser-based translation editor
- Source and target string comparison
- Suggestions and comments
- Translation history
- Review states
- Glossaries
- Translation memory
- Search and filtering
- Bulk operations
- Automatic quality checks
- Automatic fixups
- Terminology validation

### Version Control

- Git integration
- Automated repository synchronization
- Translation commits
- Push and pull workflows
- Branch-based components
- Repository hooks
- Review-request workflows
- Gerrit support
- Optional Mercurial integration

### Localization Formats

Weblate supports many localization formats, including:

- GNU gettext
- Android resources
- Apple strings
- XLIFF
- JSON
- YAML
- TOML
- Java properties
- Microsoft RESX and RESW
- Qt Linguist files
- Fluent
- i18next JSON
- CSV
- INI
- PHP translations
- Ruby YAML
- subtitles
- Markdown
- application-store metadata

### Collaboration

- Projects and components
- Translation teams
- Role-based permissions
- Review workflows
- Contributor statistics
- User profiles
- Notifications
- Component lists
- Public and private projects

### Authentication

- Password authentication
- Two-factor authentication
- WebAuthn
- Social authentication
- Optional LDAP
- Optional SAML
- External identity-provider integration

### Automation

- REST API
- API tokens
- Command-line client support
- Webhooks
- Add-ons
- Celery background jobs
- Scheduled synchronization
- Machine-translation integrations
- Management commands

### Observability

- OpenTelemetry instrumentation
- Sentry integration
- Graylog integration
- Celery task processing
- Performance reporting
- Database and cache monitoring

## Tech Stack

| Area | Technologies |
| --- | --- |
| Language | Python 3.12 or later |
| Backend | Django 6 |
| API | Django REST Framework |
| API schema | OpenAPI, drf-spectacular |
| Background processing | Celery |
| Scheduling | django-celery-beat |
| Database | PostgreSQL 13 or later |
| Recommended database | PostgreSQL 15 or later |
| Cache and task queue | Valkey or Redis |
| Translation engine | Translate Toolkit |
| Repository access | Git, GitPython |
| Frontend | Django templates, Bootstrap, jQuery |
| Frontend bundling | Webpack |
| Frontend dependencies | Yarn |
| Authentication | Django auth, Social Auth, WebAuthn |
| WSGI serving | Granian-compatible deployment |
| Observability | OpenTelemetry, Sentry |
| Testing | Pytest, pytest-django, Selenium |
| Quality tooling | Ruff, mypy, Pylint, Biome, pre-commit |
| Documentation | Sphinx |
| Packaging | uv, setuptools |
| Deployment | Docker, Docker Compose, Kubernetes, OpenShift |

## Installation

For production, container-based deployment is recommended.

For repository development, use the included Docker development environment.

### Requirements

- Git
- Docker Engine or Docker Desktop
- Docker Compose
- Linux, macOS, or another Unix-like environment
- At least 3 GB RAM
- At least 2 CPU cores

Windows is not a supported native runtime. Use a Linux environment or WSL when developing from Windows.

### Start Development Environment

From the repository root:

```bash
./rundev.sh
```

The development helper builds and starts the required services and exposes Weblate on port `8080`.

### Wait for Startup

```bash
./rundev.sh wait
```

### View Logs

```bash
./rundev.sh logs
```

### Stop Development Services

```bash
./rundev.sh stop
```

### Rebuild Containers

```bash
./rundev.sh build
./rundev.sh
```

## Source Installation

Direct source installation is intended for advanced development and custom deployments.

### Requirements

- Python 3.12 or newer
- PostgreSQL 13 or newer
- Valkey or Redis
- Git
- Pango
- Cairo
- GObject introspection libraries
- Node.js supported by the frontend toolchain
- Yarn

### Create Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### Install Weblate

Using `uv`:

```bash
uv pip install -e ".[postgres]"
```

Install all optional features when required:

```bash
uv pip install -e ".[all]"
```

### Configure PostgreSQL

Create a dedicated PostgreSQL database and user.

Weblate uses PostgreSQL extensions including:

```text
pg_trgm
btree_gin
```

Ensure the application database can use these extensions before running migrations.

### Configure Application

Create local settings from the repository example:

```bash
cp weblate/settings_example.py weblate/settings.py
```

Configure:

- Database connection
- Secret key
- Allowed hosts
- Data directory
- Cache connection
- Celery broker
- Email delivery
- Public application origin

### Apply Migrations

```bash
weblate migrate
```

### Create Administrator

```bash
weblate createadmin
```

### Compile Translations

```bash
weblate compilemessages
```

## Usage

### Create a Project

1. Sign in as an administrator or project manager.
2. Create a project.
3. Configure its access policy.
4. Add a translation component.
5. Connect the component to a source repository.
6. Select the translation format.
7. Configure synchronization.
8. Add target languages.
9. Assign teams and permissions.
10. Begin translation.

### Translation Workflow

1. Open a project.
2. Select a component and language.
3. Open untranslated or failing strings.
4. Review source context.
5. Enter or select a translation.
6. Resolve quality checks.
7. Save the translation.
8. Continue to the next string.

### Review Workflow

Reviewers can:

- Inspect changed strings
- Approve translations
- Reject or edit translations
- Review failed checks
- Resolve comments
- Search translated content
- Filter by translation state

## Translation Memory

Translation memory helps reuse existing translations and maintain consistency.

It can provide:

- Similar translations
- Previous project translations
- Shared suggestions
- Imported translation data
- Context-aware reuse

## Machine Translation

Weblate can integrate with automatic translation providers.

Machine translation can assist translators by generating suggestions, but important projects should retain appropriate human review.

Provider credentials should always be stored outside version control.

## Add-ons

Add-ons automate repository and translation workflows.

Typical uses include:

- Repository maintenance
- File synchronization
- Translation cleanup
- Automatic commits
- Translation propagation
- Quality automation

## REST API

The REST API supports automation for:

- Projects
- Components
- Languages
- Translation units
- Translation files
- Repository operations
- Users and teams
- Statistics

Use dedicated API tokens with the minimum required permissions.

## Configuration

### Core Application

| Setting | Purpose |
| --- | --- |
| `SECRET_KEY` | Django cryptographic secret |
| `ALLOWED_HOSTS` | Permitted application hostnames |
| `SITE_DOMAIN` | Public application domain |
| `DATA_DIR` | Repository and uploaded-data storage |
| `CACHE_DIR` | Generated and cached data |
| `DEFAULT_FROM_EMAIL` | Default sender address |
| `REGISTRATION_OPEN` | Controls registration |
| `ADMINS` | Administrative contacts |

### Database

| Setting | Purpose |
| --- | --- |
| `ENGINE` | Django PostgreSQL backend |
| `NAME` | Database name |
| `USER` | Database user |
| `PASSWORD` | Database password |
| `HOST` | PostgreSQL host |
| `PORT` | PostgreSQL port |
| `CONN_MAX_AGE` | Persistent connection lifetime |
| `CONN_HEALTH_CHECKS` | Connection validation |

PostgreSQL 15 or newer is recommended for new installations.

### Cache and Celery

Weblate uses Valkey or Redis-compatible storage for:

- Caching
- Celery task queues
- Shared runtime state

All WSGI and Celery processes should use the same shared service in multi-node deployments.

### Email

Common email settings include:

```text
EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
EMAIL_USE_TLS
EMAIL_USE_SSL
```

### Storage

`DATA_DIR` contains important runtime data such as:

- Cloned repositories
- Uploaded user data
- Generated files

All application and worker processes must have consistent access to this storage.

## Production Deployment

A production installation normally includes:

- Reverse proxy
- WSGI application processes
- Celery workers
- PostgreSQL
- Valkey or Redis
- Shared filesystem storage
- SMTP service

Production deployments should:

- Use PostgreSQL
- Use PostgreSQL 15 or newer for new installations
- Use persistent shared storage
- Protect the database and cache from public access
- Run Celery workers continuously
- Use HTTPS
- Configure trusted proxy headers
- Use secure application secrets
- Configure SMTP
- Back up PostgreSQL
- Back up `DATA_DIR`
- Monitor workers and database connections
- Test repository connectivity after network changes
- Verify upgrades in staging

## Frontend Development

The frontend uses Bootstrap, jQuery, Django templates, and bundled third-party libraries.

### Requirements

- Supported Node.js release
- Yarn

Install dependencies:

```bash
cd client
yarn install --check-files
```

Build frontend libraries:

```bash
yarn build
```

JavaScript and CSS are formatted and linted with Biome.

User-facing strings must remain localizable.

Frontend changes should preserve:

- Keyboard navigation
- Logical focus order
- Visible focus states
- Semantic HTML
- Accessible labels
- Screen-reader feedback
- Reduced-motion preferences

## Testing

### Container Tests

```bash
./rundev.sh test
```

Run a targeted test path:

```bash
./rundev.sh test weblate/trans/tests
```

### Direct Tests

```bash
pytest
```

Run tests in parallel:

```bash
pytest -n auto
```

### Application Checks

```bash
./rundev.sh check
```

### Python Quality

```bash
ruff check .
ruff format --check .
```

The repository also uses mypy and Pylint for additional static validation.

## Contributing

Create a focused branch from the current development branch and follow existing coding, accessibility, localization, and review conventions.

Before submitting changes:

- Add tests for fixes and new behavior
- Run targeted Pytest suites
- Run application checks
- Run Python linting and formatting
- Run type checks when applicable
- Build frontend assets when dependencies change
- Keep user-facing strings translatable
- Preserve accessibility requirements
- Add migrations for database-model changes
- Keep REST API behavior backward-compatible where possible
- Avoid committing credentials or private settings
- Update documentation for operational changes
- Keep changes focused and clearly explained
