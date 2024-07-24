from fastapi import APIRouter

from ..controllers.signup import signup

auth = APIRouter()

auth.add_api_route('/auth/signup', signup)
