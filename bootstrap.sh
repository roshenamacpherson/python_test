#!/bin/bash

set -o errexit
set -o pipefail

VENV_DIR="venv"

# Initialize virtualenv subdir.
function init_venv() {
  echo 'Setting up venv...'
  if ! python3 -m venv "${VENV_DIR}"; then
    echo "ERROR: failed to create virtual env dir."
    echo
    echo "Maybe some deps are missing? Re-run build_setup.sh from main repo."
    exit 1
  fi
}

# Installs/updates python packages under venv.
function install_python_requirements() {
  echo 'Upgrading...'
  ${VENV_DIR}/bin/pip install --upgrade pip setuptools wheel virtualenv

  echo 'Installing python packages in venv...'
  ${VENV_DIR}/bin/pip install --upgrade --process-dependency-links -e .

  echo 'Installing dev python packages in venv...'
  ${VENV_DIR}/bin/pip install --upgrade -r requirements-dev.txt
}

init_venv
install_python_requirements

echo
echo "Ok!"
echo
