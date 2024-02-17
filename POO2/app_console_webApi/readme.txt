---crear ambiente virtual
python -m venv myenv

---activar ambiente virtual
.\myenv\Scripts\activate


---actulizar pip
python.exe -m pip install --upgrade pip

---instalar mysql conector
python -m pip install mysql-connector-python

**********************API WEB*************************
--instalar fastapi
pip install fastapi

--instalar webapi
pip install uvicorn

--levartar servidor
python -m uvicorn mainAPI:app


---recargar cambios en caliente
python -m uvicorn mainAPI:app --reload


--cargar en diferente puerto
python -m uvicorn mainAPI:app --reload --port 8081


--swagger OPenAPI
http://localhost:8081/docs


*******************ORM**********************
---ORM SQLAlchemyClase 
libreria para vscode:   sqlLite Viewer
modulo:  pip install sqlalchemy

#crear carpeta config y dentro el archivo database.py