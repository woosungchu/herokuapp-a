import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#from flask_script import Manager, Server
from tumblelog import app

#manager = Manager(app)

#manager.add_command("runserver", Server(use_debugger = True , use_reloader=True, host='0.0.0.0', port=5000),)

#if __name__ == "__main__":
#    app.debug = app.config['DEBUG']
#    capture_all_args = True
#    manager.run()
#    port = int(os.environ.get('$PORT')) or 30133
#    port = int(os.getenv('$PORT',5000))
#    app.run(host='0.0.0.0',port=port)
#     app.run()

if __name__ == '__main__':
    if app.debug: use_debugger = True
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)