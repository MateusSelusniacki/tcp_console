import os
import ctypes
from ctypes import c_int, c_bool, c_wchar_p

libc = ctypes.WinDLL(".\\Ezcad2.14.11(20200526)-SDK\\MarkEzd.dll")

if not libc:
    print('Erro')
    quit()

print('Biblioteca MultiMark carregada')

path = '.\\Ezcad2.14.11(20200526)-SDK\\'

rc = libc.lmc1_Initial(c_wchar_p(path),c_bool(False),c_int(0))

if(rc):
    print('Erro ao inicializar biblioteca do laser')
    quit()

print('Inicialização bem sucedida')

rc = libc.lmc1_MarkEntity(c_wchar_p("Ushin"))