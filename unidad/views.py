from django.shortcuts import render

def convertidor_unidades(request):
    resultado = None
    unidad_resultado = ""
    
    if request.method == "POST":
        cantidad = float(request.POST.get("cantidad", 0))
        unidad_origen = request.POST.get("unidad_origen")
        unidad_destino = request.POST.get("unidad_destino")

        # Diccionario de conversiones entre unidades
        conversiones = {
            "km-m": 1000,
            "m-km": 0.001,
            "cm-m": 0.01,
            "m-cm": 100,
        }

        # Construimos la clave para buscar la conversión
        clave_conversion = f"{unidad_origen}-{unidad_destino}"
        
        # Verificamos si la conversión es válida y realizamos el cálculo
        if clave_conversion in conversiones:
            resultado = cantidad * conversiones[clave_conversion]
            unidad_resultado = unidad_destino  # Asignamos la unidad de destino
        else:
            resultado = "Conversión no soportada"
    
    # Pasamos el resultado y la unidad de destino al contexto
    return render(request, "unidad/convertidor.html", {"resultado": resultado, "unidad_resultado": unidad_resultado})
