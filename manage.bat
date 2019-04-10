@echo off
echo.
echo 	Lista de comandos aceitos:
echo. 
echo 	c	cycle (run many iterations)
echo 	d	debug (run one iteration)
echo 	r	remove all posts
echo 	z	zip
echo.

set /p i=" >>> "
goto %i%

:c
echo.
set /p iterations=" #iterations = "
set /a counter = 1
echo.
:c_loop
echo Iteration #%counter% --------------
python debug.py
set /a counter += 1
if %counter% GTR %iterations% goto end
goto c_loop

:d
python debug.py
goto end

:r
python remove_all_posts.py
goto end

:z
if exist function.zip del function.zip
7z a -r -y -xr!.\.git/ function.zip .\*\ lambda_function.py tokens.tk
goto end

:end
pause
cls
call manage.bat