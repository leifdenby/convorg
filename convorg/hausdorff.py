import numpy as np

def hausdorff_dimension(cloudmask):
    if not len(cloudmask.shape) == 2:
        raise NotImplementedError("Can only calculate Hausdorff fractal"
                                  " dimension of 2D arrays")

    collapsed = np.argwhere(cloudmask > 0)
    Lx, Ly = cloudmask.shape

    # computing the fractal dimension
    # considering only scales in a logarithmic list
    scales=np.logspace(0.01, 10, num=10, endpoint=False, base=1.8)

    Ns= np.zeros_like(scales)
    # looping over several scales
    for i, scale in enumerate(scales):
        try:
            bins = (np.arange(0,Lx,scale),np.arange(0,Ly,scale))
            H, edges = np.histogramdd(collapsed, bins=bins)
            Ns[i] = np.sum(H>0)
        except Exception as e:

            Ns = Ns[:i]
            scales = scales[:i]

            raise

            break

    # linear fit, polynomial of degree 1
    data =np.polyfit(x=np.log(scales), y=np.log(Ns), deg=1, full=True)

    coeffs, residuals, rank, singular_values, rcond = data

    return -coeffs[0]
