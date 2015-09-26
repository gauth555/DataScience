# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 12:04:58 2015

@author: manghnani
"""
import pickle
games=["cricket","tennis","soccer"]
physicists=["Einstein","Planck","Bohr"]
out_file=open("my_lists.dat","wb")
pickle.dump(games,out_file)
pickle.dump(physicists,out_file)
out_file.close()

in_file=open("my_lists.dat","rb")
games=pickle.load(in_file)
physicists=pickle.load(in_file)
print("Games:",games)
print("Physicists:",physicists)
in_file.close()
