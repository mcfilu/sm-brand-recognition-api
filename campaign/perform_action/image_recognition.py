def detect_logos(path):
    """Detects logos in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.logo_detection(image=image)
    print(response)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print(logo)
        print(logo.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


detect_logos('/Users/filipolszewski/PycharmProjects/LogoTest/ig_test1.jpg')

def detect_objects():
    from keras.applications.vgg16 import VGG16
    model = VGG16(weights='imagenet')
    print(model.summary())

    from tensorflow.keras.preprocessing import image
    from tensorflow.keras.applications.vgg16 import preprocess_input,decode_predictions
    import numpy as np

    img_path = '/kaggle/input/images/dog.jpg'
    #There is an interpolation method to match the source size with the target size
    #image loaded in PIL (Python Imaging Library)
    img = image.load_img(img_path,color_mode='rgb', target_size=(224, 224))
    display(img)

    # Converts a PIL Image to 3D Numy Array
    x = image.img_to_array(img)
    x.shape
    # Adding the fouth dimension, for number of images
    x = np.expand_dims(x, axis=0)

    #mean centering with respect to Image
    x = preprocess_input(x)
    features = model.predict(x)
    p = decode_predictions(features)