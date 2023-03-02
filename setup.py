from setuptools import find_packages, setup

setup(
    name='dcstit',
    version='0.1dev',
    entry_points={
        'console_scripts': [
            'dcstit_train = dcstit.train:main',
            'dcstit_edit = dcstit.edit_video:main',
            'dcstit_edit_turing = dcstit.edit_video_stitching_tuning:main',
        ],
    },
    packages=find_packages(),
    license='',
    python_requires=">=3.8",
    install_requires=[
        'pillow>=9.0.1',
        'dlib>=19.22.1',
        'numpy>=1.20.3',
        'scipy>=1.7.1',
        'scikit-image>=0.18.3',
        'tqdm>=4.62.3',
        'wandb>=0.12.9',
        'matplotlib>=3.4.3',
        'opencv-python>=4.5.4.60',
        'requests>=2.26.0',
        'click>=8.0.3',
        'lpips>=0.1.4',
        'imageio>=2.14.1',
        'imageio-ffmpeg>=0.4.5',
        'face-alignment>=1.3.5',
        'ninja',
    ],
    include_package_data=True,
    package_data={'': ['*.yaml', '*.cu', '*.cpp', '*.h']},
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown'
)