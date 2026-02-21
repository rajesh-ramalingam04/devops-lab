# Use a Node.js base image (Alpine variant for smaller size)
FROM node:18-alpine

# Create app directory
WORKDIR /app

# Install dependencies
# Copy package files first for better layer caching
COPY package.json package-lock.json* ./
RUN npm ci --only=production || npm install --only=production

# Copy app source
COPY . ./

# Expose the port the app listens on
EXPOSE 3000

# Start the app
CMD ["node", "app.js"]
