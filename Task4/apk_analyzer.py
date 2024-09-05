from androguard.misc import AnalyzeAPK
from loguru import logger

class APKAnalyzer:
    def __init__(self, apk_path):
        self.apk_path = apk_path
        self.package_name = None
        self.version_code = None
        self.version_name = None
        self.permissions = []
        
        logger.remove()
        logger.add(lambda msg: None, level="ERROR")
    
    def analyze(self):
        try:
            a, d, dx = AnalyzeAPK(self.apk_path)
            self.package_name = a.get_package()
            self.version_code = a.get_androidversion_code()
            self.version_name = a.get_androidversion_name()
            self.permissions = a.get_permissions()
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise

    def get_package_name(self):
        return self.package_name

    def get_version_code(self):
        return self.version_code

    def get_version_name(self):
        return self.version_name

    def get_permissions(self):
        return self.permissions
