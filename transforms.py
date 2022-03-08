import cv2

class transforms:
    def __init__(self):
        self.glow_strength = 3 # 0: no glow, no maximum
        self.glow_radius = 25 # blur radius
    
    def filterHologram(self, _img):
        img_blurred = cv2.GaussianBlur(_img, (self.glow_radius, self.glow_radius), 1)
        img_blended = cv2.addWeighted(_img, 1, img_blurred, self.glow_strength, 0)
        return img_blended

