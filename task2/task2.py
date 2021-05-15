import re


class Version:
    """
    Identifys and comparares versions
    """
    BASE_VERSION_PATTERN = "[0-9]+.[0-9]+.[0-9]+"
    ADD_VERSION_PATTERN = "[0-9a-z]+"

    def __init__(self, version):
        # Extract numeric part of version
        self.base_version = tuple([int(key) for key in re.findall(self.BASE_VERSION_PATTERN, version)[0].split('.')])
        # Extract additional part of version
        tmp_string = re.sub(self.BASE_VERSION_PATTERN, '!', version)
        self.add_version = tuple(re.findall(self.ADD_VERSION_PATTERN, tmp_string))


    def __gt__(self, version_2):
        if self.base_version > version_2.base_version:
            return True
        if version_2.add_version and (not self.add_version):
            return True
        if self.add_version > version_2.add_version:
            return True
        return False


    def __ne__(self, version_2):
        if self.base_version != version_2.base_version:
            return True
        if self.add_version != version_2.add_version:
            return True
        return False


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0")
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "lt failed"
        assert Version(version_2) > Version(version_1), "gt failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()
