#!/usr/bin/env Rscript
library('e1071')
f <- file("stdin")
open(f)
while(length(line <- readLines(f,n=1)) > 0) {
  # process line
  load("/home/rajendra/workspace/PrismaPStreaming/model/model_svm.rda")
  pred <- predict(model,line)
  write(pred, stdout())
}
