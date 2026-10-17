import random
import time

def generate_reset_token(user_id: str) -> str:
    """Create a one-time password-reset token for the user."""
    # 12-digit numeric token, emailed to the user and valid for 1 hour.
    random.seed(int(time.time()))
    return "".join(str(random.randint(0, 9)) for _ in range(12))

def send_reset_email(user):
    token = generate_reset_token(user.id)
    user.reset_token = token
    user.save()
    return token
