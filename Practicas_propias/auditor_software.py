# Software que encontramos instalado en el equipo
software_instalado = {
    "Google Chrome",
    "7-Zip",
    "AnyDesk",
    "VLC",
    "Python"
}

# Software autorizado por la empresa
software_autorizado = {
    "Google Chrome",
    "7-Zip",
    "VLC",
    "Microsoft Edge",
    "Microsoft Defender"
}

# Software que debe estar instalado obligatoriamente
software_obligatorio = {
    "Google Chrome",
    "Microsoft Edge",
    "Microsoft Defender"
}

print("\n")
titulo = " AUDITORÍA DE SOFTWARE "
print(titulo.center(40, "="))
print("\n")
print("Software autorizado instalado:")
instalado_autorizado =software_instalado.intersection(software_autorizado)
for software in instalado_autorizado:
    print(f'- {software}')
print("\nSoftware no autorizado:")
instalado_no_autorizado = software_instalado.difference(software_autorizado)
for software in instalado_no_autorizado:
    print(f'- {software}')
print("\nSoftware obligatorio faltante:")
obligatorio_faltante = software_obligatorio.difference(software_instalado)
for software in obligatorio_faltante:
    print(f'- {software}')
print("\n")
print("".center(40, "="))