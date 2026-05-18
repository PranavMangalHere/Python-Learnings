import logging

logging.basicConfig(filename="app.log",
                    level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

def divide(a, b):
    logging.info(f"Dividing by {a} and {b}")
    try:
        logging.info(a/b)
        return a / b
    except ZeroDivisionError:
        logging.exception("Division failed")
        return None

divide(1, 2)
divide(1, 0)