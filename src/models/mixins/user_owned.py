



import uuid
from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class UserOwnedMixin:
	user_id: Mapped[uuid.UUID] = mapped_column(
		UUID(as_uuid=True),
		ForeignKey("users.uid", ondelete="CASCADE"),
		nullable=False,
		index=True
	)

