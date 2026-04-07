

from datetime import datetime
from typing import Union
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import Base
from src.models.mixins.id import IDMixin
from src.models.mixins.timestamp import TimestampMixin
from src.models.mixins.user_owned import UserOwnedMixin


class TokenFamily(
	IDMixin,
	UserOwnedMixin,
	TimestampMixin, 
	Base
):
	__tablename__ = "token_families"
	
	revoked_at: Mapped[Union[datetime, None]] = mapped_column(
		DateTime(timezone=True),
		nullable=True
	)


