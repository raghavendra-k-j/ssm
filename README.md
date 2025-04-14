# Small Service Manager (SSM)

## Purpose of the Application

Small Service Manager (SSM) is a simple yet powerful service management tool designed to help users easily manage and control multiple services running on a Windows system. This tool is ideal for users who work with **jar files** or any other **CMD-based services**, providing a clean interface to manage these services without manually handling the command line each time.

With **Small Service Manager**, you can:

- **Start** and **Stop** services with a single click.
- View a **list of all services** running on your system.
- **Add new services** and manage them easily through a web interface.
- **Edit** service configurations (e.g., command, port).
- **Delete services** from the list when no longer needed.

SSM is designed as a Windows-specific solution and can be a great alternative for managing **Java-based applications** or other services that require command-line execution.

---

## Features

- **Add New Service**: Add a new service by specifying its name, start command, and port.
- **Start/Stop Services**: Easily start and stop services directly from the app interface.
- **Service Editing**: Edit the service configuration while ensuring the service is stopped before modification.
- **Service Deletion**: Remove a service from the list when no longer needed.

---

## How to Run the Application on Windows

Follow these simple steps to set up and run **Small Service Manager (SSM)** on a Windows machine.

### 1. **Create a Virtual Environment**

Ensure that Python is installed on your system. Open Command Prompt or PowerShell and create a virtual environment for the project:

```bash
python -m venv ssm-env
```

### 2. **Activate the Virtual Environment**

Activate the virtual environment by running the appropriate command:

For Command Prompt:

```bash
.\ssm-env\Scripts\activate
```

For PowerShell:

```bash
.\ssm-env\Scripts\Activate.ps1
```

Once activated, you'll see `(ssm-env)` in your terminal prompt.

### 3. **Install Required Packages**

With the virtual environment active, install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all the required libraries and dependencies needed for the application to run.

### 4. **Run the Application**

Now that all dependencies are installed, you can run the Flask application:

```bash
python app.py
```

This will start the application locally. You can access the Small Service Manager by navigating to:

```
http://localhost:5000
```

### 5. **Optional: Run the Application in the Background**

If you want the application to run as a service, you can use NSSM (Non-Sucking Service Manager) or any other Windows service manager to handle the app as a background service.

---

## Troubleshooting

- **Issue with dependencies**: If you encounter any issues during the installation of dependencies, ensure that your Python version is up to date and try running `pip install --upgrade pip`.
- **Port conflicts**: If you face issues related to port conflicts, change the port number in `app.py` where the Flask app is initialized.

---

## License

This project is open source and available under the MIT License.

---

## Contributing

We welcome contributions! Please fork the repository and submit a pull request for any features or bug fixes you'd like to contribute.

---

## Contact

For any inquiries or support, feel free to contact us at [16102000.raghu@gmail.com].