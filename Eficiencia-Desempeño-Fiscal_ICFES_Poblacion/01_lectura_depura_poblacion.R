###############################################################################
# Lectura y adecuación de la base de datos de población estimada para 2024
###############################################################################

rm(list = ls())

library(readxl)
library(tidyverse)


poblacion <- read_excel("datos/DCD-area-sexo-edad-proypoblacion-Mun-2020-2035-ActPostCOVID-19.xlsx",
                    skip = 8)

deptos_total_2024 <- poblacion |> 
  filter(AÑO == 2024, 
         `ÁREA GEOGRÁFICA` == "Total") |> 
  select(DP:DPNOM,
         `Hombres_15`:`Hombres_19`, 
         Mujeres_15:Mujeres_19, 
         `Total Hombres`:Total) |>
  
  group_by(DP, DPNOM) |> 
  summarise(`Hombres_15-19` = sum(c_across(Hombres_15:Hombres_19) , na.rm = TRUE),
           `Mujeres_15-19` = sum(c_across(Mujeres_15:Mujeres_19) , na.rm = TRUE)
            #Hombres_16 = sum(Hombres_16, na.rm = TRUE),
            #Hombres_17 = sum(Hombres_17, na.rm = TRUE),
            #Hombres_18 = sum(Hombres_18, na.rm = TRUE),
            #Hombres_19 = sum(Hombres_19, na.rm = TRUE),
            #Mujeres_15 = sum(Mujeres_15, na.rm = TRUE),
            #Mujeres_16 = sum(Mujeres_16, na.rm = TRUE),
            #Mujeres_17 = sum(Mujeres_17, na.rm = TRUE),
            #Mujeres_18 = sum(Mujeres_18, na.rm = TRUE),
            #Mujeres_19 = sum(Mujeres_19, na.rm = TRUE),
            #Total_Hombres_15 = sum(Hombres_15, na.rm = TRUE), 
            #Total_Mujeres_15 = sum(Mujeres_15, na.rm = TRUE)
            #Total_Hombres_15 = sum(Hombres_15, na.rm = TRUE),
            #Total_Mujeres_15 = sum(Mujeres_15, na.rm = TRUE)
            ) |>
  mutate(`Total_15-19` = `Hombres_15-19` + `Mujeres_15-19`)

save(deptos_total_2024, file = "datos/deptos_total_2024.RData",
     compress = TRUE)
