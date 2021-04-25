from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageFilter
import getopt, sys, textwrap, getopt, argparse

def deepfrier(img):
    enhancer = ImageEnhance.Sharpness(img)
    converter = ImageEnhance.Color(img)
    img = enhancer.enhance(99999)
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    img = converter.enhance(3.5)
    return img

def addtext(img, text, iw, ih, pos, color, mock=False):
    if(mock == True):
        res = ""
        for idx in range(len(text)):
            if not idx % 2 :
               res = res + text[idx].upper()
            else:
               res = res + text[idx].lower()  
        text = res
    
    fontstyle = ImageFont.truetype('./comic-sans-ms/ComicSansMS3.ttf', 75)
        
    if(pos == "tl"):
        splits = textwrap.wrap(text, width=20)
        text = ""
        for part in splits:
            text += part
            text += "\n"
        edtb = ImageDraw.Draw(img)
        w_t, h_t = edtb.textsize(text, font=fontstyle)
        edtb.text((width/200,height/10), text, color, font=fontstyle)
        return img
    
    elif(pos == "tc"):
        splits = textwrap.wrap(text, width=80)
        text = ""
        for part in splits:
            text += part
            text += "\n"
        edtb = ImageDraw.Draw(img)
        w_t, h_t = edtb.textsize(text, font=fontstyle)
        edtb.text((((width-w_t)/2),height/10), text, color, font=fontstyle)
        return img
    
    elif(pos == "tr"):
        splits = textwrap.wrap(text, width=20)
        text = ""
        for part in splits:
            text += part
            text += "\n"
        edtb = ImageDraw.Draw(img)
        w_t, h_t = edtb.textsize(text, font=fontstyle)
        edtb.text(((width*0.6,height/10),height/10), text, color, font=fontstyle)
        return img
                  
    elif(pos == "bl"):  
        splits = textwrap.wrap(text, width=20)
        text = ""
        for part in splits:
            text += part
            text += "\n"
        edtb = ImageDraw.Draw(img)
        w_t, h_t = edtb.textsize(text, font=fontstyle)
        edtb.text((width/200,height*0.7), text, color, font=fontstyle)
        return img
                  
    elif(pos == "bc"):
        splits = textwrap.wrap(text, width=50)
        text = ""
        for part in splits:
            text += part
            text += "\n"
        edtb = ImageDraw.Draw(img)
        w_t, h_t = edtb.textsize(text, font=fontstyle)
        edtb.text((((width-w_t)/2),height*0.7), text, color, font=fontstyle)
        return img
                  
    elif(pos == "br"):
        splits = textwrap.wrap(text, width=20)
        text = ""
        for part in splits:
            text += part
            text += "\n"
        edtb = ImageDraw.Draw(img)
        w_t, h_t = edtb.textsize(text, font=fontstyle)
        edtb.text((width*0.6,height*0.7), text, color, font=fontstyle)
        return img

meme_template = Image.open("./willsmithtemplate.jpg")

yellow = (255,255,0)
width, height = meme_template.size

meme = addtext(meme_template, "console program for memes, magic numbers everywhere", width, height, "bc", yellow, mock=True)

meme = deepfrier(meme)

meme = meme.save("test.jpg")

        splits = textwrap.wrap(text, width=50)
        text = ""
        for part in splits:
            text += part
            text += "\n"
        edtb = ImageDraw.Draw(img)
        w_t, h_t = edtb.textsize(text, font=fontstyle)
        edtb.text((((width-w_t)/2),height*0.7), text, color, font=fontstyle)
        return img
                  
    elif(pos == "br"):
        splits = textwrap.wrap(text, width=20)
        text = ""
        for part in splits:
            text += part
            text += "\n"
        edtb = ImageDraw.Draw(img)
        w_t, h_t = edtb.textsize(text, font=fontstyle)
        edtb.text((width*0.6,height*0.7), text, color, font=fontstyle)
        return img

meme_template = Image.open("./willsmithtemplate.jpg")

yellow = (255,255,0)
width, height = meme_template.size

meme = addtext(meme_template, "console program for memes, magic numbers everywhere", width, height, "bc", yellow, mock=True)

meme = deepfrier(meme)

meme = meme.save("test.jpg")

parser = argparse.ArgumentParser()
