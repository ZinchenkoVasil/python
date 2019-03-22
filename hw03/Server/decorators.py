import inspect
import logging
import traceback
import functools
INDENT = 4*' '

def log(func):
        @functools.wraps(func)
        def callf(*args, **kwargs):
            logger = logging.getLogger('server.main')
            logger.debug("Вызов %s: %s, %s" % (func.__name__, args, kwargs))
            #callstack = '\n'.join([INDENT + line.strip() for line in traceback.format_stack()][:-1])
            #print('{}() called:'.format(func.__name__))
            logger.debug(f"функция {func.__name__} вызвана из функции {inspect.stack()[1][3]}")
            r = func(*args, **kwargs)
            logger.debug("%s вернула %s" % (func.__name__, r))
            return r
        return callf
