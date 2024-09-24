meses = {
    "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04", "Mayo": "05",
    "Junio": "06", "Julio": "07", "Agosto": "08", "Septiembre": "09", "Octubre": "10",
    "Noviembre": "11", "Diciembre": "12"
}

fecha = input("Ingrese una fecha en formato MM/DD/AAAA o Mes día, Año: ")

if "/" in fecha:
    mes, dia, ano = fecha.split("/")
    print(f"{ano}-{int(mes):02d}-{int(dia):02d}")
else:
    mes_nombre, dia_ano = fecha.split(" ", 1)
    dia, ano = dia_ano.split(", ")
    mes = meses[mes_nombre]
    print(f"{ano}-{mes}-{int(dia):02d}")
