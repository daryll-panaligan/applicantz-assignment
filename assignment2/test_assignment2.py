import filecmp
import os
import shutil

import pytest

import assignment2


def copy_to_temp_file(tmp_path, file_path):
    tmp_file_path = os.path.join(tmp_path, file_path)
    shutil.copyfile(file_path, tmp_file_path)
    return tmp_file_path

@pytest.fixture
def input_file(tmp_path, request):
    input_file_src = request.param[0]
    tmp_file_path = copy_to_temp_file(tmp_path, input_file_src)

    expected_file_src = request.param[2]
    tmp_file_result_path = copy_to_temp_file(tmp_path, expected_file_src)

    return tmp_file_path, request.param[1], tmp_file_result_path

@pytest.mark.parametrize('input_file',
                         [['VERSION', 'ADLMSDK_VERSION_POINT=', 'VERSION_expected'],
                          ['SConstruct', 'point=', 'SConstruct_expected']],
                         indirect=True)
def test_update_build_number(input_file):
    path = input_file[0]
    pattern = input_file[1]
    result = input_file[2]
    buildNum = 123
    assignment2.updateBuildNumber(path, pattern, buildNum)
    assert filecmp.cmp(path, result)
