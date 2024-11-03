# MM_Dectection

# Download and install Anaconda

# Create a conda environment and activate it
conda create --name openmmlab python=3.8 -y
conda activate openmmlab

# Install PyTorch following official instructions, e.g.
On GPU platforms:

conda install pytorch torchvision -c pytorch
On CPU platforms:

#  Install MMEngine and MMCV using MIM
pip install -U openmim
mim install mmengine

pip install "mmcv>=2.0.0rc4,<2.2.0" -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.10.0/index.html
pip install mmdet

git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection

pip install -v -e .

## Still have some error
