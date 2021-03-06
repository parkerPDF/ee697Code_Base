import sys
import sklearn.linear_model
import sklearn.model_selection
import sklearn
import numpy as np
from scipy.io import loadmat
import functionList

memNumber = (sys.argv[1]) #unpack from the inputs
ridgeNumber = (sys.argv[2])
whatCv = (sys.argv[3])
fileName = (sys.argv[4])
cvNum = 10

memNumber = int(memNumber)
ridgeNumber = float(ridgeNumber)
whatCv = int(whatCv)

raw = loadmat(fileName)
X = raw['data']  
mask = raw['mask']
l = X.shape[0]
c = X.shape[1]

xClean = functionList.removeTrash(X, mask, memNumber)

crossVal = sklearn.model_selection.KFold(n_splits=cvNum)
folds = [next(crossVal.split(xClean)) for i in range(cvNum)] #do this to pick one particular split for cv
train_in = folds[whatCv][0]
test_in = folds[whatCv][1]

errOut = ""
for thisChannel in range(c):
    xStrip = np.array(X) # if you don't initialize like this the code WILL break
    xStrip[:, thisChannel] = 0
    featureMat = functionList.buildFeatureMat(xStrip, memNumber)
    featureMat = functionList.removeTrash(featureMat, mask, memNumber)
    ridgeNormal = ridgeNumber*np.linalg.norm(xClean[:,thisChannel]) #norm of the channel we're currently in, for regularization scaling
    pred = functionList.predRrOutput(featureMat[train_in, :], featureMat[test_in, :], xClean[train_in, thisChannel], ridgeNormal, 0)
    error = functionList.findMSE(pred, xClean[test_in, thisChannel], 0, 1)
    errOut = errOut + str(error) + ","

print(errOut)