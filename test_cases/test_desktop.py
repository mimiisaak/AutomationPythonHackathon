import pytest
from test_cases.conftest import my_mobile_starter


@pytest.mark.usefixtures("my_mobile_starter")
class Test_Desktop:

    def test_01(self):
        print()