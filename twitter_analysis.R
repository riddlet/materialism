library(haven)

df <- read_sav('Documents/Gits/materialism/data/Twitter_Personality_pilot.sav')
write.csv(df, 'Documents/Gits/materialism/data/Twitter_Personality_pilot.csv', row.names = F)

df <- read.csv('Documents/Gits/materialism/data/twitterdat.csv')

library(ggplot2)

names(df)

ggplot(df, aes(x=factor(Study_Type), y=total_tweets)) + 
  geom_point(position=position_jitter(width=.2)) +
  theme_classic()

ggplot(df, aes(x=total_tweets, group=factor(Study_Type), color=factor(Study_Type))) +
  geom_density()

t.test(df$total_tweets~df$Study_Type)
