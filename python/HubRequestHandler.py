from http.server import HTTPServer, SimpleHTTPRequestHandler
import time
from urllib.parse import urlparse, parse_qs, urlsplit


class HubRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        res = urlsplit(self.path)

        if res.path == "/":
            # home page
            self.writeHeader()
            self.writeHTML(
                """
            <html>
            <head>
                <style>
                /* Style the tab */
                .tab {
                overflow: hidden;
                border: 1px solid #ccc;
                background-color: #f1f1f1;
                }

                /* Style the buttons inside the tab */
                .tab button {
                background-color: inherit;
                float: left;
                border: none;
                outline: none;
                cursor: pointer;
                padding: 14px 16px;
                transition: 0.3s;
                font-size: 17px;
                }

                /* Change background color of buttons on hover */
                .tab button:hover {
                background-color: #ddd;
                }

                /* Create an active/current tablink class */
                .tab button.active {
                background-color: #ccc;
                }

                /* Style the tab content */
                .tabcontent {
                display: none;
                padding: 6px 12px;
                border: 1px solid #ccc;
                border-top: none;
                }
                </style>
            </head>
            <body>
            
            <img src="data:image/png;base64,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">
            <h2>Taeho</h3>
            <!-- Desc here -->
            <h4>Arduino Controller with Python web server</h2>
            
            <div class="tab">
            <button class="tablinks" onclick="openTab(event, 'Volt')">Volt</button>
            <button class="tablinks" onclick="openTab(event, 'Light')">Light</button>
            <button class="tablinks" onclick="openTab(event, 'Servo')">Servo</button>
            <button class="tablinks" onclick="openTab(event, 'LED')">LED</button>
            <button class="tablinks" onclick="openTab(event, 'Buzzer')">Buzzer</button>
            </div>

            <div id="Volt" class="tabcontent">
            <h3>Volt</h3>
            <p><a href="/MeasOneVolt">MeasOneVolt</a></p>
            <p><a href="/Samplevolt">Samplevolt</a></p>
            </div>

            <div id="Light" class="tabcontent">
            <h3>Light</h3>
            <p><a href="/MeasOneLight">MeasOneLight</a></p>
            <p><a href="/Samplelight">Samplelight</a></p>
            </div>

            <div id="Servo" class="tabcontent">
            <h3>Servo</h3>
            <p><a href="/ServoMove">ServoMove</a></p>
            <p><a href="/ServoMove90">ServoMove90</a></p>
            <p><a href="/ServoMove180">ServoMove180</a></p>
            </div>

            <div id="LED" class="tabcontent">
            <h3>LED</h3>
            <p><a href="/led">led</a></p>
            </div>

            <div id="Buzzer" class="tabcontent">
            <h3>Buzzer</h3>
            <p><a href="/buzzer">buzzer</a></p>
            </div>

            <script>
            function openTab(evt, tabName) {
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tabcontent");
            for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].style.display = "none";
            }
            tablinks = document.getElementsByClassName("tablinks");
            for (i = 0; i < tablinks.length; i++) {
                tablinks[i].className = tablinks[i].className.replace(" active", "");
            }
            document.getElementById(tabName).style.display = "block";
            evt.currentTarget.className += " active";
            }
            </script>

            </body>
            </html>
            """
            )

        elif res.path == "/MeasOneVolt":
            ntime = time.time()
            volt = self.server.gateway.saveVoltToDB()
            self.server.gateway.clearVoltTuple()
            self.server.gateway.loadFromDB()
            count = self.server.gateway.countVoltDB()
            mean = self.server.gateway.getVoltMeanPD()
            dev = self.server.gateway.getVoltstdevPD()
            med = self.server.gateway.getVoltMedianPD()
            self.writeHeader()
            self.writeHTML("<html><body><h1>Volt</h1>")
            self.writeHTML("<p>Volt page</p>")
            self.writeHTML("<p>Volt: " + str(volt) + "</p>")
            self.writeHTML("<p>Time: " + str(ntime) + "</p>")
            self.writeHTML("<p>Count: " + str(count) + "</p>")
            self.writeHTML("<p>Mean: " + str(mean) + "</p>")
            self.writeHTML("<p>Dev: " + str(dev) + "</p>")
            self.writeHTML("<p>Med: " + str(med) + "</p>")
            self.writeHTML(self.server.gateway.writeHtmlVoltTuple())
            self.writeHTML("</body></html>")
            pass

        elif res.path == "/Samplevolt":
            self.writeHeader()
            ntime = time.time()

            self.writeHTML("<html><body><h1>Samplevolt</h1>")
            self.writeHTML("<p>Samplevolt page</p>")
            # input box and save value to count and delay
            self.writeHTML("<form action='/Samplevolt' method='get'>")
            self.writeHTML("<input type='text' name='count' value='0'>")
            self.writeHTML("<input type='text' name='delay' value='0'>")
            self.writeHTML("<input type='submit' value='submit'>")

            if res.query != "":
                qdict = parse_qs(res.query)
                count = int(qdict["count"][0])
                delay = int(qdict["delay"][0])

            self.server.gateway.clearVoltTuple()
            self.server.gateway.samplingVoltandSaveToTuple(delay, count)
            self.server.gateway.saveVoltToDB()

            self.writeHTML("<p>Count: " + str(count) + "</p>")
            self.writeHTML("<p>Delay: " + str(delay) + "</p>")
            self.writeHTML("<p>Time: " + str(ntime) + "</p>")
            self.writeHTML(
                "<p>Mean: " + str(self.server.gateway.getVoltMeanPD()) + "</p>"
            )
            self.writeHTML(
                "<p>Dev: " + str(self.server.gateway.getVoltstdevPD()) + "</p>"
            )
            self.server.gateway.clearVoltTuple()
            self.server.gateway.loadFromDB()
            self.writeHTML(self.server.gateway.writeHtmlVoltTuple())
            self.writeHTML("</body></html>")
            pass

        elif res.path == "/MeasOneLight":
            ntime = time.time()
            light, lightstep = self.server.gateway.saveLightToDB()
            self.server.gateway.clearLightTuple()
            self.server.gateway.loadLightFromDB()
            count = self.server.gateway.countLightDB()
            mean = self.server.gateway.getLightMeanPD()
            dev = self.server.gateway.getLightstdevPD()
            med = self.server.gateway.getLightMedianPD()
            self.writeHeader()
            self.writeHTML("<html><html><head><title>Light</title></head>")
            self.writeHTML("<body><h1>Light</h1>")
            self.writeHTML("<p>Light page</p>")
            self.writeHTML("<p>Light: " + str(light) + "</p>")
            self.writeHTML("<p>Light Step: " + str(lightstep) + "</p>")
            self.writeHTML("<p>Time: " + str(ntime) + "</p>")
            self.writeHTML("<p>Count: " + str(count) + "</p>")
            self.writeHTML("<p>Mean: " + str(mean) + "</p>")
            self.writeHTML("<p>Dev: " + str(dev) + "</p>")
            self.writeHTML("<p>Med: " + str(med) + "</p>")
            self.writeHTML(self.server.gateway.writeHtmlLightTuple())
            self.writeHTML("</body></html>")
            pass

        elif res.path == "/Samplelight":
            ntime = time.time()
            self.writeHeader()
            self.writeHTML("<html><body><h1>Samplelight</h1>")
            self.writeHTML("<p>Samplelight page</p>")
            # input box and save value to count and delay
            self.writeHTML("<form action='/Samplelight' method='get'>")
            self.writeHTML("<input type='text' name='count' value='0'>")
            self.writeHTML("<input type='text' name='delay' value='0'>")
            self.writeHTML("<input type='submit' value='submit'>")
            self.server.gateway.clearLightTuple()
            if res.query != "":
                qdict = parse_qs(res.query)
                count = int(qdict["count"][0])
                delay = int(qdict["delay"][0])

            self.server.gateway.clearLightTuple()
            self.server.gateway.samplingVoltandSaveToTuple(delay, count)
            self.server.gateway.saveLightToDB()
            self.writeHTML("<p>Count: " + str(count) + "</p>")
            self.writeHTML("<p>Delay: " + str(delay) + "</p>")
            self.writeHTML("<p>Time: " + str(ntime) + "</p>")
            self.writeHTML(
                "<p>Mean: " + str(self.server.gateway.getLightMeanPD()) + "</p>"
            )
            self.writeHTML(
                "<p>Dev: " + str(self.server.gateway.getLightstdevPD()) + "</p>"
            )
            self.server.gateway.clearLightTuple()
            self.server.gateway.loadLightFromDB()
            self.writeHTML(self.server.gateway.writeHtmlLightTuple())
            self.writeHTML("</body></html>")
            pass

        elif res.path == "/ServoMove":
            self.writeHeader()
            self.writeHTML("<html><body><h1>ServoMove</h1>")
            self.writeHTML("<p>ServoMove page</p>")
            # input box and save value to degree
            self.writeHTML("<form action='/ServoMove' method='get'>")
            self.writeHTML("<input type='text' name='degree' value='0'>")
            self.writeHTML("<input type='submit' value='submit'>")
            self.writeHTML("</form>")

            if res.query != "":
                qdict = parse_qs(res.query)
                degree = int(qdict["degree"][0])
            self.server.gateway.setServo(degree)
            self.writeHTML("</body></html>")
            pass

        elif res.path == "/ServoMove90":
            self.writeHeader()
            self.writeHTML("<html><body><h1>ServoMove90</h1>")
            self.writeHTML("<p>ServoMove90 page</p>")
            self.server.gateway.setServo(90)
            self.writeHTML("</body></html>")
            pass

        elif res.path == "/ServoMove180":
            self.writeHeader()
            self.writeHTML("<html><body><h1>ServoMove180</h1>")
            self.writeHTML("<p>ServoMove180 page</p>")
            self.server.gateway.setServo(180)
            self.writeHTML("</body></html>")
            pass

        elif res.path == "/led":
            self.writeHeader()
            self.writeHTML("<html><body><h1>led</h1>")
            self.writeHTML("<p>led page</p>")
            # input box and save value to count and delay
            self.writeHTML("<form action='/led' method='get'>")
            self.writeHTML("<input type='text' name='led' value='0'>")
            self.writeHTML("<input type='submit' value='submit'>")
            self.writeHTML("</form>")
            if res.query != "":
                qdict = parse_qs(res.query)
                led = qdict["led"][0]
            self.server.gateway.setLed(led)
            self.writeHTML("</body></html>")

        elif res.path == "/buzzer":
            self.writeHeader()
            self.writeHTML("<html><body><h1>buzzer</h1>")
            self.writeHTML("<p>buzzer page</p>")
            # input box and save value to freq and duration
            self.writeHTML("<form action='/buzzer' method='get'>")
            self.writeHTML("<input type='text' name='buzzer' value='0'>")
            self.writeHTML("<input type='text' name='buzzer' value='0'>")
            self.writeHTML("<input type='submit' value='submit'>")
            self.writeHTML("</form>")
            if res.query != "":
                qdict = parse_qs(res.query)
                freq = qdict["buzzer"][0]
                duration = qdict["buzzer"][1]
            self.server.gateway.setBuzzer(freq, duration)
            self.writeHTML("</body></html>")

        else:
            self.writeHeader(404)
            self.writeHTML("<html><body><h1>404</h1>")
            self.writeHTML("<p>404 page</p>")
            self.writeHTML("</body></html>")
            pass

    def writeHeader(self, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def writeHTML(self, html):
        self.wfile.write(html.encode())
