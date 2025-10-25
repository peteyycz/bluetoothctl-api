# Bluetoothctl API

A simple Flask API to control Bluetooth connections via `bluetoothctl`.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Start the server:

```bash
python app.py
```

The server will run on `http://localhost:5000`

## Endpoints

### Connect to Bluetooth Device

```
GET /connect?uid=<MAC_ADDRESS>
```

**Parameters:**
- `uid` (required): MAC address of the Bluetooth device (e.g., `50:1B:6A:F4:F3:2F`)

**Example:**
```bash
curl "http://localhost:5000/connect?uid=50:1B:6A:F4:F3:2F"
```

**Response:**
```json
{
  "uid": "50:1B:6A:F4:F3:2F",
  "command": "bluetoothctl connect 50:1B:6A:F4:F3:2F",
  "returncode": 0,
  "stdout": "Attempting to connect to 50:1B:6A:F4:F3:2F...",
  "stderr": "",
  "success": true
}
```

### Health Check

```
GET /health
```

**Example:**
```bash
curl http://localhost:5000/health
```

**Response:**
```json
{
  "status": "healthy"
}
```

## Requirements

- Python 3.6+
- Flask
- `bluetoothctl` command-line tool (usually part of BlueZ package on Linux)

## Installation on Raspbian Lite

1. Install Python and Flask:
```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install Flask==3.0.0
```

2. Copy the application to your Raspberry Pi:
```bash
# Create directory
sudo mkdir -p /home/peteyycz/bluetoothctl-api

# Copy files
sudo cp app.py /home/peteyycz/bluetoothctl-api/
sudo cp requirements.txt /home/peteyycz/bluetoothctl-api/
sudo chown -R peteyycz:peteyycz /home/peteyycz/bluetoothctl-api
```

3. Install and enable the systemd service:
```bash
# Copy service file
sudo cp bluetoothctl-api.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable service to start on boot
sudo systemctl enable bluetoothctl-api.service

# Start the service
sudo systemctl start bluetoothctl-api.service

# Check status
sudo systemctl status bluetoothctl-api.service
```

4. View logs:
```bash
# View service logs
sudo journalctl -u bluetoothctl-api.service -f
```

5. Manage the service:
```bash
# Stop the service
sudo systemctl stop bluetoothctl-api.service

# Restart the service
sudo systemctl restart bluetoothctl-api.service

# Disable service from starting on boot
sudo systemctl disable bluetoothctl-api.service
```
