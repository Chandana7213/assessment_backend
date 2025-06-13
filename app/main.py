from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.gzip import GZipMiddleware
# from starlette.middleware.trustedhost import TrustedHostMiddleware

from app.routes import auth_routes, question_routes, user_routes
from app.core.config import Base, engine
from app.models import user, question

app = FastAPI(title="Assessment Tool")


# Middleware for compression (improves performance)
# app.add_middleware(GZipMiddleware, minimum_size=1000)


# CORS Middleware (adjust allowed origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Add your frontend domains here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Trusted Host Middleware
# app.add_middleware(
#     TrustedHostMiddleware,
#     allowed_hosts=["*"],
# )

# Optional: Custom Security Headers Middleware
# @app.middleware("http")
# async def security_headers(request, call_next):
#     response = await call_next(request)
#     response.headers["X-Content-Type-Options"] = "nosniff"
#     response.headers["X-Frame-Options"] = "DENY"
#     response.headers["X-XSS-Protection"] = "1; mode=block"
#     response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
#     return response

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(question_routes.router)
app.include_router(user_routes.router)

