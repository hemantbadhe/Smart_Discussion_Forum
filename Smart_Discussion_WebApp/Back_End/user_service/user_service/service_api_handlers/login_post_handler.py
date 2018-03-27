from user_service.db.user_models.models import LoginEntry
from user_service.utils.user_related_methods import \
    check_credentials_and_get_object


def create_login_entry(request_data):
    username = request_data['username']
    password = request_data['password']
    client_id = request_data['clientId']
    user_object = check_credentials_and_get_object(username, password)
    if not user_object:
        return None

    try:
        login_entry_object, is_created = LoginEntry.objects.get_or_create(
            user=user_object,
            client_id=client_id,
            is_active=True)
        print login_entry_object
        return login_entry_object
    except:
        return None
