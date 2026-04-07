

from typing import Union

from src.errors.app_exception import AuthenticationException
from src.models.user import User
from src.utils.hash import DUMMY_HASH, verify_password



def authenticate_user_via_email(
	user: Union[User, None],
	passwd: str,
) -> User:
	if user is None:
		verify_password(DUMMY_HASH, passwd) # timing attacks
		raise AuthenticationException(
			message="Invalid email or password.",
		)
	
	if not verify_password(user.password_hash, passwd):
		raise AuthenticationException(
			message="Invalid email or password."
		)
	
	return user




