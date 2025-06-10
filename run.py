from app import initialize_app
import threading
from . import simulator  # Import the simulator module from the same directory

app = initialize_app()

if __name__ == '__main__':
    simulator_thread = threading.Thread(target=simulator.run_simulator)
    simulator_thread.daemon = True  # Allow the main program to exit even if the thread is running
    simulator_thread.start()
    app.run(debug=True)