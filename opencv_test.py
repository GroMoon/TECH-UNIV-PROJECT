import cv2, time
from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np

class ColorDetectionModule(QThread):
    color_detected = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0)
        self.is_running = True

    def run(self):
        while self.is_running:
            _, frame = self.cap.read()
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            lower_red1 = np.array([0, 100, 100])
            upper_red1 = np.array([10, 255, 255])
            lower_red2 = np.array([160, 100, 100])
            upper_red2 = np.array([180, 255, 255])

            mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
            mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
            mask = cv2.bitwise_or(mask1, mask2)

            red_pixel_count = cv2.countNonZero(mask)

            if red_pixel_count >= 10:
                self.color_detected.emit(red_pixel_count)
            
            time.sleep(0.5)

    def stop_detection(self):
        self.is_running = False
        self.cap.release()

    def get_red_pixels(self):
        _, frame = self.cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red1 = np.array([0, 100, 100])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([160, 100, 100])
        upper_red2 = np.array([180, 255, 255])
        mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
        mask = cv2.bitwise_or(mask1, mask2)
        red_pixel_count = cv2.countNonZero(mask)
        return red_pixel_count


    def stop_detection(self):
        self.is_running = False
        self.cap.release()

    def get_red_pixels(self):
        _, frame = self.cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red1 = np.array([0, 100, 100])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([160, 100, 100])
        upper_red2 = np.array([180, 255, 255])
        mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
        mask = cv2.bitwise_or(mask1, mask2)
        red_pixel_count = cv2.countNonZero(mask)
        return red_pixel_count
