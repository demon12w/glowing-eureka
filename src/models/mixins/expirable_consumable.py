



from datetime import datetime
from typing import Union
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class ExpirableConsumableMixin:
	expires_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True),
		nullable=False,
	)
	
	used_at: Mapped[Union[datetime, None]] = mapped_column(
		DateTime(timezone=True),
		nullable=True
	)

