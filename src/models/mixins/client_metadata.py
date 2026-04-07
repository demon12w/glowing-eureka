


from typing import Union
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class ClientMetaDataMixin:
	user_agent: Mapped[Union[str, None]] = mapped_column(
		String(255),
		nullable=True
	)
	
	ip_address: Mapped[Union[str, None]] = mapped_column(
		String(45),
		nullable=True,
	)
	
	location: Mapped[Union[str, None]] = mapped_column(
		String(255),
		nullable=True,
	)
