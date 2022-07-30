def build_person(first_name, last_name,age=None):
    """Return a dictionary of information about a person."""
    person = {'frist':first_name, 'last':last_name}
    if age:
        person['age']=age
    return person
musician = build_person('jimi','hendrix')
print(musician)

dreamer = build_person('younghoon','kim',41)
print(dreamer)