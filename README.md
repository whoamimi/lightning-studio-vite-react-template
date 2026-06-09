# React-Vite-App on Lightning Studio Demo

This project uses a hybrid setup where main.py runs a FastAPI server that serves both the API and the built React app from /dist. This makes the whole app deployable as a single container or endpoint.

- Purpose: A minimal fullstack AI/web app project — backend in Python, frontend in React/Vite.
- Frontend: Handles UI/UX with a modern JS toolchain.
- Backend: Runs logic, models, or API endpoints (main.py entry).
- Environment: Ideal for Lightning AI Studio — build backend models and visualize via frontend templates.

## How it works

**Tech Stack**

- Frontend: Vite + React 
- Backend: Python

```text
+-------------------+        +------------------------+
|  React (frontend) |  <-->  |  Python backend (API)  |
|  vite + JSX       |        |  main.py / FastAPI     |
|  fetch("/api/...")|        |  serves JSON or models |
+-------------------+        +------------------------+
```

## Project Directory 

```bash

├── main.py
└── react_templates
    └── react-app
        ├── README.md
        ├── index.html
        ├── package-lock.json
        ├── package.json
        ├── public
        │   └── vite.svg
        ├── src
        │   ├── App.css
        │   ├── App.jsx
        │   ├── assets
        │   │   └── react.svg
        │   ├── index.css
        │   └── main.jsx
        └── vite.config.js
```

## Setup

### Frontend

To run the frontend seperately from root path.

```bash

cd react_templates/react-app
npm install
npm run dev    # start dev server
npm run build  # builds into dist/

```

### Backend

To run the backend seperately from root path.

```bash

pip install -r requirements.txt
python main.py

```

## Lightning AI Studio Community

This template is intended for the Lightning AI Studio community and can be shared there as a reusable starter.

- Community page: https://lightning.ai/community
- Repository: https://github.com/whoamimi/lightning-studio-vite-react-template

## License

This project is licensed under the MIT License. See `LICENSE`.
