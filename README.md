# Projecto de clasifficacion pacientes con diabetes
Este projecto buscar predecir si una personas con diabetes tiene alta probabilidad de reingresar en menos de 30 dias , 30 dias despues o no ingresar despues del ultimo ingreso.


## Contenido:

- EDA: Contienen jupyter notebook. Con exploratory data analisis. Se generar insight que permitieron mejorar el performance del modelo y evitar sesgos a la hora de hacer analsis o modelos predictivos.
- data_processing: Contiene jupyter notebook que  realiza la ingenieria de datos necesaria para crear un set de entrenamiento de la base de diabetes, se genrar dataset  limpio y listo para modelar.
- experiment_models: Contiene jupyter notebook con la experimentacion de hiperparametros y arquietecturas de machine learning. Exporta los mejore modelos y genera insigths acerca de la capacidad predictiva de las variables.

## Conclusiones de EDA:

1.  A simple vista pareciera que no hubieran nulos en la base de datos, sin embargo, cuando se analisa una a una el contenido de las columnas categoricas se **encuentra valores que significacn falta de informacion o nulidad en los datos**. Se encuntran 7 variables con nulos, que pueden impactar negativamente cualquier analsis.
2.  Se encontro desbalance significativo en la variable objectivo.  Se sugieren tecnicas o posibilidades para controlarlo en el moemnto de modelar.
3.  Se encontraron 5 columnas con **problemas de sobredimensionalidad** 'oversize'. La literatura y experiencia personal a demostrado que esta columnas pueden **generar overfitting** en el modelamiento.  Es muy importante controlar esta variables y simplificar su complejidad.
4.  Se exploro **Una a una** las columnas categoricas con grafico de barras en busqueda de nulos, categoria erradas o exceso de peso en alguna categoria. Se encontraron algunas columnas con demasiados nulos y otras con desbalance entre sus categorias
5. Se exploro **Una a una** las columnas numericas con grafico boxplot en busqueda de outliers, distribucciones erraticas o problemas de densidad. Se encontraron algunas columnas con problemas de ouliers
6. Se grafico scatterplots entre las principales variables numericas dividiendo por la variable objetivo. **Se encontra variables como 'number_inpatiente' con aparente gran capacidad de distriminación.**
7. Se encontro correlaciones en variables como edad, tiempo en el hospital, medicacion para diabetes , entre otras y el reingreso menor a 30 dias o mayore a 30 dias.

## Resumen Processing Data

1.  Limpieza de datos nulos. Se encontraron las columnas 'max_glu_serum' y 'A1Cresult' tienen nulos intrinseco porque son examenes que no se hacen de rutina, lo cual hace que los nulos tenga valor importante al ser una referencia de a quien se le realizan estas pruebas especificas. Se uso como referencia el trabajo academico https://www.hindawi.com/journals/bmri/2014/781670/ 

Se imputaron datos basados en la moda a aqullas columasn que no superaban el 30% de nulidad.

Se eliminaron todas aquellas columnas que no aportaban informacion y con una incompletitud alta no pueden ser inputados.

2.  Se tranformo la columna objetivo a numerica para poder modelar.
3.  Se eliminaron los **outliers con el z -score estadistico.**
4.  Los diagnosticos fueron simplificados basados en la tabla 2 (https://www.hindawi.com/journals/bmri/2014/781670/tab2/) del trabajo (https://www.hindawi.com/journals/bmri/2014/781670/) . Pasaron de mas de 150 categorias a menos de 10.
5.    Se exporto la bas elimpia para modelar

## Experimentacion de modelos:
1. Se creo un Pipeline con estandarizacion de varibles numericas, las variables categoricas se tranformaron en formato one-hot
2. Se genero un proceso de de **sobremuestreo** para controlar el problema de balance en los datos
3. Se entrenaron los siguiente modelos:
  3.1 Modelo logistico
  3.2 Modelo estocastico de gradiente desendente
  3.3 Arbol de desicion
  3.4 Random Forest
  3.5 Gradient Boosting
  3.6 Ada Boosting
  Estos son los resultados globales:
  
  |Modelo|N° modelos entrenados|Acurracy|weighted avg|f1 score para <30|
  |---|---|---|---|---|
  |Logistico|2|0.49 |0.5 |0.22|
  |Estocastico de gradiente desendente |10|0.48 |0.5 |0.23 |
  | Arbol de desicion |144 | 0.48|0.46|0.2|
  | Random Forest| 56 |0.56 |0.54 | 0.23|
  | Ada Boosting| 80|0.54 |0.55 |0.22|
  | Ada Boosting| 24|0.51 |0.47|0.24|
 

## Conclusiones Generales

En general los modelos tienen inconvenientes a la hora de predecir el reingreso menor a 30 dias. Esto en parte se debe al inbalance de los datos, que apesar de generar resample puede generar problema en la prediccion. Ademas, aprece que no hay tantas diferencias entre los pacientes que reingresan en menoso de 30 dias y aquellos que no reingresan. Puede que un set mas amplio o mayores carateristicas puedan mejorar la prediccion.

Adicioanal este trabajo puede mejorar de dos formas:

1. Generando transformacion de la variables actuales  que permitan ser mas eficiente al modelo
2. Probando mas arquitecturas o algoritmos, para encontrar mejores metricas de ajuste

Conclusiones de las variables relevantes:
1. number_inpatient es la variable con mayor poder predictivo. Es decir, debe ser prioridad en la recoleccion de datos para prediccion. Que un paciente se hospitalice varias veces puede ser signo de alarma que el tratamiento para la diabetes no vaya funcionar correctamente. sin embargo es una variable con un alto nivel de **endogeniedad** por lo cual puede restringir el analsis. ¿ Es necesario que una personas sea hopitalizada 5 o mas veces para saber que su probabilidad de reingreo es alta?
2. La razon de salida de hospitalizacion tambien afecta la probabiliad de que el paciente vuelva a ingresar.
3.  En algunos modelos el numerode emergencia del paciente , tambien puede ser un signo de alarma.


