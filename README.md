# opencv


## 安装依赖-Ubuntu

### 更新包索引
```bash
sudo apt update
```

### 安装 OpenCV 所需的依赖项（摄像头支持 + 编译依赖）
```bash
sudo apt install -y python3-opencv python3-pip libopencv-dev
```
### 使用 pip 安装最新的 opencv-python（有时系统包太旧）
```bash
pip3 install --upgrade opencv-python
```

### 可选：支持更多图像格式和扩展功能
```bash
pip3 install opencv-contrib-python
```

## 安装依赖-windows

### 如果未安装 pip，请先安装 pip（通常 Python 3.4+ 已内置）
### 安装 opencv-python 主库（包含 cv2、QRCodeDetector 等功能）
```bash
pip install opencv-python
```

### 如果你想额外支持某些扩展图像格式（如 TIFF），也可以装这个（可选）
```bash
pip install opencv-contrib-python
```
