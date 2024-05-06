###############################################################################
# Lectura y adecuación de la base de datos los resultados del ICFES 2022 - 02
###############################################################################


rm(list = ls())

library(tidyverse)

load("datos/icfes202202.RData")

icfes202202_resumido <- icfes202202 |>
  filter(ESTU_DEPTO_RESIDE!="EXTRANJERO"&ESTU_DEPTO_RESIDE!="")|>
  select(ESTU_DEPTO_RESIDE, 
         ESTU_COD_RESIDE_DEPTO,
         PUNT_GLOBAL,
         COLE_GENERO) |> 
  group_by(ESTU_DEPTO_RESIDE, 
           ESTU_COD_RESIDE_DEPTO) |> 
  summarise(num_pres = n(),
            genero_mix = sum(COLE_GENERO == "MIXTO"),
            genero_fem = sum(COLE_GENERO == "FEMENINO"),
            genero_mas = sum(COLE_GENERO == "MASCULINO"),
            punt_prom = mean(PUNT_GLOBAL))|>
  mutate(`genero_unico` = `genero_fem` + `genero_mas`)

save(icfes202202_resumido, file = "datos/icfes202202_resumido.RData")
