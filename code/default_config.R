algorithm <- "gaussprPoly";
defGrid <- data.frame(degree=1, scale=1);
# https://cran.r-project.org/web/packages/kernlab/kernlab.pdf (pag 9)

algorithm <- "xgbLinear";
defGrid <- data.frame(nrounds=15, lambda=1, alpha=0, eta=0.3);
# https://cran.r-project.org/web/packages/xgboost/xgboost.pdf (pag 38)

algorithm <- "AdaBoost.M1"; 
data.frame(mfinal=100, maxdepth=30, coeflearn="Breiman");
# https://cran.r-project.org/web/packages/adabag/adabag.pdf (pag 9)
# https://cran.r-project.org/web/packages/rpart/rpart.pdf (pag 22)

algorithm <- "svmRadial";
defGrid <- data.frame(C=1, sigma=1);
# https://cran.r-project.org/web/packages/kernlab/kernlab.pdf (pag 56) 
# https://cran.r-project.org/web/packages/kernlab/kernlab.pdf (pag 9)

algorithm <- "rf";
defGrid <- data.frame(mtry=sqrt(p)); 
# https://cran.r-project.org/web/packages/randomForest/randomForest.pdf (pag 18)

algorithm <- "LogitBoost";
defGrid <- data.frame(nIter=ncol(x)); 
# https://cran.r-project.org/web/packages/caTools/caTools.pdf (pag 10)

algorithm <- "C5.0";
defGrid <- data.frame(trials=1, model="tree", winnow=FALSE);
# https://cran.r-project.org/web/packages/C50/C50.pdf (pag 2)

algorithm <- "treebag";
defGrid <- data.frame(parameter="none");
# https://cran.r-project.org/web/packages/ipred/ipred.pdf
# NOTE: no tuning parameter

algorithm <- "randomGLM";
defGrid <- data.frame(maxInteractionOrder=1);
# https://cran.r-project.org/web/packages/randomGLM/randomGLM.pdf

algorithm <- "mlp";
defGrid <- data.frame(size=5);
# https://cran.r-project.org/web/packages/RSNNS/RSNNS.pdf

algorithm <- "knn";
defGrid <- data.frame(k=9);
# https://stat.ethz.ch/R-manual/R-devel/library/class/html/knn.html
# NOTE: def k=1

algorithm <- "svmLinear";
defGrid <- data.frame(C=1);
# https://cran.r-project.org/web/packages/kernlab/kernlab.pdf

algorithm <- "glmnet";
defGrid <- data.frame(alpha=1, lambda=100);
# https://cran.r-project.org/web/packages/glmnet/glmnet.pdf

