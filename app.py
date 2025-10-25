from flask import Flask, request, jsonify
import subprocess
import re

app = Flask(__name__)

def is_valid_mac_address(mac):
    """Validate MAC address format"""
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return re.match(pattern, mac) is not None

@app.route('/connect', methods=['GET'])
def connect_bluetooth():
    """
    Endpoint to connect to a Bluetooth device using bluetoothctl.
    Query parameter: uid (MAC address of the Bluetooth device)
    Example: /connect?uid=50:1B:6A:F4:F3:2F
    """
    uid = request.args.get('uid')

    if not uid:
        return jsonify({
            'error': 'Missing required parameter: uid',
            'example': '/connect?uid=50:1B:6A:F4:F3:2F'
        }), 400

    # Validate MAC address format
    if not is_valid_mac_address(uid):
        return jsonify({
            'error': 'Invalid MAC address format',
            'provided': uid,
            'expected_format': 'XX:XX:XX:XX:XX:XX'
        }), 400

    try:
        # Run bluetoothctl connect command
        result = subprocess.run(
            ['bluetoothctl', 'connect', uid],
            capture_output=True,
            text=True,
            timeout=30
        )

        return jsonify({
            'uid': uid,
            'command': f'bluetoothctl connect {uid}',
            'returncode': result.returncode,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'success': result.returncode == 0
        }), 200 if result.returncode == 0 else 500

    except subprocess.TimeoutExpired:
        return jsonify({
            'error': 'Command timed out after 30 seconds',
            'uid': uid
        }), 504
    except FileNotFoundError:
        return jsonify({
            'error': 'bluetoothctl command not found. Is bluetooth installed?'
        }), 500
    except Exception as e:
        return jsonify({
            'error': f'Unexpected error: {str(e)}',
            'uid': uid
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
