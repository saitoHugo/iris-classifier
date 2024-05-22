import uvicorn
from create_app import create_app

"""
  Entry point to FastAPI
"""
# Create the application
application = create_app()

if __name__ == "__main__":
    # Run the application
    uvicorn.run(application, port=8000)
