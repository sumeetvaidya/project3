# POC

## Requirements
```
conda create -n project3 python=3.7 anaconda -y
conda activate project3
conda install scikit-learn-intelex
conda install -c pyviz hvplot geoviews
pip install python-dotenv

conda install -c anaconda requests
conda install ipykernel
conda install nb_conda_kernels

pip install streamlit
pip install streamlit-aggrid
conda install pandas


pip install opencv-python
#pip install pillow
#pip install SimpleCV
#pip install mahotas

conda install -c conda-forge dlib
#for apple M1 chips
git clone git@github.com:davisking/dlib.git

install CMake from https://cmake.org/install/

sudo "/Applications/CMake.app/Contents/bin/cmake-gui" --install
cd dlib
mkdir build; cd build; cmake .. ; cmake --build .
python3 setup.py install --no USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA

pip install face_recognition
pip install imutils

```

## Run
* Prep
Copy/Move the images that you need to encode to the images directory

* Create enncoding
```
python image_processor_encode_eval.py
```

* Start Webcam and check that it can recognize images that it stored
```
python image_processor_webcam_eval.py
```
* load image and check that it can recognize images that it stored
```
python image_processor_images_eval.py
```
* Run Streamlist app to load image and check that it can recognize images that it stored
```
streamlit run image_processor_app.py
```
