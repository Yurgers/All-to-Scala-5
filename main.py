import asyncio
from operations import perform_operation
# Инициализация asyncio loop
loop = asyncio.get_event_loop()

# Запуск асинхронной операции
result = loop.run_until_complete(perform_operation("qwer"))
print(result)
