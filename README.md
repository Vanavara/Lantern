<h1>Network-controlled Lantern</h1>
<h3>This project is an implementation of a network-controlled lantern using FastAPI and Docker. The flashlight communicates with the flashlight server over a TCP connection using the Flashlight Control Protocol (FCP).</h3>

<h2>Installation and Setup</h2>
<h3>Before getting started, make sure you have Docker and Docker Compose installed on your system. Then follow these steps:

1. Clone the repository to your machine:
git clone https://github.com/your-username/flashlight.git
cd flashlight
2. Configure the host and port of the flashlight server. By default, it uses 127.0.0.1:9999.
3. Build and start the Docker containers:
docker-compose up -d --build
4. The flashlight will be available at http://localhost:8000.</h3>

<h2>Network-controlled Flashlight</h2>
<h3>This project is an implementation of a network-controlled flashlight using FastAPI and Docker. The flashlight communicates with the flashlight server over a TCP connection using the Flashlight Control Protocol (FCP).</h3>

<h2>Usage</h2>
.<h3>You can use any tool to send commands to the lantern following the Flashlight Control Protocol (FCP) over a TCP connection. Commands should be sent in JSON format, adhering to FCP version 1..</h3>

<h3>You can use SWAGGER (http://localhost:8000/docs), PowerShell, Postman e.t.c. to send command to the lantern. 
GET method allow us heve info concernint current lantern status
PUT methods allow us change the status (ON/OFF) and change the color of light.</h3>

<h2>Error Handling and Exceptions</h2>
<h3>This flashlight implementation handles errors and exceptions. You can customize errors based on your own taste.</h3>

<h2>Shutdown</h2>
<h3>To stop the flashlight and the associated Docker containers, run the following command:
docker-compose down</h3>
