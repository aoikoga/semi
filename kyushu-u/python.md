# 九州大学ITOシステムの初期設定

## 九州大学の標準環境 (2018年12月1日現在)
```
module load python/3.6.2
module load cuda/9.1
```
* Python 3.6.2
* CUDA 9.1
* Tensorflow(-gpu) 1.8


## pyenv のインストール

```
git clone git://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

## anaconda のインストール
```
pyenv install -l | grep anaconda3
pyenv install anaconda3-5.3.1
pyenv global anaconda3-5.3.1
```

## anaconda を用いた python 3.6 のインストール
```
conda create -n py36 python=3.6
```

## 作業場所の作成と環境設定
```
mkdir -p ~/Workplace/tensorflow
cd ~/Workplace/tensorflow
pyenv local anasonda3-5.3.1/envs/py36
```

## GPU 利用状況の確認
```
from tensorflow.python.client import device_lib
device_lib.list_local_devices()
```
