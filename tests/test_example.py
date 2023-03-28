import time


def test_example(tester_bot):
    tester_bot.send_message()
    # Если тестируемый бот отвечает на каждое сообщение, можно добавить явное ожидание прямо в send_message
    time.sleep(2)
    assert tester_bot.get_last_message() == "Привет, я бот!"
