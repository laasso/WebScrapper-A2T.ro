# scraper/webscraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import os

class WebScraper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')  # Para ejecutar en modo sin cabeza (sin abrir una ventana de navegador)
        self.driver = webdriver.Chrome(options=self.options)

    def scrape(self, url, csv_filename):
        # Cargar la página web
        self.driver.get(url)

        # Esperar unos segundos para asegurarse de que la página se cargue completamente (puedes ajustar el tiempo según sea necesario)
        time.sleep(5)

        # Simular desplazamiento hacia abajo para cargar más elementos
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            # Desplazarse hacia abajo
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Esperar a que se carguen los nuevos elementos
            time.sleep(2)
            # Calcular nueva altura de la página
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Encontrar todos los elementos que contienen los detalles de los productos
        productos = self.driver.find_elements(By.CLASS_NAME, 'product-item')

        # Crear un archivo CSV en la ruta especificada
        csv_path = os.path.join(csv_filename)  # Reemplaza "ruta" con la ruta específica
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            # Crear el escritor CSV
            writer = csv.writer(csvfile)
            # Escribir encabezados
            writer.writerow(['Product', 'Price'])

            # Iterar sobre los elementos de productos y extraer nombres y precios
            for producto in productos:
                # Extraer nombre del producto
                nombre = producto.find_element(By.CLASS_NAME, 'product-item-link').text.strip()

                # Extraer precio del producto
                precio = producto.find_element(By.CLASS_NAME, 'price').text.strip()

                # Escribir en el archivo CSV
                writer.writerow([nombre, precio])

        print("Todos los productos de {} han sido guardados en {}.".format(url, csv_path))

    def close(self):
        # Cerrar el navegador
        self.driver.quit()
