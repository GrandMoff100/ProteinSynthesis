class BasesCheck(str):
    bases: str = ""

    def __new__(cls, content: str):
        if any(map(lambda x: x not in cls.bases, content.upper())):
            raise ValueError(f"Can only contain these letters, {cls.bases}")
        return str.__new__(cls, content.upper())
