### exercises about strings:


name= 'Ganymede'
planet= 'Mars'
gravity= 1.43

template= f"""Gravity Facts about {name}
{'-' * 20}
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2 """


print(template.format(name=name, planet=planet, gravity=gravity))