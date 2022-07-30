def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name(first_name='jimi',middle_name='hooker',last_name='hendrix')
print(musician)
dreamer = get_formatted_name(first_name='kim', last_name='younghoon')
print(dreamer)

