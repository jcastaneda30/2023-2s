#install.packages("MASS")
#install.packages("car")
#install.packages("fitdistrplus")
#install.packages("moments")
library("MASS")
library("car")
library("fitdistrplus")
library("moments")

tmin<-read.table("demcom1.txt")
x<-tmin$V1
#Medidas de posicion
mean(x)
median(x)
mode(x)

#medidas de forma
skewness(x,na.rm = FALSE)
kurtosis(x,na.rm = FALSE)

##Graficar los datos
plotdist(x,histo=TRUE,demp = TRUE)
summary(x)

#Valores
descdist(x,boot = 1000) #Saca las medidas de arriba xd
#Ademas del grafico de Cullen
# Ajusta las distribuciones
fit_n <- fitdist(x, "norm")
fit_lg <- fitdist(x, "logis")
fit_ln <- fitdist(x, "lnorm")
fit_g <- fitdist(x, "gamma")
fit_w <- fitdist(x, "weibull")

gofstat(list(fit_g,fit_lg,fit_ln,fit_g,fit_w))

par(mfrow=c(2,2))

plot.legend<-c("normal","logistic","lognormal", "gamma","Weibull")
denscomp(list(fit_g,fit_lg,fit_ln,fit_g,fit_w),legendtext = plot.legend)
cdfcomp(list(fit_g,fit_lg,fit_ln,fit_g,fit_w),legendtext = plot.legend)
qqcomp(list(fit_g,fit_lg,fit_ln,fit_g,fit_w),legendtext = plot.legend)
ppcomp(list(fit_g,fit_lg,fit_ln,fit_g,fit_w),legendtext = plot.legend)
