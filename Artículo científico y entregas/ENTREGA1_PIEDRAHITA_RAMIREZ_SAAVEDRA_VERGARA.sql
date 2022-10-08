DROP TABLE IF EXISTS `entrega1-355423.primera_entrega.urbanas `;
CREATE TABLE `entrega1-355423.primera_entrega.urbanas `(
fecha_corte Date,
departamento varchar(150) not NULL, 
municipio varchar(150) not NULL,
estados varchar(150) check(estados = "Operativo" OR "Desconectado" OR "Sin información") NOT NULL,
fecha_inicio_operacion DATE,
fecha_fin_operacion DATE,
velocidad_subida int check(velocidad_subida >= 0),
velocidad_bajada int check(velocidad_bajada >= 0),
trafico_mensual_subida float check(trafico_mensual_subida >= 0),
trafico_mensual_bajada float check(trafico_mensual_bajada >= 0),
usuarios_conectados int CHECK(usuarios_conectados >=0),
inversion FLOAT CHECK(inversion >=0),
meta_vigencia INT CHECK(meta_vigencia >= 0),
fecha_vigencia date);

PRAGMA table_info(`entrega1-355423.primera_entrega.urbanas `);

INSERT INTO `entrega1-355423.primera_entrega.urbanas ` VALUEs("2022-06-10", "META", "EL CALVARIO", "Operativo", "2020-06-23", "2023-08-27", 30, 30, 12.3486328125, 137.4296875, 4, 6591537347, 758, "2022-12-31");


DROP TABLE IF EXISTS `entrega1-355423.primera_entrega.rurales`;
CREATE TABLE `entrega1-355423.primera_entrega.rurales`(
 fecha_corte Date,
 departamento varchar(150) not NULL, 
 municipio varchar(150) not NULL,
 priorizacion VArchar(150) CHECK(priorizacion = "AUS" OR priorizacion = "NO APLICA" OR priorizacion = "PDET BASE" OR priorizacion = "PDET BASE-AUS"  OR priorizacion = "PENDIENTE CLASIFICAR"),
 zona VARCHAR(150) CHECK(zona = "A" OR zona = "RURAL" OR zona = "PENDIENTE CLASIFICAR"),
 Dificultad varchar(150) CHECK(Dificultad = "ALTO" OR Dificultad = "BAJO" OR Dificultad = "MEDIO" OR Dificultad = "MUY ALTO" OR Dificultad = "PENDIENTE CLASIFICAR" OR Dificultad = "SIN INFORMACION") NOT NULL,
 Nombre_Centro_Poblado VARCHAR (150) NOT NULL,
 Tipo_Sitio VArchar (150) CHECK(Tipo_Sitio = "CASOS ESPECIALES" OR Tipo_Sitio = "SEDES EDUCATIVAS"),
Tipo_Conectividad VArchar (150) CHECK(Tipo_Conectividad = "PENDIENTE CLASIFICAR" OR Tipo_Conectividad =  "FIBRA OPTICA" OR Tipo_Conectividad = "SATELITAL" OR Tipo_Conectividad = "RADIO ENLACE") NOT NULL,
 Nombre_Institucion_Educativa varchar (250) NOT NULL,
  Nombre_sede_educativa VARCHAR(250) NOT NULL,
 estados varchar(150) check(estados = "Operativo" OR "Desconectado" OR "En planeación" OR "Sin información") NOT NULL,
 Tipo_Energia varchar (150) CHECK( Tipo_Energia = "PENDIENTE CLASIFICAR" OR  Tipo_Energia = "RED INTERCONECTADA" OR  Tipo_Energia = "SOLUCION SOLAR") NOT NULL,
 Detalle_Sitio varchar (150) NOT NULL,
 usuarios_activos_mes int CHECK( usuarios_activos_mes >= 0) ,
 velocidad_subida int CHECK( velocidad_subida >= 0),
 velocidad_bajada int CHECK(velocidad_bajada >= 0),
 trafico_mensual_subida float check(trafico_mensual_subida >= 0),
 trafico_mensual_bajada float check(trafico_mensual_subida >= 0),
 inversion FLOAT CHECK(inversion >= 0),
 meta INT CHECK(meta >=0));
    
