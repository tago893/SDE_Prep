class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split(".")
        version2 = version2.split(".")
        if len(version1)>len(version2):
            version2.extend(['0']*(len(version1)-len(version2)))
        elif len(version1)<len(version2):
            version1.extend(['0']*(len(version2)-len(version1)))
        
        for i in range(0,len(version1)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version2[i])>int(version1[i]):
                return -1
        return 0