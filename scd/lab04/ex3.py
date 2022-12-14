import threading
import urllib.request
import time

def downloadImage(imagePath,fileName):
    print("Downloading image from ", imagePath)
    urllib.request.urlretrieve(imagePath,fileName)

def main():
    t0=time.time()
    for i in range(10):
        imageName="image-"+str(i)+".jpg"
        downloadImage("https://picsum.photos/300/300?random",imageName)

    t1=time.time()
    totalTime=t1-t0
    print("Total execution time {}".format(totalTime))

if __name__ == '__main__':
    main()
