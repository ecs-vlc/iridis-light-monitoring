import sys

sys.path.insert(0, '/var/www/iridis-light-monitoring')

# activate the environment
activate_this = '/root/.local/share/virtualenvs/iridis-light-monitoring-eGk6KKsR/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict=__file__=activate_this)

from app import app as application
