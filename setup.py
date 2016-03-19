from distutils.core import setup

setup(
    name='SerialPad',
    version='0.1dev',
    packages=['serialpad',],
    license='BSD',
    long_description=open('README.md').read(),
    scripts=['scripts/playerpad', 'scripts/padnotify.sh'],
    data_files=[('/etc/serialpad', ['config.yaml']),
                ('/etc/udev/rules.d', ['udev/rules.d/10-serialpad.rules'])]
)
