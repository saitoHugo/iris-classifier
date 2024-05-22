import logging
from fastapi import FastAPI
from models.models_monostate import IrisModelMonostate
from routers import predict, health, root

app = FastAPI()



def create_app() -> FastAPI:
    """Creates app in function with the FastAPI framework.

    :return: FastAPI App
    """
    app = FastAPI(
        title="Iris Classifier API",
        version="1",
        sumary="Iris Classifier API is resposible to make real time inference.",
        description="### Iris Classifier API is resposible to make real time inference.",
        docs_url="/docs",
        redoc_url="/redoc",
        contact={"name": "Hugo Saito", "email": "hugovcsaito@gmail.com"},
        tracing=True,
    )
    def startup_event():
        """Startup event to load the model and species."""
        iris_model = IrisModelMonostate()
        app.state.model = iris_model.model
        app.state.species_map = iris_model.SPECIES_MAP

    # Add the startup event
    app.add_event_handler("startup", startup_event)
    
    # Add the routers
    app.include_router(predict.router)
    app.include_router(health.router)
    app.include_router(root.router)
    
    

    return app
