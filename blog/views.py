from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import blog,url_post,topic,product,called,visited,other_photos
from .forms import post,my_blog,new_blog,new_pro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from datetime import datetime
from django.contrib.auth import login,authenticate
import pyperclip

def index(request):
	data=[]
	title=topic.objects.all()
	for one in title:
		hi={'name':one.title,'id':one.id}
		data.append(hi)
	context={'data':data}
	return render(request,'blog/index.html',context)

def link(request):
	links=url_post.objects.all()
	data=[]
	for url in links:
		pink={'name':url.name,'url':url.url,'id':url.id}
		data.append(pink)
	context={'data':data}
	return render(request,'blog/link.html',context)

def bloger(request,pk):
	yo=topic.objects.filter(id=pk).get()
	if request.user==yo.user:
		if request.method=='POST':
			form=my_blog(request.POST)
			if form.is_valid():
				data=request.POST['data']
				write=blog(data=data)
				write.save()
				yo.blog.add(write)
				yo.save()
	lis=[]
	for one in yo.blog.all():
		lis.append(one.data)
	data={'title':yo.title,'list':lis,'date':yo.date}
	form=my_blog()
	context={'data':data,'form':form,'id':yo.id}
	print(context)
	return render(request,'blog/blog.html',context)
def add(request):
	if request.method=='POST':
		form=post(request.POST)
		if form.is_valid():
			url=request.POST['url']
			name=request.POST['name']
			new=url_post(name=name,url=url)
			new.save()
			return redirect('link')
	form=post()
	context={'form':form}
	return render(request,'blog/add.html',context)

def send(request,id):
	link=url_post.objects.filter(id__exact=id).get()
	link.visited=link.visited+1
	if request.user.is_authenticated:
		if request.user not in link.visitors.all():
			link.visitors.add(request.user)
	link.save()
	return redirect(link.url)

def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user=authenticate(username=username,password=password)
			login(request,user)
			return redirect('bloger')
	else:
		form=UserCreationForm()
		context={'form':form}
		return render(request,'registration/register.html',context)

def stats(request):
	pre=product.objects.all()
	data=[]
	
	for link in pre:
		total=link.visited.visited
		use=link.visited.visitors.all().count()
		som=link.called.visitors.all().count()
		su=link.called.visited
		pink={'distinct_users':use,'total':total,'name':link.title,'by':link.name,'total_called':su,'distinct_call':som,'username':link.user.username}
		data.append(pink)
	context={'data':data}
	return render(request,'blog/stats.html',context)
def new(request):
	if request.method=='POST':
		form=new_blog(request.POST)
		if form.is_valid():
			blog_topic=form.cleaned_data['title']
			new=topic(title=blog_topic,user=request.user)
			new.save()
			return redirect('bloger',new.id)
	else:
		form=new_blog()
		context={'form':form}
		return render(request,'blog/new_blog.html',context)

# new code

def view_products(request):
	pre=product.objects.all().order_by('-date')
	data=[]
	for some in pre:
		pink={'name':some.title,'by':some.name,'user':some.user.username,'image':some.image,'desciption':some.desciption,'viewed':some.visited.visitors.all().count(),'id':some.id}
		data.append(pink)
	context={'data':data}
	return render(request,'blog/product.html',context)

def give_detail(request,pk):
	pro=product.objects.filter(pk=pk).get()
	ki=pro.visited
	ki.visited=ki.visited+1
	ki.save()
	pro.save()
	if request.user.is_authenticated:
		li=pro.visited.visitors.all()
		if request.user not in li:
			pro.visited.visitors.add(request.user)
	pro.save()
	return details(request,pk)
def details(request,pk):
	pro=product.objects.filter(pk=pk).get()
	use=pro.visited.visitors.all()
	data=[]
	for one in use:
		som=product.objects.filter(visited__visitors__username=one)
		for some in som:
			if some== pro:
				continue
			red={'name':some.title,'by':some.name,'user':some.user.username,'image':some.image,'desciption':some.desciption,'viewed':some.visited.visitors.all().count(),'id':some.id}
			data.append(red)
	sug=[]
	for d in data:
		if d not in sug:
			sug.append(d)
	ans=0
	if request.user in pro.called.visitors.all():
		ans=1
	pink={'name':pro.title,'phone':pro.phone_number,'by':pro.name,'user':some.user.username,'image':pro.image,'description':pro.desciption,'viewed':pro.visited.visited,'distinct':pro.visited.visitors.all().count(),'called':pro.called.visited,'date':pro.date,'id':pro.id,'category':pro.category}
	context={'data':pink,'sug':sug,'ans':ans,'other':pro.other.all()}
	return render(request,'blog/detail.html',context)

def new_add(request):
	if request.method=='POST':
		print(request.FILES)
		form=new_pro(request.POST,request.FILES)
		if form.is_valid():
			title=request.POST['title']
			image=request.FILES['image']
			description=request.POST['description']
			phone_number=request.POST['phone_number']
			name=request.POST['name']
			category=request.POST['category']
			vis=called()
			vis.save()
			you=visited()
			you.save()
			hello=product(title=title,image=image,desciption=description,phone_number=phone_number,name=name,user=request.user,called=vis,visited=you,category=category)
			hello.save()
			for file in request.FILES.getlist('file'):
				de=other_photos(image=file)
				de.save()
				hello.other.add(de)
			hello.save()
			return redirect('view_products')
	form=new_pro()
	context={'form':form}
	return render(request,'blog/new_product.html',context)
def call(request,pk):
	pro=product.objects.filter(pk=pk).get()
	ji=pro.called
	ji.visited=ji.visited+1
	ji.save()
	if request.user.is_authenticated:
		if request.user not in pro.called.visitors.all():
			pro.called.visitors.add(request.user)
	pro.save()
	return details(request,pk)





















