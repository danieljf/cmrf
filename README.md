# cmrf

The **cmrf** package implements **C**ross-**M**edia **R**elevance **F**usion [1], with
* four individual method (i.e. image2text, text2image, text2image as Parzen window and semantic embedding)
* learning optimized weights for relevance fusion
* cross-platform support (linux, mac, windows) 

## Prerequisites:

* The package does not include any visual feature extractors. Features of training and test data need to be pre-computed, and converted to required binary format using [txt2bin.py](https://github.com/li-xirong/simpleknn/blob/master/txt2bin.py).
* To minimize one's coding effort, the package requires training data and test data to be organized in a fixed structure, see the sample [training](http://www.mmc.ruc.edu.cn/research/irc2015/data/msr2013train.tar.gz) and [test](http://www.mmc.ruc.edu.cn/research/irc2015/data/msr2013dev.tar.gz) data.
* All visual features had been used in our paper can be download from our [project page](http://www.mmc.ruc.edu.cn/research/irc2015/index.html).

## Setup:

* Add [simpleknn](https://github.com/li-xirong/simpleknn) to `PYTHONPATH`
* Change `ROOT_PATH` in [basic/constant.py](basic/constant.py) to local folder where training and test data are stored
Download [training](http://www.mmc.ruc.edu.cn/research/irc2015/data/msr2013train.tar.gz) and [test](http://www.mmc.ruc.edu.cn/research/irc2015/data/msr2013dev.tar.gz) data without pre-computed visual feature.
* Download at leaset three visual feature ( i.e. [train.caffenet.fc7](http://www.mmc.ruc.edu.cn/research/irc2015/data/train.ruccaffefc7.imagenet.tar.gz) [dev.caffenet.fc7](http://www.mmc.ruc.edu.cn/research/irc2015/data/dev.ruccaffefc7.imagenet.tar.gz) [dev.caffenet.prob](http://www.mmc.ruc.edu.cn/research/irc2015/data/dev.ruccaffeprob.imagenet.tar.gz)) and extract them into 'FeatureData' folder of sample data.
* Dowload [word2vec](http://www.mmc.ruc.edu.cn/research/irc2015/data/flickr25m.word2vec.tar.gz) model learned from user tags of 25 million Flickr images and extract them into `ROOT_PATH`.


As image and query are of two distinct modalities, they have to be represented in a common space so that cross-media relevance can be computed. We implement four individual methods in our package.
* individual methods:
** image2text: project image and query into Bag-of-Words space.
** text2image: project image and query into visual feature space.
** text2image as Parzen window: an extreme case of text2image.
** semantic embedding:  project image and query into semantic space.
How to run these methods using our package, please refer to 'search_example.sh' and source code.

* Relevance fusion:
** we employ Coordinate Ascent to learn optimized weights, then fuse different methods.
The detials of employing relevance fusion, please refer to 'fusion_example.sh' and source code.

## Note:
After running different individual methods, you need firstly write the result path of these methods into file "data/{inputfile=data_source.txt}". The format of {inputfile}: first line is the path of ture label of valid date, following lines are the path of different individual methods, one line one method.

For ease of efficiency, we only run 20 text queries. If you want to run all 1000 queries, please rewrite the file name of 'qid.text.all.txt' in `/rootpath/msr2013dev/Annotations/` into 'qid.text.txt', while the program will take a while.


## Reference:

[1] Jianfeng Dong, Xirong Li, Shuai Liao, Jieping Xu, Duanqing Xu, Xiaoyong Du. [Image Retrieval by Cross-Media Relevance Fusion](http://www.mmc.ruc.edu.cn/research/irc2015/p173-dong.pdf). ACM multimedia 2015
