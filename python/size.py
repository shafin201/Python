from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size=(1024, 1024)):
    os.makedirs(output_folder, exist_ok=True)
    [Image.open(os.path.join(input_folder, f)).resize(target_size, Image.LANCZOS).save(os.path.join(output_folder, f)) for f in os.listdir(input_folder)]

if __name__ == "__main__":
    input_folder = "C:\\Users\\ASUS\\OneDrive\\Desktop\\data\\New folder\\Yellow_dragon"
    output_folder = "C:\\Users\\ASUS\\OneDrive\\Desktop\\data\\Yellow_dragon"
    target_size = (1024, 1024)

    resize_images(input_folder, output_folder, target_size)
