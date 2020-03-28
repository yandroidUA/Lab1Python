from PIL import ImageEnhance, ImageFilter, Image, ImageStat


def testPil(image):
    im = Image.open(image).convert('L')
    stat = ImageStat.Stat(im)
    return stat.rms[0]