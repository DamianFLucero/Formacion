
--SELECT: Permite seleccionar las columnas que se van a mostrar y en el orden en que lo van a hacer. * es el comod�n que representa todas las columnas
--FROM: define las tablas o vistas de las cuales se obtendr�n los datos
	--SELECT * FROM SalesLT.Customer						--solicita todas las columnas de la tabla SalesLT.Customer
	--SELECT FirstName FROM SalesLT.Customer				--solicita la columna FirstName de la tabla SalesLT.Customer
--ALL: es el valor predeterminado, especifica que el conjunto de resultados puede incluir filas duplicadas. Por regla general nunca se utiliza.
--DISTINCT: especifica que el conjunto de resultados s�lo puede incluir filas �nicas. Es decir, si al realizar una consulta hay registros exactamente iguales que aparecen m�s de una vez, �stos se eliminan.
	--SELECT  DISTINCT FirstName FROM SalesLT.Customer		--solicita la columna FirstName de la tabla SalesLT.Customer, SIN DUPLICADOS
--WHERE: especifica una condici�n para filtrar las filas devueltas.
	--SELECT * FROM SalesLT.Customer WHERE Title = 'Mr.'	--solicita todas las columnas de la tabla SalesLT.Customer donde Title sea Mr.
--AS: Permite renombrar columnas si lo utilizamos en la cl�usula SELECT, o renombrar tablas si lo utilizamos en la cl�usula FROM. Es opcional.
	--SELECT FirstName AS NOMBRE, LastName AS APELLIDO FROM SalesLT.Customer	--Solicita las columnas FirstName y LastName pero las muestra como NOMBRE y APELLIDO  respectivamente.
--LIKE: permite comprar strings. Con %  indicamos que en su lugar puede ir cualquier cadena de caracteres, y con _  que puede ir cualquier car�cter individual (un solo caracter)
	--SELECT * FROM SalesLT.Customer WHERE FirstName LIKE 'O%'		--solitita todas las columnas de la tabla SalesLT.Customer cuyo FirstName empiece con O
	--SELECT * FROM SalesLT.Customer WHERE FirstName LIKE '_c%'		--solicita todas las columnas de la tabla SalesLT.Customer cuyo FirstName tenga como segunda letra la c
--BETWEEN: define un intervalo entre valores, a usar como filtro
	--SELECT * FROM SalesLT.Customer WHERE ModifiedDate BETWEEN '20050101' AND '20060101'	--solicita todas las columnas de la tabla SalesLT.Customer cuya ModifiedDate est� entre 01/01/2005 (20050101) y 01/01/2006 (20060101)
	--SELECT * FROM SalesLT.Customer WHERE CustomerID BETWEEN 0 AND 30						--solicita todas las columnas de la tabla SalesLT.Customer cuyo CustomerID e�t� entre 0 y 30
--ORDER BY: Define el orden de las filas del conjunto de resultados. Se especifica el campo o campos (separados por comas) por los cuales queremos ordenar los resultados.
--ASC / DESC: especifica si la columna indicada en la cl�usula ORDER BY se ordenar� de forma ascendente o descendente (por defento ordena por ASC)
	--SELECT * FROM SalesLT.Customer ORDER BY FirstName						--solicita todas las columnas de la tabla SalesLT.Customer ordenados por FirstName (por defecto, de forma ascendente)
	--SELECT * FROM SalesLT.Customer ORDER BY FirstName DESC, LastName ASC	--solicita todas las columnas de la tabla SalesLT.Customer ordenados por FirstName descendente y posteriormente por LastName ascendente
--GROUP BY: Cl�usula de la instrucci�n SELECT que divide el resultado de la consulta en grupos de filas, normalmente con el fin de realizar una o varias agregaciones en cada grupo. La instrucci�n SELECT devuelve una fila por grupo.
--La columna debe aparecer en la cl�usula FROM de la instrucci�n SELECT, pero no es necesario que aparezca en la lista SELECT. Aun as�, deben incluirse en la lista GROUP BY todas las columnas de la tabla o la vista de cualquier expresi�n no agregada de la lista de SELECT
	--SELECT LastName FROM SalesLT.Customer GROUP BY LastName				--solicita la columna LastName agrupada por LastName
