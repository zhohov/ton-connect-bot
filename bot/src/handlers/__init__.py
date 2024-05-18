__all__ = [
    "handlers_list",
]

from .user_interaction_handlers import register_user_interaction_handlers


handlers_list = [
    register_user_interaction_handlers
]
