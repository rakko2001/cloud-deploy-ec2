#!/usr/bin/env bash
set -euo pipefail

sudo dnf update -y
sudo dnf install git python3 python3-pip -y

echo "Servidor preparado. Versoes instaladas:"
git --version
python3 --version
pip3 --version
