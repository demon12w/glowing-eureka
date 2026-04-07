from src.models.base import Base
from src.models.mixins.client_metadata import ClientMetaDataMixin
from src.models.mixins.expirable_consumable import ExpirableConsumableMixin
from src.models.mixins.hashed_token import HashedTokenMixin
from src.models.mixins.id import IDMixin
from src.models.mixins.timestamp import TimestampMixin
from src.models.mixins.user_owned import UserOwnedMixin


class PasswordResetToken(
    IDMixin,
    UserOwnedMixin,
    HashedTokenMixin,
    ClientMetaDataMixin,
    ExpirableConsumableMixin,
    TimestampMixin,
    Base,
):
    __tablename__ = "password_reset_tokens"
