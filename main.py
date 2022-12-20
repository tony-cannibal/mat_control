

class Materiales:
    todos = {}
    def __init__(self, area, codigo, cantidad=0, pkg=0, cantidad_pkg=0, pkg_entregado=0):

        self.area = area
        self.codigo = codigo
        self.cantidad = cantidad
        self.pkg = pkg
        self.cantidad_pkg = cantidad_pkg
        self.pkg_entregado = pkg_entregado
        self.cantidad_entregada = self.pkg * self.pkg_entregado
        
        # Append all Instances of the Class to Dictionary
        Materiales.todos[f"{self.area}{self.codigo}"] = self

    def esta_excedido(self):
        if  self.pkg_entregado >= self.cantidad_pkg:
            print('El material esta excedido')
            return True
        else:
            print('El material no esta excedido')
            return False

    def entregar_material(self):
        if self.esta_excedido() == True:
            print('El material esta excedido')
            print('No se puede entregar')
        else:
            self.pkg_entregado += 1

    @classmethod
    def instantiate_list(cls, mats):
        for i in mats:
            Materiales(
                area=i.get('area'),codigo=i.get('codigo'), cantidad=i.get('cantidad'),
                pkg=i.get('pkg'), cantidad_pkg=i.get('cantidad_pkg'),
                pkg_entregado=i.get('pkg_entregado'))

    def __repr__(self):
        return f"area: {self.area}, codigo: {self.codigo}, cantidad:{self.cantidad}, pkg: {self.pkg}, pkg_entregado: {self.pkg_entregado}"


mats=[
     {'area':'m1', 'codigo':'tkt', 'cantidad':3000, 'pkg':1500, 'cantidad_pkg':2, 'pkg_entregado':0},
     {'area':'m1', 'codigo':'tyr', 'cantidad':6000, 'pkg':2000, 'cantidad_pkg':3, 'pkg_entregado':0},
     {'area':'m1', 'codigo':'tap', 'cantidad':6000, 'pkg':1500, 'cantidad_pkg':4, 'pkg_entregado':0},
     {'area':'m2', 'codigo':'tsm', 'cantidad':10000, 'pkg':2500, 'cantidad_pkg':4, 'pkg_entregado':0},
      ]

Materiales.instantiate_list(mats)

for i in Materiales.todos:
    print(i)


area = 'm1'

mat = 'tkt'

print(Materiales.todos[area + mat])
print(Materiales.todos[area + mat].esta_excedido())

#####################################
#
#      Notes
#
#####################################

       
# Use this metho to convert a pandas data frame to dictionaries
# where each row is a dictionary and the the colunm name is the
# key
#
#   df.to_dict('records')
       
