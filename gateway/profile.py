def update_profile(user, payload: dict):
    """Update the current user's profile from the request JSON.

    Applies the submitted fields to the user record.
    """
    for key, value in payload.items():
        setattr(user, key, value)
    user.save()
    return {"status": "ok", "user": user.id}
