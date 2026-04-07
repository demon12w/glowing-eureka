



from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class HashedTokenMixin:
	token_hash: Mapped[str] = mapped_column(
		String(255),
		nullable=False,
		index=True
	)