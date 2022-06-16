def greet(name, surname: str = ""):
    return f'Hi {name} {surname}!'


def greet_with_type(name: str, surname: str = "") -> str:
    return f'Hi {name} {surname}!'


print(greet(1))
print(greet_with_type(1))


age: int = 24
print(age)
age = "Hola mundo"
print(age)
