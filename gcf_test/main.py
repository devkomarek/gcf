from googlecloudfunctions import gcf
print('hello world pk')


@gcf
def test_func(request):
    return (['test1', 'test2'], 200)


test_func(123)
