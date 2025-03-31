# Projects in Data Science (2025)

The purpose of this repository is to develop a model which correctly identifies cancerous skin lesions.
In 2022, approximately 331,722 new cases of melanoma were diagnosed worldwide, wcrf.org.
Melenoma and Skin Cancers account around 60,000 deaths per year according to Skin Cancer Statistics wcrf.org.
In Denmark Melenoma is the 5th most comman cancer who.org.

Medical image analysis plays a crucial role in diagnosing skin conditions, such as melanoma and other dermatological diseases. However, hair in clinical images can obstruct important details, making it difficult for automated algorithms and human experts to accurately assess lesions. Removing hair from images improves the visibility of skin features, allowing for better segmentation and analysis.

In this project, we implement a hair removal method based on morphological operations and inpainting techniques using OpenCV. The method detects hair strands, creates a mask, and fills in the obstructed areas using surrounding pixel information.

main.py holds the original file and main_test.py has the built in Image Data Loader. To run main_test.py correctly ensure the file paths are setup with the correct folders:

data directory (data_dir) should have the file path for the folder of the unprocessed images. 

save directory (save_dir) should have the file path for the folder where the processed images will be saved.

instructions can be found as comments in the file itself.

While annotating the images, we generally agreed on the classification of hair presence (None, Some, A Lot). However, there were still some mismatches in ratings. The differences were mostly due to varying strictness in defining 'having hair.' Some team members classified an image as 'No Hair' only if there was absolutely no visible hair, while others were more lenient and allowed for a small presence of hair as long as it did not obstruct the lesion significantly. Below you can see an example of an image type that would cause most disagreement: there is some hair,so it is not clear 0,but it doesn't seem to block the view of the turmoil.

![Description](https://github.com/Peter-mitch1/2025-FYP-groupE/blob/main/data/img_0582.png?raw=true)


For the images provided to the team img_524 - img_723, the default setting of the hair removal algorithm struggled more specifically with white/grey haired images, classified as hairy.
The code was run as follows below:
apply hair removal
blackhat, thresh, img_out = removeHair(img_rgb, img_gray, kernel_size=10, threshold=2)

![output_img_0713.png](https://github.com/Peter-mitch1/2025-FYP-groupE/blob/main/data/output_img_0713BH.png)

apply hair removal
tophat, thresh, img_out = removeHair(img_rgb, img_gray, kernel_size=10, threshold=2)
![output_img_0713.png](https://github.com/Peter-mitch1/2025-FYP-groupE/blob/main/data/output_img_0713WH.png)

"In mathematical morphology and digital image processing, a top-hat transform is an operation that extracts small elements and details from given images. There exist two types of top-hat transform: the white top-hat transform is defined as the difference between the input image and its opening by some structuring element, while the black top-hat transform is defined dually as the difference between the closing and the input image."
https://en.wikipedia.org/wiki/Top-hat_transform

In OpenCV black top-hat is known as 'blackhat' and white top-hat is known as 'tophat'.
These functions are used in the inpaint_util.py which is called through main.py and main_test.py respectively.

tophat function is tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat function is blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

[OpenCV has great documentation](https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html) for other transformations that can be applied.
By adjusting the morphology it can be seen that the 'tophat' function for white hairs of rating 2, results in a clearer image.
However for darker hairs 'blackhat' is better.

blackhat, thresh, img_out = removeHair(img_rgb, img_gray, kernel_size=10, threshold=2)
![output_img_0573.png](https://github.com/Peter-mitch1/2025-FYP-groupE/blob/main/data/output_img_0573BH.png)


tophat, thresh, img_out = removeHair(img_rgb, img_gray, kernel_size=10, threshold=2)

![output_img_0573.png](https://github.com/Peter-mitch1/2025-FYP-groupE/blob/main/data/output_img_0573WH.png)

We could, moving forward, make the program regonize if the hair is more black or more white, and then use "blackhat" and "tophat" functions respectively. By doing that, we get the best possible outcomes from the pictures with both the white hair and black hair. 



We discovered that that pictures with marker often get more noise after being processed. The images become more blurry therefore, the lesions appear more faded and less distinguishable on the skin. One reason for this could be that the marker causes bias in the algorithm’s colour detection. It could be a possible way forward to tackle down this problem by training the algorithm to recognise the marker as well.


Examples for this error (processed picture first):


![output_img_0611.png](https://github.com/Peter-mitch1/2025-FYP-groupE/blob/main/data/output_img_0611.png)
![img_0611.png](https://github.com/Peter-mitch1/2025-FYP-groupE/blob/main/data/img_0611.png)
![output_img_0551.png](https://github.com/Peter-mitch1/2025-FYP-groupE/blob/main/data/output_img_0551.png)
![img_0551.png](https://github.com/Peter-mitch1/2025-FYP-groupE/blob/main/data/img_0551.png)

One possible approach to fix this error is to first identify if there is a marker by finding the color of possible markers, which in this dataset most often appears as black and darkblue. Instead of converting the image to grayscale, we can convert it to HSV and define a suitable HSV range to distinguish the marked area. For blue markers, an effective range would be:

Lower bound: [100, 150, 0]

Upper bound: [140, 255, 255]

If a marker is found, we can use the inpaint function to replace it with a background color that matches the person’s skin tone, just like in the hair removal process.

However, when the lesion and the marker have similar colors, it will be difficult for the algorithm to differentiate between them. And the same if the color of the pen is not known by the program. In such cases, alternative methods can be explored, such as analyzing the shape and compactnes of both the lesion and the marker. Since lesions typically have irregular, compact shapes, whereas markers tend to form thin lines or not compact circular patterns, we could use this distinction to identify and remove the marker while preserving the lesion. 

