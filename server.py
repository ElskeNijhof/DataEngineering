# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import pickle

with open("Titanic_model.pkl", 'rb') as file:
    pickle_model = pickle.load(file)

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        parameters = self.path.split("/")

        try:
            age = int(parameters[1])
            ship_class = int(parameters[2])
            pred = pickle_model.predict([[int(parameters[1]), int(parameters[2])]])[0]
        except:
            pred = -1
        result = {
            "Name": "Tom",
            "Parameters": parameters,
            "prediction" : float(pred)
        }
        self.wfile.write(bytes(json.dumps(result).encode("utf-8")))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

    #  To do: port van de server exposen? 
    # -p 