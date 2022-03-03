# Final Capstone Project: Future of Airline Travel
Combining AI and Smart Contracts to expedite secured entry

## Overview
Bottleneck interference during boarding is the cause of flight delay and increased turnaround times. We propose here a system to expedite the boarding process by enabling contact free entry via facial recognition and a smart contract.

### ML
We developed a system using Biometric authentication as a form of identification and access control. The passenger checks into a flight via a distributed application by taking either a live photograph or video of themselves and comparing to officially verifiable identification, either a drivers license or for international travel a passport.

### IPFS
During the checkin flow the passenger uploads their passport-scan to IPFS and submits the IPFS hash to the function to construct their ERC721 Boarding Pass NFT which includes this IPFS hash.

### ERC721 Contract
The main design decision for the contract is to use the ERC721 token standard for Non-Fungible to model boarding passes which are distributed to passengers upon successful completion of checkin web-flows. ERC721 NFTs enabled us to token assets with distinctive characteristics. This token standard is perfectly suited to value-assets like flight seats and boarding passes where each boarding pass should be associated with a unique passenger. The benefit of allowing the passenger to hold an ERC721 seat after booking is that it allows the passenger to sell, trade, swap, or give away their seat before checkin, if they wish to.

### OpenZeppelin
To implement ERC721 NFTs, the Booker program inherits from the OpenZeppelin implementation of the the ERC721 standard.


## Overview of completed steps

* Build Multi App application in Steamlit and Remix
* Imported the scikit-learn-intelex, opencv, dlib, face_recognition machine learning libraries
* Developed and integrated two integrated web pages, biometric login and boarding pass
* Biometric login allows users to confirm identity by uploading a saved image or using live image detect or webcam video
* Boarding pass app allows passenger to use their wallet to interact with a deployed smart contract to bypass traditional checkin and retrieve boarding pass via the contract
* Images are then compared in the app and recognized images then create smart contract resulting in delivery of boarding pass
* Used IPFS to store official images and deliver ERC721 tokenized image
* ERC721 token can then be traded on NFT marketplace such as OpenSea as a collectable
* Use application to sign into blockchain, register, collect token, display token and receive boarding pass


## Technical Requirements
### Creating the Conda Environment
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

conda install -c conda-forge dlib
#for apple M1 chips
git clone git@github.com:davisking/dlib.git

install CMake from https://cmake.org/install/

sudo "/Applications/CMake.app/Contents/bin/cmake-gui" --install
cd dlib
mkdir build; cd build; cmake .. ; cmake --build .
cd ..
python setup.py install --no USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA

pip install face_recognition
pip install imutils
pip install web3
pip install pybase64
```
### Code Organization
#### Apps
The applications are all in the apps directory
Each app file needs to be added to the app.py in the parent folder
#### Modules
Each module is in it's own folder


## Run
* Create conda environment based on requirement instruction.
* Prep Utility:
Copy/Move the images that you need to encode to the images directory

* Create enncoding
```
cd image_process
python image_processor_encode.py
```

* Run the app
from the root dir
```
streamlit run app.py
```

### Utilities Run Config
* Start Webcam and check that it can recognize images that it stored
```
python image_processor_webcam.py
```
* load image and check that it can recognize images that it stored
```
python image_processor_images.py
```
