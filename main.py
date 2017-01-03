import cv2


def sketch(img):
    bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(bw_img, (5, 5), 0)
    edge_img = cv2.Canny(blur_img, 10, 70)
    ret, mask = cv2.threshold(edge_img, 90, 255, cv2.THRESH_BINARY_INV)
    return mask


cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    cv2.imshow("Sketchy", sketch(img))
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(-1)
