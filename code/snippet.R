## EXAMPLE TRAINING AND TEST ###

## annotation vector of the current GO class
y <- ann[,i]; 
indices <- 1:length(y);
positives <- which(y==1);
#stratified partitioning
folds <- do.stratified.cv.data.single.class(indices, positives, 
                                            kk=kk, seed=seed);
testIndex <- mapply(c, folds$fold.positives, 
                    folds$fold.negatives, SIMPLIFY=FALSE);
model <- vector(mode="list", length=kk);
charpos <- "annotated";
charneg <- "not_annotated";
y[which(y==1)] <- charpos;
y[which(y==0)] <- charneg;
y <- as.factor(y);
## setting caret parameter
fitControl <- trainControl(method="none", classProbs=TRUE, 
                           returnData=TRUE, sampling=NULL, 
                           seeds=seed, 
                           summaryFunction=summaryFunction);
#cross-validation
for(k in 1:kk){
  ## training set
  W.training <- W[-testIndex[[k]], ];
  # model tuning 
  model[[k]] <- train(
    x=as.data.frame(W.training),
    y=y[-testIndex[[k]]],
    method=algorithm,
    trControl=fitControl,
    tuneGrid=defGrid,
    tuneLength=1,
    metric=metric
  );
  ## test
  W.test <- W[testIndex[[k]], ];
  ## test model
  model.prob <- predict(model[[k]], newdata=as.data.frame(W.test), type="prob");
  ## true labels
  obs <- y[testIndex[[k]]];
  ## computing predicted labels at a given cutoff
  pred <- factor(ifelse(model.prob[[charpos]] >= cutoff, charpos, charneg), levels=levels(y));
}