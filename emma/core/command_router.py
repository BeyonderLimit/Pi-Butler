# core/command_router.py
from commands import system_commands, math_tools, reminders, file_scanner, app_launcher

class CommandRouter:
    def execute(self, packet):
        intent = packet["intent"]

        match intent:
            case "greet": return "Good evening, sir."
            case "standby": return "Entering standby mode, sir."
            case "time": return system_commands.get_time()
            case "date": return system_commands.get_date()
            case "status": return system_commands.get_status()
            case "math": return math_tools.calculate(packet["text"])
            case "reminder": return reminders.create(packet["text"])
            case "file_scan": return file_scanner.scan(packet["text"])
            case "launch_app": return app_launcher.launch(packet["text"])
            case "volume": return system_commands.set_volume(packet["text"])
            case "capabilities": return system_commands.capabilities()
            case "assistant_help": return "Allow me to guide you, sir."
            case "task_priority": return "I will prioritize your tasks, sir."
            # case : return "I’m afraid I do not recognize that command, sir."
            case "identity": return "I am EMMA, your personal digital assistant, designed to aid you in all tasks, sir."
            case "help": return (
                "I am here to assist you, sir. "
                "You may ask me about time, schedule reminders, scan files, "
                "launch applications, perform calculations, or manage tasks."
                )

