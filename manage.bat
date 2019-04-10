@echo off
echo.
echo 	Lista de comandos aceitos:
echo. 
echo 	c	cycle (run indefinitely)
echo 	d	debug (run one iteration)
echo 	rp	remove all posts
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

:rp
python remove_all_posts.py
goto end

:z
if exist function.zip del function.zip
7z a -r -y function.zip .\*\ lambda_function.py protected.ids tokens.tk
goto end

:end
pause