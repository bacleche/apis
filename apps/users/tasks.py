from celery import shared_task
from .models import User

@shared_task
def add_xp_to_user(user_id: int, xp_amount: int):
    """
    Ajoute de l'expérience à un utilisateur.
    """
    try:
        user = User.objects.get(id=user_id)
        user.xp += xp_amount
        user.save()
        return f"{xp_amount} XP added to {user.username}"
    except User.DoesNotExist:
        return f"User {user_id} does not exist"


@shared_task
def level_up_check(user_id: int):
    """
    Vérifie si l'utilisateur peut monter de niveau.
    """
    try:
        user = User.objects.get(id=user_id)
        # Exemple simple : 100 xp = 1 level
        new_level = (user.xp // 100) + 1
        if new_level > user.level:
            user.level = new_level
            user.save()
            return f"{user.username} leveled up to {new_level}"
        return f"{user.username} remains at level {user.level}"
    except User.DoesNotExist:
        return f"User {user_id} does not exist"
