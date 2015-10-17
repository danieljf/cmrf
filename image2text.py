import os
import math
from util.tools import readNnData, readImageClickture
from util.irc_query import getQuerySimer

SEARCH_STOP_WORDS = set(str.split('and or for of the pic img picture image photo a an imgs images pics pictures photos'))


class Image2Text:
    def __init__(self, nnimage_file, imgClick_file, qrysim='O', n_top_img = 50, n_top_query = 30):

        # load nn info with distances of images
        self.img2nnimgdis = readNnData(nnimage_file, n_top_img)  # format: img_id img_id dis ...
        print ("[%s] %d images and these top %d nearest neighbours with distance loaded from %s" % 
            (self.__class__.__name__, len(self.img2nnimgdis) , n_top_img, nnimage_file))

        # load query info with click of images  
        self.img2query_clc = readImageClickture(imgClick_file, n_top_query)  # format: img_id /t query /t click ...
        print ("[%s] %d images and these %d queris with click loaded from %s" % 
            (self.__class__.__name__, len(self.img2query_clc) , n_top_query, imgClick_file))

        self.qrySimer = getQuerySimer(qrysim)



    #........................image2text..............................
    #TODO  topimage
    def image2text(self, query, img_list, clickthres = 1):
        scorelist = []
        for img in img_list:
            score = self.image2text_one(query, img, clickthres )
            scorelist.append(score)
        return scorelist

    
    def image2text_one(self, query, image, clickthres = 1):
        score_list = []
        for iid, dis in self.img2nnimgdis[image]:
            # dis = float(dis)
            score = self.qrySimer.calsimiQuerywithClick(query, self.img2query_clc.get(iid, []), clickthres)
            score_list.append( score / dis)

        
        return 0 if len(score_list) == 0 else ( 1.0 * sum(score_list) / len(score_list) )
