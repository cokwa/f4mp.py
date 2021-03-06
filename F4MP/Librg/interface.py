import os
import ctypes
from F4MP.Librg.classes import Address

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dll = ctypes.cdll.LoadLibrary(os.path.join(BASE_DIR, "bin/librg.dll"))


def init(ctx):
    dll.librg_init(ctx)


def is_client(ctx):
    return bool(dll.librg_is_client(ctx))


def is_connected(ctx):
    return bool(dll.librg_is_connected(ctx))


def event_add(ctx, event_id, callback):
    if not dll.librg_event_add(ctx, event_id, callback):
        raise


def network_add(ctx, message_id, callback):
    dll.librg_network_add(ctx, message_id, callback)


def network_start(ctx, address: bytes, port: int):
    address = Address(port, address)

    ret = dll.librg_network_start(ctx, address)


def tick(ctx):
    dll.librg_tick(ctx)


def data_write(data, type, value):
    getattr(dll, "librg_data_w" + type)(data, value)


def data_read(data, type):
    return getattr(dll, "librg_data_r" + type)(data)
