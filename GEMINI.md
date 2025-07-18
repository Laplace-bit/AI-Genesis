# Gemini Project Guidance: AI Genesis

This document outlines the established conventions, technology stack, and architectural patterns for the AI Genesis project. Adhering to these guidelines ensures consistency and maintainability.

## 1. Core Technologies

### Backend
- **Framework**: **FastAPI** on Python 3.12.
- **Database ORM**: **SQLAlchemy**. The project is currently configured for **SQLite** (`aigenesis.db`) for development, with PostgreSQL as a likely production target.
- **Asynchronous Tasks**: **Celery** with a **Redis** broker.
- **Authentication**: **Passlib** with `bcrypt` for password hashing and **python-jose** for JWT token management.
- **Server**: **Uvicorn**.

### Frontend
- **Framework**: **Vue.js 3** with the Composition API.
- **State Management**: **Pinia**.
- **Routing**: **Vue Router**.
- **UI**: A hybrid approach using **Element Plus** for components and **Tailwind CSS** for utility-first styling.
- **Build Tool**: **Vite**.
- **API Communication**: **Axios**.

## 2. Development Conventions

### Backend
- **Structure**: The application follows a standard FastAPI structure:
    - `main.py`: Main application entry point.
    - `database.py`: SQLAlchemy engine and session setup.
    - `models.py`: SQLAlchemy ORM models.
    - `schemas.py`: Pydantic schemas for data validation and serialization.
    - `crud.py`: Reusable functions for database operations.
    - `security.py`: Authentication and security-related utilities.
    - `routers/`: Directory containing API route modules, separated by feature (e.g., `auth.py`, `timeline.py`).
- **Dependencies**: Manage all Python packages via `backend/requirements.txt`.
- **Running the server**: Use `uvicorn main:app --reload` from the `backend` directory.

### Frontend
- **Structure**: The application follows a standard Vue.js project structure:
    - `src/main.js`: Main application entry point.
    - `src/App.vue`: Root Vue component.
    - `src/router.js`: Vue Router configuration.
    - `src/stores/`: Pinia store modules.
    - `src/views/`: Page-level components, mapped to routes.
    - `src/components/`: Reusable, shared components.
    - `src/utils/api.js`: Centralized Axios instance and API call functions.
- **Styling**:
    - Use **Tailwind CSS** for layout, spacing, and general styling (`<div class="p-4 bg-gray-100">...</div>`).
    - Use **inspira-uis** components for complex UI elements，and use more inspira-ui for all component.
    - Global styles are located in `src/style.css`.
- **State Management**: Define Pinia stores in the `src/stores` directory. Access stores within components via `import { useMyStore } from '@/stores/myStore';`.
- **Dependencies**: Manage all JavaScript packages via `frontend/package.json`. Use `npm install` to add new packages.
- **Running the dev server**: Use `npm run dev` from the `frontend` directory.

## 3. Code Style

- **Python**: Adhere to **PEP 8** standards. Use a linter like `flake8` or `black` if possible.
- **JavaScript/Vue**: Follow the official Vue.js Style Guide. Use a linter like ESLint with the recommended Vue 3 plugins.
- **Naming**:
    - Python variables and functions: `snake_case`.
    - Python classes: `PascalCase`.
    - JavaScript variables and functions: `camelCase`.
    - Vue components: `PascalCase` (e.g., `PromptCard.vue`).
- **API Endpoints**: Use plural nouns for resource endpoints (e.g., `/api/timelines`, `/api/prompts`).
