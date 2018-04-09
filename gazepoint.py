import time
import threading
from tools import OpenGazeTracker

class GazePoint(threading.Thread):

    def __init__(self, ip='127.0.0.1', port=4242):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interrupted = threading.Lock()

        self.gaze_position = (None, None)

        self.open(ip, port)
        self.start()
        self.wait_until_running()

    def get_gaze_position(self):
        return self.gaze_position

    def run(self):
        self.interrupted.acquire()
        while self.interrupted.locked():
            self.gaze_position = self.tracker.sample()

    def stop(self):
        self.interrupted.release()
        self.close()

    def open(self, ip, port):
        print 'Setting Up Gaze Point device, this takes about 10 seconds'
        self.tracker = OpenGazeTracker(ip=ip, port=port)
        self.tracker.calibrate()
        self.tracker.enable_send_data(True)

    def close(self):
        print 'Closing connection to Gaze Point device, this takes about 5 seconds'
        self.tracker.enable_send_data(False)
        self.tracker.close()

    def __del__(self):
        self.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def wait_until_running(self, sleep_time=0.01):
        while not self.interrupted.locked():
            time.sleep(sleep_time)


if __name__ == '__main__':

    gazetracker = GazePoint()

    start = time.time()
    while time.time() - start < 5:
        print gazetracker.get_gaze_position()
        time.sleep(0.1)

    gazetracker.stop()
