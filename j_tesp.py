# Проверим какая версия jinja2 установлена
try:
    import jinja2
    print(f"Текущая версия jinja2: {jinja2.__version__}")
except ImportError:
    print("jinja2 не установлен")