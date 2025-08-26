import time

import torch
from PIL import Image
import trimesh

from hy3dgen.rembg import BackgroundRemover
from hy3dgen.texgen import Hunyuan3DPaintPipeline

images_path = [
    "/content/Hunyuan3D-2-Abimael/assets/example_mv_images/1/Front.png",
    "/content/Hunyuan3D-2-Abimael/assets/example_mv_images/1/Side.png",
    "/content/Hunyuan3D-2-Abimael/assets/example_mv_images/1/Back.png"
]

images = []
for image_path in images_path:
    image = Image.open(image_path)
    if image.mode == 'RGB':
        rembg = BackgroundRemover()
        image = rembg(image)
    images.append(image)

pipeline = Hunyuan3DPaintPipeline.from_pretrained(
    'tencent/Hunyuan3D-2',
    subfolder='hunyuan3d-paint-v2-0-turbo'
)

mesh = trimesh.load('assets/1.glb')

mesh = pipeline(mesh, image=images)
mesh.export('demo_textured.glb')