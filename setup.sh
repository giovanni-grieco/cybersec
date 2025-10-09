#!/bin/bash
# ...existing code...

# ANSI color helpers
RESET='\033[0m'
DIM='\033[2m'
BOLD='\033[1m'
GREEN_BOLD='\033[1;32m'

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    cat <<'MSG' >&2
This script must be sourced to activate the virtual environment in your current shell.
Run:
  source setup.sh
or
  . setup.sh
MSG
    exit 1
fi

if [ ! -d ".venv" ]; then
    printf "%b\n" "${DIM}Creating virtual environment...${RESET}"
    python3 -m venv .venv
    
    printf "%b" "${DIM}"
    source .venv/bin/activate
    printf "%b\n" "${RESET}"
else
    printf "%b\n" "${DIM}Virtual environment already exists.${RESET}"
    printf "%b" "${DIM}"
    source .venv/bin/activate
    printf "%b\n" "${RESET}"
fi

printf "%b\n" "${DIM}Installing packages (output dimmed)...${RESET}"
printf "%b" "${DIM}"
pip install -r requirements.txt
printf "%b\n" "${RESET}"

echo ""

printf "%b\n" "${GREEN_BOLD}Virtual environment activated. To deactivate, run 'deactivate'.${RESET}"

echo ""