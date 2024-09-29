from PIL import Image

# Open an image file
with Image.open('example.jpg') as img:
    # Print original size
    print(f"Original size: {img.size}")

    # Resize the image
    img_resized = img.resize((300, 300))

    # Save the resized image
    img_resized.save('resized_example.jpg')
    print("Resized image saved as 'resized_example.jpg'")
