@echo off 
setlocal enabledelayedexpansion
title serwetka
:menu
cls
echo **************************
echo  ********SERWETKA********
echo **************************
echo 1.Start
echo 2.Backup
echo 3.Info
echo 4.Exit

echo Aby wybrac opcje wpisz odpowiednia cyfre.
set /p wybor="Twoj wybor to: "
if %wybor%==1 goto m_start
if %wybor%==2 goto backup
if %wybor%==3 goto info
if %wybor%==4 goto exit
goto error


:m_start
cls
forfiles /p .\input /C "cmd /c ..\serwetka_maker.exe @file"
set filename=
set date= %date% %time%
for %%a in (.\input\*.txt) do (
    set filename=%%~nxa
    call set filename=!filename:.txt=!
    set files=
    for %%i in ("output\!filename!\*") do (
        call set files=!files! "%%i"
    )
    website_maker.py "%%a" "!date!"!files!
)
index.html
goto exit

:backup
cls
if not exist backup mkdir backup
@ROBOCOPY ..\projekt .\backup /S /XD backup
cls
echo Backup wykonany pomyslnie
set /p enter="Wcisnij Enter aby kontynuowac"
goto exit

:info
cls
echo Serwetka - info
echo Program tworzy obrazy o rozszerzeniu JPG na ktorych znajduje sie serwetka o wielkosci zaleznej od zadanego parametru.
echo.
echo INSTRUKCJA
echo 1. W folderze "input" umiesc plik tekstowy z parametrami (kazdy w nowej linii).
echo 2. Uruchom start.bat
echo 3. Wybierz pierwsza opcje (1.Start)
echo 4. Gotowe
echo.
echo Utworzone obrazy znajduja sie w folderze "output".
set /p enter="Wcisnij Enter aby kontynuowac"
goto menu

:error
echo Zly wybor
set /p enter="Wcisnij Enter aby kontynuowac"
goto menu


:exit

echo on