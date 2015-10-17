
dev_collection=msr2013dev
train_collection=msr2013train
overwrite=1

# image2text
method=i2t
feature=ruccaffefc7.imagenet
nnimagefile=id.100nn.dis.txt
imageclickfile=image.clicked.txt

python cmrf_main.py $train_collection $dev_collection --method $method --feature $feature --nnimagefile $nnimagefile --imageclickfile $imageclickfile --overwrite $overwrite


# text2image
method=t2i
nnqueryfile=qid.100nn.score.txt
queryclickfile=query.clicked.txt

python cmrf_main.py $train_collection $dev_collection --method $method --feature $feature --nnqueryfile $nnqueryfile --queryclickfile $queryclickfile --overwrite $overwrite


#text2image as Parzen window
method=pw
sigma=20
python parzenWindow.py $dev_collection --method $method --sigma $sigma --overwrite $overwrite


# semantic embedding
method=se
corpus=flickr
word2vec=vec200flickr25m
feature_se=ruccaffeprob.imagenet
label_source=ilsvrc12

python cmrf_main.py $train_collection $dev_collection --method $method --feature $feature_se --corpus $corpus --word2vec $word2vec --label_source $label_source  --overwrite $overwrite
