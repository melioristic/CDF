from torch.utils.data import Dataset
import xarray as xr
import torch

class YearWiseData(Dataset):
    def __init__(self, ds_path:str, folder_name:str) -> None:
        super().__init__()

        self.ds_path = ds_path
        self.folder_name = folder_name
        self.var_name = folder_name + "hPa" if folder_name == "geopotential_500" else folder_name #! Needs to be fixed

    def __getitem__(self, index):
        # TODO take leap year into account
        # TODO var_name and folder name are not same every time
        
        year = index%365*24 + 1979 # ! Needs to be fixed


        file_to_load = f"{self.ds_path}{self.folder_name}/{self.var_name}_{year}_5.625deg.nc" 
        data = xr.open_dataset(file_to_load)

        key_list = list(data.keys())        
        
        assert len(key_list)==1
        
        return torch.from_numpy(data[key_list[0]].values[index%365*24, :, :])

        # print(data)