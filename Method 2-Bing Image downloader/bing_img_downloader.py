# !pip install bing_image_downloader
from bing_image_downloader import downloader

downloader.download("koala", limit=100, output_dir='images', force_replace=False, timeout=2,verbose=True)