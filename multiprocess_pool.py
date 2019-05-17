from multiprocessing.pool import ThreadPool
import multiprocessing

cores=multiprocessing.cpu_count()
def foo(bar, baz):
	Second="second return"
	Third=33
	print ('\nhello {0}'.format(bar))
	return 'foo' + baz , Second , Third


pool = ThreadPool(processes=cores)

async_result = pool.apply_async(foo, ('world', 'fighters')) # tuple of args for foo

# do some other stuff in the main process

return_val,Second,Third = async_result.get()  # get the return value from your function.
print(return_val,",",Second,",",Third)
print("the machine has",cores,"Cores")