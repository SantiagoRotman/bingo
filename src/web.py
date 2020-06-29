from jinja2 import Template
from bingo import generar_carton

template = Template(open('plantilla.j2').read())

carton1 = generar_carton()
print(template.render(carton = carton1))
