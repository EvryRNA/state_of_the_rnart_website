class AbstractPage:
    def __init__(self, img_path: str, *args, **kwargs):
        self.img_path = img_path

    def get_page(self):
        raise NotImplementedError()
