#!/usr/bin/python

from PIL import Image, ImageChops
import sys
import getopt

'''
# 3 parameters are expected when running the script:
    # - the name of the file containing the plaintext (or ciphertext, if decrypting),
    # - the name of the file containing the key, and
    # - the name of the file where the result of the XOR will be stored.
    # Both the plaintext and the key should be bitmap images of the same size (number of pixels).
'''


def usage():
    print('usage: images_invert.py -p <plaintext> -c <ciphertext>')


def main(argv):
    plaintext_filename = ''
    encryption_filename = ''
    try:
        opts, args = getopt.getopt(argv, "p:k:c:")
    except getopt.GetoptError as exc:
        print(exc)
        usage()
        sys.exit()
    for opt, arg in opts:
        if opt == '-p':
            plaintext_filename = arg
        elif opt == '-c':
            encryption_filename = arg
        else:
            usage()
            sys.exit()

    if len(opts) != 2:  # check that all options are present
        usage()
        sys.exit()
    try:
        # load images
        plaintext = Image.open(plaintext_filename).convert("1")

        # If either the plaintext or the key are not B/W images,
        # they will be converted to one.
        # If you want to see the converted image, uncomment the following two lines
        # plaintext.show()
        # key.show()

        # compute the XOR
        ciphertext = ImageChops.invert(plaintext)
        ciphertext.save(encryption_filename)
        print("Script finished successfully")

    except Exception as exc:
        print("Error:", exc)


if __name__ == "__main__":
    main(sys.argv[1:])
