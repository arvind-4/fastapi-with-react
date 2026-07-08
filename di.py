"""Dependency Injection utilities for FastAPI apps."""

import functools
import inspect
from collections.abc import Callable
from typing import Any, TypeVar, cast

T = TypeVar("T")


class DependencyError(Exception):
    """Raised on registration or resolution problems."""


class _Registry:
    """Internal holder for everything the DI system knows about."""

    def __init__(self) -> None:
        self.dependencies: dict[type, list[type]] = {}
        self.instances: dict[type, object] = {}

    def reset(self) -> None:
        """Mainly useful for tests — wipes all registrations and instances."""
        self.dependencies.clear()
        self.instances.clear()


_registry = _Registry()


def register(
    dependencies: list[type] | None = None,
) -> Callable[[type[T]], type[T]]:
    """Register a class with the DI container."""

    def decorator(cls: type[T]) -> type[T]:
        _registry.dependencies[cls] = dependencies or []
        return cls

    return decorator


def resolve[T](cls: type[T]) -> T:
    """Resolve a class from the DI container."""
    if cls in _registry.instances:
        return cast("T", _registry.instances[cls])

    if cls not in _registry.dependencies:
        msg = f"{cls.__name__!r} is not registered. Did you forget @register() on it?"
        raise DependencyError(msg)

    dep_classes = _registry.dependencies[cls]
    resolved_deps = [resolve(dep) for dep in dep_classes]

    try:
        instance = cls(*resolved_deps)
    except TypeError as e:
        msg = f"Failed to resolve {cls.__name__}: {e}"
        raise DependencyError(msg) from e

    _registry.instances[cls] = instance
    return instance


def inject(**deps: type) -> Callable:
    """Inject dependencies into a function."""

    def decorator(func: Callable) -> Callable:
        is_async = inspect.iscoroutinefunction(func)

        if is_async:

            @functools.wraps(func)
            async def async_wrapper(*args: object, **kwargs: object) -> object:
                for name, cls in deps.items():
                    kwargs.setdefault(name, resolve(cls))
                return await func(*args, **kwargs)

            wrapper = async_wrapper
        else:

            @functools.wraps(func)
            def sync_wrapper(*args: object, **kwargs: object) -> object:
                for name, cls in deps.items():
                    kwargs.setdefault(name, resolve(cls))
                return func(*args, **kwargs)

            wrapper = sync_wrapper

        original_signature = inspect.signature(func)
        visible_params = [
            param
            for name, param in original_signature.parameters.items()
            if name not in deps
        ]
        cast("Any", wrapper).__signature__ = original_signature.replace(
            parameters=visible_params
        )

        return wrapper

    return decorator


def load_all_deps() -> None:
    """Resolve all registered dependencies to build singletons."""
    for cls in list(_registry.dependencies.keys()):
        resolve(cls)