--Las funciones de agregaci�n en SQL nos permiten efectuar operaciones sobre un conjunto de resultados, pero devolviendo un �nico valor agregado para todos ellos. Es decir, nos permiten obtener medias, m�ximos, etc... sobre un conjunto de valores.
--COUNT: devuelve el n�mero total de filas seleccionadas por la consulta.
--SUM: suma los valores del campo que especifiquemos. S�lo se puede utilizar en columnas num�ricas.
--MIN: devuelve el valor m�nimo del campo que especifiquemos.
--MAX: devuelve el valor m�ximo del campo que especifiquemos.
--AVG: devuelve el valor promedio del campo que especifiquemos. S�lo se puede utilizar en columnas num�ricas.
--Todas estas funciones se aplican a una sola columna, que especificaremos entre par�ntesis, excepto la funci�n COUNT, que se puede aplicar a una columna o indicar un �*�. La diferencia entre poner el nombre de una columna o un �*�, es que en el primer caso no cuenta los valores nulos para dicha columna, y en el segundo si.

	--SELECT LastName, COUNT(*) AS Cantidad FROM SalesLT.Customer GROUP BY LastName	--solicita la columna LastName y la cantidad de filas de cada grupo, agrupada por LastName
	--SELECT Color, SUM (ListPrice) ListPriceSum FROM SalesLT.Product GROUP BY Color				--solicita la columna Color y la suma de los ListPrice, agrupados por color
	--SELECT Color, MIN(ListPrice) AS PrecioMinimo FROM SalesLT.Product GROUP BY Color				--solicita la columna Color y el menor ListPrice de cada grupo
	--SELECT Color, MAX(ListPrice) AS PrecioMaximo FROM SalesLT.Product GROUP BY Color				--solicita la columna Color y el mayor ListPrice de cada grupo
	--SELECT Color, AVG(ListPrice) AS PrecioMaximo FROM SalesLT.Product GROUP BY Color				--solicita la columna Color y el promedio de ListPrice de cada grupo

--Consultas multitabla: siendo dos tablas tA y tB respectivamente
--INNER JOIN: devuelve las filas de ambas tablas (tA y tB) que cumplan con la condici�n (ON) definida
		--SELECT * FROM SalesLT.Customer INNER JOIN SalesLT.SalesOrderHeader ON SalesLT.Customer.CustomerID = SalesLT.SalesOrderHeader.CustomerID	--devuelve una tabla formada por las filas de SalesLT.Customer y SalesLT.SalesOrderHeader cuyos respectivos CustomerID sean iguales, es decir, devuelve una lista de los clientes que registran al menos una compra
--LEFT JOIN: devuelve todas las filas de tA y s�lo las filas de tB que cumplan la condici�n (ON) definida
		--SELECT * FROM SalesLT.SalesOrderDetail LEFT JOIN SalesLT.Product ON SalesLT.Product.ProductID = SalesLT.SalesOrderDetail.ProductID		--devuelve una tabla con todas las filas de SalesLT.SalesOrderDetail y s�lo las filas de SalesLT.Product donde SalesLT.Product.ProductID = SalesLT.SalesOrderDetail.ProductId
--RIGHT JOIN: devuelve todas las filas de tB y s�lo las filas de tA que cumplan la condici�n (ON) definida
		--SELECT * FROM SalesLT.Product RIGHT  JOIN SalesLT.SalesOrderDetail  ON   SalesLT.SalesOrderDetail.ProductID = SalesLT.Product.ProductID	--devuelve una tabla s�lo con las filas de SalesLT.Product donde SalesLT.Product.ProductID = SalesLT.SalesOrderDetail.ProductId y todas las filas de SalesLT.SalesOrderDetail (invert� las tablas para que el resultado sea el mismo que el anterior)
--FULL JOIN: devuelve todas las filas de ambas tablas (tA y tB) rellenando con con NULL las casillas que no coincidan con la condici�n (ON) definida
		--SELECT * FROM SalesLT.Customer FULL JOIN SalesLT.SalesOrderHeader ON SalesLT.Customer.CustomerID = SalesLT.SalesOrderHeader.CustomerID	--devuelve una tabla formada por las filas de SalesLT.Customer y SalesLT.SalesOrderHeader cuyos respectivos CustomerID sean iguales, es decir, devuelve una lista de los clientes que registran al menos una compra

--CARTESIAN JOIN: devuelve un producto cartesiando entre dos tablas



