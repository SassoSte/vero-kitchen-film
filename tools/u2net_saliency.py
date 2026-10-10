"""Full-frame U2-Net saliency for a box (local ~/.u2net/u2net.onnx via OpenCV DNN).
usage: u2net_saliency.py IMAGE x0 y0 x1 y1 OUT_PNG"""
import os, sys
import cv2
import numpy as np
img = cv2.imread(sys.argv[1]); x0, y0, x1, y1 = map(int, sys.argv[2:6])
net = cv2.dnn.readNetFromONNX(os.path.expanduser('~/.u2net/u2net.onnx'))
c = cv2.cvtColor(img[y0:y1, x0:x1], cv2.COLOR_BGR2RGB).astype(np.float32) / 255.
c = (cv2.resize(c, (320, 320)) - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]
net.setInput(c.transpose(2, 0, 1)[None].astype(np.float32)); s = net.forward()[0, 0]
s = (s - s.min()) / (s.max() - s.min() + 1e-6)
full = np.zeros(img.shape[:2], np.float32); full[y0:y1, x0:x1] = cv2.resize(s, (x1 - x0, y1 - y0))
cv2.imwrite(sys.argv[6], (full * 255).astype(np.uint8))
