import requests
 
url = 'https://www.web.onpe.gob.pe/modElecciones/elecciones/elecciones2016/PRP2V2016/generar_datos_participacion_excel.php?tipoCobertura=Nacional&ubigeo=020200-Pie.html'
 
myfile = requests.get(url)
 
open('PythonImage.xls', 'wb').write(myfile.content)
