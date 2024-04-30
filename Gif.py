import imageio.v2 as imageio
filenames=["sketched.png","original.png"]
images=[]
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif',images,'GIF',duration=4)
