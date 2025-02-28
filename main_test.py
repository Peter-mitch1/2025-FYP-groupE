import os
from os.path import join
import matplotlib.pyplot as plt

from util.img_util import readImageFile, saveImageFile
from util.inpaint_util import removeHair

# Define directories
#Currently setup for windows where r'filepath' ensure that underscores and correct backslashes
data_dir = r"C:\Users\Peter\Documents\Data Science\Semester 2 - Projects in Data Science\Mandatory Assignment\data\data"
save_dir = r"C:\Users\Peter\Documents\Data Science\Semester 2 - Projects in Data Science\Mandatory Assignment\2025-FYP-groupE\result"

# Ensure save directory exists
os.makedirs(save_dir, exist_ok=True)

# Track last successfully processed image
last_processed_image = None

# Iterate over the range of image numbers
for i in range(524, 724):  # Covers img_0524.png to img_0723.png (the range group E was requested to cover)
    file_name = f"img_{i:04d}.png"  # Format with leading zeros
    file_path = join(data_dir, file_name)

    if not os.path.exists(file_path):
        print(f"Skipping {file_name}: File does not exist.")
        continue

    try:
        # Read image
        img_rgb, img_gray = readImageFile(file_path)

        # Apply hair removal
        blackhat, thresh, img_out = removeHair(img_rgb, img_gray, kernel_size=10, threshold=2)

        # Save processed image
        save_file_path = join(save_dir, f"output_{file_name}")
        saveImageFile(img_out, save_file_path)
        print(f"Processed and saved: {save_file_path}")

        # Store last processed image for visualization
        last_processed_image = (img_rgb, blackhat, thresh, img_out)

    except Exception as e:
        print(f"Error processing {file_name}: {e}")

# Visualize the last processed image
if last_processed_image:
    img_rgb, blackhat, thresh, img_out = last_processed_image

    plt.figure(figsize=(15, 10))

    images = [img_rgb, blackhat, thresh, img_out]
    titles = ["Original Image", "BlackHat Image", "Thresholded Mask", "Inpainted Image"]
    cmaps = [None, "gray", "gray", None]

    for i, (image, title, cmap) in enumerate(zip(images, titles, cmaps), start=1):
        plt.subplot(2, 2, i)
        plt.imshow(image, cmap=cmap)
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Save visualization output
    save_file_path = join(save_dir, "output_last_processed.jpg")
    saveImageFile(img_out, save_file_path)
    print(f"Last processed image saved at: {save_file_path}")

else:
    print("No images were successfully processed.")
