import LoadingUtils
import ImageUtils
from PIL import Image
import ModuleTests
from datetime import datetime



def main():
    with open("urls.xml", "rt") as urls:
        for url in urls:
            LoadingUtils.load(url, "test-images")
        ImageUtils.sortByImageBrightness("test-images")

    #ModuleTests.testsForBrightness("module-test-images")

if __name__ == '__main__':
    start_time = datetime.now()
    main()
    print("Total time = ", str(datetime.now() - start_time))