# Analyze-X

Analyze traffic on X-road.


## Components

- OpenCV v3.2.0
- python v2.7.12


## Install OpenCV v3.2.0 on Ubuntu

**Links:**
- http://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html
- https://www.youtube.com/watch?v=i1K9rXiei9I

1. Install required packages:

`sudo apt install build-essential`

`sudo apt install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev`

`sudo apt install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-de`

**For 17.10:**

`libjasper-dev` is not available for Ubuntu 17.04. Need to install the package from an earlier release:

```
echo "deb http://us.archive.ubuntu.com/ubuntu/ yakkety universe" | sudo tee -a /etc/apt/sources.list`
sudo apt upgrade
```

2. Download OpenCV release from GitHub:

https://github.com/opencv/opencv/releases

```
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.2.0.zip && unzip opencv.zip
```


3. Download OpenCV Contrib release from GitHub:

https://github.com/opencv/opencv_contrib/releases/tag/3.2.0

```
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.2.0.zip && unzip opencv_contrib.zip
```

4. Create a temporary build directory:

```
cd opencv
mkdir build && cd build
```

5. Open CMake GUI:

```
sudo apt install cmake-qt-gui
cmake-gui
```

6. Set path to source code folder (opencv-3.2.0) and build folder, created above (opencv-3.2.0/build).

**Where is the source code:** `~/Development/opencv-3.2.0`

**Where to build the binaries:** `~/Development/opencv-3.2.0/build`

7. Click `Configure` -> `Use default native compilers` -> `Finish`. Wait until configuring will be done.

8. Set `OPENCV_EXTRA_MODULES_PATH` to `opencv_contrib-3.2.0/modules`. Click `Generate`. Wait until configuring will be done.

9. From build directory run make (`-j7` runs 7 jobs in parallel):
```
make -j7
```

10. From build directory run make install:
```
sudo make install
```

11. For Python:
```
sudo apt install python-pip
sudo pip install numpy
sudo pip install --upgrade pip
sudo pip install -U setuptools
sudo pip install matplotlib
sudo apt install python-tk
```
