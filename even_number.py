from loguru import logger


def validate(f):
    def wrap(a,b):
        print(a,b)
        if a > b:
            logger.info("End must be higher or equal to Start")
        f(a,b) 
    return f


def even_or_odd(number:int)->bool:
    if number % 2 == 0:
        logger.info(f"The given number {number} is even")
    else:
        logger.info(f"The given number {number} is even")
@validate
def generate_even_number(start,end)-> list:
    return [i for i in range(start,end) if i%2==0]
@validate
def generate_odd_number(start,end)-> list:
    return [i for i in range(start,end) if i%2==1]


if __name__ == "__main__":
    even_or_odd(10)
    print(generate_even_number(10,30))
    print(generate_odd_number(10,30))