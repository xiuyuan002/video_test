from django.views.generic import View
from django.shortcuts import redirect,reverse
from app.libs.base_render import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator
from app.utils.permission import dashboard_auth

class Login(View):
    TEMPLATE='dashboard/auth/login.html'


    def get(self,request):

        #print(dir(request.COOKIES))

        if request.user.is_authenticated:
            return redirect(reverse('dashboard_index'))

        to=request.GET.get('to','')
        data={'error':'','to':to}
        return render_to_response(request,self.TEMPLATE,data=data)


    def post(self,request):
        username= request.POST.get('username')
        password= request.POST.get('password')
        print(username,password)
        data={}
        exists=User.objects.filter(username=username).exists()

        to=request.GET.get('to','')

        if not exists:
            data['error'] = '不存在该用户'
            return render_to_response(request,self.TEMPLATE,data=data)

        user=authenticate(username=username,password=password)

        if not user:
            data['error'] = '密码错误'
            return  render_to_response(request,self.TEMPLATE,data=data)

        if not user.is_superuser:
            data['error'] = '无权登录'
            return render_to_response(request, self.TEMPLATE,data=data)

        login(request,user)

        if to:
            redirect(to)
        return redirect(reverse('dashboard_index'))


class AdminManger(View):
    TEMPLATE='dashboard/auth/admin.html'

    @dashboard_auth
    def get(self,request):

        #users=User.objects.filter(is_superuser=True)
        users = User.objects.all()

        page=request.GET.get('page',1)
        p=Paginator(users,1)
        totl_page = p.num_pages
        if int(page)<=1:
            page=1

        current_page_users=p.get_page(int(page)).object_list


        data={'users':current_page_users,'totl_page':totl_page,'page_num':int(page)}

        return render_to_response(request,self.TEMPLATE,data=data)

    def post(self,request):
        pass

class UpdateAdminStatus(View):
    def get(self,request):
        status=request.GET.get('status','on')
        #username=request.GET.get('status','')
        print(status)
        #cu_user=User.objects.filter(username=username)
        _status=True if status=='on' else False
        # if username==None:
        #     return redirect(reverse('admin_manger'))
        # print(username)
        # cu_user.is_superuser= _status
        # cu_user.save()
        request.user.is_superuser=_status
        request.user.save()

        return redirect(reverse('admin_manger'))

class LogOut(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('dashboard_login'))