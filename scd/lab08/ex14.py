from asyncio import Future

my_future=Future()
print(f'Done: {my future.done()}") my_future.set_result(42)
print(f'Done: {my_future.done()}") print(f'Value: {my_future.result()}')
