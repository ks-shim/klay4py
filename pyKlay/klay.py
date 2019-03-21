import os

from py4j.java_gateway import JavaGateway, GatewayParameters
from py4j.java_gateway import launch_gateway

__all__ = ['gateway']

"""gateway = None

def init_gateway(jar_path="./libs", max_heap=1024):
    global gateway

    if gateway is not None:
        return
"""
libraries = [
    '{0}{1}klay-python-wrapper-0.3.jar'
]
jar_path = './libs'
max_heap = 1024

classpath = os.pathsep.join([lib.format(jar_path, os.sep) for lib in libraries])
py4j_path = '{0}{1}py4j0.10.8.1.jar'.format(jar_path, os.sep)

port = launch_gateway(jarpath=py4j_path,
                      classpath=classpath,
                      javaopts=['-Dfile.encoding=UTF8', '-ea', '-Xmx{}m'.format(max_heap)],
                      die_on_exit=True)

try:
    gateway = JavaGateway(gateway_parameters=GatewayParameters(port=port, auto_convert=True))
except Exception as e:
    gateway = None

config_file_path = './data/configuration/klay.conf'
klay_ep = gateway.jvm.klay.python.wrapper.KlayEntryPoint(config_file_path)
morphs = klay_ep.doKlay('안녕하세요 KLAY입니다.')
for morph in morphs.iterator():
    print(morph)