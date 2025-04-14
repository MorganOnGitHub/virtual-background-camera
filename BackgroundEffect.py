import pyvirtualcam
import cv2
import mediapipe as mp
import numpy as np
import os

class BackgroundEffect:
    def __init__(self, source=0, blur_strength=(55, 55), model_selection=1,
                 replace_bg=False, bg_image_path=None):
        self.source = source
        self.blur_strength = blur_strength
        self.model_selection = model_selection
        self.replace_bg = replace_bg
        self.bg_image_path = bg_image_path

        # Camera
        self.cap = cv2.VideoCapture(self.source)
        if not self.cap.isOpened():
            raise ValueError(f"Unable to open video source: {self.source}")

        self.segmentation = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=self.model_selection)

        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS) or 30

        # Load background image
        if self.replace_bg:
            if self.bg_image_path and os.path.exists(self.bg_image_path):
                self.bg_image = cv2.imread(self.bg_image_path)
                if self.bg_image is None:
                    raise ValueError(f"Failed to load background image: {self.bg_image_path}")
            else:
                self.bg_image = cv2.imread("images/default.jpg")
                if self.bg_image is None:
                    raise ValueError("Failed to load fallback background image.")
            self.bg_image = cv2.resize(self.bg_image, (self.width, self.height))

    def process_frame(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.segmentation.process(rgb)
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        background = self.bg_image if self.replace_bg else cv2.GaussianBlur(frame, self.blur_strength, 0)
        output = np.where(condition, frame, background)
        return output

    def run(self):
        with pyvirtualcam.Camera(width=self.width, height=self.height, fps=int(self.fps)) as cam:
            print(f"Virtual camera started: {cam.device}")
            print("Press 'q' to quit.")

            while self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    break

                frame = cv2.flip(frame, 1)
                processed = self.process_frame(frame)

                # Show in window
                cv2.imshow("Background Effect", processed)

                # Send to virtual cam
                cam.send(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB))
                cam.sleep_until_next_frame()

                # Exit on 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            self.cap.release()
            cv2.destroyAllWindows()
