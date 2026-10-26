#!/usr/bin/env bash
# Copies this case's input files into the run's workspace (needs --scaffold).
set -eu
cp -R "$(dirname "$0")/files/." .
