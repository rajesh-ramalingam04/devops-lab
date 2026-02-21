# Simple Dockerfile Example

This minimal example builds an Alpine-based container that prints a hello message.

Build (PowerShell):

```powershell
# From repository root (d:\My Learning\Docker)
docker build -t simple-express-app .
```

Run (PowerShell):

```powershell
docker run --rm -p 3000:3000 simple-express-app
```

Try locally without Docker:

```powershell
npm install
npm start
# then open http://localhost:3000 in your browser
```

Notes:
- The app is a minimal Express server that serves `public/index.html` and exposes `/api/hello`.
- Docker image listens on port 3000; the example command maps container port 3000 to host port 3000.
- `.dockerignore` excludes node_modules and other common files to speed up build context.
