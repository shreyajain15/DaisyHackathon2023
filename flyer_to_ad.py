import PIL
import cv2
import imageai

from imageai.Detection import ObjectDetection

obj_detector = ObjectDetection()

obj_detector.setModelTypeAsYOLOv3()

detected_objects = obj_detector.detectObjectsFromImage(input_image="freshco_flyer_4.png", output_image="filtered.png")