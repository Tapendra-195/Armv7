from PIL import Image
filename="3.jpg"
image = Image.open(filename)
img=Image.new('RGB',(320,240),"black")
pixels = img.load()

f = open(filename+".txt", "a")


for y in range(240):
    for x in range(320):
        colors = image.getpixel((x,y))
        #print(colors)
        r=format(int(colors[0]*31/255.),'05b')
        g=format(int(colors[1]*63/255.),'06b')
        b=format(int(colors[2]*31/255.),'05b')
        #print(r)
        #print(g)
        #print(b)
        n = str(r)+str(g)+str(b)
        #print(n)
        #print(int(n))
        n1=hex(int(n,2))
        print(n1)
        f.write(n1+", ")
        pixels[x,y]=(int(colors[0]*31/255.),int(colors[1]*63/255.),int(colors[2]*31/255.))
        
img.save("pixels.jpg")
f.close()
        
