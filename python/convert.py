from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size=(512, 512)):
    os.makedirs(output_folder, exist_ok=True)
    [Image.open(os.path.join(input_folder, f)).resize(target_size, Image.LANCZOS).save(os.path.join(output_folder, f)) for f in os.listdir(input_folder)]


if __name__ == "__main__":
    input_folder = "C:\\Users\\ASUS\OneDrive\\Desktop\\Paper\\dataset\\images\\"
    output_folder = "C:\\Users\\ASUS\\OneDrive\\Desktop\\Paper\\dataset\\output\\"
    target_size = (512, 512)

    resize_images(input_folder, output_folder, target_size)