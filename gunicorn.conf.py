# Gunicorn configuration file

# Server socket
bind = '0.0.0.0:5000'
backlog = 2048

# Worker processes
workers = 4
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Process naming
proc_name = 'bluetoothctl-api'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL (uncomment and configure if needed)
# keyfile = None
# certfile = None
