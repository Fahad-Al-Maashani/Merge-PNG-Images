# import PIL from images
from PIL import Image
#inlcude all images and should be in the same folder of python code. 
images = [Image.open(img) for img in ["Transcript of Record-1.png", "Transcript of Record-2.png", "Transcript of Record-3.png","Transcript of Record-4.png","Transcript of Record-5.png"]]

widths, heights = zip(*(i.size for i in images))

# Calculate final canvas size
max_width = max(widths)
total_height = sum(heights)

merged_image = Image.new("RGBA", (max_width, total_height))

# Paste images one below the other
y_offset = 0
for img in images:
    merged_image.paste(img, (0, y_offset))
    y_offset += img.height

# Save the final image
merged_image.save("merged_vertical_image.png")
print("Vertical merge completed!")
