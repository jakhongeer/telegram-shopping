from functools import wraps
from database.connector import cursor


def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        a = cursor.execute("SELECT telegram_id FROM admins"
                           .format(user_id)).fetchall()
        IS_ADMIN = []
        for i in a:
            IS_ADMIN.append(i[0])
        if user_id not in IS_ADMIN:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context, *args, **kwargs)

    return wrapped
