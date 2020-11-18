
import GetBondDuration_File

def test_getBondDuration():
    assert round(GetBondDuration_File.getBondDuration(.03, 2000000, .04, 10,1),2) == 8.51
