from functools import wraps


def fsm_log_by(by_field_name=False, description_field_name=False):
    def inner_transition(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            kwargs['django_fsm_log_keys'] = {}
            kwargs['django_fsm_log_keys']['by_field_name'] = by_field_name
            kwargs['django_fsm_log_keys']['description_field_name'] = description_field_name
            
            out = func(instance, *args, **kwargs)

            return out

        return wrapped
    return inner_transition
