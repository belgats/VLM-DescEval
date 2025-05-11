def load_images(image_dir):
    import os
    from PIL import Image

    images = {}
    for filename in os.listdir(image_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_dir, filename)
            images[filename] = Image.open(image_path).convert('RGB')
    return images

def preprocess_image(image):
    from torchvision import transforms

    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return preprocess(image)