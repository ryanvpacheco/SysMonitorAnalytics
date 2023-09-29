# SysMonitorAnalytics

O **SysMonitorAnalytics** é uma ferramenta de monitoramento do sistema que permite acompanhar o consumo de CPU e memória de processos ao longo do tempo. A aplicação realiza uma leitura periódica dos processos em execução, acumula os dados e gera um arquivo de saída (por padrão, um arquivo de texto).

## Funcionalidades

- Monitoramento em tempo real do consumo de CPU e memória.
- Leitura periódica dos processos em execução.
- Geração de arquivo de saída com os dados acumulados.

## Requisitos

- Python 3.x instalado
- Bibliotecas Python necessárias (instaláveis via `pip install -r requirements.txt`)

## Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/SysMonitorAnalytics.git
cd SysMonitorAnalytics
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o monitoramento:

```bash
python monitor.py
```

## Configurações

- `duration_minutes`: Define a duração do monitoramento em minutos.
- `interval_seconds`: Define o intervalo de leitura em segundos.

## Resultado

Os resultados do monitoramento serão salvos em um arquivo de saída (por padrão, `output.txt`) no diretório raiz do projeto.

---

Lembre-se de substituir "seu-usuario" pelo seu nome de usuário do GitHub ou o nome do seu repositório, se for público. Certifique-se de criar o arquivo `requirements.txt` com as dependências necessárias e adaptar as configurações conforme o seu código final.
