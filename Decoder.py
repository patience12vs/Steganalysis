# Credit: https://www.geeksforgeeks.org/image-based-steganography-using-python/
import re

from PIL import Image

# Global Variable
#global frame_location

# Decode the data in the image
def decode(number,frame_location):
    data = ''
    numbering = str(number)
    decoder_numbering = frame_location + "\\" + numbering + ".png"
    image = Image.open(decoder_numbering, 'r')
    imagedata = iter(image.getdata())
    while (True):
        pixels = [value for value in imagedata.__next__()[:3] + imagedata.__next__()[:3] + imagedata.__next__()[:3]]
        # string of binary data
        binstr = ''
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        if re.match("[ -~]", chr(int(binstr,2))) is not None: # only decode printable data
            data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data

# Runtime
def process(frame_start,frame_end,frame_location):
    print("Extracting Data...")
    decodedtextfile = open('output\decoded_frame.txt', 'a')
    decodedtextfile.write('Decoded Text:\n')
    for convnum in range(frame_start, frame_end + 1):
        try:
            decodedtextfile.write(decode(convnum,frame_location))
            print("Data found in Frame %d" % convnum)
        except StopIteration:
            print("No data found in Frame %d" % convnum)
    decodedtextfile.close()
    print("\nExtraction Complete!")
