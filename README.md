# cmrf

The **cmrf** package implements **C**ross-**M**edia **R**elevance **F**usion [1], with
* four individual method (i.e. image2text, text2image, text2image as Parzen window and semantic embedding),
* learning optimized weights for relevance fusion,
* cross-platform support (linux, mac, windows).

It is complete solution for [MSR-Bing Image Retrieval Challenge](http://research.microsoft.com/en-US/projects/irc/).

## Prerequisites:
* Download the sample [training](http://www.mmc.ruc.edu.cn/research/irc2015/data/msr2013train.tar.gz) and [test](http://www.mmc.ruc.edu.cn/research/irc2015/data/msr2013dev.tar.gz) data without image visual feature.
* Download at leaset three visual feature ( i.e. [train.caffenet.fc7](http://www.mmc.ruc.edu.cn/research/irc2015/data/train.ruccaffefc7.imagenet.tar.gz) [dev.caffenet.fc7](http://www.mmc.ruc.edu.cn/research/irc2015/data/dev.ruccaffefc7.imagenet.tar.gz) [dev.caffenet.prob](http://www.mmc.ruc.edu.cn/research/irc2015/data/dev.ruccaffeprob.imagenet.tar.gz)) and extract them into 'FeatureData' folder of sample data. All visual features had been used in our paper can be download from our [project page](http://www.mmc.ruc.edu.cn/research/irc2015/index.html).
* Change `ROOT_PATH` in [basic/common.py](basic/common.py) to local folder where training and test data are stored in
* Dowload [word2vec](http://www.mmc.ruc.edu.cn/research/irc2015/data/flickr25m.word2vec.tar.gz) model learned from user tags of 25 million Flickr images and extract them into `ROOT_PATH`.
* Download [simpleknn](https://github.com/li-xirong/simpleknn) and add it to `PYTHONPATH`
* The package does not include any visual feature extractors. Features of training and test data need to be pre-computed, and converted to required binary format using [txt2bin.py](https://github.com/li-xirong/simpleknn/blob/master/txt2bin.py).
* If you would like to use your own dataset, we recommand you to organize dataset in a fixed structure like sample data, which can minimize your coding effort.


## Content:
In order to generate cross-media relevance, image and query have to be represented in a common space as they are of two distinct modalities. In our package, we implement four individual methods and how to fuse relevance form different methods.

#####individual methods:
* [image2text](image2text.py): project image and query into Bag-of-Words space.
* [text2image](text2image.py): project image and query into visual feature space.
* [text2image as Parzen window](parzenWindow.py): an extreme case of text2image.
* [semantic embedding](semantic_embedding.py):  project image and query into semantic space.

How to run these methods using our package, please refer to 'search_example.sh' and source code.

#####Relevance fusion:
* [weight optimization](weightOptimization.py) we employ Coordinate Ascent to learn optimized weights
* [relevance fusion](relevanceFusion.py) then fuse different methods with optimized weights.

The detials of employing relevance fusion, please refer to 'fusion_example.sh' and source code.

## Note:
After running different individual methods, you need firstly write the result path of these methods into file "data/{inputfile=data_source.txt}". The format of {inputfile}: first line is the path of ture label of valid date, following lines are the path of different individual methods, one line one method.

For ease of efficiency, we only run 20 text queries. If you want to run all 1000 queries, please rewrite the file name of 'qid.text.all.txt' in `/rootpath/msr2013dev/Annotations/` into 'qid.text.txt', while the program will take a while.


## Reference:

[1] Jianfeng Dong, Xirong Li, Shuai Liao, Jieping Xu, Duanqing Xu, Xiaoyong Du. [Image Retrieval by Cross-Media Relevance Fusion](http://www.mmc.ruc.edu.cn/research/irc2015/p173-dong.pdf). ACM multimedia 2015
