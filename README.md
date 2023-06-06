# Projecto de clasifficacion pacientes con diabetes
Este projecto buscar predecir si una personas con diabetes tiene alta probabilidad de reingresar en menos de 30 dias despues de la ultima salida, 30 dias despues o no ingresar.


## Contenido:

- EDA: Contienen jupyter notebook. Con exploratory data analisis. Se generar insight que permitieron mejorar el performance del mdoelso y evitar sesgos
- data_processing: Contiene jupyter notebook que  realiza la ingenieria de datos necesaria para crear un set de entrenamiento de la base de diabetes limpio y lsito para modelar.
- experiment_models: Contiene juppyter notebook con la experimentacion de hiperparametros y arquietecturas de mchine learning. Exporta los mejore modelos y genera insgths acerca de la capacidad predictiva de las variables.

## Conclusiones Generales

En general los modelos tienen inconvenientes a la hora de predecir el reingreso menor a 30 dias. Esto en parte se debe al inbalance de los datos, que apesar de generar resample puede generar problema en la prediccion. Ademas, aprece que no hay tantas diferencias entre los pacientes que reingresan en menoso de 30 dias y aquellos que no reingresan. Puede que un set mas amplio o mayores carateristicas puedan mejorar la prediccion.

Adicioanal este trabajo puede mejorar de dos formas:

1. Generando transformacion de la variables actuales  que permitan ser mas eficiente al modelo
2. Probando mas arquitecturas o algoritmos, para encontrar mejores metricas de ajuste

Conclusiones de las varables relevantes:
1. number_inpatient es la variable con mayor poder predictivo. Es decir, debe ser prioridad en la recoleccion de datos para prediccion. Que un paciente se hospitalice varias veces puede ser signo de alarma que el tratamiento para la diabetes no vaya funcionar correctamente
2. La razon de salida de hospitalizacion tambien afecta la probabiliad de que el paciente vuelva a ingresar.
3.  En algunos modelos el numerode emergencia del paciente , tambien puede ser un signo de alarma.


