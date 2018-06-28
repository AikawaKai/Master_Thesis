algorithm <- "ranger"
defGrid <- data.frame(mtry=trunc(sqrt(nfeature)), splitrule="gini", min.node.size=1);	
# ftp://cran.r-project.org/pub/R/web/packages/ranger/ranger.pdf

algorithm <- "kknn"
defGrid <- data.frame(kmax=19, distance=2, kernel="optimal");
# https://cran.r-project.org/web/packages/kknn/kknn.pdf

algorithm <- "mlp"
defGrid <- data.frame(size=5);	
# https://cran.r-project.org/web/packages/RSNNS/RSNNS.pdf

algorithm <- "xgbLinear"
defGrid <- data.frame(nrounds=15, lambda=1, alpha=0, eta=0.3);
# https://cran.r-project.org/web/packages/xgboost/xgboost.pdf (pag 38)

algorithm <- "LogitBoost"
defGrid <- data.frame(nIter=nfeature);
# https://cran.r-project.org/web/packages/caTools/caTools.pdf (pag 10)

algorithm <- "treebag"
defGrid <- data.frame(parameter="none");
# https://cran.r-project.org/web/packages/ipred/ipred.pdf
# NOTE: no tuning parameter

algorithm <- "lda"
defGrid <- data.frame(parameter="none");
# https://cran.r-project.org/web/packages/MASS/MASS.pdf
# NOTE: no tuning parameter

algorithm <- "C5.0"
defGrid <- data.frame(trials=1, model="tree", winnow=FALSE);
# https://cran.r-project.org/web/packages/C50/C50.pdf (pag 2)

algorithm <- "glmnet"
defGrid <- data.frame(alpha=1, lambda=100);
# https://cran.r-project.org/web/packages/glmnet/glmnet.pdf

algorithm <- "naive_bayes"
defGrid <- data.frame(laplace=0, usekernel=FALSE, adjust=1);
# https://cran.r-project.org/web/packages/naivebayes/naivebayes.pdf

algorithm <- "svmLinear2"
defGrid <- data.frame(cost=1);
# https://cran.r-project.org/web/packages/e1071/e1071.pdf

algorithm <- "adaboost"
defGrid <- data.frame(nIter=trunc(sqrt(nfeature)), method="Adaboost.M1");
# https://cran.r-project.org/web/packages/fastAdaboost/fastAdaboost.pdf
