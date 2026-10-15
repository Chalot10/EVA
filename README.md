<!--
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║   ███████╗██╗   ██╗ █████╗                                               ║
║   ██╔════╝██║   ██║██╔══██╗                                              ║
║   █████╗  ██║   ██║███████║                                              ║
║   ██╔══╝  ╚██╗ ██╔╝██╔══██║                                              ║
║   ███████╗ ╚████╔╝ ██║  ██║                                              ║
║   ╚══════╝  ╚═══╝  ╚═╝  ╚═╝                                              ║
║                                                                          ║
║   Entidade Virtual Assistiva                                             ║
║   Projeto Yuni                                                           ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
-->

<h1 align="center">
  <br>
  🤖 EVA — Entidade Virtual Assistiva
  <br>
</h1>

<h4 align="center">
  Assistente virtual inteligente desenvolvida em Python, com reconhecimento de voz,
  síntese de fala, sistema de plugins extensível e arquitetura preparada para IA.
</h4>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.13+">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License MIT">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Projeto-Yuni-purple?style=for-the-badge" alt="Projeto Yuni">
</p>

<p align="center">
  <a href="#-sobre-o-projeto">Sobre</a> •
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-arquitetura">Arquitetura</a> •
  <a href="#-instalação">Instalação</a> •
  <a href="#-uso">Uso</a> •
  <a href="#-plugins">Plugins</a> •
  <a href="#-roadmap">Roadmap</a> •
  <a href="#-contribuir">Contribuir</a> •
  <a href="#-licença">Licença</a>
</p>

---

## 📖 Sobre o Projeto

**EVA (Entidade Virtual Assistiva)** é uma assistente virtual inteligente desenvolvida em **Python**, concebida para interagir com o utilizador através de voz e texto, executar tarefas automatizadas e integrar-se com serviços externos.

A EVA faz parte do ecossistema **Yuni**, um projeto mais amplo que explora a integração de **Inteligência Artificial**, **processamento de linguagem natural** e **automação** num assistente pessoal modular e extensível.

### 🎯 Objetivos

- Fornecer uma interface natural (voz e texto) para interagir com o computador
- Automatizar tarefas do dia-a-dia através de um sistema de plugins
- Servir como plataforma de aprendizagem para IA, NLP e arquitetura de software
- Ser totalmente open source e extensível pela comunidade

---

## ✨ Funcionalidades

### 🎤 Interação por Voz
- **Reconhecimento de voz** — converte fala em texto usando `SpeechRecognition` + `sounddevice` (alternativa ao PyAudio)
- **Síntese de voz** — responde em português europeu com `gTTS` (Google Text-to-Speech) e fallback para `pyttsx3`
- **Modo texto** — alternativa quando não há microfone disponível

### 🔌 Sistema de Plugins
- Arquitetura modular baseada em **plugins independentes**
- Comandos configuráveis via `comandos.json`
- Fácil adição de novas funcionalidades sem alterar o core

### 🧠 Preparado para IA
- Estrutura preparada para integração com **LLM** (GPT, Llama, etc.)
- Módulos para **processamento de linguagem natural**
- Espaço para algoritmos de **classificação, similaridade e recomendação**

### 💾 Memória Persistente
- Histórico de conversas
- Preferências do utilizador
- Armazenamento em JSON (preparado para migração para SQLite/PostgreSQL)

---

## 🏗️ Arquitetura

A EVA foi projetada com uma arquitetura em **camadas**, promovendo separação de responsabilidades e escalabilidade.

```
                         UTILIZADOR
                              │
                              ▼
                       ┌────────────┐
                       │    VOZ     │
                       │  ouvir.py  │
                       └─────┬──────┘
                             │
                             ▼
                          TEXTO
                             │
                             ▼
                    ┌────────────────┐
                    │     CORE       │
                    │  assistente.py │
                    └───────┬────────┘
                            │
                            ▼
                     ┌─────────────┐
                     │   ROUTER    │
                     └──────┬──────┘
                            │
              ┌─────────────┼──────────────┐
              │             │              │
              ▼             ▼              ▼
          PROCESSAMENTO     LLM        ALGORITMOS
              │             │              │
              ▼             ▼              ▼
          INTENÇÃO       RESPOSTA      PREDIÇÃO/
          ENTIDADES      COMPLEXA      CLASSIFICAÇÃO
              │             │              │
              └─────────────┼──────────────┘
                            │
                            ▼
                       ┌─────────┐
                       │ MEMÓRIA │
                       └────┬────┘
                            │
                            ▼
                       ┌─────────┐
                       │EXECUTOR │
                       └────┬────┘
                            │
                            ▼
                         PLUGINS
                            │
                            ▼
                       RESULTADO
                            │
                            ▼
                         falar.py
                            │
                            ▼
                        UTILIZADOR
```

### 📂 Estrutura de Diretórios

```
eva-assistente-virtual/
│
├── main.py                    # Ponto de entrada da aplicação
├── comandos.json              # Configuração de comandos
├── requirements.txt           # Dependências Python
├── .env.example               # Exemplo de variáveis de ambiente
├── .gitignore                 # Ficheiros ignorados pelo Git
├── README.md                  # Este ficheiro
├── LICENSE                    # Licença MIT
├── CONTRIBUTING.md            # Guia de contribuição
├── CHANGELOG.md               # Histórico de versões
│
├── core/                      # Núcleo da EVA
│   ├── __init__.py
│   ├── assistente.py          # Coordenador principal
│   ├── router.py              # Encaminhamento de pedidos
│   ├── executor.py            # Execução de plugins
│   ├── comandos.py            # Gestão de comandos
│   └── contexto.py            # Gestão de contexto
│
├── voz/                       # Comunicação por voz
│   ├── __init__.py
│   ├── ouvir.py               # Reconhecimento de voz
│   └── falar.py               # Síntese de voz
│
├── plugins/                   # Capacidades da EVA
│   ├── __init__.py
│   ├── abrir_programas.py     # Abrir aplicações e websites
│   ├── colocar_alarme.py      # Alarmes e temporizadores
│   ├── emailplugin.py         # Envio de emails
│   ├── pastas.py              # Gestão de pastas
│   ├── pesquisa.py            # Pesquisa na web
│   └── tocar_musica.py        # Reprodução de música
│
├── ia/                        # Inteligência Artificial
│   ├── __init__.py
│   ├── llm/                   # Integração com LLM
│   │   ├── __init__.py
│   │   ├── cliente.py
│   │   ├── prompts.py
│   │   └── modelos.py
│   ├── algoritmos/            # Algoritmos de IA
│   │   ├── __init__.py
│   │   ├── classificacao.py
│   │   ├── similaridade.py
│   │   ├── recomendacao.py
│   │   ├── previsao.py
│   │   └── deteccao.py
│   └── processamento/         # Processamento de linguagem
│       ├── __init__.py
│       ├── intencao.py
│       ├── entidades.py
│       └── texto.py
│
├── memoria/                   # Memória persistente
│   ├── __init__.py
│   ├── memoria.py
│   ├── historico.py
│   └── armazenamento.py
│
├── utils/                     # Utilitários
│   ├── __init__.py
│   ├── config.py
│   └── logger.py
│
└── dados/                     # Dados persistentes
    ├── memoria.json
    └── historico.json
```

---

## 🚀 Instalação

### Pré-requisitos

- **Python 3.13+** — [Download](https://www.python.org/downloads/)
- **pip** — incluído no Python
- **Git** — [Download](https://git-scm.com/downloads)
- **Microfone** (opcional, para modo voz)

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/Chalot10/EVA.git
cd EVA
```

### Passo 2: Criar ambiente virtual

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Passo 3: Instalar dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Passo 4: Configurar variáveis de ambiente

```bash
# Windows
copy .env.example .env

# Linux / macOS
cp .env.example .env
```

Edita o `.env` com as tuas configurações.

### Passo 5: (Opcional) Instalar drivers de áudio

Se quiseres usar o **modo voz**, instala o `sounddevice`:

```bash
pip install sounddevice numpy
```

> 💡 A EVA usa `sounddevice` em vez de `PyAudio` por ser mais compatível com Python 3.13.

---

## 🎮 Uso

### Executar a EVA

```bash
python main.py
```

### Modos de funcionamento

**Modo Texto** (padrão, sem necessidade de microfone):

```
🔤 Modo TEXTO ativado
📝 Digite 'sair' para terminar

📝 Digite seu comando:
>>> abre o google
Assistente: A abrir o Google
```

**Modo Voz** (requer `sounddevice`):

```
🎤 Modo VOZ ativado

🎤 Ouvindo...
🎯 Você disse: abre o google
Assistente: A abrir o Google
```

### Comandos disponíveis

| Comando | Descrição |
|---------|-----------|
| `abre o google` | Abre o Google no navegador |
| `abre o youtube` | Abre o YouTube |
| `coloca alarme em X minutos` | Cria um alarme |
| `que horas são` | Diz as horas atuais |
| `toca música X` | Reproduz música |
| `pesquisa X` | Pesquisa na web |
| `envia email para X` | Envia email |
| `sair` | Encerra a EVA |

> 📝 Consulta `comandos.json` para a lista completa.

---

## 🔌 Plugins

A EVA possui um sistema de plugins modular. Cada plugin é um ficheiro Python independente na pasta `plugins/`.

### Estrutura de um plugin

```python
# plugins/exemplo.py

def executar(parametro, assistente):
    """
    Função principal do plugin.
    
    Args:
        parametro (str): Parâmetro passado pelo comando
        assistente (Assistente): Referência à assistente
    """
    assistente.falar(f"A executar: {parametro}")
    # Lógica do plugin aqui
```

### Registar um plugin

Adiciona o comando ao `comandos.json`:

```json
{
  "comandos": [
    {
      "categoria": [
        {
          "nome do comando *": {
            "acao": "plugins.exemplo.executar",
            "resposta": "A executar o comando {param}"
          }
        }
      ]
    }
  ]
}
```

---

## 🗺️ Roadmap

### ✅ Versão 0.1.0 (Atual)
- [x] Arquitetura base em camadas
- [x] Sistema de voz (reconhecimento e síntese)
- [x] Sistema de plugins modular
- [x] Modo texto como fallback
- [x] Estrutura de pastas profissional

### 🚧 Versão 0.2.0 (Em desenvolvimento)
- [ ] Integração com LLM (OpenAI / Ollama)
- [ ] Processamento de linguagem natural
- [ ] Memória persistente de conversas
- [ ] Sistema de contexto

### 🔮 Versão 0.3.0 (Futuro)
- [ ] Algoritmos de recomendação
- [ ] Deteção de intenção
- [ ] Aprendizagem contínua
- [ ] Interface web

### 🌟 Versão 1.0.0 (Visão)
- [ ] Assistente totalmente autónoma
- [ ] Multi-plataforma (Windows, Linux, macOS, Android)
- [ ] Integração com casa inteligente
- [ ] API pública para plugins externos

---

## 🤝 Contribuir

Contribuições são **muito bem-vindas**! Este projeto é uma oportunidade de aprender e crescer em conjunto.

### Como contribuir

1. Faz **fork** do repositório
2. Cria uma **branch** para a tua feature:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Faz **commit** das tuas alterações seguindo [Conventional Commits](https://www.conventionalcommits.org/):
   ```bash
   git commit -m "feat(voz): adiciona suporte a múltiplos idiomas"
   ```
4. Faz **push** para a branch:
   ```bash
   git push origin feature/nova-funcionalidade
   ```
5. Abre um **Pull Request**

### Padrões de código

- Segue a [PEP 8](https://peps.python.org/pep-0008/)
- Usa **type hints** sempre que possível
- Escreve **docstrings** em português
- Adiciona **testes** para novas funcionalidades

### Tipos de commit

| Tipo | Descrição |
|------|-----------|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Documentação |
| `refactor` | Refatoração |
| `test` | Testes |
| `chore` | Tarefas de manutenção |

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** — consulta o ficheiro [LICENSE](LICENSE) para mais detalhes.

```
MIT License

Copyright (c) 2026 Chalot10

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Agradecimentos

- **Projeto Yuni** — pelo ecossistema e inspiração
- **Comunidade Python** — pelas bibliotecas fantásticas
- **Contribuidores** — por tornarem este projeto melhor

### Bibliotecas utilizadas

| Biblioteca | Propósito |
|-----------|-----------|
| [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) | Reconhecimento de voz |
| [gTTS](https://pypi.org/project/gTTS/) | Síntese de voz (Google) |
| [pyttsx3](https://pypi.org/project/pyttsx3/) | Síntese de voz offline |
| [sounddevice](https://pypi.org/project/sounddevice/) | Captura de áudio |
| [pygame](https://pypi.org/project/pygame/) | Reprodução de áudio |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Variáveis de ambiente |
| [requests](https://pypi.org/project/requests/) | Pedidos HTTP |

---

## 📞 Contacto

**Autor**: Francisco Bento Novela

- 🐙 GitHub: [@Chalot10](https://github.com/Chalot10)
- 📧 Email: franciscobentonovela@gmail.com

**Link do Projeto**: [https://github.com/Chalot10/EVA](https://github.com/Chalot10/EVA)

---

<p align="center">
  <strong>⭐ Se este projeto te foi útil, considera dar uma estrela! ⭐</strong>
</p>

<p align="center">
  Feito com ❤️ em Moçambique
</p>

<p align="center">
  <sub>EVA — Entidade Virtual Assistiva | Projeto Yuni | 2026</sub>
</p>

