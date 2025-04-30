@echo off
@title=LinuxUsersLinuxMint-Calculator Setup
:m
cls
echo LinuxUsersLinuxMint-Calculator Setup
echo Which Version Do You Want To Install?
echo 1.LinuxUsersLinuxMint-Calculator-TR
echo 2.LinuxUsersLinuxMint-Calculator-EN
echo Choose:
set input=nothing
set/p input=Choose:
if %input%==1 goto one
if %input%==2 goto two
goto m
:one
echo LinuxUsersLinuxMint-Calculator-TR Version will be downloaded.
pause
copy TR/calc C:\Users\%users%\
pause
exit
goto m
:two
echo LinuxUsersLinuxMint-Calculator-EN Version will be downloaded.
pause
copy EN/calc C:\Users\%users%\
pause
exit