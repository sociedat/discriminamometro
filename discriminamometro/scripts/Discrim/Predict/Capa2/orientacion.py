from Discrim.Predict import base_modelos

class Orientacion(base_modelos.BasePredict):
    
    def __init__(self):
        
        # Instanciamos la clase padre
        super().__init__()
        
        # Escribimos la información referente a esta clase
        self.str_ruta_modelo_s3 = '01_modelos/capa2/orientacion/modelo_capa2_orientacion.p'
        self.str_archivo_modelo_local = 'modelo_capa2_orientacion.p'
        
        # Descargamos de s3 y cargamos el modelo correspondiente
        self.descargar_modelo()
        self.cargar_modelo()
        
        return