import asyncio
import string

# Gurtam char iterator
class CharIterator:
    def __init__(self):
        self.pos = 1

    def __aiter__(self):
        return self

    async def __anext__(self):
        while self.pos < len(string.ascii_lowercase):
            self.pos += 1
            char = string.ascii_lowercase[self.pos -1]

            if self.pos == 7:
                return char.capitalize()
            elif self.pos in (21, 18, 20, 1, 13):
                return char[self.pos]
            else:
                raise StopAsyncIteration


# Gurtam Chars position generator
def char_pos_gen():
    char_pos = [4, 0, 5, 3, 2, 1]
    for pos in char_pos:
        yield pos


# main section
async def main():
    dw = ()
    cpg = char_pos_gen()
    async for char in CharIterator:
        dw[next(cpg)] = char

    res = ''
    for n in sorted(dw):
        res =+ dw[n]

    print(res)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except:
        loop.close()