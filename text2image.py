import os
import math
from util.irc_image import ImageSimer
from util.tools import readNnData, readQueryClickture 


class Text2Image:
    def __init__(self, nnquery_file, qryClick_file, dev_feat_path, train_feat_path, top_n=50):

        # load nn info with score of query
        self.qid2nnqidscore = readNnData(nnquery_file, top_n) # format: query_id query_id score ...
        print ("[%s] %d queris and these top %d nearest neighbours with score loaded from %s" %
        	(self.__class__.__name__, len(self.qid2nnqidscore) , top_n, nnquery_file))


        self.qry2img_clk = readQueryClickture(qryClick_file)   # format: query_id  \t image_id click ...  
        print ("[%s] %d queris and these click info loaded from %s" % 
        	(self.__class__.__name__, len(self.qry2img_clk) ,  qryClick_file))


        self.imgSimer = ImageSimer( dev_feat_path, train_feat_path )

    #......................text2image.............................


    def text2image(self, qid, img_list, qrythres = 0.3, clickthres = 1):
        scorelist = []
        for img in img_list:
            score = self.text2image_one(qid, img, qrythres, clickthres )
            scorelist.append(score)
        return scorelist


    def text2image_one(self, qid, image, qrythres = 0.3, clickthres = 1):

        score_list = []
        flag = 0
        for trainqid, score in self.qid2nnqidscore[qid]:
            # score = float(score)
            if score < qrythres: break
            # TODO
            # clickthres
            if score == 1.0:
                flag = 1
            if score < 1.0 and flag > 0:
            	score_list.append(score * self.imgSimer.calsimiImagewithClick(image, self.qry2img_clk[int(trainqid)], clickthres))
                break

            score_list.append(score * self.imgSimer.calsimiImagewithClick(image, self.qry2img_clk[int(trainqid)], clickthres))
        
        return 0 if len(score_list) == 0 else sum(score_list) / len(score_list)