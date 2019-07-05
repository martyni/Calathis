import os
import imageio
from datetime import datetime
from pytz import timezone
from picamera import PiCamera

CAMERA=PiCamera()
CAMERA.resolution = (1024, 768)

def take_picture(filename, directory=''):
    CAMERA.capture(directory + filename + '.jpg')

def create_dated_path(base_dir='/media/pi/data'):
    date = datetime.now(timezone('Europe/London'))
    filename = "{:0>2d}:{:0>2d}:{:0>2d}".format(date.hour, date.minute, date.second)
    directory = "{}/{}/{:0>2d}/{}/".format(
            base_dir,
            date.year,
            date.month,
            date.day)
    if not os.path.exists(directory):
       os.makedirs(directory)
    return filename, directory   

def create_gif(size=90,base_dir='/media/pi/data'):
    _, latest_directory = create_dated_path() 
    root, dirs, files = [_ for _ in  os.walk(latest_directory)][0]
    images = []
    print('getting files for gif')
    files = sorted(files)
    for image in files[:size:]:
        if '.jpg' in image:
            print('adding {}{}'.format(root, image))
            try:
                images.append(imageio.imread(root + image, 'jpg'))
            except:
                print('skipped {}{} deleting'.format(root, image))
                #os.remove(root + image)


    base_dir=base_dir + '/gifs'
    filename, directory = create_dated_path(base_dir=base_dir)
    output_file = directory + filename + '.gif'
    print('creating gif {} in {}'.format(filename + '.gif', directory))
    imageio.mimsave(output_file, images, duration=0.2)
    print('{}{}.gif'.format(directory, filename))


if __name__ == "__main__":
    take_picture(*create_dated_path())
    #create_gif()
