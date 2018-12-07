from PIL import Image, ImageFont, ImageDraw
text = u
font = ImageFont.truetype("msyh.ttf",18)
lines = []
line =''
for word in text.split():
    print(word)
    if font.getsize(line+word)[0] >= 300:
        lines.append(line)
        line = u''
        line += word
        print('size=',font.getsize(line+word)[0])
    else:
        line = line + word
line_height = font.getsize(text)[1]
img_height = line_height*(len(lines)+1)
print('len=',len(lines))
print('lines=',lines)