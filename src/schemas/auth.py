




from typing import Annotated, Literal, Self

from pydantic import BeforeValidator, EmailStr, Field, model_validator
from src.schemas.base import BaseSchema


Email = Annotated[EmailStr, BeforeValidator(lambda value: value.lower())]

Password = Annotated[str, Field(min_length=8, max_length=13)]


class CredentialsMixin(BaseSchema):
	email: Email
	password: Password


class SignupRequest(CredentialsMixin):
	confirm_password: Password
	
	@model_validator(mode="after")
	def compare_passwords(self) -> Self:
		if self.password != self.confirm_password:
			raise ValueError("Passwords do not match.")
		return self


class LoginRequest(CredentialsMixin):
	pass


class ReactivateAccountRequest(CredentialsMixin):
	pass


class DeactivateAccountRequest(BaseSchema):
	password: Password


class ResetPasswordRequest(BaseSchema):
	old_password: Password
	new_password: Password
	confirm_new_password: Password
	
	@model_validator(mode="after")
	def compare_passwords(self) -> Self:
		if self.new_password != self.confirm_new_password:
			raise ValueError("Passwords do not match.")
		return self


class TokenResponse(BaseSchema):
	token_type: Literal["Bearer"] = "Bearer"
	access_token: str
	refresh_token: str


class RefreshRequest(BaseSchema):
	refresh_token: str
