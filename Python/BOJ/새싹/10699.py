from datetime import datetime, timezone

now = datetime.now(timezone.utc)
print(str(now)[:10])