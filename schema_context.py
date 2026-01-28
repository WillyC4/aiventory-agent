SCHEMA_CONTEXT = """
Base de datos de inventario (AIventory).

Este sistema de gestion de inventarios basado en lotes, el flujo es el siguiente:

La gente de compras registra sus facturas de los porductos que van a venir, para esto usamos la tabla
Facturas que son los encabezados de todas las facturas, de ahi los detalles estan en detalle_facturas y cuando el bodeguero
recibe los productos este los registra en lotes, por eso el inventario general que se encuenntra en bodega esta en lotes.

Despues de esto el equipo de ventas registra sus pedidos de despacho en el que ordenes_despacho tiene todas las cabeceras, 
de ahi los detalles estan en detalle_orden_despacho y cuando el bodeguero despacha los productos estos se registran en lotes_despachados.

y este es el flujo basico del sistema.

A parte de eso tenemos las siguientes tablas:

- audit_logs:
  Registra las acciones realizadas en el sistema.

- catalogos:
  Contiene la información maestra de los productos
  (nombre, código, categoría, unidad).

- categorias:
  Son las categorias generales que usa el sistema

- categoria_proveedor
  Es la tabla de relaciones para saber que cateogria posee cada proveedor

- proveedores:
  Almacena los datos de los proveedores de productos.

- destinatarios
  Son las personas a quien enviamos o nos compran los productos

- historico_diario:
  Guarda un historial diario de movimientos de inventario.

- model_metadata:
  Son los resultados que nos devuelve el modelo al ser entrenado

- predicciones_demanda
  Es donde el modelo registra su prediccion por fechas de la demanda

- Reposiciones:
  Registra las solicitudes de reposición de inventario.

- Reposiciones_suugeridas:
  Son las reposiciones que el sistema sugiere basadas en la prediccion.


- ubicaciones:
  Define las ubicaciones físicas del inventario
  (bodegas, estanterías, áreas).

*NUNCA* debes responder con info PRIVADA de la tabla users y session
"""
