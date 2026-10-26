#!/bin/bash
# ==============================================================================
# Noche Madrid Press — Cron Runner de Prospección de Medios, Blogs y Creadores
# ==============================================================================

# Directorio base del proyecto
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Variables de entorno
export DIRECTUS_URL="${DIRECTUS_URL:-https://mlpdirectus.116.203.118.1.sslip.io}"
export DIRECTUS_STATIC_TOKEN="${DIRECTUS_STATIC_TOKEN:-mlp_secret_directus_token_2026}"

LOG_FILE="$SCRIPT_DIR/cron.log"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

echo "==========================================================" >> "$LOG_FILE"
echo "[$TIMESTAMP] Ejecutando bot de prospección semanal..." >> "$LOG_FILE"
echo "==========================================================" >> "$LOG_FILE"

# Activar entorno virtual y ejecutar bot
if [ -f "$PROJECT_ROOT/.venv/bin/python" ]; then
    "$PROJECT_ROOT/.venv/bin/python" "$SCRIPT_DIR/run_bots.py" >> "$LOG_FILE" 2>&1
    EXIT_CODE=$?
else
    python3 "$SCRIPT_DIR/run_bots.py" >> "$LOG_FILE" 2>&1
    EXIT_CODE=$?
fi

echo "[$TIMESTAMP] Prospección finalizada con código de salida: $EXIT_CODE" >> "$LOG_FILE"
exit $EXIT_CODE
