from utils.serializers import BaseSerializer


class UserSerializer(BaseSerializer):
    """ 用户的基础信息 """
    def to_dict(self):
        user = self.obj
        return {
            'nickname': user.nickname,
            'avatar': user.avatar_url
        }


class UserProfileSerializer(BaseSerializer):
    """ 用户的详细信息 """
    def to_dict(self):
        profile = self.obj
        return {
            'real_name': profile.real_name,
            'sex': profile.sex,
            # 通过 get_sex_display() 返回对应的中文信息
            'sex_display': profile.get_sex_display(),
        }