PRAGMA table_info(`entrega1-355423.primera_entrega.rurales`);

INSERT INTO `entrega1-355423.primera_entrega.rurales` VALUEs("2022-06-10", "ANTIOQUIA", "TURBO", "PDET BASE", "Sin información", "PUESTO DE SALUD DE RIOGRANDE", "Casos especiales", 
                                           "Radio enlace", "PUESTO DE SALUD DE RIOGRANDE", "Operativo", "RED INTERCONECTADA", "PUESTO SALUD", 1429, 5, 10, 
                                           0, 0, 142684114, 7468);

    
PRAGMA table_info(`entrega1-355423.primera_entrega.urbanas `);

INSERT INTO `entrega1-355423.primera_entrega.urbanas ` VALUEs("2022-06-10", "META", "EL CALVARIO", "Operativo", "2020-06-23", "2023-08-27", 30, 30, 12.3486328125, 137.4296875, 4, 6591537347, 758, "2022-12-31");

DROP TABLE IF EXISTS `entrega1-355423.primera_entrega.universal`;
CREATE TABLE `entrega1-355423.primera_entrega.universal`(
DIRCON FLOAT CHECK(DIRCON >= 0),
NOMBRE_OPERADOR varchar(150) not NULL,
OPERADOR VARCHAR (150) NOT NULL,
DANE_DEPARTAMENTO INT NOT NULL,
DEPARTAMENTO varchar(150) not NULL,
DANE_MUNICIPIO FLOAT CHECK(DANE MUNICIPIO > 0) NOT NULL,
MUNICIPIO VARCHAR(150) NOT NULL,
DANE_CENTRO_POBLADO FLOAT CHECK(DANE CENTRO POBLADO > 0) NOT NULL,
CENTRO_POBLADO VARCHAR(250) NOT NULL,
ESTADO VARCHAR(150) CHECK(ESTADO = "DESCONECTADA" OR "OPERATIVA),
COORDENADAS_DE_REFERENCIA_LATITUD FLOAT NOT NULL,
COORDENADAS_DE_REFERENCIA_LONGITUD FLOAT NOT NULL,
INICIO_DE_OPERACIÃ“N DATE,
FECHA_FIN_OPERACIÃ“N DATE,
FECHACORTE	DATE,
VIGENCIA DATE,
NÂ°_USUARIOS_ACTIVOS_MES INT CHECK(NÂ°_USUARIOS_ACTIVOS_MES >= 0) ,
TRAFICO_MENSUAL float check(TRAFICO MENSUAL >= 0),
VELOCIDAD_SUBIDA INT CHECK(VELOCIDAD_SUBIDA >= 0),
VELOCIDAD_BAJADA INT CHECK(VELOCIDAD_SUBIDA >= 0),
INVERSIÃ“N FLOAT CHECK(INVERSIÃ“N >= 0));

PRAGMA table_info (`entrega1-355423.primera_entrega.universal`)
INSERT INTO `entrega1-355423.primera_entrega.universal` VALUES("72285", "RED DE INGENIERIA S.A.S.",	"804012847-1", "68", "SANTANDER", "68770", "SUAITA", "68770002", "SAN JOSï¿½ DE SUAITA", "DESCONECTADA", "6,15888889",	"-73,44805556", "10/08/2020", "2/09/2022", "28/02/2022", "31/12/2022", "163", "448,5", "1",	"9", "27007800")


---------------------------------------------------------------- PUNTO 1 ----------------------------------------------------------------------------------------------------------------
----1.	¿Cuál es el promedio de velocidad de subida y bajada de las zonas urbanas y rurales por departamento?
DROP TABLE IF EXISTS entrega1-355423.primera_entrega.TA1;
CREATE TABLE entrega1-355423.primera_entrega.TA1 AS
SELECT DEPARTAMENTO, ROUND(AVG(VELOCIDAD_CONEXION_SUBIDA),2) AS Velocidad_Subida_Promedio_Rural, ROUND(AVG(VELOCIDAD_CONEXION_BAJADA),2) AS Velocidad_Bajada_Promedio_Rural FROM `entrega1-355423.primera_entrega.rurales`
GROUP BY DEPARTAMENTO
ORDER BY DEPARTAMENTO ASC;

DROP TABLE IF EXISTS entrega1-355423.primera_entrega.TA2;
CREATE TABLE entrega1-355423.primera_entrega.TA2 AS
SELECT DEPARTAMENTO, ROUND(AVG(VELOCIDAD_SUBIDA),2) AS Velocidad_Subida_Promedio_Urbana, ROUND(AVG(VELOCIDAD_BAJADA),2) AS Velocidad_Bajada_Promedio_Urbana FROM `entrega1-355423.primera_entrega.urbanas `
GROUP BY DEPARTAMENTO
ORDER BY DEPARTAMENTO ASC;

SELECT `entrega1-355423.primera_entrega.TA1`.*, `entrega1-355423.primera_entrega.TA2`.DEPARTAMENTO AS DEPARTAMENTO_URBANO, `entrega1-355423.primera_entrega.TA2`.Velocidad_Subida_Promedio_Urbana,`entrega1-355423.primera_entrega.TA2`.Velocidad_Bajada_Promedio_Urbana FROM `entrega1-355423.primera_entrega.TA1`
FULL JOIN `entrega1-355423.primera_entrega.TA2` 
ON `entrega1-355423.primera_entrega.TA1`.DEPARTAMENTO = `entrega1-355423.primera_entrega.TA2`.DEPARTAMENTO
ORDER BY DEPARTAMENTO ASC ;
/*-----RESPUESTA 1= De los resultados obtenidos, es posible evidenciar que en todos los departamentos donde se
encuentran zonas rurales y urbanas, la velocidad de subida y bajada promedio es mayor en
las zonas urbanas para todos los casos. De la misma manera, se observa que en todas las
zonas rurales el promedio de velocidad de bajada es de 5, mientras que la de subida es de
10; en las zonas urbanas se encuentra una variación mayor en la velocidad, pero se observa
que es al menos 4 veces mayor la velocidad de bajada y 2 veces mayor la velocidad de
subida respecto a las zonas rurales.*/
------------------------------------------------------------- PUNTO 2 ----------------------------------------------------------------------------------------------------------------
--2.	¿Cuántos lugares por departamento siguen aún sin operar en las zonas rurales?
DROP TABLE IF EXISTS entrega1-355423.primera_entrega.TA3;
CREATE TABLE entrega1-355423.primera_entrega.TA3 AS
SELECT DEPARTAMENTO, ESTADOS FROM `entrega1-355423.primera_entrega.rurales`
WHERE ESTADOS <> "OPERACION";

SELECT INITCAP(DEPARTAMENTO), ESTADOS, COUNT(ESTADOS) AS N_Lugares_Sin_Operar FROM `entrega1-355423.primera_entrega.TA3`
GROUP BY DEPARTAMENTO, ESTADOS
ORDER BY DEPARTAMENTO ASC;
/*------RESPUESTA 2= Sin discriminar por departamento, 5953 lugares rurales continúan sin internet de 7468
lugares en total. Los lugares que aún permanecen sin operar se encuentran con un estado
de instalación o en planeación, siendo Antioquia la que mayor cantidad de lugares tiene
en estos estados y San Andrés y Providencia la que menos tienes (sin hacer
comparación de tamaños de departamentos).*/

---------------------------------------------------------------- PUNTO 3 ------
---3. ¿Cuántos lugares  tienen una dificultad de acceso alta o muy alta en las zonas rurales por departamento? ------------

DROP TABLE IF EXISTS entrega1-355423.primera_entrega.TA4;
CREATE TABLE entrega1-355423.primera_entrega.TA4 AS
SELECT DEPARTAMENTO, DIFICULTADACCESO FROM `entrega1-355423.primera_entrega.rurales`
WHERE DIFICULTADACCESO = "ALTO" OR DIFICULTADACCESO = "MUY ALTO";

SELECT DEPARTAMENTO, DIFICULTADACCESO, COUNT(DIFICULTADACCESO) AS N_Dificultad FROM `entrega1-355423.primera_entrega.TA4`
GROUP BY DEPARTAMENTO, DIFICULTADACCESO
ORDER BY DEPARTAMENTO ASC;
/*--- RESPUESTA 3= Sin discriminar por departamento, de 7468 lugares rurales 472 tienen dificultad alta o
muy alta para acceder a internet. Sucre es el departamento que registra más número de
lugares con dificultad muy alta, mientras que Tolima es el que menos presenta. Por otro
lado, Norte de Santander es el que presenta mayor cantidad de zonas con dificultad de
acceso alta y Atlántico y Cesar los que menos.*/


---------------------------------------------------------------------- PUNTO 4 ----------------------------------------------------------------------------------------------------------------
--4.	¿Cuál es el máximo de usuarios activos al mes por departamento y zona (rural o urbana)?
DROP TABLE IF EXISTS entrega1-355423.primera_entrega.TA5;
CREATE TABLE entrega1-355423.primera_entrega.TA5 AS
SELECT DEPARTAMENTO, MAX(USUARIOS_ACTIVOS_MES) AS Maximo_Usuarios_Activos_Rurales FROM `entrega1-355423.primera_entrega.rurales`
GROUP BY DEPARTAMENTO
ORDER BY DEPARTAMENTO ASC;

DROP TABLE IF EXISTS entrega1-355423.primera_entrega.TA6;
CREATE TABLE entrega1-355423.primera_entrega.TA6 AS
SELECT DEPARTAMENTO, MAX(USUARIOS_CONECTADOS) AS Maximo_Usuarios_Activos_Urbanos FROM `entrega1-355423.primera_entrega.urbanas `
GROUP BY DEPARTAMENTO
ORDER BY DEPARTAMENTO ASC;

SELECT `entrega1-355423.primera_entrega.TA5`.*, `entrega1-355423.primera_entrega.TA6`.* FROM `entrega1-355423.primera_entrega.TA5`
FULL JOIN `entrega1-355423.primera_entrega.TA6` 
ON `entrega1-355423.primera_entrega.TA5`.DEPARTAMENTO = `entrega1-355423.primera_entrega.TA6`.DEPARTAMENTO;

/*----- RESPUESTA 4 = En los resultados obtenidos se obtiene un mayor número de usuarios activos en las
zonas rurales que urbanas, siendo Guajira la de mayor registro en zonas rurales y Nariño
en zonas urbanas. No obstante, los resultados no concuerdan con valores obtenidos en
preguntas anteriores, por lo que se plantea la posibilidad de que la variable “Usuarios
conectados” de la base de datos de zonas urbanas no describa lo mismo que la variable
“Usuarios activos mes” de la base de datos de zonas rurales.*/


--------------------------------------------------------Preguta 5 -----------------------------
-----¿Cuál es el tipo de conectividad de aquellos que tienen dificultad de acceso alta o muy alta en las zonas rurales? --------

select  TIPO_CONECTIVIDAD, COUNTIF(DIFICULTADACCESO = 'ALTO' ) AS DIFALTO, COUNTIF(DIFICULTADACCESO = 'MUY ALTO') AS DIFMUYALTO from `entrega1-355423.primera_entrega.rurales`
GROUP BY TIPO_CONECTIVIDAD ;
/*Se puede observar que las personas con alta y muy alta dificultad de acceso a la red ni
siquiera tienen conectividad (null), y quienes logran hacerlo lo hacen principalmente por
medio de radio enlace o satélite.*/


--------------------------------------------------------Pregunta 6------------------------------
-------6. ¿Cuál es el tráfico mensual promedio de subida y bajada por departamento en zonas rurales y urbanas? ----------------

SELECT DEP, PROM_SUBIDA_RURAL, PROM_BAJADA_RURAL, PROM_SUBIDA_URBANA, PROM_BAJADA_URBANA from 
(SELECT DEPARTAMENTO AS DEP, ROUND(AVG(TRAFICO_MENSUAL_SUBIDA)) AS PROM_SUBIDA_RURAL, ROUND(AVG(TRAFICO_MENSUAL_BAJADA)) AS PROM_BAJADA_RURAL,  FROM `entrega1-355423.primera_entrega.rurales` 
	GROUP BY DEPARTAMENTO  ) t1
left join (SELECT DEPARTAMENTO , ROUND(AVG(CAST(REPLACE(TRAFICO_MENSUAL_SUBIDA,'.',"") AS INT64))) AS PROM_SUBIDA_URBANA,  ROUND(AVG(CAST(REPLACE(TRAFICO_MENSUAL_BAJADA,'.',"") AS INT64))) AS PROM_BAJADA_URBANA FROM `entrega1-355423.primera_entrega.urbanas `
GROUP BY DEPARTAMENTO ) t2 ON t1.DEP = t2.DEPARTAMENTO ORDER BY t1.DEP; 


/* En general hay muchas fluctuaciones en cuanto a los tráficos de subida y bajada tanto
para las zonas rurales como para las zonas urbanas, por sí sola la consulta no da mucha
información específica, sería bueno comparar tanto el tráfico, como la velocidad y el
tipo de conexión ya que esto sí daría una información más completa, además de que
dependiendo de los departamentos estos datos varían mucho.*/


--------------------------------------------------------Pregunta 7 ------------------------------
--------------------7. ¿Cuántos operadores hay por departamento? 

SELECT DEPARTAMENTO, NOMBRE_OPERADOR AS OPERADOR, COUNT(*) AS CANTIDAD from `entrega1-355423.primera_entrega.universal`
GROUP BY DEPARTAMENTO, NOMBRE_OPERADOR  ;

/* En términos generales la RED DE INGENIERIA S.A.S es la que tiene mayor número
de operadores en el país, pero específicamente en la zona centro, pero en la periferia del
país en departamento como Putumayo, amazonas, Guainía, Guaviare, Vaupés y Vichada
solo tienen presencia EMTEL y con un menor número de operadores */


--------------------------------------------------------Pregunta 8 ----------------------------
------------¿Cuántos Centros Poblados por departamento se encuentran desconectados actualmente?

select  RPAD(DEPARTAMENTO, 30, '.'), COUNTIF(ESTADO = 'DESCONECTADA') as Desconectados  from `entrega1-355423.primera_entrega.universal` 
GROUP BY DEPARTAMENTO order by Desconectados desc  ;

/*Se puede observar una alta cantidad de centros desconectados principalmente en los
departamentos del Tolima y Santander, en departamento de la periferia como Choco, La
Guajira, Amazonas no tienen centros poblados desconectados.*/


-----------------------------prueba--------------
SELECT DEP, MUNICIPIO_RURAL, MUNICIPIO_URBANO from 
(SELECT DEPARTAMENTO AS DEP, COUNT(MUNICIPIO) AS MUNICIPIO_RURAL  FROM `entrega1-355423.primera_entrega.rurales` 
	GROUP BY DEPARTAMENTO  ) t1
left join (SELECT DEPARTAMENTO , COUNT(MUNICIPIO) AS MUNICIPIO_URBANO FROM `entrega1-355423.primera_entrega.urbanas `
GROUP BY DEPARTAMENTO ) t2 ON t1.DEP = t2.DEPARTAMENTO ORDER BY t1.DEP ; 



------------------------------------------------punto 9 ------------------------------------------
---¿Cuántos Centros Poblados por municipio tienen más de 5000 usuarios conectados?
SELECT MUNICIPIO, CP_5000_USUARIOS FROM(
SELECT T1.MUNICIPIO, COUNT(CASE WHEN T1.N___USUARIOS_ACTIVOS_MES >= 5000 OR T2.USUARIOS_ACTIVOS_MES >= 5000 THEN 1 END) AS CP_5000_USUARIOS 
FROM `entrega1-355423.primera_entrega.universal` T1
LEFT JOIN `entrega1-355423.primera_entrega.rurales` T2 ON T1.MUNICIPIO = T2.MUNICIPIO
GROUP BY T1.MUNICIPIO)
GROUP BY MUNICIPIO, CP_5000_USUARIOS
HAVING CP_5000_USUARIOS >=1 
ORDER BY MUNICIPIO ;

/*Se observa cuantos municipios en sus centros poblados tienen más de 5000 usuarios
conectados o activos, en esta consulta se puede afirmar que el municipio de candelaria
tiene 8 centros poblados con más de 5000 o más usuarios activos*/

--------------------------------------------------punto 10 --------------------
--¿Cuál es el máximo de usuarios conectados por departamento y minimo en las zonas urbanas?
SELECT LOWER(DEPARTAMENTO) AS LUGAR, MAX(USUARIOS_CONECTADOS) AS MAX_CONECTADOS, MIN(USUARIOS_CONECTADOS) AS MIN_CONECTADOS 
FROM `entrega1-355423.primera_entrega.urbanas `
GROUP BY DEPARTAMENTO
ORDER BY DEPARTAMENTO;

/* Se puede examinar cual es el mínimo y el máximo de usuarios conectados por zonas
urbanas en cada uno de los departamentos, adicionalmente se logra identificar que este
tipo de zonas tienen en sus centros digitales un numero alto de usuarios activos pues los
máximos tienen a ser altos. */

--------------------------------------------------------------------punto 11
--¿Cuál es la inversión total por departamento por zona rural y zona urbana?

DROP TABLE IF EXISTS `entrega1-355423.primera_entrega.RESUMINVRURAL` ;
CREATE TABLE `entrega1-355423.primera_entrega.RESUMINVRURAL` AS
SELECT t1.DEPARTAMENTO, t1.INVERSI__N AS INVERSION_UNI, t2.INVERSION AS INVERSION_RU
FROM `entrega1-355423.primera_entrega.universal` t1
LEFT JOIN `entrega1-355423.primera_entrega.rurales` t2 ON t1.MUNICIPIO = t2.MUNICIPIO;


DROP TABLE IF EXISTS `entrega1-355423.primera_entrega.RESUMINVURB` ;
CREATE TABLE `entrega1-355423.primera_entrega.RESUMINVURB` AS
SELECT t1.DEPARTAMENTO, t1.INVERSI__N AS INVERSION_UNI, t2.INVERSION AS INVERSION_URB
FROM `entrega1-355423.primera_entrega.universal` t1
LEFT JOIN `entrega1-355423.primera_entrega.urbanas ` t2 ON t1.MUNICIPIO = t2.MUNICIPIO;


SELECT T1.DEPARTAMENTO, CONCAT('$',COALESCE(SUM(T1.INVERSION_UNI), 0)) AS INV_TOTAL_UNI, CONCAT('$',COALESCE(SUM(T2.INVERSION_URB), 0)) AS INV_TOTAL_URBANA, CONCAT('$',COALESCE(SUM(T1.INVERSION_RU), 0)) AS INV_TOTAL_RURAL
FROM `entrega1-355423.primera_entrega.RESUMINVRURAL` T1
LEFT JOIN `entrega1-355423.primera_entrega.RESUMINVURB`T2 ON T1.DEPARTAMENTO = T2.DEPARTAMENTO
GROUP BY T1.DEPARTAMENTO
ORDER BY INV_TOTAL_UNI, INV_TOTAL_URBANA, INV_TOTAL_RURAL;

/*Se puede examinar el total de inversión, por cada uno de sus departamentos, además de
estar agrupada por zonas, podemos ver qué zona puede tener más inversión según sea
rural o urbana. En el caso de Vaupés la inversión es para sus zonas rurales y en su zona
urbana no hay inversión; Por otra parte, podemos decir que en general la inversión
universal para este tipo de proyecto es alta.*/

-------------------------------------------------------------------------punto 12
--¿Cuál es el nombre del operador que hay en los departamentos de antioquia, atlántico, santander, caquetá, amazonas, bolívar en las zonas rurales?
DROP TABLE IF EXISTS `entrega1-355423.primera_entrega.RES_OPUNI` ;
CREATE TABLE `entrega1-355423.primera_entrega.RES_OPUNI` AS
SELECT t1.DEPARTAMENTO, t1.NOMBRE_OPERADOR
FROM `entrega1-355423.primera_entrega.universal` t1
LEFT JOIN `entrega1-355423.primera_entrega.rurales` t2 ON t1.DEPARTAMENTO = t2.DEPARTAMENTO;

SELECT  DEPARTAMENTO, LOWER(NOMBRE_OPERADOR) AS OPERADOR FROM `entrega1-355423.primera_entrega.RES_OPUNI`
GROUP BY DEPARTAMENTO, NOMBRE_OPERADOR
HAVING DEPARTAMENTO ="ANTIOQUIA" OR DEPARTAMENTO ="ATLANTICO" OR DEPARTAMENTO = "CAQUETA" OR DEPARTAMENTO = "SANTANDER" OR DEPARTAMENTO = "AMAZONAS" OR DEPARTAMENTO = "BOLIVAR"
order by DEPARTAMENTO;

/*Se puede examinar algunos departamentos y su operador principal, en esta consulta se
puede ver una preferencia por el operador “emtel” sin embargo, en lugares como

Amazonas y Caquetá que podrían ser más sitios rurales el operador es “emtel” y en
lugares como Antioquia y Santander es “red de ingeniería s.a.s”.*/



----------------------- Pregunta 13
-------¿Cuál es el total de usuarios activos al mes en las zonas rurales y el total en urbanas?
SELECT 

  SUM(TD1.USUARIOS_ACTIVOS_MES) AS Total_Activos_Mes_Rural,
  SUM(TD2.USUARIOS_CONECTADOS) AS Total_Activos_Mes_Urbanos

FROM
  `entrega1-355423.primera_entrega.rurales` AS TD1, `entrega1-355423.primera_entrega.urbanas ` AS TD2;

/* Se puede evidenciar, que existe número alto de usuarios activos en los centros digitales
rurales, incluso muy por encima de los centros digitales urbanos. Es probable que este
tipo de situaciones sucedan por la facilidad y la sencillez del acceso al internet en las
grandes urbes, cosa que no sucede en las zonas rurales, donde el acceso es más escaso. */





----------------------- Pregunta 14
-----------¿El aumento de inversión en los departamentos significa una alta velocidad de subida?

SELECT 
  TD1.DEPARTAMENTO, SUM(TD1.INVERSI__N) AS INVERSION, MAX(TD1.VELOCIDAD_BAJADA__Mb_) AS MAX_VEL_BAJADA, MAX(TD1.VELOCIDAD_SUBIDA__Mb_) AS MAX_VEL_SUB
FROM
  `entrega1-355423.primera_entrega.universal` AS TD1
GROUP BY DEPARTAMENTO
ORDER BY INVERSION;

/* En los resultados obtenidos en esta consulta, se ordena de mayor a menor la
inversión y se observa que donde hay más inversión no necesariamente hay más
velocidad de bajada, por ejemplo, en los departamentos que hay más inversión hay 9
Mb de velocidad máxima de bajada y en otros que hay menos inversión hay más
velocidad de bajada, lo cual en esta variable entre más alto sea el valor se considera
mejor */

----------------------- Pregunta 15
------¿Promedio de usuarios activos al mes por departamento?


SELECT 
  TD1.DEPARTAMENTO, AVG(TD1.N___USUARIOS_ACTIVOS_MES) AS PROMEDIO_USUARIOS_ACTIVOS
FROM
  `entrega1-355423.primera_entrega.universal` AS TD1
GROUP BY DEPARTAMENTO
ORDER BY PROMEDIO_USUARIOS_ACTIVOS DESC;

/*Se puede examinar que el numero promedio de usuarios activos por departamento
pueden estar entre los 10.000 usuarios y los 16.000 aproximadamente, incluso la
diferencia entre los departamentos puede estar dada en un aproximado de 1.000
usuarios activos. Podría decirse que existe un rango de usuarios estable teniendo en
cuenta las diferencias territoriales entre los departamentos.*/
