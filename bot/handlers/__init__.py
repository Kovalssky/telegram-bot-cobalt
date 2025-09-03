from aiogram import Router

def setup() -> Router:
    from . import commands, inline

    router = Router()
    router.include_routers(commands.router)
    router.include_routers(inline.router)
    return router
