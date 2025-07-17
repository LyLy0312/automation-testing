import os
import time
import allure
import functools

def screenshot_decorator(func):
    @functools.wraps(func)
    def wrapper(self, name: str, *args, **kwargs):
        folder = os.path.join("..", "screenshots", "image_xno")
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, name)

        try:
            print(f"[Start Screenshot] {name}")
            start = time.time()
            result = func(self, name, *args, **kwargs)
            self.page.wait_for_timeout(2000)
            self.page.screenshot(path=path, full_page=True)
            end = time.time()
            print(f"[Done Screenshot] {name} in {round(end - start, 2)}s")

            if os.path.exists(path):
                allure.attach.file(
                    path,
                    name=name,
                    attachment_type=allure.attachment_type.PNG
                )
            return result
        except Exception as e:
            print(f"[Error Screenshot] {name} - {str(e)}")
            raise
    return wrapper
