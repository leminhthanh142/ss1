from PIL import Image, ImageDraw, ImageFont
import time
import subprocess


def pillow():
    start_time = time.time()
    image = Image.open('test_sample.jpg')
    font = ImageFont.truetype("am_bold.ttf", 145)

    ImageDraw.Draw(image).text((100, 500), "Sample text", fill=(255, 255, 255), font=font)
    # for i in range(1, 11):
    image.resize((round(image.size[0] / 2), round(image.size[1] / 2))).rotate(90, expand=True).save(
        f'imageOutput/test_sample_output_pillow_1.jpg', quality=100)
    print("--- %s seconds ---" % (time.time() - start_time))


def image_magick():
    start_time = time.time()
    # for i in range(1, 11):
    tempo = 'Sample text'
    subprocess.call(
        f'magick test_sample.jpg -draw "text 100,500 ' + str(
            tempo) + '" -resize 50% -quality 100 -rotate -90 '
                     'imageOutput/test_sample_output_magick_1.jpg',
        shell=True)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    # pillow()
    image_magick()
