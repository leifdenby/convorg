import numpy as np

import convorg

CLOUD_MASK = np.random.random((200, 200)) > 0.9

def test_iorg():
    o = convorg.iorg(cloudmask=CLOUD_MASK)

def test_scai():
    convorg.scai(cloudmask=CLOUD_MASK)
