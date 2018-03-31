# from django.contrib.auth.hashers import check_password
# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend
#
# class LoginBackend(ModelBackend):
#
#     def authenticate(self, request, username="", password="", **kwargs):
#         try:
#             user = get_user_model().objects.get(email__iexact=username)
#             if check_password(password, user.password):
#                 return user
#             else:
#                 return None
#         except get_user_model().DoesNotExist:
#             return None
