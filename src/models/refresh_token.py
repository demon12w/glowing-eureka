

import uuid

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import Base
from src.models.mixins.client_metadata import ClientMetaDataMixin
from src.models.mixins.expirable_consumable import ExpirableConsumableMixin
from src.models.mixins.hashed_token import HashedTokenMixin
from src.models.mixins.id import IDMixin
from src.models.mixins.timestamp import TimestampMixin


class RefreshToken(
	IDMixin, 
	HashedTokenMixin,
	ClientMetaDataMixin, 
	ExpirableConsumableMixin, 
	TimestampMixin, 
	Base
):
	__tablename__ = "refresh_tokens"
	
	family_id: Mapped[uuid.UUID] = mapped_column(
		UUID(as_uuid=True),
		ForeignKey("token_families.uid", ondelete="CASCADE"),
		nullable=False,
		index=True
	)

