from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from features.generate_title.generate_title_endpoint import router as generate_title_router
from features.improve_content.improve_content_endpoint import router as improve_content_router


app = FastAPI()
app.include_router(generate_title_router)
app.include_router(improve_content_router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def main():
    uvicorn.run(app, port=8080, host='127.0.0.1')

if __name__ == '__main__':
    main()