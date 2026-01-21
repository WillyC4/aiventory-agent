SCHEMA_CONTEXT = """
Base de datos de inventario (AIventory).

Tablas principales:

- lotes:
  Representa los lotes físicos de productos en inventario.
  Cada lote tiene una cantidad disponible, fecha de caducidad
  y está asociado a un producto del catálogo.

- catalogos:
  Contiene la información maestra de los productos
  (nombre, código, categoría, unidad).

- ubicaciones:
  Define las ubicaciones físicas del inventario
  (bodegas, estanterías, áreas).

- detalle_factura:
  Relaciona facturas con productos y lotes ingresados.

Relaciones importantes:
- lotes.catalogo_id → catalogos.id
- lotes.ubicacion_id → ubicaciones.id
- detalle_factura.lote_id → lotes.id
"""
