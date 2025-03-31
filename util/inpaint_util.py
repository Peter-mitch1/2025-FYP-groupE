import cv2

def removeHair(img_org, img_gray, kernel_size=25, threshold=10, radius=3, method="blackhat"):
    # kernel for the morphological filtering
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))

    # perform the morphological filtering based on the method
    if method == "blackhat":
        transform = cv2.morphologyEx(img_gray, cv2.MORPH_BLACKHAT, kernel)
    elif method == "tophat":
        transform = cv2.morphologyEx(img_gray, cv2.MORPH_TOPHAT, kernel)
    else:
        raise ValueError("Method must be 'blackhat' or 'tophat'")

    # intensify the hair contours in preparation for the inpainting algorithm
    _, thresh = cv2.threshold(transform, threshold, 255, cv2.THRESH_BINARY)

    # inpaint the original image depending on the mask
    img_out = cv2.inpaint(img_org, thresh, radius, cv2.INPAINT_TELEA)

    return transform, thresh, img_out