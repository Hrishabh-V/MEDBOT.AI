import re
from datetime import datetime, timedelta, timezone
# --- Simple natural-language relative time parser ---
def parse_time_from_message(message: str) -> datetime:
    """
    Parse simple relative times like:
      - "in 30 seconds"
      - "in 1 minute"
      - "in 2 hours"
    Returns a timezone-aware UTC datetime.
    Fallback: now + 1 minute.
    """
    now = datetime.now(timezone.utc)
    msg = (message or "").lower().strip()

    match = re.search(r"in\s+(\d+)\s+(second|seconds|minute|minutes|hour|hours)", msg)
    if match:
        value = int(match.group(1))
        unit = match.group(2)
        if "second" in unit:
            return now + timedelta(seconds=value)
        if "minute" in unit:
            return now + timedelta(minutes=value)
        if "hour" in unit:
            return now + timedelta(hours=value)

    # Fallback
    return now + timedelta(minutes=1)
