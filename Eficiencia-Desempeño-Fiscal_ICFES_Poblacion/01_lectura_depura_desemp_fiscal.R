###############################################################################
# Lectura y adecuación de la base de datos del desempeño fiscal del 2021
###############################################################################

rm(list = ls())

library(readxl)
library(tidyverse)


desem_fiscal <- read_excel("datos/Anexos_Desempeno_Fiscal_2021_Nueva_Metodologia.xlsx",
                           sheet = "Municipios 2021",
                           skip = 6,
                           na = c("N.D", ""))

desem_fiscal <- desem_fiscal |> 
  select(`Código Departamento`, `Departamento`,
         `Calificación Resultados`) |>
  group_by(`Código Departamento`, `Departamento`) |> 
  summarise(prom_calif_resultados = mean(`Calificación Resultados`))


save(desem_fiscal, file = "datos/desem_fiscal.RData")

