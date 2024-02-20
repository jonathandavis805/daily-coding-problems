from daily_coding_problems.lfu_cache import Cache


def test_cache():
    cache = Cache(5)
    cache.set("test0", "test")
    assert cache.get("test0") is not None
    cache.set("test1", "test")
    cache.get("test1")
    cache.set("test2", "test")
    cache.get("test2")
    cache.set("test3", "test")
    cache.get("test3")
    cache.set("test4", "test")
    cache.set("test5", "test")
    assert cache.get("test0") is not None
    assert cache.get("test1") is not None
    assert cache.get("test2") is not None
    assert cache.get("test3") is not None
    assert cache.get("test5") is not None
    assert cache.get("test4") is None
