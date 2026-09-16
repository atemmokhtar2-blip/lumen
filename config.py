import os

APP_NAME = os.getenv("APP_NAME", "DAF Defensive Awareness Framework")
PORT = int(os.getenv("PORT", "8080"))

# Intentionally no bot tokens, target identifiers, command queues, or telemetry stores.
