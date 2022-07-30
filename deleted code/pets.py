def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"{animal_type}'s name is {pet_name.title()}")


describe_pet('jay','hamster')
describe_pet(pet_name='jay',animal_type='snake')
describe_pet(animal_type='cat',pet_name='jay')
