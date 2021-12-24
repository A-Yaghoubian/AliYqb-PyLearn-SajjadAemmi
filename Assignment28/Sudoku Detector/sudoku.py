import argparse
import cv2
from imutils.perspective import four_point_transform
import numpy as np

parser = argparse.ArgumentParser(description='Ali Sudoku Detector')

parser.add_argument('--input', type=str, help='Path of your input image', default='sudoku1.jpg')
parser.add_argument('--filter-size', type=int, help='Size of GaussianBlur mask', default=7)
parser.add_argument('--epsilon-parameter', type=float, help='Effective coefficient on epsilon', default=0.1)
parser.add_argument('--final-size', type=int, help='Size of final sudoku image', default=700)
parser.add_argument('--contour-color', type=int, help='1.BLUE 2.GREEN 3.RED', default=2)
parser.add_argument('--contour-thickness', type=int, help='Thickness of drawing contours', default=5)
parser.add_argument('--output', type=str, help='Path of your output image', default='output_test.jpg')
parser.add_argument('--final-output', type=str, help='Path of your final output image', default='final_output_test.jpg')

args = parser.parse_args()

try:
    img = cv2.imread(args.input)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
except:
    print('This image address is WRONG!')
    exit()
    
img_blurred = cv2.GaussianBlur(img_gray, (args.filter_size, args.filter_size), 3)
thresh = cv2.adaptiveThreshold(img_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = list(contours[0])
contours = sorted(contours, key=cv2.contourArea, reverse=True)

sudoku_contour = None

for contour in contours:
    
    epsilon = args.epsilon_parameter * cv2.arcLength(contour, True)        
    appprox = cv2.approxPolyDP(contour, epsilon, True)
    
    if len(appprox) == 4:
        sudoku_contour = appprox
        break
        
if sudoku_contour is None:
    print("Oops, I can't find sudoku.")

else:
    src_pts = np.array([sudoku_contour[1], sudoku_contour[0], sudoku_contour[3], sudoku_contour[2]], dtype=np.float32)
    dst_pts = np.array([[0, 0],   [args.final_size, 0],  [args.final_size, args.final_size], [0, args.final_size]], dtype=np.float32)

    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warp = cv2.warpPerspective(img, M, (args.final_size, args.final_size))
    
    if (args.contour_color) == 1:
        result = cv2.drawContours(img, [sudoku_contour], -1, (255, 0, 0), args.contour_thickness)
    elif (args.contour_color) == 3:
        result = cv2.drawContours(img, [sudoku_contour], -1, (0, 0, 255), args.contour_thickness)
    else:
        result = cv2.drawContours(img, [sudoku_contour], -1, (0, 255, 0), args.contour_thickness)

    cv2.imwrite(args.output, result)
    cv2.imwrite(args.final_output, warp)