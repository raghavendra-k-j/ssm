from flask import Flask, render_template, request, redirect, url_for
import os
import xml.etree.ElementTree as ET
import platform

from waitress import serve


app = Flask(__name__)

# Path to the XML file that acts as a "database"
DATABASE_PATH = 'data.xml'

# Function to load services from XML
def load_services():
    tree = ET.parse(DATABASE_PATH)
    root = tree.getroot()
    services = []
    for index, service in enumerate(root.findall('service')):
        services.append({
            'index': index,
            'name': service.find('name').text,
            'cmd': service.find('cmd').text,
            'port': service.find('port').text,
            'status': service.find('status').text
        })
    return services

# Function to save services to XML
def save_services(services):
    tree = ET.ElementTree(ET.Element('services'))
    root = tree.getroot()
    for svc in services:
        service_elem = ET.SubElement(root, 'service')
        ET.SubElement(service_elem, 'name').text = svc['name']
        ET.SubElement(service_elem, 'cmd').text = svc['cmd']
        ET.SubElement(service_elem, 'port').text = svc['port']
        ET.SubElement(service_elem, 'status').text = svc['status']
    tree.write(DATABASE_PATH)

# Function to start a service using a new terminal window
def start_service_in_terminal(cmd):
    if platform.system() == 'Windows':
        os.system(f'start cmd /K "{cmd}"')  # Open a new command prompt and run the command
    elif platform.system() == 'Linux':
        os.system(f'gnome-terminal -- bash -c "{cmd}; exec bash"')  # Open a new terminal window and run the command
    elif platform.system() == 'Darwin':  # macOS
        os.system(f'osascript -e \'tell application "Terminal" to do script "{cmd}"\'')

# Route to display all services
@app.route('/')
def index():
    services = load_services()
    return render_template('index.html', services=services)

# Route to add a new service
@app.route('/add', methods=['POST'])
def add_service():
    name = request.form['name']
    cmd = request.form['cmd']
    port = request.form['port']

    services = load_services()

    # Adding new service to the list
    new_service = {
        'name': name,
        'cmd': cmd,
        'port': port,
        'status': 'Stopped'
    }
    services.append(new_service)

    # Save updated services list
    save_services(services)

    return redirect(url_for('index'))

# Route to delete a service
@app.route('/delete/<int:index>', methods=['GET'])
def delete_service(index):
    services = load_services()
    del services[index]
    save_services(services)
    return redirect(url_for('index'))

# Route to start a service
@app.route('/start/<int:index>', methods=['GET'])
def start_service(index):
    services = load_services()
    service = services[index]
    service['status'] = 'Running'
    save_services(services)
    # Start the service in a new terminal window
    start_service_in_terminal(service['cmd'])
    return redirect(url_for('index'))

# Route to stop a service
@app.route('/stop/<int:index>', methods=['GET'])
def stop_service_route(index):
    services = load_services()
    service = services[index]
    service['status'] = 'Stopped'
    save_services(services)
    # Here, we stop the service by using the kill command (you may opt for another method like closing terminal windows)
    if platform.system() == 'Windows':
        os.system(f'taskkill /F /IM {service["cmd"]}')  # Kill the process by name (Windows)
    elif platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system(f'pkill -f "{service["cmd"]}"')  # Kill process by command name (Linux/macOS)
    return redirect(url_for('index'))

# Route to edit a service
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_service(index):
    services = load_services()
    service = services[index]

    if request.method == 'POST':
        name = request.form['name']
        cmd = request.form['cmd']
        port = request.form['port']

        # Stop the service before editing
        stop_service_route(index)

        # Update service details
        service['name'] = name
        service['cmd'] = cmd
        service['port'] = port
        service['status'] = 'Stopped'  # Ensure it's stopped before editing

        save_services(services)
        return redirect(url_for('index'))

    return render_template('edit_service.html', service=service, index=index)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
