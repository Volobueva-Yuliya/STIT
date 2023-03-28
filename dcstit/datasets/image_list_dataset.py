from torch.utils.data import Dataset
from PIL import Image

class ImageListDataset(Dataset):

    def __init__(self, images, quads, image_size, source_transform=None, names=None):
        self.images = images
        self.quads = quads
        self.image_size = image_size
        self.source_transform = source_transform
        self.names = names

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        image = self.images[index]
        quad = self.quads[index]
        name = self.names[index] if self.names is not None else str(index)
        from_im = crop_image(image, self.image_size, quad.copy())

        if self.source_transform:
            from_im = self.source_transform(from_im)

        return name, from_im

