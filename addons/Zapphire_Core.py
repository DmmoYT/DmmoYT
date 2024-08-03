def nopremiummode():
    file_path = '../servidor_minecraft/server.properties'
    linea_a_buscar = 'online-mode=true'
    nueva_linea = 'online-mode=false'

    with open(file_path, 'r') as file:
        lineas = file.readlines()

    if any(linea.strip() == linea_a_buscar for linea in lineas):
    # Reemplazar la línea si existe
        lineas_modificadas = [nueva_linea + '\n' if linea.strip() == linea_a_buscar else linea for linea in lineas]

        with open(file_path, 'w') as file:
            file.writelines(lineas_modificadas)
        print(f"Tus configuraciones fueron cambiadas correctamente, tu servidor ahora es no premium.")
    else:
        print(f"Tu servidor ya es no premium.")

def premiummode():
    file_path = '../servidor_minecraft/server.properties'
    linea_a_buscar = 'online-mode=false'
    nueva_linea = 'online-mode=true'

    with open(file_path, 'r') as file:
        lineas = file.readlines()

    if any(linea.strip() == linea_a_buscar for linea in lineas):
    # Reemplazar la línea si existe
        lineas_modificadas = [nueva_linea + '\n' if linea.strip() == linea_a_buscar else linea for linea in lineas]

        with open(file_path, 'w') as file:
            file.writelines(lineas_modificadas)
        print(f"Tus configuraciones fueron cambiadas correctamente, tu servidor ahora es premium.")
    else:
        print(f"Tu servidor ya es premium.")
