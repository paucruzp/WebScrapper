import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página web de la que queremos extraer datos
url = 'https://emprendedores.es/gestion/business-angels-inversores/'

# Headers para simular una solicitud desde un navegador web
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

# Realizar la solicitud GET a la URL
response = requests.get(url, headers=headers)
response.raise_for_status()  # Verificar que la solicitud fue exitosa

# Parsear el contenido HTML con BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
data = []

# Asumiendo que cada <h3> contiene un nombre y el siguiente <p> contiene la descripción
for h3 in soup.find_all('h3'):
    name = h3.get_text(strip=True)
    p = h3.find_next('p')  # Encontrar el primer <p> después de <h3>
    description = p.get_text(strip=True) if p else ""

    data.append({
        'Name': name,
        'Description': description
    })

# Crear DataFrame de pandas con los datos
df = pd.DataFrame(data)

# Guardar en un archivo Excel
df.to_excel('business_angels.xlsx', index=False)

print("Datos guardados en 'business_angels.xlsx'.")
