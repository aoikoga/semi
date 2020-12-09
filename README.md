# PyTorch によるディープラーニングのメモ

## Python環境のセットアップ(Windows)

### (1) Anacondaのインストール

[Anacondaのサイト](http://anaconda.com)にアクセスし、「Products」メニューから「Individual Edition」を選択し、表示されるページで「Download」をクリックし、環境にあったインストーラーをダウンロードする。

Windows 64-Bit版のインストーラーへの直リンクは[こちら(Anaconda3-2020.07)](https://repo.anaconda.com/archive/Anaconda3-2020.07-Windows-x86_64.exe)。

インストーラーを実行し、ウィザードに従ってインストールを完了させる。

### (2) Microsoft Visual Studioのインストール

CUDAに対応したパッケージのインストール時に必要となる場合があるようなので、CUDAインストール前にMicrosoft Visual Community 2019をインストールする。

[Visual Studio Communityのページ](https://visualstudio.microsoft.com/ja/vs/community/)の「Visual Studio のダウンロード」からインストーラーをダウンロードする。

インストール時に、「Desktop development with C++」オプションを選択する。

### (3) CUDA Toolkitのインストール

GPUを利用できるように、CUDA Toolkitをインストールする。

[NDIVIAのCUDA Toolkitページ](https://developer.nvidia.com/cuda-toolkit)の「Download Now」から最新のCUDA Toolkitをダウンロードする。

最新バージョンを利用しない場合は、自分が利用するGPUとライブラリに対応したものを選択すること。

### (4) cuDNN のインストール

深層学習用ライブラリCUDA Deep Neural Network library(cuDNN)をインストールする。

NVIDIA Developer Program Membershipへの登録が必要なので、参加してからダウンロードする。

利用するCUDA Toolkitに対応したバージョンをダウンロードすること。

cuDNNはzip形式で配布されているので、[インストレーションガイド](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)を参考に、CUDAのインストールフォルダ以下にコピーすること。

### (5) Python仮想環境の準備

PyTorch+CUDAを利用する仮想環境を準備する。

Anaconda Navigatorを起動し、「Enviroment」メニューから新しい環境(Pythonのバージョンは3.7)を作成する。

環境が作成されたら、実行メニューの「Opne Terminal」からコマンドプロンプトを起動し、以下のコマンドを実行する。

    conda install pytorch torchvision torchaudio cudatoolkit=11.0 -c pytorch
    conda install -c conda-forge notebook

Anacondaの仮想環境を利用する場合、極力`conda`コマンドでパッケージをインストールし、`pip`は利用しないようにする。

