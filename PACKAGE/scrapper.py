from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

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

        # Crear un archivo CSV
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
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

        print("Todos los productos de {} han sido guardados en {}.".format(url, csv_filename))

    def close(self):
        # Cerrar el navegador
        self.driver.quit()

def read_urls_and_filenames(filename):
    urls_and_filenames = []
    with open(filename, 'r') as file:
        for line in file:
            url, csv_filename = line.strip().split(',')
            urls_and_filenames.append((url.strip(), csv_filename.strip()))
    return urls_and_filenames

# Ejemplo de uso
def main():
    scraper = WebScraper()
    urls_and_filenames = read_urls_and_filenames('INFO/sites&files.txt')
    for url, csv_filename in urls_and_filenames:
        scraper.scrape(url, csv_filename)
    scraper.close()

if __name__ == "__main__":
    main()
