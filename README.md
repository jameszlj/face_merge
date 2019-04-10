- 安装 dlib
```
1.安装开发环境
sudo yum update 
sudo yum groupinstall "Development Tools"
2.安装OpenCV
sudo yum install cmake python-devel numpy gcc gcc-c++ gtk2-devel libdc1394-devel libv4l-devel ffmpeg-devel gstreamer-plugins-base-devel libpng-devel libjpeg-turbo-devel jasper-devel openexr-devel libtiff-devel libwebp-devel opencv opencv-python opencv-devel
3.devtoolset升级gcc版本
yum install centos-release-scl-rh centos-release-scl
yum check-update
yum install devtoolset-3-gcc  devtoolset-3-gcc-c++
source /opt/rh/devtoolset-3/enable 这条命令加入到~/.bashrc中
4.安装boost
yum install boost boost-devel boost-doc
5.安装dlib
pip install dlib
```
- 安装 requirements.txt 所需库
```
pip install -r requirements.txt
```
- 运行 run.py 的主函数,为保持后台长期运行，使用nohup
```
python te_run.py
```



