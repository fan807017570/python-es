from numpy import *
import operator
import pdb
def createDataSet():
        group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
        labels=['A','A','B','B']
	return group,labels
def classify(inX,dataSet,labels,k):
        dataSetSize=dataSet.shape[0]
	diffMat=tile(inX,(dataSetSize,1))-dataSet
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1)
	print sqDistances
	distances=sqDistances**0.5
	print distances
	sortedDistances=distances.argsort()
	classCount={}
	for i in range (k):
		#pdb.set_trace()
		voteIlabel=labels[sortedDistances[i]]
		classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
	print classCount
if __name__=="__main__":
        print ("this is main of module ")
        group,labels=createDataSet()
        classify([0,0],group,labels,3)

