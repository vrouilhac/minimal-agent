# src/main.py
import json, os

event = json.loads(os.environ.get("HH_EVENT", "null"))
print(
    f"Hello from HollowHost! run={os.environ.get('HH_RUN_ID')} source={os.environ.get('HH_SOURCE')} event={event}"
)
