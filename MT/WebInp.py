from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import requests

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("""
<!DOCTYPE html>
<html>
<head>
  <script>
      function buttPress() {
        document.getElementById("PRESS").innerHTML = "TRUE";
        document.getElementById("HID").value = "TRUE";
        var nameValue = document.getElementById("FileInp").value;
        console.log(nameValue);
      }
  </script>
  <meta charset="UTF-8">
  <title>The Three W's</title>
  <link rel="stylesheet" type="text/css" href="path to css stylesheet">
</head>
<body>
  <h1>
    The Three W's
  </h1>
  <h2>
    Word, Were, Work.
  </h2>
  <div>
    <input name="FileInp" id="FileInp" type="file" accept=".wav">
  </div>
  <p>Enter a .wav file above</p>
  <p id="PRESS" value="FALSE">FALSE</p>
    <form method="POST">
    <br>    <button name="Sub" onclick="buttPress()">Submit</button><br>
  <input type="hidden" id="HID" name="HID" value="FALSE">
   </form>
   <form ENCTYPE=\"multipart/form-data\" method=\"post\">
    <input name=\"file\" type=\"file\"/>
    <input type=\"submit\" value=\"upload\"/></form>\n
</body>
</html>

            ""","utf8"))
        return

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        themood = str(form["HID"].value).strip()
        #url = 'http://172.31.66.53:8181/'
        #files = {'file': open('gestTema.txt', 'rb')}
        #r = requests.post(url, files=files)
        for i in themood:
            print(i+"\n")
        if themood == "TRUE":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes("""
            <html><head></head>
            <body>
            <iframe width="1903" height="764" src="https://www.youtube.com/embed/17KmNrG9pE4" frameborder="0" gesture="media" allowfullscreen></iframe>
            </body>
            </html>

            
            ""","utf8"))
        return
            
server = HTTPServer(('172.31.66.53', 8181), Handler)
server.serve_forever()
