from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, UserBankAccountUpdateView, user_logout,pass_change,return_item, BorrowListView ,borrow_now1 ,return_item1
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('register/', UserRegistrationView.as_view(), name='register' ),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    path('logout/', user_logout, name='logout'),
    # path('profile/', Profile, name='profile' ),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ),
    path('profile/pass_change/', pass_change, name='pass_change'),
    # path('profile/borrow-list/', borrow_list, name='borrow_list'),
    path('borrow_list/', BorrowListView.as_view(), name='borrow_list'),
    path('return-item/<int:cart_item_id>/', return_item, name='return_item'),
    path('borrow_list/borrow_more/<int:book_id>/', borrow_now1, name='borrow_now1'),
    path('return-item1/<int:cart_item_id>/', return_item1, name='return_item1'),

]