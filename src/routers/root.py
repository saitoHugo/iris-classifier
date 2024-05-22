from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from logger import logger
router = APIRouter()


@router.get("/", include_in_schema=True)
def docs_redirect():
    """Redirects to the API documentation."""
    # Teste do logger
    logger.debug('Isso é uma mensagem de debug')
    logger.info('Isso é uma mensagem de informação')
    logger.warning('Isso é uma mensagem de aviso')
    logger.error('Isso é uma mensagem de erro')
    logger.critical('Isso é uma mensagem de erro crítico')
    return RedirectResponse(url='/docs')
