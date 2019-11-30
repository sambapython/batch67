import logging
#debug,info,warn,error
logging.basicConfig(level=logging.DEBUG, filename="log.txt",
	format="%(asctime)s==>%(levelname)s==>%(message)s")
logging.info("welcome")
number1 = input("Enter number1:")
logging.info("number1 entered")
number2 = input("Enter number2:")
logging.info("number2 entered")
logging.debug(f"before conversion: number1:{number1},number2:{number2}")
try:
    number1=float(number1)
    logging.info("number1 converrted")
    number2 = float(number2)
    logging.info("number2 converted")
    logging.debug(f"after conversion: number1:{number1},number2:{number2}")
    res = number1/number2
    logging.info("result calculated")
    print(res)
    logging.debug("RESULT: %s" % res)
except ValueError as err:
    print("exepecting digits only")
    logging.error("exepecting digits only")
except ZeroDivisionError as err:
    print("number should not exquals to zero")
    logging.error(err)
except Exception as err:
    print("some issue: %s"%err)
    logging.error(err)
logging.info("Operation completed")