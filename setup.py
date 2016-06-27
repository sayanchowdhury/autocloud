from setuptools import setup, find_packages

requires = [
    'redis',
    'retask',
    'fedmsg',
]

setup(
    name='autocloud',
    version='0.4',
    description='',
    author='',
    author_email='',
    url='https://github.com/kushaldas/autocloud',
    install_requires=requires,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
    entry_points={
        'moksha.consumer': [
            "autocloud_consumer = autocloud.consumer:AutoCloudConsumer",
        ],
    },
)
