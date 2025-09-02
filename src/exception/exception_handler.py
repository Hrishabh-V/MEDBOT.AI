import functools
import traceback

def catch_exceptions(func):
    """
    Decorator for synchronous functions.
    Prints full traceback on exception.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"\n❌ Exception in {func.__name__}: {e}")
            traceback.print_exc()
            return None
    return wrapper


def catch_async_exceptions(func):
    """
    Decorator for async functions (coroutines).
    Prints full traceback on exception.
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            print(f"\n❌ Exception in {func.__name__}: {e}")
            traceback.print_exc()

            # If Telegram update exists, also reply back
            update = kwargs.get("update") or (args[0] if args else None)
            if update and hasattr(update, "message"):
                try:
                    await update.message.reply_text(f"⚠️ Error: {e}")
                except Exception:
                    pass
            return None
    return wrapper


def handle_exception(e: Exception, context: str = "") -> str:
    """
    Handle exceptions in a consistent way across the project.
    Returns a user-friendly error message including exception type.
    """
    if context:
        return f"⚠️ Error in {context}: {type(e).__name__} - {e}"
    return f"⚠️ Error: {type(e).__name__} - {e}"

def run_safe(func):
    """
    Run a top-level function safely (like main()).
    Shows full traceback if it crashes.
    """
    try:
        func()
    except KeyboardInterrupt:
        print("🛑 Stopped manually.")
    except Exception as e:
        print(f"\n❌ Fatal error in {func.__name__}: {e}")
        traceback.print_exc()
