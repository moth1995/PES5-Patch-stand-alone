pes5='PES5.exe'
pes5_settings='Settings.exe'
chunk_size = 4096
chunk_size2 = 4096
i = 0
while i != 22:
  valornuevo22 = input("Ingrese el nombre de su parche debe tener SI O SI 22 caracteres: ")
  if len(valornuevo22) == 22:
    break
  i = len(valornuevo22)

i = 0
while i != 4:
  valornuevo4 = input("Ingrese un nombre corto para su parche debe tener SI O SI 4 caracteres: ")
  if len(valornuevo4) == 4:
    break
  i = len(valornuevo4)

code =input("Ingrese el serial del juego SIN ESPACIOS (si no lo sabe presione enter y se generara uno automaticamente): ")
if len(code)==0:
    code="CETT7JXPUM5NU6L7TJ54"
else:
     i = len(code)
     while i!=20:
         code = input("Ingrese el serial del juego SIN ESPACIOS: ")
         if len(code) == 20:
             break
         i = len(code)

print("Su serial es: "+code)

#Si el usuario no ingresa nada de lo de arriba correctamente nunca se pasa a lo de abajo

#primero creamos un backup de los dos archivos

with open(pes5,'rb') as rf_exe:
    with open('PES5.bak','wb') as wf_exe:
        rf_exe_chunk = rf_exe.read(chunk_size)
        while len(rf_exe_chunk) >0:
            wf_exe.write(rf_exe_chunk)
            rf_exe_chunk = rf_exe.read(chunk_size)


with open(pes5_settings,'rb') as rf_settings:
      with open('settings.bak','wb') as wf_settings:
           rf_settings_chunk = rf_settings.read(chunk_size2)
           while len(rf_settings_chunk) >0:
              wf_settings.write(rf_settings_chunk)
              rf_settings_chunk = rf_settings.read(chunk_size2)

#abrimos el exe del pes5 en modo lectoescritura

wf_exe=open(pes5,'r+b')
wf_exe.seek(0x6CE7F0,0)
wf_exe.write(valornuevo4.encode('utf8'))
wf_exe.seek(0x6CE4B8,0)
wf_exe.write(valornuevo22.encode('utf8'))
wf_exe.close()

wf_settings=open(pes5_settings,'r+b')
wf_settings.seek(0x6BC58,0)
wf_settings.write(valornuevo4.encode('utf8'))
wf_settings.seek(0x6BC70,0)
wf_settings.write(valornuevo22.encode('utf8'))
wf_settings.close()

#codigo a modo de ejemplo, de esta manera se lee una direccion de memoria

#rf_exe=open(pes5,'rb')
#rf_exe.seek(0x6CE4B8,0)
#cuando usamos la funcion .read() lo que va entre parentesis es la cantidad de caracteres que queremos agarrar, 
#puede ir en formato hexadecimal o decimal, yo prefiero usar hexadecimal
#print(rf_exe.read(0x16))
#rf_exe.close()


with open("Instalador ejecutar como Administrador.bat", "w+") as myfile:
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES5\\"+ valornuevo4 + "\" /V code /T REG_SZ /F /D \""+code+"\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES5\\"+ valornuevo4 + "\" /V installdir /T REG_SZ /F /D \"%~dp0\\\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES5\\"+ valornuevo4 + "\" /V installfrom /T REG_SZ /F /D %~d0\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_e /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_f /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_g /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_i /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_p /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_s /T REG_DWORD /F /D \"1\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\KONAMIPES5\\"+ valornuevo4 + "\\1.0\" /F\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES5\\"+ valornuevo4 + "\" /V code /T REG_SZ /F /D \""+code+"\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES5\\"+ valornuevo4 + "\" /V installdir /T REG_SZ /F /D \"%~dp0\\\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES5\\"+ valornuevo4 + "\" /V installfrom /T REG_SZ /F /D %~d0\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_e /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_f /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_g /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_i /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_p /T REG_DWORD /F /D \"0\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES5\\"+ valornuevo4 + "\" /V lang_s /T REG_DWORD /F /D \"1\"\n")
    myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES5\\"+ valornuevo4 + "\\1.0\" /F\n")

with open("Desinstalador ejecutar como Administrador.bat", "w+") as myfile:
    myfile.write("reg delete \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\KONAMIPES5\\"+ valornuevo4 + "\" /F\n")
    myfile.write("reg delete \"HKEY_LOCAL_MACHINE\SOFTWARE\KONAMIPES5\\"+ valornuevo4 + "\" /F\n")

with open("serial.txt", "w+") as myfile:
    myfile.write(code)
