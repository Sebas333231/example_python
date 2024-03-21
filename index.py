from http.server import BaseHTTPRequestHandler, HTTPServer 
#HTTPServer Representa un servidor HTTP que puede escuchar conexiones en un determinado puerto.
# BaseHTTPRequestHandler Se utiliza para manejar las solicitudes HTTP que llegan al servidor.
#Importo las librerias necesarias para el procedimiento

#Creo una clase principal y le paso un parametro
class Principal(BaseHTTPRequestHandler): 
    #Creo una función
    def do_GET(self):
        #Responde codigo 200
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        #Establece el tipo de contenido
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hola Mundo</title>
        </head>
        <body>
            <h1>Hola Mundo desde Python!</h1>
        </body>
        </html>
        """
        #escribe la respuesta HTML en el flujo de escritura del cliente
        self.wfile.write(html.encode('utf-8'))

def run_server():
    #Configuro la direccion y el puerto del servidor
    server_address = ('', 2020)
    #Creo una instancia del servidor HTTP con la clase HTTPServer
    httpd = HTTPServer(server_address, Principal)
    #Imprime un mensaje
    print('Servidor iniciado :)')
    #Mantiene el servidor en ejecucion indefinido
    httpd.serve_forever()

if __name__ == '__main__':
    #llama a la funcion run_server si el script se ejecuta directamente
    run_server()
