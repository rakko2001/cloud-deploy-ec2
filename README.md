# Mural da Turma na Nuvem

Aplicação Flask simples para uma aula de Computação em Nuvem: o código fica no GitHub e o deploy manual é feito em uma instância Amazon EC2.

## Executar localmente

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abra:

```text
http://localhost:5000
```

## Deploy manual em EC2 Amazon Linux 2023

```bash
sudo dnf update -y
sudo dnf install git python3 python3-pip -y

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

No navegador:

```text
http://IP_PUBLICO_DA_EC2:5000
```

Lembre-se de liberar a porta TCP 5000 no Security Group da instância.

## Rodar com Gunicorn

```bash
source venv/bin/activate
gunicorn --bind 0.0.0.0:8000 app:app
```

Nesse caso, libere a porta TCP 8000 no Security Group.
