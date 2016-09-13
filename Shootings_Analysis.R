setwd("/Users/christopherlee/Documents/CAL/Real_Life/LogiCal")
MJ<-read.csv('MJ_USMassShootings.csv')
library(zoo)
library(ggplot2)
library(plyr)
library(ggrepel)
library(reshape2)
source('cbind.na.R')

MJ$Date<-as.Date(as.character(MJ$Date), format='%m/%d/%y')
MJ$Venue<-gsub("\n", "", MJ$Venue)
qplot(data=MJ, x=Date, y=Fatalities, color=Race, shape=Gender) + geom_text_repel(data=subset(MJ, Fatalities>20), aes(x=Date, y=Fatalities, label = Case, size=0.33), color='black', box.padding = unit(3, "lines")) + scale_size_continuous(guide=FALSE) + ggtitle("US Mass Shooting Demographic Info")
qplot(data=MJ, x=Date, y=rep(1, nrow(MJ)), size=Fatalities, color=Race)
rollmean(-diff(MJ$Date), 5)
peacetime<--diff(MJ$Date)
MJ$Peacetime<-as.numeric(c(peacetime, 160))
MJ$Decade<-(MJ$Year %/% 10) * 10
MJ$Decade<-paste(MJ$Decade, "s", sep='')
ggplot(MJ) + geom_density(aes(Peacetime, fill=Decade), position="Stack") + ggtitle("Mass Shootings by Decade") + labs(x="Days Between Mass Shootings")

cbind(ddply(MJ, .(Year), summarize, Fatalities=sum(Fatalities)), Incidents=count(MJ$Year)$freq)->Counts
qplot(data=Counts, x=Year, y=Incidents, cex=Fatalities, color='red') + scale_colour_discrete("blue", guide=FALSE)+ ylim(0,10) + ggtitle("Shootings per Year") 

rpois(12350, 1/160)->X1
Y1<-c(which(X1==1)[1], diff(which(X1==1)))
rpois(12350, 1/160)->X2
Y2<-c(which(X2==1)[1], diff(which(X2==1)))
rpois(12350, 1/154)->X3
Y3<-c(which(X3==1)[1], diff(which(X3==1)))
as.data.frame(cbind.na(Real=MJ$Peacetime, Sim1=Y1, Sim2=Y2, Sim3=Y3))->sim_df
simGG<-melt(sim_df)
ggplot(simGG,aes(x=value, fill=variable)) + geom_density(alpha=0.25)