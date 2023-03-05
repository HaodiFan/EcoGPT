from routines import routines as default_routines
from loguru import logger
class PromptParser:
    def __init__(self, routines = default_routines):
        self.__routine = routines


    def parse(self, text, debug=False):
        for process in self.__routine:
            if debug:
                logger.debug(f'Current process: {process.__name__}')
            text = process(text)
            if debug:
                logger.debug(f'Output: {text}')
        return text



if __name__ == "__main__":
    a = PromptParser()
    a.parse("我想操死你fucking bitch", debug=True)