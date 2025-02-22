import os
from rembg import remove

input_folder = 'hand_images/pics'
output_folder = 'hand_images/processed_pics'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_no_bg.png")

    # Check if it's a file and has an image extension
    if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input_image = i.read()
                output_image = remove(input_image)
                o.write(output_image)

        print(f"Processed {filename}, saved to {output_path}")
