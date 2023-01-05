import torch
from .profiling import memprof, disable_memprof


@memprof(columns=('active_bytes.all.peak', 'reserved_bytes.all.peak', 'active_bytes.all.current', 'time'))
def test_func():
    A = torch.ones(1000, 1000).cuda()
    B = torch.ones(1000, 1000).cuda()

    C = A + B
    for i in range(3):
        D = inner_func(C)

@memprof(columns=('active_bytes.all.peak', 'reserved_bytes.all.peak', 'active_bytes.all.current'))
def inner_func(tensor):
    tensor = torch.exp(tensor)
    A = torch.ones(10000, 10000).cuda()
    return tensor

if __name__ == '__main__':
    # disable_memprof()
    test_func()