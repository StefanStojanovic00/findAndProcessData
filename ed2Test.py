import pytest
import pandas as pd
from ed2 import update

def test_merge_tables():

    df1 = pd.DataFrame({
        "Fabr.broj aktivnog brojila": ["00730045", "00730050"], 
       "Krajnje stanja aktiv. VT": [None, None], 
    })

    df2 = pd.DataFrame({
        "SERIJSKI BROJ BROJILA": ["00730045", "00730050"],
        "1.8.1 [kWh]": [100, 200],
       
    })
  
    result = update(df1, df2)

    assert pd.isna(result.loc["00730045", "1.8.1 "])  

    
    assert result.loc["00730045", "1.8.1 "] == 100  




def test_excel_merge():
    df1 = pd.read_excel(r"c:\Users\SS\Desktop\eksel za eps\radni\Nites AMM očitavanja - 01.01.2025.xlsx")
    df2 = pd.read_excel(r"c:\Users\SS\Desktop\eksel za eps\radni\KP - Registar početna stanja i obračun - XII -  03.01.2025.xlsx")
    expected = pd.read_excel(r"2UPDATOVANA-KP - Registar početna stanja i obračun - XII -  03.01.2025.xlsx")

    result = update(df2, df1)

    pd.testing.assert_frame_equal(result, expected)

def test_excel_write(tmp_path):
    output_file = tmp_path / "test_output.xlsx"
    df = pd.DataFrame({"A": [1, 2, 3]})
    df.to_excel(output_file, index=False)

    loaded = pd.read_excel(output_file)
    pd.testing.assert_frame_equal(df, loaded)
