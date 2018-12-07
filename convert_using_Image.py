from PIL import Image, ImageDraw, ImageFont

def getSize(txt, font):
    testImg = Image.new('RGB', (200, 100), (255,255,255))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)

if __name__ == '__main__':

    fontname = '/Users/yu/Documents/cuhk/Li/text-image-convert/方正楷体繁体.ttf'
    # fontname = '/Users/yu/Documents/cuhk/Li/text-image-convert/经典繁方篆.ttf'
    # fontname = '/Users/yu/Documents/cuhk/Li/text-image-convert/金文大篆体.ttf'
    size = 24 
    text = ''

    font = ImageFont.truetype(fontname, size)
    
    width, height = getSize(text, font)
    img = Image.new('RGB', (width+10, height+10), (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((4, 4), text, fill=(0, 0, 0), font=font)
    img.save("image.png")
