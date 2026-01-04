# Stage 1: Build the TypeScript application
FROM node:24 AS builder

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build

# Stage 2: Create a lean production image
FROM node:24-slim

WORKDIR /app

# Copy compiled JavaScript from the builder stage
COPY --from=builder /app/dist ./dist 
COPY package.json package-lock.json my-deployment-configs.json ./
RUN npm install --production

RUN ls .

# TODO Student: Expose application port

# TODO Student: Run the application using node
## HINT: you need dist/index.js...