import os
import pandas as pd
import veeries.io as vio


class SampleClass:
    def __init__(self) -> None:
        self.dct_paths = {
            "vsp_input": {
                "produtos": r"C:\veeries\veeries\vsp - Documentos\0_BD\1_fontes\veeries_padroes\dicionario_produtos.xlsx",
                "geografia": r"C:\veeries\veeries\vsp - Documentos\0_BD\1_fontes\veeries_padroes\geografia\dicionarios_geografia_veeries.xlsx",
                "dummy_csv": r"C:\veeries\veeries\vsp - Documentos\0_BD\1_fontes\B3\commodity_settlement_price.csv",
            },
            "input": {
                "produtos": "input/dicionario_produtos.xlsx",
                "geografia": "input/dicionarios_geografia_veeries.xlsx",
                "dummy_csv": "input/dummy_csv.csv",
            },
            "output": {
                "sample_xlsx": "output/sample.xlsx",
                "sample_csv": "output/sample.csv",
            },
            "vsp_output": {
                "sample_xlsx": r"C:\veeries\veeries\vsp - Documentos\9_Testes\testes\sample.xlsx",
                "sample_csv": r"C:\veeries\veeries\vsp - Documentos\9_Testes\testes\sample.csv",
            },
        }

    @staticmethod
    def copy_files_to_input(dct_paths: dict):
        for key in dct_paths["input"].keys():
            source = dct_paths["vsp_input"][key]
            destination = dct_paths["input"][key]
            vio.shutil.copy(source, destination)

    @staticmethod
    def copy_files_to_vsp(dct_paths: dict):
        for key in dct_paths["vsp_output"].keys():
            source = dct_paths["output"][key]
            destination = dct_paths["vsp_output"][key]
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            vio.shutil.copy(source, destination)

    @staticmethod
    def get_reg_veeries(dct_dfs_geografia: dict[str, pd.DataFrame]) -> pd.DataFrame:
        return dct_dfs_geografia["reg_veeries"].copy()
    
    def run_process(self):
        print("start process")
        os.makedirs("input", exist_ok=True)
        os.makedirs("output", exist_ok=True)
        self.copy_files_to_input(self.dct_paths)
        df_first_sheet_from_xlsx = vio.pandas.read_excel(self.dct_paths["input"]["produtos"])
        dct_dfs_geografia = vio.pandas.read_excel(self.dct_paths["input"]["geografia"], sheet_name=None)
        sample_csv = vio.pandas.read_csv(self.dct_paths["input"]["dummy_csv"])
        sample_xlsx = self.get_reg_veeries(dct_dfs_geografia)
        vio.pandas.to_csv(sample_csv, self.dct_paths["output"]["sample_csv"])
        vio.pandas.to_excel(sample_xlsx, self.dct_paths["output"]["sample_xlsx"], index=False)
        self.copy_files_to_vsp(self.dct_paths)
        print("end process")


if __name__ == "__main__":
    SampleClass().run_process()
