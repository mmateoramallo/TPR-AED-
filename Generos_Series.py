class Gen_ser:

    def __init__(self, id_gen, nombre_gen, cant):
        self.id_gen = id_gen
        self.nombre_gen = nombre_gen
        self.cant = cant

    def __str__(self):
        return f"EL genero cuyo nombre es {self.nombre_gen}, se corresponde con el codigo {str(self.id_gen)}, y hay una cantidad de {str(self.cant)} series con dicho genero"