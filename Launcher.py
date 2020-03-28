import LoadingUtils
import ImageUtils
from PIL import Image


def main():
    print("Working?")
    LoadingUtils.load("https://www.thepythoncode.com/topic/web-scraping", "test-images")
    print(ImageUtils.testPil("test-images/link-extractor.png"))


if __name__ == '__main__':
    main()
