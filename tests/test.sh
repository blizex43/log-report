#!/bin/bash
set -e

mkdir -p /logs/verifier

pytest /tests -rA --ctrf=/logs/verifier/ctrf.json
result=$?
if [ "$result" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi