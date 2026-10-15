import importlib


class Executor:
    def __init__(self, assistente):
        self.assistente = assistente

    def executar(self, func_path, parametro=None):
        """Executa um plugin ou comando interno"""
        if parametro is None:
            parametro = ""

        # Comandos internos (abrir_programas, etc.)
        if func_path.startswith(('web!', 'web?', 'path:', 'commands', 'system:', 'media:')):
            from plugins.abrir_programas import parse_command
            parse_command(func_path, parametro, self.assistente)

        # Comandos de alarme (quando é um dicionário)
        elif isinstance(func_path, dict):
            from plugins.colocar_alarme import parse_command as parse_alarm_command
            from plugins.colocar_alarme import extract_argument_with_time

            # Pega o primeiro comando de alarme
            alarme_comandos = self.assistente.comandos.comandos[0]['alarme'][0]

            argument, when = extract_argument_with_time(
                parametro,
                list(alarme_comandos.keys())[0],
                func_path['time_indicator']
            )

            parse_alarm_command(func_path, argument, when, self.assistente)

        else:
            # Comando de plugin externo
            try:
                parts = func_path.split(".")
                if len(parts) < 2:
                    raise ValueError(f"Caminho inválido: {func_path}")

                module_name = ".".join(parts[:-1])
                func_name = parts[-1]

                plugin = importlib.import_module(module_name)
                func = getattr(plugin, func_name)

                if parametro:
                    func(parametro, self.assistente)
                else:
                    func(self.assistente)

            except ImportError:
                self.assistente.falar(f"Módulo {module_name} não encontrado")
            except AttributeError:
                self.assistente.falar(f"Função {func_name} não existe no módulo {module_name}")
            except Exception as e:
                self.assistente.falar(f"Erro ao executar comando: {str(e)}")