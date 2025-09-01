# Environment

Permette di mantenere pacchetti, dipendenze e informazioni separate da il resto
Questo file prende forma dal video [Youtube](https://www.youtube.com/watch?v=Y21OR1OPC9A)

## Lista di pacchetti installati

Per avere la lista dei pacchetti installati:

```python
pip list
```

## Creare un environment

- Andare da shell sulla cartella dove ci sono i files di progetto
- Crea un ambiente virtuale:

```python
python -m venv nome_env_di_soluto_env
```

## Attivare e disattivare il virtual environment

Dopo aver creato l'ambiente basta attivarlo ed al termine si può disattivare.
Dopo l'attivazione dovrei vedere un (env) all'inizio della stringa e facendo un `pip list` dovrei vedere pochissimi pacchetti installati

```bash
.\env\Scripts\activate.bat
```

Se si vuole utilizzarlo da Visual Studio Code:

```bash
pip install ipykernel
python -m ipykernel install --user --name=env
```

Per disattivare l'ambiente basta fare

```bash
.\env\Scripts\deactivate.bat
```

## Requisiti

Per avere una lista dei requisiti necessari per il pacchetto o il programma:

```bash
pip freeze > requirements.txt
```

e successivamente per installare i pacchetti necessari

```bash
pip install -r requirements.txt
```
