#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "Installing Node.js via NVM..."
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm install 20
nvm use 20

echo "Installing pnpm..."
npm install -g pnpm

echo "Building frontend..."
cd frontend
pnpm install
pnpm run build
cd ..

echo "Copying frontend build to backend static folder..."
mkdir -p backend/src/static
cp -r frontend/dist/* backend/src/static/

echo "Installing backend dependencies..."
cd backend
pip install -r requirements.txt
