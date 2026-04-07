



from datetime import datetime, timezone
from http import HTTPStatus
from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy import and_, func, select
from sqlalchemy.orm import Session

from src.deps.auth import get_current_user
from src.deps.database import get_db
from src.errors.app_exception import NotFoundException
from src.models.refresh_token import RefreshToken
from src.models.user import User
from src.schemas.api_response import SuccessResponse
from src.schemas.session import SessionResponse, SessionsResponse


router = APIRouter(
	prefix="/sessions",
	tags=["Sessions"]
)


@router.get(
	"",
	status_code=HTTPStatus.OK,
	response_model=SuccessResponse[SessionsResponse]
)
def get_current_sessions(
	user: User = Depends(get_current_user),
	db: Session = Depends(get_db)
) -> SuccessResponse[SessionsResponse]:
	# Step 1 — find the max created_at per family_id
	subq = (
	    select(
	        RefreshToken.family_id,
	        func.max(RefreshToken.created_at).label("max_created_at")
	    )
	    .where(
	        RefreshToken.user_id == user.uid,
	        RefreshToken.is_used.is_(False),
	        RefreshToken.expires_at > datetime.now(timezone.utc)
	    )
	    .group_by(RefreshToken.family_id)
	    .subquery()
	)
	
	# Step 2 — join back to get full row
	stmt = (
	    select(RefreshToken)
	    .join(
	        subq,
	        and_(
	            RefreshToken.family_id == subq.c.family_id,
	            RefreshToken.created_at == subq.c.max_created_at
	        )
	    )
	)
	
	sessions = db.scalars(stmt).all()
	
	return SuccessResponse[SessionsResponse](
		message="All sessions for current user fetched successfully.",
		data=SessionsResponse(
			sessions=[SessionResponse.model_validate(sess) for sess in sessions]
		)
	)


@router.delete(
	"/{family_id}",
	status_code=HTTPStatus.NO_CONTENT,
	response_model=None
)
def delete_session_by_family_id(
	family_id: UUID,
	user: User = Depends(get_current_user),
	db: Session = Depends(get_db)
) -> None:
	sessions = db.scalars(select(RefreshToken).where(RefreshToken.family_id == family_id, RefreshToken.user_id == user.uid)).all()
	
	if len(sessions) <= 0:
		raise NotFoundException(
			message="User has none tokens with the provided family_id"
		)

	for sess in sessions:
		sess.is_used = True


	
