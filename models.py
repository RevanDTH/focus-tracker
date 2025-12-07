import uuid
import datetime
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class focusTime:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    start_time: datetime.datetime = field(default_factory=lambda: datetime.datetime.now())
    end_time: Optional[datetime.datetime] = None
    duration_minutes: Optional[int] = None
    task: Optional[str] = None