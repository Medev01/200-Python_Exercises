from collections import Counter

# count the number of images based on thier extensions 
fnames = [
    '001_image.png',
    '002_image.png',
    '003_image.jpg',
    '004_image.png',
    '005_image.png',
    '006_image.png',
    '007_image.jpg',
    '008_image.png',
    '009_image.jpg',
    '010_image.jpg',
    '011_image.jpg',
    '012_image.png',
    '013_image.jpg',
    '014_image.jpg',
    '015_image.jpg',
    '016_image.png',
    '017_image.jpg',
    '018_image.jpg',
    '019_image.png',
    '020_image.png',
    '021_image.jpg',
    '022_image.jpg',
    '023_image.png',
    '024_image.png',
    '025_image.jpg',
    '026_image.png',
    '027_image.png',
    '028_image.jpg',
    '029_image.png',
    '030_image.png'
]

extensions = [(img.split('.')[1]) for img in fnames]

""" Second solution """
img_extensions = []
for img in fnames:
    img = img[10:]
    img_extensions.append(img)

cnt_img = Counter(img_extensions)
cnts = Counter(extensions)
print(cnt_img)
print(cnts)