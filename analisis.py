import pandas as pd

def calcular_metricas(data):

    ingreso_total = data["ingreso"].sum()
    producto_top = data.groupby("producto")["cantidad"].sum().idxmax()
    producto_low = data.groupby("producto")["cantidad"].sum().idxmin()

    return ingreso_total, producto_top, producto_low

# Cargar datos
data = pd.read_csv("ventas.csv")

# Crear columna ingreso
data["ingreso"] = data["cantidad"] * data["precio_unitario"]

# Métricas principales
ingreso_total, producto_top, producto_low = calcular_metricas(data)

# Ventas por día
ventas_dia = data.groupby("fecha")["ingreso"].sum()

# Detectar caída simple
caida = False
if len(ventas_dia) > 1:
    if ventas_dia.iloc[-1] < ventas_dia.iloc[-2]:
        caida = True

# Simulación tipo agente
print("=== REPORTE AUTOMATIZADO ===")
print(f"Ingreso total: ${ingreso_total}")
print(f"Producto más vendido: {producto_top}")
print(f"Producto con menor rotación: {producto_low}")

if caida:
    print("⚠ Se detectó caída en ventas respecto al día anterior.")
    print("Recomendación: Evaluar estrategia promocional.")
else:
    print("Ventas estables o en crecimiento.")
