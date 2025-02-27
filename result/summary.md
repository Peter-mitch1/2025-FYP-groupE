# Projects in Data Science (2025)

The purpose of this repository is to develop a model which correctly identifies cancerous skin lesions.
In 2022, approximately 331,722 new cases of melanoma were diagnosed worldwide, wcrf.org.
Melenoma and Skin Cancers account around 60,000 deaths per year according to Skin Cancer Statistics wcrf.org.
In Denmark Melenoma is the 5th most comman cancer who.org.

Medical image analysis plays a crucial role in diagnosing skin conditions, such as melanoma and other dermatological diseases. However, hair in clinical images can obstruct important details, making it difficult for automated algorithms and human experts to accurately assess lesions. Removing hair from images improves the visibility of skin features, allowing for better segmentation and analysis.

In this project, we implement a hair removal method based on morphological operations and inpainting techniques using OpenCV. The method detects hair strands, creates a mask, and fills in the obstructed areas using surrounding pixel information.

While annotating the images, we generally agreed on the classification of hair presence (None, Some, A Lot). However, there were still some mismatches in ratings. The differences were mostly due to varying strictness in defining 'having hair.' Some team members classified an image as 'No Hair' only if there was absolutely no visible hair, while others were more lenient and allowed for a small presence of hair as long as it did not obstruct the lesion significantly.


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
By adjusting the morphology it can be seen that the 'tophat' function for white hairs of rating 2, results in a clearer image.
However for darker hairs 'blackhat' is better.

blackhat, thresh, img_out = removeHair(img_rgb, img_gray, kernel_size=10, threshold=2)
![output_img_0713.png](https://github.com/Peter-mitch1/2025-FYP-groupE/blob/main/data/output_img_0573BH.png)


tophat, thresh, img_out = removeHair(img_rgb, img_gray, kernel_size=10, threshold=2)
![output_img_0713.png](https://github.com/Peter-mitch1/2025-FYP-groupE/blob/main/data/output_img_0573WH.png)



The pictures with marker often get more noise after being processed. The images become more blurry therefore, the lesions appear more faded and less distinguishable on the skin. One reason for this could be that the marker causes bias in the algorithm’s colour detection. It could be a possible way forward to tackle down this problem by training the algorithm to recognise the marker as well.
A few examples for this error:
- img_0630.png
- img_0611.png
- img_0551.png













