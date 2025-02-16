
from torcheeg.datasets import HMCDataset

import torcheeg.transforms as transforms


dataset=HMCDataset(root_path='/mnt/replace_disk/EEG_data/HMC/haaglanden-medisch-centrum-sleep-staging-database-1.1/recordings',
                    sfreq=100,
                    channels=['EEG F4-M1', 'EEG C4-M1', 'EEG O2-M1', 'EEG C3-M2'],
                    label_transform=transforms.Compose([
                        transforms.Select('label'),
                        transforms.Mapping({'Sleep stage W': 0,
                                            'Sleep stage N1': 1,
                                            'Sleep stage N2': 2,
                                            'Sleep stage N3': 3,
                                            'Sleep stage R': 4,
                                            'Lights off@@EEG F4-A1': 0})
                    ]),
                    online_transform=transforms.ToTensor(),
                    io_path='/mnt/replace_disk/EEG_data/HMC/haaglanden-medisch-centrum-sleep-staging-database-1.1/processed/'
                    )
print("dataset:\t",type(dataset))