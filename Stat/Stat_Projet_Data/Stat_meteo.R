library(questionr)
library(readr)
library(dplyr)
library(stringr)

library(reticulate)

data_meteo <- read.csv("C:\\Users\\dahie\\Documents\\SDN-S6\\Projet-Data\\Projet_Data\\DataV2\\dataTrainSorti.csv", header=TRUE)

View(data_meteo)

cor.test(data_meteo$temperature , data_meteo$rain )$p.value

#hiver <- filter(data_meteo, date..date < as.Date("2018-12-21T00:00:00.000+0300"), date..date > as.Date("2018-03-20T00:00:00.000+0200"))

#View(hiver)

data_meteo_season <- data_meteo



#data_meteo_season$date..date<-strptime(data_meteo_season$date..date, format="%y/%m/%Yd %H:%M:%s")

#data_meteo_season$month<-as.numeric(format(data_meteo$date..date, "%m"))

data_meteo_season$month <- strtoi(str_sub(data_meteo$date..date, 7, 8))

data_meteo_season$season<-"summer"
data_meteo_season$season[data_meteo_season$month>9&data_meteo_season$month<=12]<-"autumn"
data_meteo_season$season[data_meteo_season$month>1&data_meteo_season$month<=3]<-"winter"
data_meteo_season$season[data_meteo_season$month>3&data_meteo_season$month<=6]<-"spring"
data_meteo_season$season<-factor(data_meteo_season$season,levels=c("summer","spring","winter","autumn"))
summary(data_meteo_season)

summer <- filter(data_meteo_season, season == "summer", rain != "NA")
autumn <- filter(data_meteo_season, season == "autumn", rain != "NA")
spring <- filter(data_meteo_season, season == "spring", rain != "NA")
winter <- filter(data_meteo_season, season == "winter", rain != "NA")

# ////////////////////MOyenne RAIN SAISONS //////////////
moyenneRainEte <- summary(summer$rain)
moyenneRainAutumn <-  summary(autumn$rain)
moyenneRainSpring <- summary(spring$rain)
moyenneRainWinter  <- summary(winter$rain) 


cor.test( summmer$pressure , summmer$rain )$p.value # 2.406952e-108
cor.test( autumn$pressure , autumn$rain )$p.value # 9.5555e-69
cor.test( spring$pressure , spring$rain )$p.value # 1.048323e-116
cor.test( winter$pressure , winter$rain )$p.value # 0.02563328
# On observe qu'on   rejette l'hypothèse H0  car la p-value est > 0.01 , donc il y une correlation
# entre la pluie et la pression en hiver

winterPluieTrue <- filter(winter , rain > 0)

winterPluieFalse <- filter(winter , rain  <= 0)

#boxplot( winter$pressure ~  winter$rain )

boxplot( winterPluieTrue$pressure ~  winterPluieTrue$rain, ylim=c(997, 1015) )

boxplot( winterPluieFalse$pressure ~  winterPluieFalse$rain , ylim=c(1000, 1012))

boxplot(winter$temperature ~ winter$rain)
summary(winterPluieTrue)
summary(winterPluieFalse)

#hum <- filter( data_meteo , humidity > 80)


cor.test( winter$temperature , winter$pressure )$p.value # 0.02563328
cor.test( winter$temperature, winter$rain, method=c("pearson", "kendall", "spearman"))$p.value


cor.test( winter$light, winter$rain, method=c("pearson", "kendall", "spearman"))  #-0.02739696  --> la correlation est moins prononcé que pour les autes saisons 
cor.test( summer$light, summer$rain, method=c("pearson", "kendall", "spearman")) #-0.07656347 --> moins de correlation donc plus flagrant qu'en hiver
cor.test( autumn$light, autumn$rain, method=c("pearson", "kendall", "spearman")) #-0.08121551 --> 
cor.test( spring$light, spring$rain, method=c("pearson", "kendall", "spearman")) #-0.09661923 --> plus il pleut moins il y a de lumière 



cor.test( winter$temperature, winter$rain, method=c("pearson", "kendall", "spearman"))  #-0.08051924  --> la correlation est moins prononcé que pour les autes saisons
cor.test( summer$temperature, summer$rain, method=c("pearson", "kendall", "spearman")) #-0.1950696 --> Plus il pleut, plus la temperature baisse 
cor.test( autumn$temperature, autumn$rain, method=c("pearson", "kendall", "spearman")) #-0.1588715  --> Plus il pleut, plus la temperature baisse 
cor.test( spring$temperature, spring$rain, method=c("pearson", "kendall", "spearman")) #-0.1390298 --> Plus il pleut, plus la temperature baisse 



cor.test( winter$pressure, winter$rain, method=c("pearson", "kendall", "spearman"))  #-0.02696862  --> la correlation est moins prononcé que pour les autes saisons
cor.test( summer$pressure, summer$rain, method=c("pearson", "kendall", "spearman")) #-0.1044213 --> Plus il pleut, plus la pression atmospherique baisse 
cor.test( autumn$pressure, autumn$rain, method=c("pearson", "kendall", "spearman")) #-0.1171976   --> Plus il pleut, plus la pression atmospherique  baisse 
cor.test( spring$pressure, spring$rain, method=c("pearson", "kendall", "spearman")) #-0.1681852 --> Plus il pleut, plus la pression atmospherique  baisse 



cor.test( winter$humidity, winter$rain, method=c("pearson", "kendall", "spearman"))  #0.4274842   --> la correlation est moins prononcé que pour les autes saisons
cor.test( summer$humidity, summer$rain, method=c("pearson", "kendall", "spearman")) #0.22722  --> Plus il pleut, plus l'humidité monte 
cor.test( autumn$humidity, autumn$rain, method=c("pearson", "kendall", "spearman")) #0.2617195    --> Plus il pleut, plus l'humidité monte 
cor.test( spring$humidity, spring$rain, method=c("pearson", "kendall", "spearman")) #0.3184181 --> Plus il pleut, plus l'humidité monte 


plot(winter$humidity , winter$rain)









