import numpy as np

import convorg

CLOUD_MASK = np.random.random((200, 200)) > 0.9

def test_iorg():
    cloud_props = convorg.get_cloudproperties(CLOUD_MASK)
    dists = convorg.neighbor_distance(cloud_props)
    o = convorg.iorg(neighbor_distance=dists, cloudmask=CLOUD_MASK)
    assert o == 0.5

def test_scai():
    cloud_props = convorg.get_cloudproperties(CLOUD_MASK)
    convorg.scai(cloudproperties=cloud_props, cloudmask=CLOUD_MASK)
